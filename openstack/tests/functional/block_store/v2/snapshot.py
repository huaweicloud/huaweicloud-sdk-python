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


def test_update_snapshot(_conn):
    snapshot_id = '0b9b6e9c-c8da-448c-9bbd-ed392be852df'
    data = {
        "name": "snapshot_from_volume_updated_by_20190312"
    }
    snapshot = _conn.block_store.update_snapshot(snapshot_id, **data)
    print(snapshot)


def test_create_snapshot_metadata(_conn):
    snapshot_id = '0b9b6e9c-c8da-448c-9bbd-ed392be852df'
    data = {
        "metadata": {
            "k1": "v1",
            "k11": "v11",
            "k111": "v111"
        }
    }
    snapshot_metadata = _conn.block_store.create_snapshot_metadata(snapshot_id, **data)
    print(snapshot_metadata)


def test_get_snapshot_metadata(_conn):
    snapshot_id = '0b9b6e9c-c8da-448c-9bbd-ed392be852df'
    snapshot_metadata = _conn.block_store.get_snapshot_metadata(snapshot_id, key=None)
    print(snapshot_metadata)


def test_update_snapshot_metadata(_conn):
    snapshot_id = '0b9b6e9c-c8da-448c-9bbd-ed392be852df'
    # update all metadata
    data_all = {
        "metadata": {
            "k1": "v1",
            "k11": "v11",
            "k111": "v111",
            "k2222": "v2222"
        }
    }
    # update one mata of metadata
    data_one = {
        "meta": {
            "k11": "k11-k22"
        }
    }
    snapshot_metadata = _conn.block_store.update_snapshot_metadata(snapshot_id, key=None, **data_all)
    print(snapshot_metadata)


def test_delete_snapshot_metadata(_conn):
    snapshot_id = '0b9b6e9c-c8da-448c-9bbd-ed392be852df'
    snapshot_metadata = _conn.block_store.delete_snapshot_metadata(snapshot_id, key='delete_key')
    print(snapshot_metadata)


def test_snapshots(_conn):
    for index in _conn.block_store.snapshots():
        print(index)


def test_create_snapshot(_conn):
    data = {
        "volume_id": "159f6570-2b13-4002-a75c-eaa21fe12ed6",
        "name": "snapshot_from_volume",
    }
    print(_conn.block_store.create_snapshot(**data))


if __name__ == '__main__':
    # test_update_snapshot(conn)
    # test_create_snapshot_metadata(conn)
    # test_get_snapshot_metadata(conn)
    # test_update_snapshot_metadata(conn)
    # test_delete_snapshot_metadata(conn)
    # test_snapshots(conn)
    # test_create_snapshot(conn)
    pass
