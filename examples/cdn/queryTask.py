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

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'https://cdn.yyy.com/v1.0')

username = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"
projectId = "xxxxxxxxxxx"
userDomainId = "xxxxxxxxxxx"
auth_url = "https://iam.xxx.yyy.com/v3"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)

def queryTask():
    print("query tasks by time:")
    now = time.time()
    end_date = int(now * 1000)
    start_date = end_date - 3600* 1000
    tasks = conn.cdn.tasks(page_size=100, page_number=1, start_date=start_date, end_date=end_date)
    task_list = list(tasks)
    print(task_list)

    print("\nquery task detail by id:")
    task_id = task_list[0].id
    task_detail = conn.cdn.get_task(task_id)
    print(task_detail)

if __name__ == "__main__":
    queryTask()
