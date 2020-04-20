# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
# Copyright (c) 2009 Jacob Kaplan-Moss - initial codebase (< v2.1)
# Copyright (c) 2011 Rackspace - OpenStack extensions (>= v2.1)
# Copyright (c) 2011 Nebula, Inc - Keystone refactor (>= v2.7)
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

import functools
import hashlib
import hmac
from six.moves import urllib
import sys
import itertools
import datetime
import requests
from keystoneauth1.session import TCPKeepAliveAdapter, _JSONEncoder, _determine_user_agent
from openstack.exceptions import EndpointNotFound, SDKException
from openstack.session import DEFAULT_USER_AGENT
from openstack import session as osession
from keystoneauth1 import _utils as log_utils
from openstack import utils
from openstack.session import map_exceptions
from openstack.service_endpoint import endpoint as _endpoint
from keystoneauth1 import exceptions
from openstack.exceptions import MissingRequiredArgument
from openstack.identity import identity_service

EMPTYSTRING = ""
TERMINATORSTRING = "sdk_request"
ALGORITHM = "SDK-HMAC-SHA256"
PYTHON2 = "2"
UTF8 = "utf-8"
PROJECTIAMURL = "https://iam.%s.%s/v3/"
GLOBALIAMURL = "https://iam.%s/v3/"

_logger = log_utils.get_logger(__name__)


def construct_session(session_obj=None):
    """
    # NOTE(morganfainberg): if the logic in this function changes be sure to
    # update the betamax fixture's '_construct_session_with_betamax" function
    # as well.
    """
    if not session_obj:
        session_obj = requests.Session()
        # Use TCPKeepAliveAdapter to fix bug 1323862
        for scheme in list(session_obj.adapters):
            session_obj.mount(scheme, TCPKeepAliveAdapter())
    return session_obj


def get_utf8_bytes(message):
    """
    Get the bytes array encoded by utf-8
    :param message: the string of message
    :type message: string
    """

    codename = 'cp936' if sys.stdin.encoding is None else sys.stdin.encoding
    if sys.version.startswith(PYTHON2):
        if type(message) == str:
            return message.decode(codename).encode(UTF8)
        if isinstance(message, type(u"")):
            return message.encode("utf-8")
    else:
        if type(message) == str:
            return message.encode(UTF8)
        if type(message) == bytes:
            return message.decode(codename).encode(UTF8)


