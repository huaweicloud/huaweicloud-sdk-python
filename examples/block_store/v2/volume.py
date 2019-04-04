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

# create volume
def create_volume():
    data = {
        "name": "volume_name",
        "availability_zone": "xxx",
        "description": "volume_description",
        "volume_type": "SATA",
        "metadata": {
            "__system__encrypted": "0"
        },
        "size": 10

    }
    volume = conn.block_store.create_volume(**data)
    print volume

# delete volume
def delete_volume():
    volume_id = "xxx"
    conn.block_store.delete_volume(volume_id)

# update volume
def update_volume():
    volume_id = 'xxx'
    data = {
        "name": "volume-name"
    }
    print(conn.block_store.update_volume(volume_id, **data))

# expand volume
def expand_volume():
    volume_id = 'xxx'
    new_size = 18
    new_vloume = conn.block_store.expand_volume(volume_id, new_size)
    print(new_vloume)

# volumes
def volumes():
    for index in conn.block_store.volumes(details=False):
        print(index)

# get volume
def get_volume():
    volume_id = 'xxx'
    volume = conn.block_store.get_volume(volume_id)
    print(volume)

# get quota set
def get_quota_set():
    print(conn.block_store.get_quota_set(projectId))

# create volume metadata
def create_volume_metadata():
    volume_id = 'xxx'
    data = {
        "metadata": {
            "k1": "v1",
            "k11": "v11",
            "k111": "v111"
        }
    }
    volume_metadata = conn.block_store.create_volume_metadata(volume_id, **data)
    print(volume_metadata)

# get volume metadata
def get_volume_metadata():
    volume_id = 'xxx'
    volume_metadata = conn.block_store.get_volume_metadata(volume_id, key=None)
    print(volume_metadata)

# update volume metadata
def update_volume_metadata():
    volume_id = 'xxx'
    data_all = {
        "metadata": {
            "k1": "v1"
        }
    }

    volume_metadata = conn.block_store.update_volume_metadata(volume_id, key=None, **data_all)
    print(volume_metadata)

# delete volume metadata
def delete_volume_metadata():
    volume_id = 'xxx'
    volume_metadata = conn.block_store.delete_volume_metadata(volume_id, key='delete_key')
    print(volume_metadata)

# set volume bootable
def set_volume_bootable():
    volume_id = 'xxx'
    bootable = conn.block_store.set_volume_bootable(volume_id, True)
    print(bootable)

# set volume readonly
def set_volume_readonly():
    volume_id = 'xxx'
    readonly = conn.block_store.set_volume_readonly(volume_id, True)
    print(readonly)

# export image by volume
def export_image_by_volume():
    volume_id = 'xxx'
    data = {
        "image_name": "make_a_image_from_volume"
    }
    image = conn.block_store.export_image_by_volume(volume_id, **data)
    print(image)


if __name__ == '__main__':
    create_volume()
    delete_volume()
    update_volume()
    expand_volume()
    volumes()
    get_volume()
    get_quota_set()
    create_volume_metadata()
    get_volume_metadata()
    update_volume_metadata()
    delete_volume_metadata()
    set_volume_bootable()
    set_volume_readonly()
    export_image_by_volume()
