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
        "volume": {
            "availability_zone": "az1.dc1",
            "size": 10,
            "name": "volume_name",
            "volume_type": "SSD",
            "count": 1,
            "metadata": {
                "__system__encrypted": "0",
                "hw:passthrough": "false"
            },
            "multiattach": True
        }
    }

    volume = conn.evs.create_volume(**data)
    print(volume)

# get job
def get_job():
    job_id = "xxx"

    job = conn.evs.get_job(job_id)
    print(job)

# expand volume
def resize_volume():
    volume_id = 'xxx'
    data = {
        "os-extend": {
            "new_size": 15
        }
    }

    volume = conn.evs.resize_volume(volume_id=volume_id, **data)
    print(volume)

# update volume
def update_volume():
    volume_id = 'xxx'
    data = {
        "name": "update_name_by_sdk",
        "description": "update_description_by_sdk",
    }

    volume = conn.evs.update_volume(volume_id, **data)
    print(volume)

# get volume
def get_volume():
    volume_id = 'xxx'

    volume = conn.evs.get_volume(volume_id)
    print(volume)

# create volume ext
def create_volume_ext():
    data = {
        "volume": {
            "availability_zone": "az1.dc1",
            "size": 120,
            "name": "_kakakak",
            "volume_type": "SSD",
            "count": 1,
            "metadata": {
                "__system__encrypted": "0",
                "hw:passthrough": "false"
            },
            "multiattach": "true"
        },
        "bssParam": {
            "chargingMode": "prePaid",
            "periodType": "year",
            "periodNum": 1,
            "isAutoPay": "true",
            "isAutoRenew": "true"
        }
    }

    volume = conn.evs.create_volume_ext(**data)
    print(volume)

# expand volume ext
def resize_volume_ext():
    volume_id = 'xxx'
    data = {
        "os-extend": {
            "new_size": 150
        },
        "bssParam": {
            "chargingMode": "prePaid",
            "isAutoPay": "true"
        }
    }

    volume = conn.evs.resize_volume_ext(volume_id=volume_id, **data)
    print(volume)

# get volumes list
def volumes():
    generator = conn.evs.volumes(limit=2)
    for volumes_list in generator:
        for volume in volumes_list.volumes:
            print(volume)

if __name__ == "__main__":
    create_volume()
    get_job()
    resize_volume()
    update_volume()
    get_volume()
    create_volume_ext()
    resize_volume_ext()
    volumes()
