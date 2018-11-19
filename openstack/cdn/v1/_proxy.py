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

from openstack.cdn.v1 import domain as _domain
from openstack.cdn.v1 import log as _log
from openstack.cdn.v1 import statistic as _statistic
from openstack.cdn.v1 import task as _task
from openstack import proxy2


class Proxy(proxy2.BaseProxy):
    def domains(self, page_size=100, page_number=1, **query):
        """List the domains matching the given query

        :param int page_size: The number of acceleration domain names on each
            page. The value ranges from 10 to 1000. Mandatory.
        :param int page_number: The page number that is queried. The value
            ranges from 1 to 65535. Mandatory.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
            the resources being returned. Available attributes include:

            * domain_name: The acceleration domain name, which is matched in
                a fuzzy manner. The value contains 1 to 255 characters.
            * business_type: The business type of the domain name.
                Values can be: 'web' (image and small file distribution),
                'download' (large file download acceleration) and
                'video' (on-demand audio and video acceleration).
            * domain_status: The status of the acceleration domain name.
                Values include 'online' (CDN is enabled);
                    'offline' (CDN is disabled);
                    'configuring' (CDN is being configured);
                    'configure_failed' (the configuration failed);
                    'checking' (the configuration is being audited);
                    'check_failed' (the audit failed);
                    'deleting' (the acceleration domain name is being deleted).

        :returns: A generator of Domain objects
        :rtype: :class:`~openstack.cdn.v1.domain.Domain`
        """
        query = query or {}
        query.update(page_size=page_size, page_number=page_number,
                     paginated=True)
        return self._list(_domain.Domain, **query)

    def create_domain(self, **attrs):
        """Create a new acceleration domain name from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.cdn.v1.domain.Domain`,
            comprised of the properties on the Domain class.
            Available attributes include:

            * domain_name: The acceleration domain name.
            * business_type: The business type. Values include
                'web': the acceleration for static contents;
                'download': the acceleration for downloads;
                'video': the acceleration for media streaming.
            * sources: A list of contents which specifies the domain name
                or the IP address of the origin server.
                Available keys for each source dict include:

                * ip_or_domain: The IP address or domain name of the origin
                                server. Mandatory.
                * origin_type: The origin type. The value can be 'ipaddr' or
                               'domain'. Mandatory.
                * active_standby: Whether the source is active. 1: active,
                                  0: standby. Mandatory.

        :returns: The results of the acceleration domain name creation
        :rtype: :class:`~openstack.cdn.v1.domain.Domain`
        """
        return self._create(_domain.Domain, **attrs)

    def get_domain(self, domain):
        """Get a single acceleration domain name

        :param domain: The value can be the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_domain.Domain, domain)

    def get_domain_detail_by_enterprise_project_id(self, domain, enterprise_project_id='ALL'):
        """Get a single acceleration domain name

        :param domain: The value can be the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.get_detail_by_enterprise_project_id(self._session, enterprise_project_id)

    def delete_domain(self, domain, ignore_missing=True):
        """Delete an acceleration domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent resource.

        :returns: ``None``
        """
        self._delete(_domain.Domain, domain, ignore_missing=ignore_missing,
                     has_body=True)

    def delete_domain_by_enterprise_project_id(self, domain, enterprise_project_id):
        """Delete an acceleration domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent resource.

        :returns: ``None``
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.delete_by_enterprise_project_id(self._session, enterprise_project_id)

    def set_domain_sources(self, domain, *sources):
        """Update information about the origin server

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param \*sources: A list of dict which specifies the domain name
            or the IP address of the origin server.
            Available keys for each source dict include:

            * ip_or_domain: The IP address or domain name of the origin server
                            Mandatory.
            * origin_type: The origin type. The value can be 'ipaddr' or
                           'domain'. Mandatory.
            * active_standby: Whether the source is active. 1: active,
                              0: standby. Mandatory.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_sources(self._session, *sources)

    def set_domain_sources_by_enterprise_project_id(self, domain, enterprise_project_id, **attrs):
        """Update information about the origin server

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param \*sources: A list of dict which specifies the domain name
            or the IP address of the origin server.
            Available keys for each source dict include:

            * ip_or_domain: The IP address or domain name of the origin server
                            Mandatory.
            * origin_type: The origin type. The value can be 'ipaddr' or
                           'domain'. Mandatory.
            * active_standby: Whether the source is active. 1: active,
                              0: standby. Mandatory.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_sources_by_enterprise_project_id(self._session, enterprise_project_id, **attrs)

    def enable_domain(self, domain):
        """Enables an acceleration domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.enable(self._session)

    def enable_domain_by_enterprise_project_id(self, domain, enterprise_project_id):
        """Enables an acceleration domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.enable_by_enterprise_project_id(self._session, enterprise_project_id)

    def disable_domain(self, domain):
        """Disable an acceleration domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.disable(self._session)

    def disable_domain_by_enterprise_project_id(self, domain, enterprise_project_id):
        """Disable an acceleration domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.disable_by_enterprise_project_id(self._session, enterprise_project_id)

    def set_domain_origin_host(self, domain, **attrs):
        """Modifies the configuration of the retrieval host

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
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
                Mandatory.
            * customize_domain: The custom domain name of the retrieval host.
                Mandatory when the value of origin_host_type is 'customize'.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_origin_host(self._session, **attrs)

    def set_domain_origin_host_by_enterprise_project_id(self, domain, enterprise_project_id, **attrs):
        """Modifies the configuration of the retrieval host

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
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
                Mandatory.
            * customize_domain: The custom domain name of the retrieval host.
                Mandatory when the value of origin_host_type is 'customize'.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_origin_host_by_enterprise_project_id(self._session, enterprise_project_id, **attrs)

    def get_domain_origin_host(self, domain):
        """Queries the configuration of the retrieval host

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: The retrieval host configuration of this domain name
        :rtype: dict
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.get_origin_host(self._session)

    def get_domain_origin_host_by_enterprise_project_id(self, domain, enterprise_project_id):
        """Queries the configuration of the retrieval host

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: The retrieval host configuration of this domain name
        :rtype: dict
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.get_origin_host_by_enterprise_project_id(self._session, enterprise_project_id)

    def set_domain_referer(self, domain, **attrs):
        """Configures a referrer list

        Self-define referrer whitelists and blacklists identify and filter
        user identities, controlling access.

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param dict attrs: Keyword arguments which contains origin host
            configuration for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * referer_type: The referer type. The values include:
            0: referer filter not set; 1: blacklist; 2: whitelist.
            * referer_list: A list of domain names that are separated from
            each other by semicolon (;).
            * include_empty: Whether blank referrers are included.
            True or False.
            A referrer blacklist including blank referrers indicates that
            requests without any referrers are not allowed to access.
            A referrer whitelist including blank referrers indicates that
            requests without any referrers are allowed to access.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_referer(self._session, **attrs)

    def set_domain_referer_by_enterprise_project_id(self, domain, enterprise_project_id, **attrs):
        """Configures a referrer list

        Self-define referrer whitelists and blacklists identify and filter
        user identities, controlling access.

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param dict attrs: Keyword arguments which contains origin host
            configuration for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * referer_type: The referer type. The values include:
            0: referer filter not set; 1: blacklist; 2: whitelist.
            * referer_list: A list of domain names that are separated from
            each other by semicolon (;).
            * include_empty: Whether blank referrers are included.
            True or False.
            A referrer blacklist including blank referrers indicates that
            requests without any referrers are not allowed to access.
            A referrer whitelist including blank referrers indicates that
            requests without any referrers are allowed to access.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_referer_by_enterprise_project_id(self._session, enterprise_project_id, **attrs)

    def get_domain_referer(self, domain):
        """Queries the referer list of the domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: The referer list of this domain name
        :rtype: dict
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.get_referer(self._session)

    def get_domain_referer_by_enterprise_project_id(self, domain, enterprise_project_id):
        """Queries the referer list of the domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: The referer list of this domain name
        :rtype: dict
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.get_referer_by_enterprise_project_id(self._session, enterprise_project_id)

    def set_domain_cache_rules(self, domain, **attrs):
        """Configures a cache policy for resources on CDN nodes

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param dict attrs: Keyword arguments which contains cache policies
            for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * ignore_url_parameter: Whether to ignore URL parameters. True or
            False. Optional.
            * rules: A list of the cache rules, which overwrite the previous
            rule configurations. Blank rules are reset to default rules.
            Each cache rule contains 'rule_type','content','ttl','ttl_type' and
            'priority' properties.
                * rule_type: 0-all types of files are matched,
                             1-files are matched based on their suffixes,
                             2-files are matched based on directories.
                             Mandatory.
                * content: The content that matches rule_type.
                           When rule_type is 0, it should be None,
                           When rule_type is 1, it is suffixes that indicate
                           different types of files, for example, .jps;.js,
                           separated by semicolons (;).
                           When rule_type is 2, be directories, for example,
                           /www/html;/www/anc, separated by semicolons (;).
                * ttl: The cache time. The maximum value of ttl is 365 days.
                       Mandatory.
                * ttl_type: The unit of cache time.
                            1-seconds; 2-minutes; 3-hours; 4-days.
                            Mandatory.
                * priority: The priority weight of this rule. A greater value
                            indicates a higher priority. The value ranges
                            from 1 to 100. Default to 1.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_cache_rules(self._session, **attrs)

    def set_domain_cache_rules_by_enterprise_project_id(self, domain, enterprise_project_id, **attrs):
        """Configures a cache policy for resources on CDN nodes

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param dict attrs: Keyword arguments which contains cache policies
            for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * ignore_url_parameter: Whether to ignore URL parameters. True or
            False. Optional.
            * rules: A list of the cache rules, which overwrite the previous
            rule configurations. Blank rules are reset to default rules.
            Each cache rule contains 'rule_type','content','ttl','ttl_type' and
            'priority' properties.
                * rule_type: 0-all types of files are matched,
                             1-files are matched based on their suffixes,
                             2-files are matched based on directories.
                             Mandatory.
                * content: The content that matches rule_type.
                           When rule_type is 0, it should be None,
                           When rule_type is 1, it is suffixes that indicate
                           different types of files, for example, .jps;.js,
                           separated by semicolons (;).
                           When rule_type is 2, be directories, for example,
                           /www/html;/www/anc, separated by semicolons (;).
                * ttl: The cache time. The maximum value of ttl is 365 days.
                       Mandatory.
                * ttl_type: The unit of cache time.
                            1-seconds; 2-minutes; 3-hours; 4-days.
                            Mandatory.
                * priority: The priority weight of this rule. A greater value
                            indicates a higher priority. The value ranges
                            from 1 to 100. Default to 1.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_cache_rules_by_enterprise_project_id(self._session, enterprise_project_id, **attrs)

    def get_domain_cache_rules(self, domain):
        """Queries the cache rules of the domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: The cache rules of this domain name
        :rtype: dict
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.get_cache_rules(self._session)

    def get_domain_cache_rules_by_enterprise_project_id(self, domain, enterprise_project_id):
        """Queries the cache rules of the domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: The cache rules of this domain name
        :rtype: dict
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.get_cache_rules_by_enterprise_project_id(self._session, enterprise_project_id)

    def set_domain_https(self, domain, **attrs):
        """Configures the HTTPS of the acceleration domain name

        This method sets HTTPS by configuring the certificate of a domain name,
        and deploy the HTTPS configuration on all CDN nodes to implement
        secure acceleration.

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param dict attrs: Keyword arguments which contains cache policies
            for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * cert_name: The certificate name. Mandatory.
            * https_status: The mode of HTTPS certificate is enabled.
                0-disabled, 1-enabled in serving and retrieving sources,
                2-only enabled in serving.
                Mandatory.
            * certificate: The certificate content used by HTTPS, PEM format.
                Optional when https_status is 0.
            * private_key: The private key content used by HTTPS, PEM format.
                Optional when https_status is 0.
            * force_redirect_https: Whether to force the client request to be
                redirected. 1: yes. 0: no. Optional.
            * http2: Whether to use HTTP 2.0. 1: yes. 0: no. Optional.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_https(self._session, **attrs)

    def set_domain_https_by_enterprise_project_id(self, domain, enterprise_project_id, **attrs):
        """Configures the HTTPS of the acceleration domain name

        This method sets HTTPS by configuring the certificate of a domain name,
        and deploy the HTTPS configuration on all CDN nodes to implement
        secure acceleration.

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.
        :param dict attrs: Keyword arguments which contains cache policies
            for :class:`~openstack.cdn.v1.domain.Domain`.
            Available attributes include:

            * cert_name: The certificate name. Mandatory.
            * https_status: The mode of HTTPS certificate is enabled.
                0-disabled, 1-enabled in serving and retrieving sources,
                2-only enabled in serving.
                Mandatory.
            * certificate: The certificate content used by HTTPS, PEM format.
                Optional when https_status is 0.
            * private_key: The private key content used by HTTPS, PEM format.
                Optional when https_status is 0.
            * force_redirect_https: Whether to force the client request to be
                redirected. 1: yes. 0: no. Optional.
            * http2: Whether to use HTTP 2.0. 1: yes. 0: no. Optional.

        :returns: One :class:`~openstack.cdn.v1.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.set_https_by_enterprise_project_id(self._session, enterprise_project_id, **attrs)

    def get_domain_https(self, domain):
        """Obtains the certificate for the acceleration domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: The HTTPS certificate of this domain name
        :rtype: dict
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.get_https(self._session)

    def get_domain_https_by_enterprise_project_id(self, domain, enterprise_project_id):
        """Obtains the certificate for the acceleration domain name

        :param domain: The value can be either the ID of a domain name or a
                       :class:`~openstack.cdn.v1.domain.Domain` instance.

        :returns: The HTTPS certificate of this domain name
        :rtype: dict
        """
        res = self._get_resource(_domain.Domain, domain)
        return res.get_https_by_enterprise_project_id(self._session, enterprise_project_id)

    def tasks(self, page_size=100, page_number=1, **query):
        """List the cache refreshing or preheating tasks matching the query

        :param int page_size: The number of acceleration domain names on each
            page. The value ranges from 10 to 1000. Default to 100.
        :param int page_number: The page number that is queried. The value
            ranges from 1 to 65535. Default to 1.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
            the resources being returned. Available attributes include:

            * status: The status of a task after refreshing.
                'task_done' indicates the refreshing task is completed
                successfully.
                'task_inprocess' indicates that the refreshing task is being
                processed.
            * start_date: The start time of a query, which is expressed as
                milliseconds since 1970-01-01 00:00:00 UTC.
            * end_date: The end time of a query, which is expressed as
                milliseconds since 1970-01-01 00:00:00 UTC.
            * order_field: The field based on which tasks are sorted.
                Supported fields include 'task_type', 'total', 'processing',
                'succeeded', 'failed', and 'created_at'.
                You must specify the values for both 'order_field' and
                'order_type'.
            * order_type: The type of ordering.
                The value is either 'desc' or 'asc'.
            * user_domain_id: The domain ID of a specified user.

        :returns: A generator of Task objects
        :rtype: :class:`~openstack.cdn.v1.task.Task`
        """
        query = query or {}
        query.update(page_size=page_size, page_number=page_number,
                     paginated=True)
        return self._list(_task.Task, **query)

    def get_task(self, task):
        """Get details about a cache refreshing or preheating task

        :param task: The value can be the ID of a task or a
                       :class:`~openstack.cdn.v1.task.Task` instance.

        :returns: One :class:`~openstack.cdn.v1.task.Task`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_task.Task, task)

    def create_refresh_task(self, **attrs):
        """Create a new cache refresh task from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.cdn.v1.task.RefreshTask`,
            comprised of the properties on the RefreshTask class.
            Available attributes include:

            * type: The type of cache contents to be refreshed. The value is
                either 'file' or 'directory'. The default value is 'file'.
            * urls: The list of urls to refresh.

        :returns: The results of the refresh task creation
        :rtype: :class:`~openstack.cdn.v1.task.RefreshTask`
        """
        return self._create(_task.RefreshTask, **attrs)

    def create_preheat_task(self, **attrs):
        """Create a new preheat task from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.cdn.v1.task.PreheatTask`,
            comprised of the properties on the PreheatTask class.
            Available attributes include:

            * urls: The list of urls to preheat.

        :returns: The results of the preheat task creation
        :rtype: :class:`~openstack.cdn.v1.task.PreheatTask`
        """
        return self._create(_task.PreheatTask, **attrs)

    def logs(self, domain_name, query_date,
             page_size=100, page_number=1, **query):
        """List the logs matching the query

        :param str domain_name: The name of the acceleration domain name.
        :param int query_date: The date that you want to query, which is
            expressed as milliseconds since 1970-01-01 00:00:00 UTC.
        :param int page_size: The number of logs on each page.
            The value ranges from 10 to 1000. Default to 100.
        :param int page_number: The page number that is queried. The value
            ranges from 1 to 65535. Default to 1.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
            the resources being returned.

        :returns: A generator of Task objects
        :rtype: :class:`~openstack.cdn.v1.log.Log`
        """
        query = query or {}
        query.update(domain_name=domain_name, query_date=query_date,
                     page_size=page_size, page_number=page_number,
                     paginated=True)
        return self._list(_log.Log, **query)

    def logs_by_enterprise_project_id(self, domain_name, query_date, enterprise_project_id,
             page_size=100, page_number=1, **query):
        """List the logs matching the query

        :param str domain_name: The name of the acceleration domain name.
        :param int query_date: The date that you want to query, which is
            expressed as milliseconds since 1970-01-01 00:00:00 UTC.
        :param int page_size: The number of logs on each page.
            The value ranges from 10 to 1000. Default to 100.
        :param int page_number: The page number that is queried. The value
            ranges from 1 to 65535. Default to 1.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
            the resources being returned.

        :returns: A generator of Task objects
        :rtype: :class:`~openstack.cdn.v1.log.Log`
        """
        query = query or {}
        query.update(domain_name=domain_name, query_date=query_date,
                     page_size=page_size, page_number=page_number,
                     enterprise_project_id=enterprise_project_id, paginated=True)
        return self._list(_log.Log, **query)

    def query_network_traffic(self, **query):
        """Queries the total network traffic

        :param \*\*query: The query parameters. Available parameters include:

            * start_time: The timestamp marking the start of the query.
                Optional.
            * end_time: The timestamp marking the end of the query. Optional.
            * domain_name: A domain name list. Use commas (,) to separate
                domain names from each other.
                For example, 'www.test1.com,www.test2.com'.
                The value 'ALL' indicates that all domain names under
                a tenant are queried.
                Mandatory.

        :returns: The total network traffic matching the query
        :rtype: :class:`~openstack.cdn.v1.statistic.NetworkTraffic`
        """
        res = self._get_resource(_statistic.NetworkTraffic, None)
        return res.query(self._session, **query)

    def query_network_traffic_detail(self, **query):
        """Queries the details of network traffic

        :param \*\*query: The query parameters. Available parameters include:

            * start_time: The timestamp marking the start of the query.
            * end_time: The timestamp marking the end of the query.
            * domain_name: A domain name list. Use commas (,) to separate
                domain names from each other.
                For example, 'www.test1.com,www.test2.com'.
                The value 'ALL' indicates that all domain names under
                a tenant are queried.
            * interval: The granularity of a time span during which the traffic
                is monitored. It is measured by seconds. Available values are:

                For a time span of 1 day, the value of interval can be
                5 minutes, 1 hour, 4 hours, or 8 hours.

                For a time span of 2 to 7 days, the value of interval can be
                1 hour, 4 hours, 8 hours, or 1 day.

                For a time span of 8 to 31 days, the value of interval can be
                4 hours, 8 hours, or 1 day.

                If you do not specify a value for interval, the system uses
                the smallest value corresponding to the queried time span.
                Convert an interval into seconds, if you need to specify it
                in the request.

        :returns: The network traffic data matching the query
        :rtype: :class:`~openstack.cdn.v1.statistic.NetworkTrafficDetail`
        """
        res = self._get_resource(_statistic.NetworkTrafficDetail, None)
        return res.query(self._session, **query)

    def query_bandwidth_peak(self, **query):
        """Queries the bandwidth peak value

        :param \*\*query: The query parameters. Available parameters include:

            * start_time: The timestamp marking the start of the query.
                Optional.
            * end_time: The timestamp marking the end of the query. Optional.
            * domain_name: A domain name list. Use commas (,) to separate
                domain names from each other.
                For example, 'www.test1.com,www.test2.com'.
                The value 'ALL' indicates that all domain names under
                a tenant are queried.
                Mandatory.

        :returns: The bandwidth peak value matching the query
        :rtype: :class:`~openstack.cdn.v1.statistic.BandwidthPeak`
        """
        res = self._get_resource(_statistic.BandwidthPeak, None)
        return res.query(self._session, **query)

    def query_bandwidth(self, **query):
        """Queries the bandwidth details

        :param \*\*query: The query parameters. Available parameters include:

            * start_time: The timestamp marking the start of the query.
                Optional.
            * end_time: The timestamp marking the end of the query. Optional.
            * domain_name: A domain name list. Use commas (,) to separate
                domain names from each other.
                For example, 'www.test1.com,www.test2.com'.
                The value 'ALL' indicates that all domain names under
                a tenant are queried.
                Mandatory.
            * interval: The granularity of a time span during which the traffic
                is monitored. It is measured by seconds. Available values are:

                For a time span of 1 day, the value of interval can be
                5 minutes, 1 hour, 4 hours, or 8 hours.

                For a time span of 2 to 7 days, the value of interval can be
                1 hour, 4 hours, 8 hours, or 1 day.

                For a time span of 8 to 31 days, the value of interval can be
                4 hours, 8 hours, or 1 day.

                If you do not specify a value for interval, the system uses
                the smallest value corresponding to the queried time span.
                Convert an interval into seconds, if you need to specify it
                in the request.
                Optional.

        :returns: The bandwidth peak value matching the query
        :rtype: :class:`~openstack.cdn.v1.statistic.BandwidthDetail`
        """
        res = self._get_resource(_statistic.BandwidthDetail, None)
        return res.query(self._session, **query)

    def query_summary(self, **query):
        """Queries summary information of data type and domains in the interval

        :param \*\*query: The query parameters. Available parameters include:

            * start_time: The timestamp marking the start of the query.
                Optional.
            * end_time: The timestamp marking the end of the query. Optional.
            * domain_name: A domain name list. Use commas (,) to separate
                domain names from each other.
                For example, 'www.test1.com,www.test2.com'.
                The value 'ALL' indicates that all domain names under
                a tenant are queried.
                Mandatory.
            * stat_type: The types of statistics. Available values include:
                'bw' (bandwidth),
                'flux',
                'bs_bw' (retrieval bandwidth),
                'bs_flux' (retrieval flux),
                'req_num' (number of total requests, or PVs),
                'req_hit_rate' (rate of hitting requests),
                'flux_hit_rate' (rate of hitting flux),
                'bs_fail_rate' (rate of retrieval failures),
                'qps' (requests per second),
                'http_code_2xx' (status code 2xx),
                'http_code_3xx' (status code 3xx),
                'http_code_4xx' (status code 4xx),
                'http_code_5xx' (status code 5xx),
                'bs_num' (total number of retrieval requests),
                'bs_fail_num' (number of content retrieval failures).
                Mandatory.
            * service_area: Includes mainland_china and outside_mainland_china.
                Optional. Default to mainland_china.

        :returns: The summary data matching the query
        :rtype: :class:`~openstack.cdn.v1.statistic.ConsumptionSummary`
        """
        res = self._get_resource(_statistic.ConsumptionSummary, None)
        return res.query(self._session, **query)

    def query_summary_detail(self, **query):
        """Queries details information of data type and domains in the interval

        :param \*\*query: The query parameters. Available parameters include:

            * start_time: The timestamp marking the start of the query.
                Optional.
            * end_time: The timestamp marking the end of the query. Optional.
            * domain_name: A domain name list. Use commas (,) to separate
                domain names from each other.
                For example, 'www.test1.com,www.test2.com'.
                The value 'ALL' indicates that all domain names under
                a tenant are queried.
                Mandatory.
            * interval: The granularity of a time span during which the traffic
                is monitored. It is measured by seconds. Available values are:

                For a time span of 1 day, the value of interval can be
                5 minutes, 1 hour, 4 hours, or 8 hours.

                For a time span of 2 to 7 days, the value of interval can be
                1 hour, 4 hours, 8 hours, or 1 day.

                For a time span of 8 to 31 days, the value of interval can be
                4 hours, 8 hours, or 1 day.

                If you do not specify a value for interval, the system uses
                the smallest value corresponding to the queried time span.
                Convert an interval into seconds, if you need to specify it
                in the request.
                Optional.
            * stat_type: The types of statistics. Available values include:
                'bw' (bandwidth),
                'flux',
                'bs_bw' (retrieval bandwidth),
                'bs_flux' (retrieval flux),
                'req_num' (number of total requests, or PVs),
                'req_hit_rate' (rate of hitting requests),
                'flux_hit_rate' (rate of hitting flux),
                'bs_fail_rate' (rate of retrieval failures),
                'qps' (requests per second),
                'http_code_2xx' (status code 2xx),
                'http_code_3xx' (status code 3xx),
                'http_code_4xx' (status code 4xx),
                'http_code_5xx' (status code 5xx),
                'bs_num' (total number of retrieval requests),
                'bs_fail_num' (number of content retrieval failures).
                Mandatory.
            * service_area: Includes mainland_china and outside_mainland_china.
                Optional. Default to mainland_china.

        :returns: The summary detail data matching the query
        :rtype: :class:`~openstack.cdn.v1.statistic.ConsumptionSummaryDetail`
        """
        res = self._get_resource(_statistic.ConsumptionSummaryDetail, None)
        return res.query(self._session, **query)

    def summaries(self, **query):
        """Queries summaries of data type in the interval for each domain

        :param \*\*query: The query parameters. Available parameters include:

            * start_time: The timestamp marking the start of the query.
                Optional.
            * end_time: The timestamp marking the end of the query. Optional.
            * domain_name: A domain name list. Use commas (,) to separate
                domain names from each other.
                For example, 'www.test1.com,www.test2.com'.
                The value 'ALL' indicates that all domain names under
                a tenant are queried.
                Mandatory.
            * stat_type: The types of statistics. Available values include:
                'bw' (bandwidth),
                'flux',
                'bs_bw' (retrieval bandwidth),
                'bs_flux' (retrieval flux),
                'req_num' (number of total requests, or PVs),
                'req_hit_rate' (rate of hitting requests),
                'flux_hit_rate' (rate of hitting flux),
                'bs_fail_rate' (rate of retrieval failures),
                'qps' (requests per second),
                'http_code_2xx' (status code 2xx),
                'http_code_3xx' (status code 3xx),
                'http_code_4xx' (status code 4xx),
                'http_code_5xx' (status code 5xx),
                'bs_num' (total number of retrieval requests),
                'bs_fail_num' (number of content retrieval failures).
                Mandatory.
            * service_area: Includes mainland_china and outside_mainland_china.
                Optional. Default to mainland_china.

        :returns: A generator of Task objects
        :rtype: :class:`~openstack.cdn.v1.statistic.ConsumptionSummary`
        """
        return self._list(_statistic.ConsumptionSummaryByDomain, **query)
