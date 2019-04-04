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


def test_vpcs(_conn):
    query = {
        # "": ""
    }
    objs = _conn.vpcv1.vpcs(**query)
    for obj in objs:
        print(obj)


def test_get_vpc(_conn):
    print(_conn.vpcv1.get_vpc('1069dd2e-db67-4d0a-bd2f-0205af7e6d63'))


def test_create_vpc(_conn):
    data = {
        "name": "vpc-cena-2",
    }
    print(_conn.vpcv1.create_vpc(**data))


def test_update_vpc(_conn):
    data = {
        "name": "vpc-cena-2-update",
    }
    print(_conn.vpcv1.update_vpc('1069dd2e-db67-4d0a-bd2f-0205af7e6d63', **data))


def test_delete_vpc(_conn):
    print(_conn.vpcv1.delete_vpc('1069dd2e-db67-4d0a-bd2f-0205af7e6d63'))


def test_find_vpc(_conn):
    print(_conn.vpcv1.find_vpc('1069dd2e-db67-4d0a-bd2f-0205af7e6d63'))


if __name__ == '__main__':
    # test_vpcs(conn)
    # test_get_vpc(conn)
    # test_create_vpc(conn)
    # test_update_vpc(conn)
    # test_delete_vpc(conn)
    # test_find_vpc(conn)
    pass