class AkSksignature(object):
    """
    aksk signature class
    """

    def __init__(self, accesskey=None, secretkey=None, region=None):
        """
        This class is used to sign the request header.
        The use method is to construct the class object and
        then call the signature method to generate the signature string.

        Create a signature for a ak sk session to a cloud provider.

        The AkSksignature
        creates a
        :class:`~openstack.aksksession.AkSksignature` which uses the ak
        and sk to perform request header signature.

        :param cfgfile: A config file
        :type cfgfile: string of the file name

        """
        self.ak = accesskey
        self.sk = secretkey
        self.region = region
        self.headtosign = ['Host', 'X-Sdk-Date']

    def _make_canonical_request(self, method=None, url=None, headers=None, params=None, body=EMPTYSTRING):
        """
        Create a canonical request string
        :param method : the request's http method, get/post OR other
        :type method : string
        :param url : the full path url
        :type url : string
        :param headers : the http request header,must contains Host and X-Sdk-Date fields
        :type headers : python dict
        :param params : the http request query parametrers
        :type params : python dict
        :param body : the http request body
        :type body : python dict
        :return: A string of canonical request

        """
        canonical_method = method.upper() if method else EMPTYSTRING
        uri = urllib.parse.urlparse(url).path
        if ":" in uri:
            comsplits = uri.split(":")
            res = []
            for seg in comsplits:
                urlseg = urllib.request.pathname2url(seg)
                res.append(urlseg)
            uri = "%3A".join(res)
        else:
            uri = urllib.request.pathname2url(uri)
        canonical_uri = uri if uri.endswith('/') else uri + '/'
        if params:
            result = []
            for k, vs in list(params.items()):
                if isinstance(vs, str) or not hasattr(vs, '__iter__'):
                    vs = [vs]
                for v in vs:
                    if v is not None:
                        result.append(
                            (k.encode('utf-8') if isinstance(k, str) else k,
                             v.encode('utf-8') if isinstance(v, str) else v))
            result.sort(key=lambda item: item[0])
            canonical_querystring = urllib.parse.urlencode(result, doseq=True)
            canonical_querystring = canonical_querystring.replace("+", "%20")
        else:
            canonical_querystring = EMPTYSTRING
        canonical_header = [k.lower() + ':' + headers.get(k).strip() for k in self.headtosign] if all(
            [k in headers for k in self.headtosign]) else []
        canonical_header = '\n'.join(canonical_header)
        canonical_header += '\n'
        signed_header = ';'.join([k.lower() for k in self.headtosign])
        body = body if body  else ""
        request_payload = hashlib.sha256(get_utf8_bytes(body)).hexdigest()
        return '\n'.join(
            [canonical_method, canonical_uri, canonical_querystring, canonical_header, signed_header, request_payload])

    def _make_string_to_sign(self, canonical_req, dtstamp, svr):
        """
        :param canonical_req: A string of canonical request returned by function _make_canonical_request
        :type canonical_req: string
        :param dtstamp: datetime stamp of UTC
        :type dtstamp : string
        :param svr: the name of service defined in  sdk
        :type svr :string
        :return: A string to be signed
        """
        algorithm = ALGORITHM
        request_datetime = dtstamp
        request_date = dtstamp.split('T')[0]
        region = self.region if self.region else ""
        credential_scope = '/'.join([
            request_date,
            region,
            svr,
            TERMINATORSTRING
        ])
        hashed_request = hashlib.sha256(get_utf8_bytes(canonical_req)).hexdigest()
        return "\n".join([algorithm, request_datetime, credential_scope, hashed_request]), credential_scope

    def _make_signing_key(self, dtstamp, svr):
        """
        :param dtstamp: datetime stamp of UTC
        :type dtstamp : string
        :param svr: the name of service defined in  sdk
        :type svr :string
        :return: A string to be used as the key when encry the request string
        """
        ksecret = "SDK" + self.sk
        kdate = hmac.new(get_utf8_bytes(ksecret),
                         get_utf8_bytes(dtstamp[0:8]),
                         digestmod=hashlib.sha256)
        kregion = hmac.new(kdate.digest(), get_utf8_bytes(self.region), digestmod=hashlib.sha256)
        kservice = hmac.new(kregion.digest(), get_utf8_bytes(svr), digestmod=hashlib.sha256)
        return hmac.new(kservice.digest(), get_utf8_bytes(TERMINATORSTRING), digestmod=hashlib.sha256).digest()

    def signature(self, url=None, method=None, headers=None, data=None, params=None, svr=None):
        """
        :param method : the request's http method, get/post OR other
        :type method : string
        :param url : the full path url
        :type url : string
        :param headers : the http request header,must contains Host and X-Sdk-Date fields
        :type headers : python dict
        :param params : the http request query parametrers
        :type params : python dict
        :param data : the http request body
        :type data : python dict
        :param svr: the name of service defined in  sdk
        :type svr :string
        :return: A string of signature
        """
        canonical_request = self._make_canonical_request(method=method, url=url, params=params, headers=headers,
                                                         body=data)
        # print canonical_request
        signing_key = self._make_signing_key(headers.get("X-Sdk-Date"), svr)
        string_to_sign, credential_scope = self._make_string_to_sign(canonical_request, headers.get("X-Sdk-Date"), svr)
        signature = hmac.new(signing_key, get_utf8_bytes(string_to_sign), digestmod=hashlib.sha256).hexdigest()
        signed_header = ';'.join([k.lower() for k in self.headtosign])
        return "%s Credential=%s/%s, SignedHeaders=%s, Signature=%s" % (ALGORITHM,
                                                                        self.ak,
                                                                        credential_scope,
                                                                        signed_header,
                                                                        signature)


def check(session):
    def oninit(*pargs, **kwargs):
        for arg in ['ak', 'sk', 'domain']:
            if kwargs.get(arg) is None:
                if arg == "domain":
                    arg = "cloud"
                raise MissingRequiredArgument("miss required argument: %s" % arg)
            if not kwargs.get(arg):
                if arg == "domain":
                    arg = "cloud"
                raise MissingRequiredArgument("the argument: %s is empty" % arg)
        return session(*pargs, **kwargs)

    return oninit


