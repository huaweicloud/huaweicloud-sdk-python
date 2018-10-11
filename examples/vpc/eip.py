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

def apply_eip(conn):
    data = {
        "publicip": {
            "type": "5_bgp"
        },
        "bandwidth": {
            "name": "bw_kakak",
            "size": 1,
            "share_type": "WHOLE",
            "charge_mode": "bandwidth"
        },
        "extendParam": {
            "charge_mode": "prePaid",
            "period_type": "month",
            "period_num": 1,
            "is_auto_renew": "false",
            "is_auto_pay": "true"
        }
    }
    ff = conn.vpc.create_publicip_ext(**data)
    print ff


def modify_bandwidth(conn):
    bandwidth_id = '52723dee-182f-4688-a97b-2a7a9a1fe88f'
    data = {
        "bandwidth":
            {
                "name": "bandwidthaaaakkkk3",
                "size": 100
            },
        "extendParam":
            {
                "is_auto_pay": "false"
            }
    }

    ff = conn.vpc.update_bandwidth_ext(bandwidth_id=bandwidth_id, **data)
    print ff
