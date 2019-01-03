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

import sys
from openstack import connection
from openstack import utils

# utils.enable_logging(debug=True, stream=sys.stdout)

username = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"
projectId = "xxxxxxxxxxx"
userDomainId = "xxxxxxxxxx"
auth_url = "xxxxxxxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


def test_show_all_hm():
    hms = list(conn.network.healthmonitors())
    print("healthmonitor numbers: ", len(hms))
    for hm in hms:
        print(hm)


def test_show_hm(hm_id):
    print(conn.network.get_healthmonitor(hm_id))


def test_create_hm(pool_id):
    hm = conn.network.create_healthmonitor(type = 'HTTP', delay = 10, timeout = 5,
                                           max_retries = 3, pool_id = pool_id)
    return hm


def test_update_hm(hm_id):
    hm = conn.network.update_healthmonitor(hm_id,delay = 10,
                                           max_retries= 5,
                                           name = 'updated-name',
                                           timeout = 3,
                                           http_method='POST',
                                           expected_codes = '200',
                                           url_path = '/',
                                           monitor_port = 8000
                                           )
    return hm


def test_delete_hm(hm_id):
    conn.network.delete_healthmonitor(hm_id)


if __name__ == "__main__":
    # a pool without health check
    pool_id = "852ea8da-9b84-4998-ad14-83035fbea79e"
    hm = test_create_hm(pool_id)
    hm_update = test_update_hm(hm.id)
    test_show_hm(hm_update.id)
    test_show_all_hm()
    test_delete_hm(hm_update.id)