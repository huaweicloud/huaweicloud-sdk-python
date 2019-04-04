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
import warnings
import os

from openstack import utils
from openstack import connection

utils.enable_logging(debug=False, stream=sys.stdout)
warnings.filterwarnings('ignore')

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
    password=password,
    verify=False
)


def test_ports(_conn):
    query = {
        # "": ""
    }
    objs = _conn.vpcv1.ports(**query)
    for obj in objs:
        print(obj)


def test_get_port(_conn):
    print(_conn.vpcv1.get_port('0a684452-6e1c-4f07-b53a-f3be419efe9c'))


def test_create_port(_conn):
    data = {
        "network_id": "6df498a2-3480-4faf-b6e7-ac25a053bbbc"
    }
    print(_conn.vpcv1.create_port(**data))


def test_update_port(_conn):
    data = {
        "name": "port_20190103"
    }
    print(_conn.vpcv1.update_port('0a684452-6e1c-4f07-b53a-f3be419efe9c', **data))


def test_delete_port(_conn):
    print(_conn.vpcv1.delete_port('0a684452-6e1c-4f07-b53a-f3be419efe9c'))


def test_find_port(_conn):
    print(_conn.vpcv1.find_port('0a684452-6e1c-4f07-b53a-f3be419efe9c'))


if __name__ == '__main__':
    # test_ports(conn)
    # test_get_port(conn)
    # test_create_port(conn)
    # test_update_port(conn)
    # test_delete_port(conn)
    # test_find_port(conn)
    pass
