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

def create_volume(conn):
    data = {
        "volume": {
            "availability_zone": "az1.dc1",
            "size": 10,
            "name": "new_kakakak",
            "volume_type": "SSD",
            "count": 1,
            "metadata": {
                "__system__encrypted": "0",
                "hw:passthrough": "false"
            },
            "multiattach": "true"
        }
    }

    ff = conn.evs.create_volume(**data)
    print ff


def resize_volume(conn):
    volume_id = '16d4b5e1-f613-4a1c-a92c-b40df63ba35f'
    data = {
        "os-extend": {
            "new_size": 15
        }
    }

    ff = conn.evs.resize_volume(volume_id=volume_id, **data)
    print ff


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
    print ff


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
    print ff
