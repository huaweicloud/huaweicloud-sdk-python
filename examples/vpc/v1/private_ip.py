# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
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

from openstack import connection

auth_url = '******'
userDomainId = '******'
projectId = '******'
username = '******'
password = os.getenv('get_secret_code')

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


def test_private_ips(_conn):
    query = {
        "limit": 2
    }
    objs = _conn.vpcv1.private_ips('6df498a2-3480-4faf-b6e7-ac25a053bbbc', **query)
    for obj in objs:
        print(obj)


def test_get_private_ip(_conn):
    print(_conn.vpcv1.get_private_ip('120f4621-be02-4412-b743-6e896bb88e32'))


def test_create_private_ip(_conn):
    data = {
        "subnet_id": "6df498a2-3480-4faf-b6e7-ac25a053bbbc"
    }
    print(_conn.vpcv1.create_private_ip(**data))


def test_create_private_ips(_conn):
    data = [
        {
            "subnet_id": "6df498a2-3480-4faf-b6e7-ac25a053bbbc"
        },
        {
            "subnet_id": "6df498a2-3480-4faf-b6e7-ac25a053bbbc"
        }
    ]
    print(_conn.vpcv1.create_private_ips(*data))


def test_delete_private_ip(_conn):
    print(_conn.vpcv1.delete_private_ip('c085815e-f43d-418a-913b-87771f8e7200'))


def test_find_private_ip(_conn):
    private_ip_id = 'c085815e-f43d-418a-913b-87771f8e7200'
    subnet_id = '6df498a2-3480-4faf-b6e7-ac25a053bbbc'
    print(_conn.vpcv1.find_private_ip(private_ip_id, subnet_id))


if __name__ == '__main__':
    test_private_ips(conn)
    test_get_private_ip(conn)
    test_create_private_ip(conn)
    test_create_private_ips(conn)
    test_delete_private_ip(conn)
    test_find_private_ip(conn)
