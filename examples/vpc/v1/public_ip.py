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

import sys
import warnings
import os

from openstack import utils
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


def test_public_ips(_conn):
    query = {
        "limit": 2
    }
    objs = _conn.vpcv1.public_ips(**query)
    for obj in objs:
        print(obj)


def test_get_public_ip(_conn):
    print(_conn.vpcv1.get_public_ip('6ffdbd50-1425-4901-9383-09993304db61'))


def test_create_public_ip(_conn):
    data = {
        "publicip": {
            "type": "5_bgp",
        },
        "bandwidth": {
            "share_type": "WHOLE",
            "id": "7a7781c0-6205-486b-a6d0-d321c4a7076a"
        }
    }
    print(_conn.vpcv1.create_public_ip(**data))


def test_update_public_ip(_conn):
    data = {
        "ip_version": 6,
        # "port_id": "2f8254a3-c7ec-4600-bc10-cdfdf9a4384b",
        # "port_id": None
    }
    print(_conn.vpcv1.update_public_ip('6ffdbd50-1425-4901-9383-09993304db61', **data))


def test_delete_public_ip(_conn):
    print(_conn.vpcv1.delete_public_ip('1b725806-ace8-4f02-a2ad-08870f48b4ca'))


def test_find_public_ip(_conn):
    print(_conn.vpcv1.find_public_ip('6ffdbd50-1425-4901-9383-09993304db61'))


if __name__ == '__main__':
    test_public_ips(conn)
    test_get_public_ip(conn)
    test_create_public_ip(conn)
    test_update_public_ip(conn)
    test_delete_public_ip(conn)
    test_find_public_ip(conn)
