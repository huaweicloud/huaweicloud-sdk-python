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

# create connection
username = "xxxxxx"
password = os.getenv('get_secret_code')
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)

# create snapshot
def create_snapshot():
    data = {
        "volume_id": "xxx",
        "name": "snapshot_from_volume",
    }
    print(conn.block_store.create_snapshot(**data))

# update snapshot
def update_snapshot():
    snapshot_id = 'xxx'
    data = {
        "name": "snapshot_name"
    }
    snapshot = conn.block_store.update_snapshot(snapshot_id, **data)
    print(snapshot)

# get snapshot
def get_snapshot():
    snapshot_id = 'xxx'
    snapshot = conn.block_store.get_snapshot(snapshot_id)
    print(snapshot)


# delete snapshot
def delete_snapshot():
    snapshot_id = 'xxx'
    conn.block_store.delete_snapshot(snapshot_id)

# create snapshot metadata
def create_snapshot_metadata():
    snapshot_id = 'xxx'
    data = {
        "metadata": {
            "k1": "v1"
        }
    }
    snapshot_metadata = conn.block_store.create_snapshot_metadata(snapshot_id, **data)
    print(snapshot_metadata)

# get snapshot metadata
def get_snapshot_metadata():
    snapshot_id = 'xxx'
    snapshot_metadata = conn.block_store.get_snapshot_metadata(snapshot_id, key=None)
    print(snapshot_metadata)

# update snapshot metadata
def update_snapshot_metadata():
    snapshot_id = 'xxx'
    data_all = {
        "metadata": {
            "k1": "v1_new"
        }
    }
    snapshot_metadata = conn.block_store.update_snapshot_metadata(snapshot_id, key=None, **data_all)
    print(snapshot_metadata)

# delete snapshot metadata
def delete_snapshot_metadata():
    snapshot_id = 'xxx'
    snapshot_metadata = conn.block_store.delete_snapshot_metadata(snapshot_id, key='delete_key')
    print(snapshot_metadata)

# snapshots
def snapshots():
    for index in conn.block_store.snapshots():
        print(index)

if __name__ == '__main__':
    create_snapshot()
    update_snapshot()
    get_snapshot()
    delete_snapshot()
    create_snapshot_metadata()
    get_snapshot_metadata()
    update_snapshot_metadata()
    delete_snapshot_metadata()
    snapshots()
