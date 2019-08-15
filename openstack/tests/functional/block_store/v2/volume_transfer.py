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


def test_create_volume_transfer(_conn):
    data = {
        "volume_id": "4a84d34c-e9cb-45c1-88fa-62943801c232",
        "name": "volume_transfer_test"
    }
    print(_conn.block_store.create_volume_transfer(**data))


def test_accept_volume_transfer(_conn):
    transfer_id = 'bb25a655-593f-4b43-87ab-503f2baa55bf'
    data = {
        "accept": {
            "auth_key": "d3b2176b3b138cd0"
        }
    }
    print(_conn.block_store.accept_volume_transfer(transfer_id, **data))


def test_delete_volume_transfer(_conn):
    transfer_id = '4fde2d8b-4338-455b-bd05-61e8180710ae'
    print(_conn.block_store.delete_volume_transfer(transfer_id))


def test_get_volume_transfer(_conn):
    transfer_id = '4fde2d8b-4338-455b-bd05-61e8180710ae'
    print(_conn.block_store.get_volume_transfer(transfer_id))


def test_volume_transfers(_conn):
    for index in _conn.block_store.volume_transfers(details=False):
        print(index)


if __name__ == '__main__':
    # test_create_volume_transfer(conn)
    # test_accept_volume_transfer(conn)
    # test_delete_volume_transfer(conn)
    # test_get_volume_transfer(conn)
    # test_volume_transfers(conn)
    pass
