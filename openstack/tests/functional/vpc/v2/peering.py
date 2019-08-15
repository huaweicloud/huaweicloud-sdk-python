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

utils.enable_logging(debug=True, stream=sys.stdout)
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


def test_create_peering(_conn):
    data = {
        "name": "peering_by_cena_20190313",
        "request_vpc_info": {
            "vpc_id": "90de16ce-3bd5-42e8-a6b3-d275d26ceb33"
        },
        "accept_vpc_info": {
            "vpc_id": "e49fdadd-002d-4129-97d0-11c96494db8f"
        },
    }
    print(_conn.vpc.create_peering(**data))


def test_delete_peering(_conn):
    peering_id = '7b1a5c3d-3f22-4e3c-8c56-0adf7d5ce79e'
    print(_conn.vpc.delete_peering(peering_id))


def test_update_peering(_conn):
    peering_id = '7b1a5c3d-3f22-4e3c-8c56-0adf7d5ce79e'
    data = {
        "name": "peering_by_cena_20190309_updated_by_20190313"
    }
    print(_conn.vpc.update_peering(peering_id, **data))


def test_get_peering(_conn):
    peering_id = '7b1a5c3d-3f22-4e3c-8c56-0adf7d5ce79e'
    print(_conn.vpc.get_peering(peering_id))


def test_peerings(_conn):
    for index in _conn.vpc.peerings():
        print(index)


def test_accept_peering(_conn):
    peering_id = '7b1a5c3d-3f22-4e3c-8c56-0adf7d5ce79e'
    print(_conn.vpc.accept_peering(peering_id))


def test_reject_peering(_conn):
    peering_id = '7b1a5c3d-3f22-4e3c-8c56-0adf7d5ce79e'
    print(_conn.vpc.reject_peering(peering_id))


if __name__ == '__main__':
    # test_create_peering(conn)
    # test_delete_peering(conn)
    # test_update_peering(conn)
    # test_get_peering(conn)
    # test_peerings(conn)
    # test_accept_peering(conn)
    # test_reject_peering(conn)
    pass
