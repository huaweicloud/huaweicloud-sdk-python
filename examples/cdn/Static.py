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

import os
import time
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE',
                      'xxxxxxxxxxx')  # CDN API url,example:https://cdn.myhuaweicloud.com/v1.0/

# AKSK Auth
projectId = "xxxxxxxxxxx"  # Project ID of cn-north-1
cloud = "xxxxxxxxxxx"  # cdn use: cloud = "myhuaweicloud.com"
region = "xxxxxxxxxxx"  # example: region = "cn-north-1"
AK = "xxxxxxxxxxx"
SK = "xxxxxxxxxxx"

conn = connection.Connection(
    project_id=projectId,
    cloud=cloud,
    region=region,
    ak=AK,
    sk=SK)


# token Auth
# username = "xxxxxxxxxxx"  # IAM User Name
# password = "xxxxxxxxxxx"  # IAM User Password
# projectId = "xxxxxxxxxxx"  # Project ID of cn-north-1
# userDomainId = "xxxxxxxxxxx"  # Account ID
# auth_url = "xxxxxxxxxxx"  # IAM auth url,example: https://iam.myhuaweicloud.com/v3
#
# conn = connection.Connection(
#     auth_url=auth_url,
#     user_domain_id=userDomainId,
#     project_id=projectId,
#     username=username,
#     password=password
# )


# new version API
# part 4: Statistics Analysis
# Querying Details About Top 100 URLs
def query_top_url(domain_name, stat_type, start_time, end_time, service_area, enterprise_project_id):
    print('Query top-url: ')
    result = conn.cdn.query_top_url(domain_name=domain_name, stat_type=stat_type, start_time=start_time,
                                    end_time=end_time, service_area=service_area,
                                    enterprise_project_id=enterprise_project_id)
    print(result)
    print(result.top_url_summary[0]["url"])
    print(result.service_area)


# Querying Statistics About Domain Names in Batches
def query_domain_item_details(domain_name, start_time, end_time, stat_type, enterprise_project_id):
    print('Query domain-item-details: ')
    traffic_detail = conn.cdn.query_domain_item_details(domain_name=domain_name, start_time=start_time,
                                                        end_time=end_time, stat_type=stat_type,
                                                        enterprise_project_id=enterprise_project_id)
    print(traffic_detail)
    print(traffic_detail.start_time)
    print(traffic_detail.domains[0]['bw'])


# Querying Statistics About Domain Names by Region and Carrier in Batches
def query_domain_item_location_details(domain_name, start_time, end_time, stat_type, _region, isp,
                                       enterprise_project_id):
    print('Query domain-item-location-details: ')
    traffic_detail = conn.cdn.query_domain_item_location_details(domain_name=domain_name, start_time=start_time,
                                                                 end_time=end_time, stat_type=stat_type, region=_region,
                                                                 isp=isp,
                                                                 enterprise_project_id=enterprise_project_id)
    print(traffic_detail)
    print(traffic_detail.start_time)
    print(traffic_detail.domains[0]["domain_name"])


# old version API
# part 1: Statistics Analysis
# Querying the Total Network Traffic
def query_total_flux(domain_name, start_time, end_time, enterprise_project_id):
    print('Query the total network traffic: ')
    total_traffic = conn.cdn.query_network_traffic(domain_name=domain_name, start_time=start_time, end_time=end_time,
                                                   enterprise_project_id=enterprise_project_id)
    print(total_traffic)


# Querying Details of Network Traffic
def query_detail_flux(domain_name, start_time, end_time, enterprise_project_id):
    print('Query the network traffic detail: ')
    traffic_detail = conn.cdn.query_network_traffic_detail(domain_name=domain_name, start_time=start_time,
                                                           end_time=end_time, interval=300,
                                                           enterprise_project_id=enterprise_project_id)
    print(traffic_detail)


# Querying the Peak Bandwidth Value
def query_bandwidth_peak(domain_name, start_time, end_time, enterprise_project_id):
    print('Query bandwidth peak: ')
    bandwidth_peak = conn.cdn.query_bandwidth_peak(domain_name=domain_name, start_time=start_time, end_time=end_time,
                                                   enterprise_project_id=enterprise_project_id)
    print(bandwidth_peak)


