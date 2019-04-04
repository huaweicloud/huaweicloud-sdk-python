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
    password=password
)

os.environ.setdefault(
    'OS_VPCV2.0_ENDPOINT_OVERRIDE',
    'https://******/v2.0/%(project_id)s'
)
print('endpoint: ' + os.environ.get('OS_VPCV2.0_ENDPOINT_OVERRIDE'))


def create_sharebandwidth(_conn):
    data = {
        "name": "sharebandwidth-sdk-20191012",
        "size": 8
    }
    obj = _conn.vpc.create_sharebandwidth(**data)
    print(obj)


def create_batch_sharebandwidth(_conn):
    data = {
        "name": "batct-sharebandwidth-sdk-20191012",
        "size": 9,
        "count": 2
    }
    obj = _conn.vpc.create_batch_sharebandwidth(**data)
    print(obj)


def delete_sharebandwidth(_conn):
    bandwidth_id = 'b4f056b6-c9ff-4844-8cb3-1102b36dc42e'
    obj = _conn.vpc.delete_sharebandwidth(bandwidth_id)
    print(obj)


def insert_ip_to_bandwidth(_conn):
    bandwidth_id = 'dbf2ac49-b2f0-4257-ab92-c668837f1342'
    data = {
        "publicip_info": [
            {
                "publicip_id": "f01a9741-baee-41a6-b973-dcb6b2c22b26"
            },
            {
                "publicip_id": "8a25dc1d-2e7e-417c-804a-1d153b25badc"
            }
        ]
    }
    obj = _conn.vpc.insert_ip_to_bandwidth(bandwidth_id, **data)
    print(obj)


def remove_ip_from_bandwidth(_conn):
    bandwidth_id = 'dbf2ac49-b2f0-4257-ab92-c668837f1342'
    data = {
        "publicip_info": [
            {
                "publicip_id": "f01a9741-baee-41a6-b973-dcb6b2c22b26"
            },
            {
                "publicip_id": "8a25dc1d-2e7e-417c-804a-1d153b25badc"
            }
        ],
        "charge_mode": "bandwidth",
        "size": 12
    }
    obj = _conn.vpc.remove_ip_from_bandwidth(bandwidth_id, **data)
    print(obj)


if __name__ == '__main__':
    create_sharebandwidth(conn)
    create_batch_sharebandwidth(conn)
    delete_sharebandwidth(conn)
    insert_ip_to_bandwidth(conn)
    remove_ip_from_bandwidth(conn)
