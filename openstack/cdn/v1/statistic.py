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

import abc
import six

from openstack.cdn import cdn_resource
from openstack.cdn import cdn_service
from openstack import resource2 as resource


@six.add_metaclass(abc.ABCMeta)
class Statistic(cdn_resource.Resource):
    base_path = None
    resource_key = None
    resources_key = None
    service = cdn_service.CDNService()

    allow_create = False
    allow_get = False
    allow_update = False
    allow_delete = False
    allow_list = False

    _query_mapping = cdn_resource.StatisticParameters()

    #: The timestamp marking the start of the query, which is expressed as
    #: milliseconds since 1970-01-01 00:00:00 UTC.
    start_time = resource.Body('start_time')
    #: The timestamp marking the end of the query, which is expressed as
    #: milliseconds since 1970-01-01 00:00:00 UTC.
    end_time = resource.Body('end_time')
    #: The value matching the query.
    value = resource.Body('value')

    def query(self, session, **query):
        """Queries the total network traffic

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param \*\*query: The query parameters. Available parameters include:

            * start_time: The timestamp marking the start of the query.
            * end_time: The timestamp marking the end of the query.
            * domain_name: A domain name list. Use commas (,) to separate
                domain names from each other.
                For example, 'www.test1.com,www.test2.com'.
                The value 'ALL' indicates that all domain names under
                a tenant are queried.

        :returns: The total network traffic matching the query
        :rtype: subclass of :class:`~openstack.cdn.v1.statistic.Statistic`
        """
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(self.base_path, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           params=query)
        self._translate_response(resp)
        return self


@six.add_metaclass(abc.ABCMeta)
class StatisticDetail(cdn_resource.Resource):
    base_path = None
    resource_key = None
    resources_key = None
    service = cdn_service.CDNService()

    allow_create = False
    allow_get = False
    allow_update = False
    allow_delete = False
    allow_list = False

    _query_mapping = cdn_resource.StatisticParameters('interval')

    #: The timestamp marking the start of the query, which is expressed as
    #: milliseconds since 1970-01-01 00:00:00 UTC.
    start_time = resource.Body('start_time')
    #: The timestamp marking the end of the query, which is expressed as
    #: milliseconds since 1970-01-01 00:00:00 UTC.
    end_time = resource.Body('end_time')
    #: The granularity of a time span during which the data is monitored.
    #: It is measured by seconds.
    interval = resource.Body('interval', type=int)
    #: The values matching the query.
    values = resource.Body('values', type=list)

    def query(self, session, **query):
        """Queries the detail of the statistic

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param \*\*query: The query parameters. Available parameters include:

        :returns: The statistic data matching the query
        :rtype: subclasses of
                :class:`~openstack.cdn.v1.statistic.StatisticDetail`
        """
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(self.base_path, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           params=query)
        self._translate_response(resp)
        return self


class NetworkTraffic(Statistic):
    base_path = '/cdn/statistics/flux'
    resource_key = 'flux'


class NetworkTrafficDetail(StatisticDetail):
    base_path = '/cdn/statistics/flux-detail'
    resource_key = 'flux_detail'


class BandwidthPeak(Statistic):
    base_path = '/cdn/statistics/bandwidth'
    resource_key = 'bandwidth'

    #: The timestamp when the peak occured.
    peaked_at = resource.Body('peak_time')


class BandwidthDetail(StatisticDetail):
    base_path = '/cdn/statistics/bandwidth-detail'
    resource_key = 'bandwidth_detail'


class ConsumptionSummary(Statistic):
    base_path = '/cdn/statistics/domain-summary'
    resource_key = 'domain_summary'

    _query_mapping = cdn_resource.StatisticParameters('stat_type',
                                                      'service_area')

    #: The statistics type. Available values include:
    #: bw (bandwidth),
    #: flux,
    #: bs_bw (retrieval bandwidth),
    #: bs_flux (retrieval flux),
    #: req_num (number of total requests, or PVs),
    #: req_hit_rate (rate of hitting requests),
    #: flux_hit_rate (rate of hitting flux),
    #: bs_fail_rate (rate of retrieval failures),
    #: qps (requests per second),
    #: http_code_2xx (status code 2xx),
    #: http_code_3xx (status code 3xx),
    #: http_code_4xx (status code 4xx),
    #: http_code_5xx (status code 5xx),
    #: bs_num (total number of retrieval requests),
    #: bs_fail_num (number of content retrieval failures).
    stat_type = resource.Body('stat_type')
    #: Includes mainland_china and outside_mainland_china.
    service_area = resource.Body('service_area')


class ConsumptionSummaryDetail(StatisticDetail):
    base_path = '/cdn/statistics/domain-summary-detail'
    resource_key = 'domain_summary_detail'

    _query_mapping = cdn_resource.StatisticParameters('interval',
                                                      'stat_type',
                                                      'service_area')

    #: The statistics type. Available values include:
    #: bw (bandwidth),
    #: flux,
    #: bs_bw (retrieval bandwidth),
    #: bs_flux (retrieval flux),
    #: req_num (number of total requests, or PVs),
    #: req_hit_rate (rate of hitting requests),
    #: flux_hit_rate (rate of hitting flux),
    #: bs_fail_rate (rate of retrieval failures),
    #: qps (requests per second),
    #: http_code_2xx (status code 2xx),
    #: http_code_3xx (status code 3xx),
    #: http_code_4xx (status code 4xx),
    #: http_code_5xx (status code 5xx),
    #: bs_num (total number of retrieval requests),
    #: bs_fail_num (number of content retrieval failures).
    stat_type = resource.Body('stat_type')
    #: Includes mainland_china and outside_mainland_china.
    service_area = resource.Body('service_area')


class ConsumptionSummaryByDomain(Statistic):
    base_path = '/cdn/statistics/domain'
    resources_key = 'domain'
    query_page_size_key = None
    query_page_number_key = None

    allow_list = True

    _query_mapping = cdn_resource.StatisticParameters('stat_type',
                                                      'service_area')

    #: The domain name.
    domain_name = resource.Body('domain_name')
    #: The statistics type. Available values include:
    #: bw (bandwidth),
    #: flux,
    #: bs_bw (retrieval bandwidth),
    #: bs_flux (retrieval flux),
    #: req_num (number of total requests, or PVs),
    #: req_hit_rate (rate of hitting requests),
    #: flux_hit_rate (rate of hitting flux),
    #: bs_fail_rate (rate of retrieval failures),
    #: qps (requests per second),
    #: http_code_2xx (status code 2xx),
    #: http_code_3xx (status code 3xx),
    #: http_code_4xx (status code 4xx),
    #: http_code_5xx (status code 5xx),
    #: bs_num (total number of retrieval requests),
    #: bs_fail_num (number of content retrieval failures).
    stat_type = resource.Body('stat_type')
    #: Includes mainland_china and outside_mainland_china.
    service_area = resource.Body('service_area')
