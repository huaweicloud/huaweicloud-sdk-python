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


def test_update_volume(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
    data = {
        "name": "volume-cena-test_updated_by_20190312"
    }
    print(_conn.block_store.update_volume(volume_id, **data))


def test_get_quota_set(_conn):
    print(_conn.block_store.get_quota_set(projectId))


def test_create_volume_metadata(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
    data = {
        "metadata": {
            "k1": "v1",
            "k11": "v11",
            "k111": "v111"
        }
    }
    volume_metadata = _conn.block_store.create_volume_metadata(volume_id, **data)
    print(volume_metadata)


def test_get_volume_metadata(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
    volume_metadata = _conn.block_store.get_volume_metadata(volume_id, key=None)
    print(volume_metadata)


def test_update_volume_metadata(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
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
    volume_metadata = _conn.block_store.update_volume_metadata(volume_id, key=None, **data_all)
    print(volume_metadata)


def test_delete_volume_metadata(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
    volume_metadata = _conn.block_store.delete_volume_metadata(volume_id, key='delete_key')
    print(volume_metadata)


def test_expand_volume(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
    new_size = 18
    new_vloume = _conn.block_store.expand_volume(volume_id, new_size)
    print(new_vloume)


def test_set_volume_bootable(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
    bootable = _conn.block_store.set_volume_bootable(volume_id, True)
    print(bootable)


def test_set_volume_readonly(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
    readonly = _conn.block_store.set_volume_readonly(volume_id, True)
    print(readonly)


def test_export_image_by_volume(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
    data = {
        "image_name": "make_a_image_from_volume"
    }
    _conn.block_store.export_image_by_volume(volume_id, **data)


def test_volumes(_conn):
    for index in _conn.block_store.volumes(details=False):
        print(index)


def test_get_volume(_conn):
    volume_id = '159f6570-2b13-4002-a75c-eaa21fe12ed6'
    volume = _conn.block_store.get_volume(volume_id)
    print(volume)


if __name__ == '__main__':
    # test_update_volume(conn)
    # test_get_quota_set(conn)
    # test_create_volume_metadata(conn)
    # test_get_volume_metadata(conn)
    # test_update_volume_metadata(conn)
    # test_delete_volume_metadata(conn)
    # test_expand_volume(conn)
    # test_set_volume_bootable(conn)
    # test_set_volume_readonly(conn)
    # test_export_image_by_volume(conn)
    # test_volumes(conn)
    # test_get_volume(conn)
    pass
