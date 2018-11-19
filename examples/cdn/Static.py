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
import sys
import time
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'xxxxxxxxxxxxxxxx')

username = "xxxxxxxxxxxxxxxx"
password = "xxxxxxxxxxxxxxxx"
projectId = "xxxxxxxxxxxxxxxx"
userDomainId = "xxxxxxxxxxxxxxxx"
auth_url = "xxxxxxxxxxxxxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


# AKSK
# os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'xxxxxxxxxxxxxxxx')
# projectId = "xxxxxxxxxxxxxxxx"
# domain = "xxxxxxxxxxxxxxxx"
# region= "xxxxxxxxxxxxxxxx"
# AK = "xxxxxxxxxxxxxxxx"
# SK = "xxxxxxxxxxxxxxxx"
#
# conn = connection.Connection(
#               project_id=projectId,
#               domain=domain,
#               region=region,
#               ak = AK,
#               sk = SK)

def query_total_flux(domain_name, start_time, end_time, enterprise_project_id):
    print('Query the total network traffic: ')
    total_traffic = conn.cdn.query_network_traffic(domain_name=domain_name, start_time=start_time, end_time=end_time, enterprise_project_id=enterprise_project_id)
    print(total_traffic)

def query_detail_flux(domain_name, start_time, end_time, enterprise_project_id):
    print('Query the network traffic detail: ')
    traffic_detail = conn.cdn.query_network_traffic_detail(domain_name=domain_name, start_time=start_time, end_time=end_time, interval=300, enterprise_project_id=enterprise_project_id)
    print(traffic_detail)

def query_bandwidth_peak(domain_name, start_time, end_time, enterprise_project_id):
    print('Query bandwidth peak: ')
    bandwidth_peak = conn.cdn.query_bandwidth_peak(domain_name=domain_name, start_time=start_time, end_time=end_time, enterprise_project_id=enterprise_project_id)
    print(bandwidth_peak)

def query_detail_bandwidth(domain_name, start_time, end_time, enterprise_project_id):
    print('Query bandwidth peak detail: ')
    bandwidth = conn.cdn.query_bandwidth(domain_name=domain_name, start_time=start_time, end_time=end_time, interval=300, enterprise_project_id=enterprise_project_id)
    print(bandwidth)

def query_summary_by_type(domain_name, start_time, end_time, query_type, enterprise_project_id):
    print('Query static summary by type - ' + query_type + ': ')
    summary = conn.cdn.query_summary(domain_name=domain_name, start_time=start_time, end_time=end_time, stat_type=query_type, service_area='mainland_china', enterprise_project_id=enterprise_project_id)
    print(summary)

def query_summary_detail_by_type(domain_name, start_time, end_time, query_type, enterprise_project_id):
    print('Query static summary detail by type - ' + query_type + ': ')
    summary = conn.cdn.query_summary_detail(domain_name=domain_name, start_time=start_time, end_time=end_time, stat_type=query_type, service_area='mainland_china', enterprise_project_id=enterprise_project_id)
    print(summary)

def query_domains_summary_detail_by_type(domain_name, start_time, end_time, query_type, enterprise_project_id):
    print('Query static domains summary detail by type - ' + query_type + ': ')
    summaries = conn.cdn.summaries(domain_name=domain_name, start_time=start_time, end_time=end_time, stat_type=query_type, service_area='mainland_china', enterprise_project_id=enterprise_project_id)
    for summary in summaries:
        print(summary)


if __name__ == "__main__":
    end_time = int(time.time() * 1000)
    start_time = end_time - 3600000
    domain_name = "ALL"
    enterprise_project_id = ""

    query_total_flux(domain_name, start_time, end_time, enterprise_project_id)

    query_detail_flux(domain_name, start_time, end_time, enterprise_project_id)

    query_bandwidth_peak(domain_name, start_time, end_time, enterprise_project_id)

    query_detail_bandwidth(domain_name, start_time, end_time, enterprise_project_id)

    for query_type in ['bw', 'flux', 'bs_bw', 'bs_flux', 'req_num', 'req_hit_rate', 'flux_hit_rate', 'bs_fail_rate', 'qps', 'http_code_2xx', 'http_code_3xx', 'http_code_4xx', 'http_code_5xx']:
        query_summary_by_type(domain_name, start_time, end_time, query_type, enterprise_project_id)

    for query_type in ['bw', 'flux', 'bs_bw', 'bs_flux', 'req_num', 'req_hit_rate', 'flux_hit_rate', 'bs_fail_rate', 'qps', 'http_code_2xx', 'http_code_3xx', 'http_code_4xx', 'http_code_5xx']:
        query_summary_detail_by_type(domain_name, start_time, end_time, query_type, enterprise_project_id)

    domain_name = "cdn-python-sdk-a.example.com,cdn-python-sdk.example.com.com"
    start_time = end_time - 23 * 3600 * 1000
    for query_type in ['bw', 'flux', 'bs_bw', 'bs_flux', 'req_num', 'req_hit_rate', 'flux_hit_rate', 'bs_fail_rate', 'qps', 'http_code_2xx', 'http_code_3xx', 'http_code_4xx', 'http_code_5xx']:
        query_domains_summary_detail_by_type(domain_name, start_time, end_time, query_type, enterprise_project_id)

