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
# part 3: Refreshing and Preheating
# Querying a Cache Refreshing or Preheating Task
def query_task():
    print("query tasks by time:")
    now = time.time()
    end_date = int(now * 1000)
    start_date = end_date - 3600 * 1000
    tasks = conn.cdn.tasks(page_size=100, page_number=1, start_date=start_date, end_date=end_date)
    task_list = list(tasks)
    print(task_list)


# Querying Details About a Cache Refreshing or Preheating Task
def query_task_detail(_task_id):
    print("query task detail by id:")
    task_detail = conn.cdn.get_task(_task_id)
    print(task_detail)


if __name__ == "__main__":
    # new version API
    # part 3: Refreshing and Preheating
    # Querying a Cache Refreshing or Preheating Task
    query_task()

    # Querying Details About a Cache Refreshing or Preheating Task
    task_id = 'xxxxxxx'
    query_task_detail(task_id)
