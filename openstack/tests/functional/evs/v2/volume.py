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


def create_volume_has_resource_key(conn):
    data = {
        "volume": {
            "availability_zone": "az1.dc1",
            "size": 10,
            "name": "volume_by_has_resource_key",
            "volume_type": "SSD",
            "count": 1,
            "metadata": {
                "__system__encrypted": "0",
                "hw:passthrough": "false"
            },
            "multiattach": True
        }
    }

    ff = conn.evs.create_volume(**data)
    print(ff)


def create_volume_no_resource_key(conn):
    data = {
        "availability_zone": "az1.dc1",
        "size": 10,
        "name": "volume_by_no_resource_key",
        "volume_type": "SSD",
        "count": 1,
        "metadata": {
            "__system__encrypted": "0",
            "hw:passthrough": "false"
        },
        "multiattach": True
    }

    ff = conn.evs.create_volume(**data)
    print(ff)


def create_volume_by_args(conn):
    ff = conn.evs.create_volume(
        availability_zone="az1.dc1",
        size=10,
        name="volume_by_args",
        volume_type="SSD",
        count=1,
        metadata={
            "__system__encrypted": "0",
            "hw:passthrough": "false"
        },
        multiattach=True
    )
    print(ff)


def resize_volume(conn):
    volume_id = '16d4b5e1-f613-4a1c-a92c-b40df63ba35f'
    data = {
        "os-extend": {
            "new_size": 15
        }
    }

    ff = conn.evs.resize_volume(volume_id=volume_id, **data)
    print(ff)


def create_volume_ext(conn):
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

    ff = conn.evs.create_volume_ext(**data)
    print(ff)


def resize_volume_ext(conn):
    volume_id = 'ad2c5328-e734-4600-a54e-8b25477b97e2'
    data = {
        "os-extend": {
            "new_size": 150
        },
        "bssParam": {
            "chargingMode": "prePaid",
            "isAutoPay": "true"
        }
    }

    ff = conn.evs.resize_volume_ext(volume_id=volume_id, **data)
    print(ff)


def update_volume(_conn):
    volume_id = 'a07dcedd-c22e-4800-a1eb-3eeff465f114'
    data = {
        "name": "update_name_by_sdk",
        "description": "update_description_by_sdk",
    }
    ff = _conn.evs.update_volume(volume_id, **data)
    print(ff)


def get_volume(_conn):
    volume_id = 'a07dcedd-c22e-4800-a1eb-3eeff465f114'
    ff = _conn.evs.get_volume(volume_id)
    print(ff)

def volumes(_conn):
    generator = conn.evs.volumes(limit=2)
    for volumes_list in generator:
        print(volumes_list.count)
        for volume in volumes_list.volumes:
            print(volume.get('id'))
        # volumes_links returned only when limit param is given
        for volumes_link in volumes_list.volumes_links:
            print(volumes_link.get('href'))
            print(volumes_link.get('rel'))

def get_job(_conn):
    ff = conn.evs.get_job("ff808081695b70230169700bbd932e9b")
    # single operation
    print(ff.entities.get("volume_id"))
    # batch operation
    sub_jobs = ff.entities.get("sub_jobs")
    for sub_job in sub_jobs:
        print(sub_job.get("entities").get("volume_id"))

if __name__ == "__main__":
    # create_volume_has_resource_key(conn)
    # create_volume_no_resource_key(conn)
    # create_volume_by_args(conn)
    # update_volume(conn)
    # get_volume(conn)
    # volumes(conn)
    # get_job(conn)
    pass