@check
class ASKSession(osession.Session):
    def __init__(self, profile,
                 original_ip=None, verify=True,
                 cert=None, timeout=None,
                 user_agent=None,
                 redirect=30, additional_headers=None,
                 app_name=None, app_version=None,
                 additional_user_agent=None,
                 **kwargs
                 ):
        self.auth_url = kwargs.get('auth_url', None)
        self.project_id = kwargs.get("project_id")
        self.domain_id = kwargs.get("domain_id", None)
        self.domain = kwargs.get("domain")
        self.region = kwargs.get("region")
        self.signer = AkSksignature(accesskey=kwargs.get("ak"),
                                    secretkey=kwargs.get("sk"),
                                    region=kwargs.get("region"))
        if user_agent is not None:
            self.user_agent = "%s %s" % (user_agent, DEFAULT_USER_AGENT)
        else:
            self.user_agent = DEFAULT_USER_AGENT
        self.profile = profile
        self.session = construct_session(None)
        self.original_ip = original_ip
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.redirect = redirect
        self.additional_headers = additional_headers or {}
        self.app_name = app_name
        self.app_version = app_version
        self.additional_user_agent = additional_user_agent or []
        self._determined_user_agent = None
        self._json = _JSONEncoder()
        self._securitytoken = kwargs.get("securitytoken", None)
        if timeout is not None:
            self.timeout = float(timeout)
        self.__endpoint = _endpoint
        self.__iam_endpoint = None
        self.__endpoint_cache = {}

    @map_exceptions
    def request(self, url, method, json=None, original_ip=None,
                user_agent=None, redirect=None, endpoint_filter=None,
                raise_exc=True, log=True, microversion=None,
                endpoint_override=None, connect_retries=0,
                allow=None, client_name=None, client_version=None,
                **kwargs):
        headers = kwargs.setdefault('headers', dict())

        if microversion:
            self._set_microversion_headers(headers, microversion, None, endpoint_filter)
        if self._securitytoken:
            headers.setdefault("X-Security-Token", self._securitytoken)
        if not urllib.parse.urlparse(url).netloc:
            if endpoint_override:
                base_url = endpoint_override % {"project_id": self.project_id}
            elif endpoint_filter:
                base_url = self.get_endpoint(interface=endpoint_filter.interface,
                                             service_type=endpoint_filter.service_type)
            if not urllib.parse.urlparse(base_url).netloc:
                raise exceptions.EndpointNotFound()
            url = '%s/%s' % (base_url.rstrip('/'), url.lstrip('/'))
        headers.setdefault("Host", urllib.parse.urlparse(url).netloc)
        if self.cert:
            kwargs.setdefault('cert', self.cert)
        if self.timeout is not None:
            kwargs.setdefault('timeout', self.timeout)
        if user_agent:
            headers['User-Agent'] = user_agent
        elif self.user_agent:
            user_agent = headers.setdefault('User-Agent', self.user_agent)
        else:
            # Per RFC 7231 Section 5.5.3, identifiers in a user-agent should be
            # ordered by decreasing significance.  If a user sets their product
            # that value will be used. Otherwise we attempt to derive a useful
            # product value. The value will be prepended it to the KSA version,
            # requests version, and then the Python version.

            agent = []

            if self.app_name and self.app_version:
                agent.append('%s/%s' % (self.app_name, self.app_version))
            elif self.app_name:
                agent.append(self.app_name)

            if client_name and client_version:
                agent.append('%s/%s' % (client_name, client_version))
            elif client_name:
                agent.append(client_name)

            for additional in self.additional_user_agent:
                agent.append('%s/%s' % additional)

            if not agent:
                # NOTE(jamielennox): determine_user_agent will return an empty
                # string on failure so checking for None will ensure it is only
                # called once even on failure.
                if self._determined_user_agent is None:
                    self._determined_user_agent = _determine_user_agent()

                if self._determined_user_agent:
                    agent.append(self._determined_user_agent)

            agent.append(DEFAULT_USER_AGENT)
            user_agent = headers.setdefault('User-Agent', ' '.join(agent))

        if self.original_ip:
            headers.setdefault('Forwarded',
                               'for=%s;by=%s' % (self.original_ip, user_agent))

        if json is not None:
            kwargs['data'] = self._json.encode(json)
        # surpport  maas,map_reduce when without request body
        headers.setdefault('Content-Type', 'application/json')
        if self.domain_id:
            headers.setdefault('X-Domain-Id', self.domain_id)
        # surpport sub-project id for some service the endpoint contain project id
        elif self.project_id:
            headers.setdefault('X-Project-Id', self.project_id)

        if self.additional_headers:
            for k, v in self.additional_headers.items():
                headers.setdefault(k, v)

        kwargs.setdefault('verify', self.verify)

        # if requests_auth:
        #     kwargs['auth'] = requests_auth

        # Query parameters that are included in the url string will
        # be logged properly, but those sent in the `params` parameter
        # (which the requests library handles) need to be explicitly
        # picked out so they can be included in the URL that gets loggged.
        query_params = kwargs.get('params', dict())
        headers.setdefault("X-Sdk-Date", datetime.datetime.strftime(datetime.datetime.utcnow(), "%Y%m%dT%H%M%SZ"))
        signedstring = self.signer.signature(method=method,
                                             url=url,
                                             headers=headers,
                                             svr=endpoint_filter.service_type if endpoint_filter else '',
                                             params=query_params,
                                             data=kwargs.get("data", None))
        # print(signedstring)
        headers.setdefault("Authorization", signedstring)
        if log:
            self._http_log_request(url, method=method,
                                   data=kwargs.get('data'),
                                   headers=headers,
                                   query_params=query_params,
                                   logger=_logger)

        # Force disable requests redirect handling. We will manage this below.
        kwargs['allow_redirects'] = False

        if redirect is None:
            redirect = self.redirect

        send = functools.partial(self._send_request,
                                 url, method, redirect, log, _logger,
                                 connect_retries)

        resp = send(**kwargs)

        # log callee and caller request-id for each api call
        if log:
            # service_name should be fetched from endpoint_filter if it is not
            # present then use service_type as service_name.
            service_name = None
            if endpoint_filter:
                service_name = endpoint_filter.get('service_name')
                if not service_name:
                    service_name = endpoint_filter.get('service_type')

            # Nova uses 'x-compute-request-id' and other services like
            # Glance, Cinder etc are using 'x-openstack-request-id' to store
            # request-id in the header
            request_id = (resp.headers.get('x-openstack-request-id') or
                          resp.headers.get('x-compute-request-id'))
            if request_id:
                _logger.debug('%(method)s call to %(service_name)s for '
                              '%(url)s used request id '
                              '%(response_request_id)s',
                              {'method': resp.request.method,
                               'service_name': service_name,
                               'url': resp.url,
                               'response_request_id': request_id})

        if raise_exc and resp.status_code >= 400:
            _logger.debug('Request returned failure status: %s',
                          resp.status_code)
            raise exceptions.from_response(resp, method, url)
        return resp

    def get_endpoint(self, auth=None, interface=None, service_type=None,
                     **kwargs):
        base_url = self._get_endpoint_from_iamdata(service_type)
        if base_url:
            _logger.debug("Get endpoint from Iam success,the endpoint is:%s" % base_url)
            return base_url
        base_url = self._get_endpoint_from_configdata(service_type, interface)
        if base_url:
            _logger.debug("Get endpoint from Config success,the endpoint is:%s" % base_url)
            return base_url
        return ""

    def _get_endpoint_from_iamdata(self, service_type):
        service_type_iam = service_type.replace('-', '_')
        if self.__endpoint_cache.get(service_type_iam, ""):
            return self.__endpoint_cache.get(service_type_iam)
        if not self.__iam_endpoint:
            if self.region:
                self.__iam_endpoint = self.__fetch_all_endpoint_service_project_level()
            else:
                self.__iam_endpoint = self.__fetch_all_endpoint_service_global_level()
        filt = self.profile.get_filter(service_type)
        sc_endpoint = self.__iam_endpoint.get(service_type_iam, "")
        if not sc_endpoint:
            return sc_endpoint

        if service_type == "object-store":
            self.__endpoint_cache[service_type_iam] = sc_endpoint
            return sc_endpoint

        if service_type == "iam":
            self.__endpoint_cache[service_type_iam] = sc_endpoint
            return sc_endpoint
        try:
            endpoint = self._get_endpoint_versions(service_type,
                                                   sc_endpoint)
            profile_version = self._parse_version(filt.version)
            match = self._get_version_match(endpoint, profile_version,
                                            service_type)

            _logger.debug("Using %s as %s %s endpoint",
                          match, "public", service_type)

            self.__endpoint_cache[service_type_iam] = match
            return match
        except (EndpointNotFound, SDKException):
            self.__endpoint_cache[service_type_iam] = sc_endpoint
            return sc_endpoint

    def _get_endpoint_from_configdata(self, service_type, interface):
        service_type = service_type.upper().replace('-', '_')
        base_url = ""
        if self.__endpoint and service_type in self.__endpoint:
            endpoint = self.__endpoint.get(service_type).get(interface, '')
            map = {"project_id": self.project_id, "region": self.region, "domain": self.domain}
            base_url = endpoint % map
        return base_url

    def __fetch_all_endpoint_service_project_level(self):
        kvendpoints = {}
        if self.auth_url:
            auth_url = self.auth_url
        else:
            auth_url = PROJECTIAMURL % (self.region, self.domain)
        resp = self.request(utils.urljoin(auth_url, "endpoints"), "GET",
                            endpoint_filter=identity_service.AdminService())
        endpoints = resp.json().get("endpoints", [])
        resp = self.request(utils.urljoin(auth_url, "services"), "GET",
                            endpoint_filter=identity_service.AdminService())
        services = resp.json().get("services", [])
        id_endpoint_map, servicetype_id_map = {}, {}
        lzip = itertools.izip_longest if hasattr(itertools, "izip_longest") else itertools.zip_longest
        for endpoint, service in lzip(endpoints, services):
            if endpoint and endpoint.get("enabled") and endpoint.get("region") is not None:
                id_endpoint_map.setdefault(endpoint.get("service_id"), [])
                data_map = {endpoint.get("region"): endpoint.get("url")}
                id_endpoint_map[endpoint.get("service_id")].append(data_map)
            if service and service.get("enabled"):
                servicetype_id_map.setdefault(service.get("type"), [])
                servicetype_id_map[service.get("type")].append(service.get("id"))
        for k, v in servicetype_id_map.items():
            for serviceid in v:
                for region_url_map in id_endpoint_map.get(serviceid, []):
                    url = region_url_map.get(self.region, "")
                    if url != "":
                        kvendpoints[k] = url.replace("$(tenant_id)s", self.project_id)
                        break
                if kvendpoints.get(k, ""):
                    break
        return kvendpoints

    def __fetch_all_endpoint_service_global_level(self):
        kvendpoints = {}
        if self.auth_url:
            auth_url = self.auth_url
        else:
            auth_url = GLOBALIAMURL % self.domain
        resp = self.request(utils.urljoin(auth_url, "endpoints"), "GET",
                            endpoint_filter=identity_service.AdminService())
        endpoints = resp.json().get("endpoints", [])
        resp = self.request(utils.urljoin(auth_url, "services"), "GET",
                            endpoint_filter=identity_service.AdminService())
        services = resp.json().get("services", [])
        id_endpoint_map, servicetype_id_map = {}, {}
        lzip = itertools.izip_longest if hasattr(itertools, "izip_longest") else itertools.zip_longest
        for endpoint, service in lzip(endpoints, services):
            if endpoint and endpoint.get("enabled") and endpoint.get("region") is None:
                id_endpoint_map[endpoint.get("service_id")] = endpoint.get("url")
            if service and service.get("enabled"):
                servicetype_id_map.setdefault(service.get("type"), [])
                servicetype_id_map[service.get("type")].append(service.get("id"))
        for k, v in servicetype_id_map.items():
            for serviceid in v:
                url = id_endpoint_map.get(serviceid)
                if url != "":
                    kvendpoints[k] = url
                    break
                if kvendpoints.get(k, ""):
                    break
        return kvendpoints

    def get_project_id(self):
        """
        :return: project id
        """
        return self.project_id
