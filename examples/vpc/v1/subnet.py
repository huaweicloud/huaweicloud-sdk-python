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


def test_subnets(_conn):
    query = {
        "limit": 2
    }
    objs = _conn.vpcv1.subnets(**query)
    for obj in objs:
        print(obj)


def test_get_subnet(_conn):
    print(_conn.vpcv1.get_subnet('5261b63d-ac0b-4591-b1fe-462339726f20'))


def test_create_subnet(_conn):
    data = {
        "name": "subnet_20190108_create",
        "cidr": "192.168.3.0/24",
        "gateway_ip": "192.168.3.1",
        "vpc_id": "90de16ce-3bd5-42e8-a6b3-d275d26ceb33",
    }
    print(_conn.vpcv1.create_subnet(**data))


def test_update_subnet(_conn):
    vpc_id = '90de16ce-3bd5-42e8-a6b3-d275d26ceb33'
    data = {
        "name": "update_subnet_20190108_test"
    }
    print(_conn.vpcv1.update_subnet('234081a0-60a0-4fef-a742-a8807692164c', vpc_id, **data))


def test_delete_subnet(_conn):
    vpc_id = '90de16ce-3bd5-42e8-a6b3-d275d26ceb33'
    print(_conn.vpcv1.delete_subnet('f4b04ca5-22b9-4152-9b11-984bdbcad29e', vpc_id))


def test_find_subnet(_conn):
    print(_conn.vpcv1.find_subnet('f4b04ca5-22b9-4152-9b11-984bdbcad29e'))


if __name__ == '__main__':
    test_subnets(conn)
    test_get_subnet(conn)
    test_create_subnet(conn)
    test_update_subnet(conn)
    test_delete_subnet(conn)
    test_find_subnet(conn)