# Querying Details of the Network Bandwidth
def query_detail_bandwidth(domain_name, start_time, end_time, enterprise_project_id):
    print('Query bandwidth peak detail: ')
    bandwidth = conn.cdn.query_bandwidth(domain_name=domain_name, start_time=start_time, end_time=end_time,
                                         interval=300, enterprise_project_id=enterprise_project_id)
    print(bandwidth)


# Querying Consumption Summary
def query_summary_by_type(domain_name, start_time, end_time, query_type, enterprise_project_id):
    print('Query static summary by type - ' + query_type + ': ')
    summary = conn.cdn.query_summary(domain_name=domain_name, start_time=start_time, end_time=end_time,
                                     stat_type=query_type, service_area='mainland_china',
                                     enterprise_project_id=enterprise_project_id)
    print(summary)


# Querying Consumption Details
def query_summary_detail_by_type(domain_name, start_time, end_time, query_type, enterprise_project_id):
    print('Query static summary detail by type - ' + query_type + ': ')
    summary = conn.cdn.query_summary_detail(domain_name=domain_name, start_time=start_time, end_time=end_time,
                                            stat_type=query_type, service_area='mainland_china',
                                            enterprise_project_id=enterprise_project_id)
    print(summary)


# Querying Consumption of Each Domain Name
def query_domains_summary_detail_by_type(domain_name, start_time, end_time, query_type, enterprise_project_id):
    print('Query static domains summary detail by type - ' + query_type + ': ')
    summaries = conn.cdn.summaries(domain_name=domain_name, start_time=start_time, end_time=end_time,
                                   stat_type=query_type, service_area='mainland_china',
                                   enterprise_project_id=enterprise_project_id)
    for summary in summaries:
        print(summary)


# Querying Domain Consumption by Region
def query_region_detail_summary(domain_name, stat_type, _region, start_time, end_time, enterprise_project_id):
    print('Query region-detail-summary: ')
    results = conn.cdn.query_region_detail_summary(domain_name=domain_name, stat_type=stat_type, region=_region,
                                                   start_time=start_time, end_time=end_time,
                                                   enterprise_project_id=enterprise_project_id)
    print(results.region_data)
    for result in results.region_data:
        print(result["region"] + ":" + str(result["value"]))


# Querying Domain Consumption by Carrier
def query_carrier_detail_summary(domain_name, stat_type, carrier, start_time, end_time, enterprise_project_id):
    print('Query carrier-detail-summary: ')
    results = conn.cdn.query_carrier_detail_summary(domain_name=domain_name, stat_type=stat_type, carrier=carrier,
                                                    start_time=start_time, end_time=end_time,
                                                    enterprise_project_id=enterprise_project_id)
    print(results.carrier_data)
    for result in results.carrier_data:
        print(result["carrier"] + ":" + str(result["value"]))


# Querying Statistics About Each Domain Name Under a Region or Carrier
def query_region_carrier_domain(domain_name, stat_type, _region, carrier, start_time, end_time, enterprise_project_id):
    print('Query region-carrier-domain: ')
    results = conn.cdn.query_region_carrier_domain(domain_name=domain_name, stat_type=stat_type, region=_region,
                                                   carrier=carrier, start_time=start_time, end_time=end_time,
                                                   enterprise_project_id=enterprise_project_id)
    print(results.domain)
    for result in results.domain:
        print(result["domain_name"] + ":" + str(result["value"]))


# Querying Statistics About Domain Names Under a Region or Carrier
def query_region_carrier_detail(domain_name, stat_type, _region, carrier, start_time, end_time, interval,
                                enterprise_project_id):
    print('Query region-carrier-detail: ')
    results = conn.cdn.query_region_carrier_detail(domain_name=domain_name, stat_type=stat_type, region=_region,
                                                   carrier=carrier, start_time=start_time, end_time=end_time,
                                                   interval=interval,
                                                   enterprise_project_id=enterprise_project_id)
    print(results)
    print(results.values)


