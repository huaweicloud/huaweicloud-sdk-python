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
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'xxxxxxxxxxx')

# token认证
# username = "xxxxxxxxxxx"
# password = "xxxxxxxxxxx"
# projectId = "xxxxxxxxxxx"
# userDomainId = "xxxxxxxxxxx"
# auth_url = "xxxxxxxxxxx"
#
# conn = connection.Connection(
#     auth_url=auth_url,
#     user_domain_id=userDomainId,
#     project_id=projectId,
#     username=username,
#     password=password
# )

# AKSK认证
projectId = "xxxxxxxxxxx"
domain = "xxxxxxxxxxx"   # cdn use: domain = "myhwclouds.com"
region= "xxxxxxxxxxx"    # example: region = "cn-north-1"
AK = "xxxxxxxxxxx"
SK = "xxxxxxxxxxx"

conn = connection.Connection(
              project_id=projectId,
              domain=domain,
              region=region,
              ak=AK,
              sk=SK)

def preheattask(preheatTask):
    print("preheat urls or dirs:")
    preheattask = conn.cdn.create_preheat_task(**preheatTask)
    print(preheattask)

if __name__ == "__main__":
    preheatTask={
        "urls": ["xxxxxxxxxxx",
                 "xxxxxxxxxxx"]
    }
    preheattask(preheatTask)

