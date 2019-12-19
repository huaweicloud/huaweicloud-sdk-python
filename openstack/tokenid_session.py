#!/usr/bin/env python
# coding=utf-8
import logging
import functools
from keystoneauth1 import session as _session
from openstack.identity import identity_service
from keystoneauth1 import exceptions
from six.moves import urllib
from openstack.session import map_exceptions
from keystoneauth1.session import _determine_user_agent
from openstack.exceptions import MissingRequiredArgument
from openstack import version as openstack_version
import itertools

DEFAULT_USER_AGENT = "huawei-cloud-sdk-python/%s" % openstack_version.__version__
API_REQUEST_HEADER = "openstack-api-version"

_logger = logging.getLogger(__name__)


class TokenSession(_session.Session):
    def __init__(self, profile, user_agent=None, **kwargs):
        """Create a new Keystone auth session with a profile.

        :param profile: If the user has any special profiles such as the
            service name, region, version or interface, they may be provided
            in the profile object.  If no profiles are provided, the
            services that appear first in the service catalog will be used.
        :param user_agent: A User-Agent header string to use for the
                           request. If not provided, a default of
                           :attr:`~openstack.session.DEFAULT_USER_AGENT`
                           is used, which contains the openstacksdk version
                           When a non-None value is passed, it will be
                           prepended to the default.
        :type profile: :class:`~openstack.profile.Profile`
        """
        if user_agent is not None:
            self.user_agent = "%s %s" % (user_agent, DEFAULT_USER_AGENT)
        else:
            self.user_agent = DEFAULT_USER_AGENT

        self.profile = profile

        for arg in ['auth_url', 'auth_token']:
            if kwargs.get(arg) is None:
                raise MissingRequiredArgument("miss required argument: %s" % arg)
            if not kwargs.get(arg):
                raise MissingRequiredArgument("the argument: %s is empty" % arg)
        self.auth_url = kwargs.pop("auth_url")
        self.auth_token = kwargs.pop("auth_token")
        # self.project_id = kwargs.pop("project_id")
        self.__endpoint_data = None
        api_version_header = self._get_api_requests()
        super(TokenSession, self).__init__(user_agent=self.user_agent,
                                           additional_headers=api_version_header,
                                           **kwargs)

    def _get_api_requests(self):
        """Get API micro-version requests.

        :param profile: A profile object that contains customizations about
                        service name, region, version, interface or
                        api_version.
        :return: A standard header string if there is any specialization in
                 API microversion, or None if no such request exists.
        """
        if self.profile is None:
            return None

        req = []
        for svc in self.profile.get_services():
            if svc.service_type and svc.api_version:
                req.append(" ".join([svc.service_type, svc.api_version]))
        if req:
            return {API_REQUEST_HEADER: ",".join(req)}

        return None

    def get_auth_headers(self, **kwargs):
        return {"X-Auth-Token": self.auth_token}

    def get_token(self, auth=None):
        return (self.get_auth_headers() or {}).get('X-Auth-Token')

    def get_endpoint(self, auth=None, service_type=None,
                     **kwargs):
        # Currently, we only support bss service, include bssv1 and bss-intlv1.
        if service_type == "bssv1" or service_type == "bss-intlv1":
            base_url = self._get_endpoint_from_iam(service_type)
            if base_url:
                _logger.debug("Token session Get endpoint from Iam success,the endpoint is:%s" % base_url)
                return base_url
            return ""
        else:
            _logger.debug("This service :%s is not supported" % service_type)
            return ""

    def _get_endpoint_from_iam(self, service_type):
        service_type_iam = service_type.replace('-', '_')
        if not self.__endpoint_data:
            self.__endpoint_data = self.__fetch_all_global_level_endpoint()

        sc_endpoint = self.__endpoint_data.get(service_type_iam, "")
        if sc_endpoint:
            return sc_endpoint
        return ""

    def __fetch_all_global_level_endpoint(self):
        kvendpoints = {}
        resp = self.request(self.auth_url + "/endpoints", "GET",
                            endpoint_filter=identity_service.AdminService())
        endpoints = resp.json().get("endpoints", [])
        resp = self.request(self.auth_url + "/services", "GET",
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

    @map_exceptions
    def request(self, url, method, json=None, original_ip=None,
                user_agent=None, redirect=None, endpoint_filter=None,
                raise_exc=True, log=True, microversion=None,
                endpoint_override=None, connect_retries=0,
                allow=None, client_name=None, client_version=None,
                **kwargs):
        self._determined_user_agent = None
        headers = kwargs.setdefault('headers', dict())
        auth_headers = self.get_auth_headers()
        if auth_headers is None:
            msg = 'No valid authentication is available'
            raise exceptions.AuthorizationFailure(msg)
        headers.update(auth_headers)
        base_url = ""
        if not urllib.parse.urlparse(url).netloc:
            if endpoint_override:
                base_url = endpoint_override
                # base_url = endpoint_override % {"project_id": self.project_id}
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
        headers.setdefault('Content-Type', 'application/json')
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