if __name__ == "__main__":
    end_time_example = int(time.time() * 1000)
    start_time_example = end_time_example - 3600000
    domain_name_example = "cdn-python-sdk-a.example.com,cdn-python-sdk.example.com"
    stat_type_example = "flux"
    region_example = "ALL"
    isp_example = "CTCC"
    interval_example = 300
    service_area_example = "mainland_china"
    enterprise_project_id_example = "ALL"

    # new version API
    # part 4: Statistics Analysis
    # Querying Details About Top 100 URLs
    query_top_url(domain_name_example, stat_type_example, 1575043200000, 1575079200000, service_area_example,
                  enterprise_project_id_example)

    # Querying Statistics About Domain Names in Batches
    query_domain_item_details(domain_name_example, start_time_example, end_time_example, stat_type_example,
                              enterprise_project_id_example)

    # Querying Statistics About Domain Names by Region and Carrier in Batches
    query_domain_item_location_details(domain_name_example, start_time_example, end_time_example, stat_type_example,
                                       region_example, isp_example, enterprise_project_id_example)

    # old version API
    # part 1: Statistics Analysis
    # Querying the Total Network Traffic
    query_total_flux(domain_name_example, start_time_example, end_time_example, enterprise_project_id_example)

    # Querying Details of Network Traffic
    query_detail_flux(domain_name_example, start_time_example, end_time_example, enterprise_project_id_example)

    # Querying the Peak Bandwidth Value
    query_bandwidth_peak(domain_name_example, start_time_example, end_time_example, enterprise_project_id_example)

    # Querying Details of the Network Bandwidth
    query_detail_bandwidth(domain_name_example, start_time_example, end_time_example, enterprise_project_id_example)

    # Querying Consumption Summary
    for query_type_sample in ['bw', 'flux', 'bs_bw', 'bs_flux', 'req_num', 'req_hit_rate', 'flux_hit_rate',
                              'bs_fail_rate',
                              'qps', 'http_code_2xx', 'http_code_3xx', 'http_code_4xx', 'http_code_5xx']:
        query_summary_by_type(domain_name_example, start_time_example, end_time_example, query_type_sample,
                              enterprise_project_id_example)

    # Querying Consumption Details
    for query_type_sample in ['bw', 'flux', 'bs_bw', 'bs_flux', 'req_num', 'req_hit_rate', 'flux_hit_rate',
                              'bs_fail_rate',
                              'qps', 'http_code_2xx', 'http_code_3xx', 'http_code_4xx', 'http_code_5xx']:
        query_summary_detail_by_type(domain_name_example, start_time_example, end_time_example, query_type_sample,
                                     enterprise_project_id_example)

    # Querying Consumption of Each Domain Name
    for query_type_sample in ['bw', 'flux', 'bs_bw', 'bs_flux', 'req_num', 'req_hit_rate', 'flux_hit_rate',
                              'bs_fail_rate', 'qps', 'http_code_2xx', 'http_code_3xx', 'http_code_4xx',
                              'http_code_5xx']:
        query_domains_summary_detail_by_type(domain_name_example, start_time_example, end_time_example,
                                             query_type_sample, enterprise_project_id_example)

    # Querying Domain Consumption by Region
    query_region_detail_summary(domain_name_example, stat_type_example, region_example, start_time_example,
                                end_time_example, enterprise_project_id_example)

    # Querying Domain Consumption by Carrier
    query_carrier_detail_summary(domain_name_example, stat_type_example, isp_example, start_time_example,
                                 end_time_example, enterprise_project_id_example)

    # Querying Statistics About Each Domain Name Under a Region or Carrier
    query_region_carrier_domain(domain_name_example, stat_type_example, region_example, isp_example, start_time_example,
                                end_time_example, enterprise_project_id_example)

    # Querying Statistics About Domain Names Under a Region or Carrier
    query_region_carrier_detail(domain_name_example, stat_type_example, region_example, isp_example, start_time_example,
                                end_time_example, interval_example, enterprise_project_id_example)
