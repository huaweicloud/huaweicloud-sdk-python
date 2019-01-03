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


def test_show_all_members(pool_id):
    ms = list(conn.network.members(pool_id = pool_id))
    print("member numbers: ", len(ms))
    for m in ms:
        print(m)


def test_show_member(mem_id, pool_id):
    m = conn.network.get_member(mem_id, pool_id)
    print(m)


def test_create_member(pool_id, subnet_id, ip_add, protocol_port):
    m = conn.network.create_member(name = "test-member",
                                   address = ip_add,
                                   protocol_port= protocol_port,
                                   subnet_id = subnet_id,
                                   admin_state_up = True,
                                   pool_id = pool_id
    )
    return m


def test_update_member(mem_id, pool_id):
    m = conn.network.update_member(mem_id, name='test-mem-updated-name',
                                   weight = 2,
                                   pool_id = pool_id)
    return m


def test_delete_member(mem_id, pool_id):
    conn.network.delete_member(mem_id, pool=pool_id)


if __name__ == "__main__":
    pool_id = "80ad5133-5eff-4acf-bf4f-ba7c963e6184"
    subnet_id = "d5a27dd4-2dc0-4634-a42d-256e3762b990"
    ip = "10.0.0.10"
    port = 1002
    member = test_create_member(pool_id, subnet_id, ip, port)
    member_new = test_update_member(member.id, pool_id)
    test_show_member(member_new.id, pool_id)
    test_show_all_members(pool_id)
    test_delete_member(member.id, pool_id)