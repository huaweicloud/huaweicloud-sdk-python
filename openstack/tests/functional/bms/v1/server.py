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
password = '******'

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
    verify=False
)

os.environ.setdefault(
    'OS_BMS_ENDPOINT_OVERRIDE',
    'https://******/v1/%(project_id)s'
)
print('endpoint: ' + os.environ.get('OS_BMS_ENDPOINT_OVERRIDE'))


def create_server(_conn):
    data = {
        "availability_zone": "az1.dc1",
        "name": "newserverkak",
        "imageRef": "ad134bba-dfca-4aa1-a307-26b51e4c608b",
        "root_volume": {
            "volumetype": "SATA"
        },
        "data_volumes": [
            {
                "volumetype": "SATA",
                "size": 50
            },
            {
                "volumetype": "SSD",
                "size": 10,
                "multiattach": "true",
                "hw:passthrough": "false"
            }
        ],
        "isAutoRename": "true",
        "flavorRef": "c1.xlarge",
        "personality": [
            {
                "path": "/etc/banner.txt",
                "contents": "ICAgICAgDQoiQmFjaA=="
            }
        ],
        "security_groups": [
            {
                "id": "53234334-9c3d-4344-b577-2cdd6c244707"
            }
        ],
        "vpcid": "5b2a6c9a-093d-4d56-8889-a7917e44229c",
        "nics": [
            {
                "subnet_id": "a8f622a7-0d10-470e-ae80-c8e0e8bc7d12"
            }
        ],
        "publicip": {
            "eip": {
                "iptype": "5_bgp",
                "bandwidth": {
                    "size": 1,
                    "sharetype": "PER"
                }
            }
        },
        "key_name": "KeyPair-1565",
        "count": 1,
        "metadata": {
            "ss": "ss"
        },
        "extendparam": {
            "chargingMode": "postPaid",
            "periodType": "month",
            "periodNum": 1,
            "isAutoRenew": "true",
            "isAutoPay": "true",
            "regionID": "southchina"
        },
        "os:scheduler_hints": {
            "group": "cc10d0d1-d371-4f33-9452-fd5fbf14dc06"
        }
    }

    ff = _conn.bms.create_server(**data)
    print(ff)


def get_server(_conn):
    server = _conn.bms.get_server('******')
    print(server)


def rename_server(_conn):
    server_id = '******'
    data = {
        "name": "bms-new-name"
    }
    update_server = _conn.bms.update_server_name(server_id, **data)
    print(update_server)


if __name__ == "__main__":
    # create_server(conn)
    # get_server(conn)
    # rename_server(conn)
    pass
