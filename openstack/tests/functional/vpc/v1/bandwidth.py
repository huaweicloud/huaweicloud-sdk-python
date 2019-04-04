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


def test_bandwidths(_conn):
    query = {
        # "": ""
    }
    objs = _conn.vpcv1.bandwidths(**query)
    for obj in objs:
        print(obj)


def test_get_bandwidth(_conn):
    print(_conn.vpcv1.get_bandwidth('7a7781c0-6205-486b-a6d0-d321c4a7076a'))


def test_update_bandwidth(_conn):
    data = {
        "size": 12,
        "name": "update_by_20190103"
    }
    print(_conn.vpcv1.update_bandwidth('7a7781c0-6205-486b-a6d0-d321c4a7076a', **data))


def test_find_bandwidth(_conn):
    print(_conn.vpcv1.find_bandwidth('7a7781c0-6205-486b-a6d0-d321c4a7076a'))


if __name__ == '__main__':
    # test_bandwidths(conn)
    # test_get_bandwidth(conn)
    # test_update_bandwidth(conn)
    # test_find_bandwidth(conn)
    pass
