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

# utils.enable_logging(debug = True, stream = sys.stdout)

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


def test_show_all_lb():
    lbs = list(conn.network.loadbalancers())
    print("lbs number : ", len(lbs))
    for lb in lbs:
        print(lb)


def test_show_lb(lb_id):
    lb = conn.network.get_loadbalancer(lb_id)
    print(lb)


def test_show_lb_stree(lb_id):
    st = conn.network.get_loadbalancer_status_stree(lb_id)
    print(st)


def test_create_lb(subnet_id):
    _lb = {
        "name": "ulb-python-test",
        "vip_subnet_id": subnet_id,
        "description": 'this is a test'
    }
    # lbs = list(conn.network.loadbalancers())
    # while len(lbs) <= 10:
    #     lbs.append(conn.network.create_loadbalancer(**_lb))
    lb = conn.network.create_loadbalancer(**_lb)
    print(lb)
    return lb


def test_update_lb(lb_id):
    lb_new = conn.network.update_loadbalancer(lb_id, description='this is test', name='ulb-test')
    print(lb_new)


def test_delete_lb(lb_id):
    conn.network.delete_loadbalancer(lb_id)


if __name__ == "__main__":
    subnet_id = "d5a27dd4-2dc0-4634-a42d-256e3762b990"
    lb = test_create_lb(subnet_id)
    test_update_lb(lb.id)
    test_show_lb(lb.id)
    test_show_lb_stree(lb.id)
    test_show_all_lb()
    test_delete_lb(lb.id)
