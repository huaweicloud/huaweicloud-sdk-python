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


def list_logs(domain_name, query_date):
    # example: query_date = '1532620800000'
    logs = conn.cdn.logs(domain_name=domain_name, query_date=query_date, page_number=1, page_size=10)
    log_list = list(logs)
    print(log_list)
    # for log in conn.cdn.logs(domain_name=domain_name, query_date=today):
    #     print(log)


def list_logs_by_enterprise_project_id(domain_name, query_date, enterprise_project_id):
    # example: query_date = '1532620800000'
    logs = conn.cdn.logs_by_enterprise_project_id(domain_name=domain_name, query_date=query_date, page_number=1,
                                                  page_size=10,
                                                  enterprise_project_id=enterprise_project_id)
    log_list = list(logs)
    print(log_list)


if __name__ == "__main__":
    today = int(time.time() * 1000) - 24 * 3600 * 1000
    domain = "xxxxxxxxxxx"
    enterprise_project_id_sample = "xxxxxxxxxxx"
    list_logs(domain, today)
    list_logs_by_enterprise_project_id(domain, today, enterprise_project_id_sample)
