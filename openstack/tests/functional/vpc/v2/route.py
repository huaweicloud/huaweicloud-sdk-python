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

utils.enable_logging(debug=False, stream=sys.stdout)
warnings.filterwarnings('ignore')

auth_url = '******'
userDomainId = '******'
projectId = '******'
username = '******'
password = '******'

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
    verify=False
)

os.environ.setdefault(
    'OS_VPCV2.0_ENDPOINT_OVERRIDE',
    'https://vpc.cn-north-1.myhuaweicloud.com/v2.0'
)


def test_create_route(_conn):
    data = {
        "destination": "192.168.0.0/18",
        "nexthop": "9d7ab42f-015e-4688-ad5a-d38bc97c045a",
        "type": "peering",
        "vpc_id": "90de16ce-3bd5-42e8-a6b3-d275d26ceb33",
    }
    print(_conn.vpc.create_route(**data))


def test_delete_route(_conn):
    route_id = 'ca7cbc47-c116-4893-867c-33fd70b353d4'
    print(_conn.vpc.delete_route(route_id))


def test_get_route(_conn):
    route_id = 'ca7cbc47-c116-4893-867c-33fd70b353d4'
    print(_conn.vpc.get_route(route_id))


def test_routes(_conn):
    for index in _conn.vpc.routes():
        print(index)


if __name__ == '__main__':
    # test_create_route(conn)
    # test_delete_route(conn)
    # test_get_route(conn)
    # test_routes(conn)
    pass
