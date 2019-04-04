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


def test_security_groups(_conn):
    query = {
        "limit": 2
    }
    objs = _conn.vpcv1.security_groups(**query)
    for obj in objs:
        print(obj)


def test_get_security_group(_conn):
    print(_conn.vpcv1.get_security_group('7236365d-7341-4d94-ae11-7ce0360bf155'))


def test_create_security_group(_conn):
    data = {
        "name": "sg_20190104"
    }
    print(_conn.vpcv1.create_security_group(**data))


def test_delete_security_group(_conn):
    print(_conn.vpcv1.delete_security_group('bcaac7e6-a9db-436d-b8c5-839b29407a18'))


def test_find_security_group(_conn):
    print(_conn.vpcv1.find_security_group('bcaac7e6-a9db-436d-b8c5-839b29407a18'))


if __name__ == '__main__':
    test_security_groups(conn)
    test_get_security_group(conn)
    test_create_security_group(conn)
    test_delete_security_group(conn)
    test_find_security_group(conn)
