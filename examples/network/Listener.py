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


def test_show_all_listener():
    _lss = list(conn.network.listeners())
    print("listener number : ", len(_lss))
    for _ls in _lss:
        print(_ls)


def test_show_listener(ls_id):
    _ls = conn.network.get_listener(ls_id)
    print(_ls)


def test_create_listener(lb_id):
    _ls = conn.network.create_listener(protocol_port = 20,
                                      protocol= 'TCP',
                                      loadbalancer_id = lb_id)
    print(_ls)
    return _ls


def test_update_listener(ls_id):
    ls_old = conn.network.get_listener(ls_id)
    ls_new = conn.network.update_listener(ls_old, name = 'test-update-ls',
                                          description = 'listener update test')
    print(ls_new)


def test_delete_listener(ls_id):
    conn.network.delete_listener(ls_id)


if __name__ == "__main__":
    lb_id = "3784fefc-24da-49a2-9463-b2b751090755"
    ls = test_create_listener(lb_id)
    test_update_listener(ls.id)
    test_show_listener(ls.id)
    test_show_all_listener()
    test_delete_listener(ls.id)