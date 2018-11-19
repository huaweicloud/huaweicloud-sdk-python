# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
# 
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

from openstack.cdn import cdn_resource
from openstack.cdn import cdn_service
from openstack.cdn import format
from openstack import resource2 as resource
from openstack import utils


class Domain(cdn_resource.Resource):
    base_path = '/cdn/domains'
    resource_key = 'domain'
    resources_key = 'domains'
    service = cdn_service.CDNService()

    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True

    _query_mapping = cdn_resource.QueryParameters('domain_name',
                                                  'business_type',
                                                  'domain_status',
                                                  'enterprise_project_id')

    #: The acceleration domain name.
    domain_name = resource.Body('domain_name')
    #: The business type. Values include:
    #: 'web' (the acceleration for static contents);
    #: 'download' (the acceleration for downloads);
    #: 'video' (the acceleration for media streaming).
    business_type = resource.Body('business_type')
    enterprise_project_id = resource.Body('enterprise_project_id')
    #: The domain ID of the domain name's owner.
    user_domain_id = resource.Body('user_domain_id')
    #: The status of the acceleration domain name. Values include
    #: 'online': CDN is enabled;
    #: 'offline': CDN is disabled;
    #: 'configuring': CDN is being configured;
    #: 'configure_failed': the configuration failed;
    #: 'checking': the configuration is being audited;
    #: 'check_failed': the audit failed;
    #: 'deleting': the acceleration domain name is being deleted.
    domain_status = resource.Body('domain_status')
    #: The CNAME of the acceleration domain name.
    cname = resource.Body('cname')
    #: The domain name or the IP address of the origin server.
    sources = resource.Body('sources', type=list)
    #: The configuration information of the retrieval host.
    domain_origin_host = resource.Body('domain_origin_host', type=dict)
    #: HTTPS status for the acceleration.
    #: 0: disabled,
    #: 1: enable HTTPS for acceleration and following the origin.
    #: 2: enable HTTPS only for acceleration.
    https_status = resource.Body('https_status')
    #: The time when the domain name is modified.
    created_at = resource.Body('create_time')
    #: The time when the domain name is modified.
    modified_at = resource.Body('modify_time')
    #: Whether the acceleration domain name is disabled.
    is_disabled = resource.Body('disabled', type=format.BoolInt)
    #: Whether the status is locked.
    is_locked = resource.Body('locked', type=format.BoolInt)

    def get(self, session, requires_id=True):
        """Get a remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param boolean requires_id: A boolean indicating whether resource ID
                                    should be part of the requested URI.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`~openstack.cdn.v1.domain.Domain`
        """
        request = self._prepare_request(requires_id=requires_id)
        # NOTE(samsong8610): The URL for GET is not standard.
        request.uri = utils.urljoin(request.uri, 'detail')
        endpoint_override = self.service.get_endpoint_override()
        response = session.get(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override)

        self._translate_response(response)
        return self

    def set_sources(self, session, *sources):
        """Update information about the origin server

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param \*sources: A list of dict which specifies the domain name
            or the IP address of the origin server.
            Available keys for each source dict include:

            * ip_or_domain: The IP address or domain name of the origin server
                            Mandatory.
            * origin_type: The origin type. The value can be 'ipaddr' or
                           'domain'. Mandatory.
            * active_standby: Whether the source is active. 1: active,
                              0: standby. Mandatory.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        body = {'origin': {'sources': list(sources)}}
        url = utils.urljoin(self.base_path, self.id, 'origin')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body)
        resp_json = resp.json()
        self.check_error(resp_json)
        self.sources = resp_json['origin']['sources']
        return self

    def enable(self, session):
        """Enables an acceleration domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        url = utils.urljoin(self.base_path, self.id, 'enable')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override)
        self._translate_response(resp)
        return self

    def disable(self, session):
        """Disable an acceleration domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        url = utils.urljoin(self.base_path, self.id, 'disable')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override)
        self._translate_response(resp)
        return self

    def set_origin_host(self, session, **attrs):
        """Modifies the configuration of the retrieval host

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param dict attrs: Keyword arguments which contains origin host
            configuration for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * origin_host_type: The type of the retrieval host.
                'accelerate': the acceleration domain name is used as
                the retrieval host address;
                'customize': A custom domain name is used as the retrieval
                host address;
                'source': The origin domain name is used as the retrieval
                host address.
            * customize_domain: The custom domain name of the retrieval host.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        body = {'origin_host': attrs}
        url = utils.urljoin(self.base_path, self.id, 'originhost')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body)
        resp_json = resp.json()
        self.check_error(resp_json)
        self.domain_origin_host = resp_json['origin_host']
        return self

    def get_origin_host(self, session):
        """Queries the configuration of the retrieval host

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: The retrieval host configuration of this domain name
        :rtype: dict
        """
        url = utils.urljoin(self.base_path, self.id, 'originhost')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override)
        resp_json = resp.json()
        self.check_error(resp_json)
        return resp_json['origin_host']

    def set_referer(self, session, **attrs):
        """Configures a referrer list

        Self-define referrer whitelists and blacklists identify and filter
        user identities, controlling access.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param dict attrs: Keyword arguments which contains origin host
            configuration for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * referer_type: The referer type. The values include:
            0: referer filter not set; 1: blacklist; 2: whitelist.
            * referer_list: A list of domain names that are separated from
            each other by semicolon (;).
            * include_empty: Whether blank referrers are included.
            A referrer blacklist including blank referrers indicates that
            requests without any referrers are not allowed to access.
            A referrer whitelist including blank referrers indicates that
            requests without any referrers are allowed to access.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        body = {'referer': attrs}
        url = utils.urljoin(self.base_path, self.id, 'referer')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body)
        resp_json = resp.json()
        self.check_error(resp_json)
        return self

    def get_referer(self, session):
        """Queries the referer list of the domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: The referer list of this domain name
        :rtype: dict
        """
        url = utils.urljoin(self.base_path, self.id, 'referer')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override)
        resp_json = resp.json()
        self.check_error(resp_json)
        return resp_json['referer']

    def set_cache_rules(self, session, **attrs):
        """Configures a cache policy for resources on CDN nodes

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param dict attrs: Keyword arguments which contains cache policies
            for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * ignore_url_parameter: Whether to ignore URL parameters
            * rules: A list of the cache rules, which overwrite the previous
            rule configurations. Blank rules are reset to default rules.
            Each cache rule contains 'rule_type','content','ttl','ttl_type' and
            'priority' properties.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        body = {'cache_config': attrs}
        url = utils.urljoin(self.base_path, self.id, 'cache')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body)
        resp_json = resp.json()
        self.check_error(resp_json)
        return self

    def get_cache_rules(self, session):
        """Queries the cache rules of the domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: The cache rules of this domain name
        :rtype: dict
        """
        url = utils.urljoin(self.base_path, self.id, 'cache')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override)
        resp_json = resp.json()
        self.check_error(resp_json)
        return resp_json['cache_config']

    def set_https(self, session, **attrs):
        """Configures the HTTPS of the acceleration domain name

        This method sets HTTPS by configuring the certificate of a domain name,
        and deploy the HTTPS configuration on all CDN nodes to implement
        secure acceleration.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param dict attrs: Keyword arguments which contains cache policies
            for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * cert_name: The certificate name.
            * https_status: The HTTPS certificate is enabled.
            * certificate: The certificate used by HTTPS.
            * private_key: The private key used by HTTPS.
            * force_redirect_https: Whether to force the client request to be
            redirected.
            * http2: Whether to use HTTP 2.0.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        body = {'https': attrs}
        url = utils.urljoin(self.base_path, self.id, 'https-info')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body)
        resp_json = resp.json()
        self.check_error(resp_json)
        return self

    def get_https(self, session):
        """Obtains the certificate for the acceleration domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: The HTTPS certificate of this domain name
        :rtype: dict
        """
        url = utils.urljoin(self.base_path, self.id, 'https-info')
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override)
        resp_json = resp.json()
        self.check_error(resp_json)
        return resp_json['https']


    def get_detail_by_enterprise_project_id(self, session, enterprise_project_id):
        """Get a remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param boolean requires_id: A boolean indicating whether resource ID
                                    should be part of the requested URI.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`~openstack.cdn.v1.domain.Domain`
        """

        request = self._prepare_request(requires_id=enterprise_project_id)
        # NOTE(samsong8610): The URL for GET is not standard
        request.uri = utils.urljoin(request.uri, 'detail')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        response = session.get(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override, params=params)

        self._translate_response(response)
        return self

    def set_sources_by_enterprise_project_id(self, session, enterprise_project_id, **attrs):
        """Update information about the origin server

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param \*sources: A list of dict which specifies the domain name
            or the IP address of the origin server.
            Available keys for each source dict include:

            * ip_or_domain: The IP address or domain name of the origin server
                            Mandatory.
            * origin_type: The origin type. The value can be 'ipaddr' or
                           'domain'. Mandatory.
            * active_standby: Whether the source is active. 1: active,
                              0: standby. Mandatory.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        # body = {'origin': {'sources': list(sources)}}
        # print(attrs)
        body = {'origin': attrs}
        url = utils.urljoin(self.base_path, self.id, 'origin')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body, params=params)
        resp_json = resp.json()
        self.check_error(resp_json)
        self.sources = resp_json['origin']['sources']
        return self

    def delete_by_enterprise_project_id(self, session, enterprise_project_id):
        """delete an acceleration domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        url = utils.urljoin(self.base_path, self.id)
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.delete(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override, params=params)
        self._translate_response(resp)
        return self

    def enable_by_enterprise_project_id(self, session, enterprise_project_id):
        """Enables an acceleration domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """

        url = utils.urljoin(self.base_path, self.id, 'enable')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override, params=params)
        self._translate_response(resp)
        return self

    def disable_by_enterprise_project_id(self, session, enterprise_project_id):
        """Disable an acceleration domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        # print(enterprise_project_id)
        url = utils.urljoin(self.base_path, self.id, 'disable')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override, params=params)
        self._translate_response(resp)
        return self

    def set_origin_host_by_enterprise_project_id(self, session, enterprise_project_id, **attrs):
        """Modifies the configuration of the retrieval host

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param dict attrs: Keyword arguments which contains origin host
            configuration for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * origin_host_type: The type of the retrieval host.
                'accelerate': the acceleration domain name is used as
                the retrieval host address;
                'customize': A custom domain name is used as the retrieval
                host address;
                'source': The origin domain name is used as the retrieval
                host address.
            * customize_domain: The custom domain name of the retrieval host.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        body = {'origin_host': attrs}
        url = utils.urljoin(self.base_path, self.id, 'originhost')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body, params=params)
        resp_json = resp.json()
        self.check_error(resp_json)
        self.domain_origin_host = resp_json['origin_host']
        return self

    def get_origin_host_by_enterprise_project_id(self, session, enterprise_project_id):
        """Queries the configuration of the retrieval host

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: The retrieval host configuration of this domain name
        :rtype: dict
        """
        # print(enterprise_project_id)
        url = utils.urljoin(self.base_path, self.id, 'originhost')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override, params=params)
        resp_json = resp.json()
        self.check_error(resp_json)
        return resp_json['origin_host']

    def set_referer_by_enterprise_project_id(self, session, enterprise_project_id, **attrs):
        """Configures a referrer list

        Self-define referrer whitelists and blacklists identify and filter
        user identities, controlling access.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param dict attrs: Keyword arguments which contains origin host
            configuration for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * referer_type: The referer type. The values include:
            0: referer filter not set; 1: blacklist; 2: whitelist.
            * referer_list: A list of domain names that are separated from
            each other by semicolon (;).
            * include_empty: Whether blank referrers are included.
            A referrer blacklist including blank referrers indicates that
            requests without any referrers are not allowed to access.
            A referrer whitelist including blank referrers indicates that
            requests without any referrers are allowed to access.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        body = {'referer': attrs}
        url = utils.urljoin(self.base_path, self.id, 'referer')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body, params=params)
        resp_json = resp.json()
        self.check_error(resp_json)
        return self

    def get_referer_by_enterprise_project_id(self, session, enterprise_project_id):
        """Queries the referer list of the domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: The referer list of this domain name
        :rtype: dict
        """
        url = utils.urljoin(self.base_path, self.id, 'referer')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override, params=params)
        resp_json = resp.json()
        self.check_error(resp_json)
        return resp_json['referer']

    def set_cache_rules_by_enterprise_project_id(self, session, enterprise_project_id, **attrs):
        """Configures a cache policy for resources on CDN nodes

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param dict attrs: Keyword arguments which contains cache policies
            for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * ignore_url_parameter: Whether to ignore URL parameters
            * rules: A list of the cache rules, which overwrite the previous
            rule configurations. Blank rules are reset to default rules.
            Each cache rule contains 'rule_type','content','ttl','ttl_type' and
            'priority' properties.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        body = {'cache_config': attrs}
        url = utils.urljoin(self.base_path, self.id, 'cache')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body, params=params)
        resp_json = resp.json()
        self.check_error(resp_json)
        return self

    def get_cache_rules_by_enterprise_project_id(self, session, enterprise_project_id):
        """Queries the cache rules of the domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: The cache rules of this domain name
        :rtype: dict
        """
        url = utils.urljoin(self.base_path, self.id, 'cache')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override, params=params)
        resp_json = resp.json()
        self.check_error(resp_json)
        return resp_json['cache_config']

    def set_https_by_enterprise_project_id(self, session, enterprise_project_id, **attrs):
        """Configures the HTTPS of the acceleration domain name

        This method sets HTTPS by configuring the certificate of a domain name,
        and deploy the HTTPS configuration on all CDN nodes to implement
        secure acceleration.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param dict attrs: Keyword arguments which contains cache policies
            for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * cert_name: The certificate name.
            * https_status: The HTTPS certificate is enabled.
            * certificate: The certificate used by HTTPS.
            * private_key: The private key used by HTTPS.
            * force_redirect_https: Whether to force the client request to be
            redirected.
            * http2: Whether to use HTTP 2.0.

        :returns: This :class:`Domain` instance.
        :rtype: :class:`Domain`
        """
        body = {'https': attrs}
        url = utils.urljoin(self.base_path, self.id, 'https-info')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=body, params=params)
        resp_json = resp.json()
        self.check_error(resp_json)
        return self

    def get_https_by_enterprise_project_id(self, session, enterprise_project_id):
        """Obtains the certificate for the acceleration domain name

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`

        :returns: The HTTPS certificate of this domain name
        :rtype: dict
        """
        url = utils.urljoin(self.base_path, self.id, 'https-info')
        params = {'enterprise_project_id': enterprise_project_id}
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override, params=params)
        resp_json = resp.json()
        self.check_error(resp_json)
        return resp_json['https']
