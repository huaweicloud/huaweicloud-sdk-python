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

"""
Managing anti-ddos

"""

FLOATING_IP_ID = '11ee0ec8-2b4f-438d-8235-dd22a3effa46'


def list_config(conn):
    print("list anti-ddos confit")
    print(conn.anti_ddos.query_config_list())


def list_eips(conn):
    print("list eips by status")
    print(conn.anti_ddos.list_eips(status='packetcleaning'))


def create_eip(conn):
    fip_dict = {'enable_L7': True,
                'traffic_pos_id': 1,
                'http_request_pos_id': 1,
                'cleaning_access_pos_id': 1,
                'app_type_id': 0}

    fip = conn.anti_ddos.create_floating_ip(FLOATING_IP_ID, **fip_dict)
    print(fip)


def update_eip(conn):
    fip = conn.anti_ddos.get_floating_ip(FLOATING_IP_ID)

    fip_update_dict = {'enable_L7': False,
                       'traffic_pos_id': 1,
                       'http_request_pos_id': 1,
                       'cleaning_access_pos_id': 1,
                       'app_type_id': 0}
    ufip = conn.anti_ddos.update_floating_ip(fip, **fip_update_dict)
    print(ufip)


def delete_eip(conn):
    fip = conn.anti_ddos.get_floating_ip(FLOATING_IP_ID)
    conn.anti_ddos.delete_floating_ip(fip)


def query_task_status(conn):
    # query_task_status requires to provide task_id, task_id is only
    # returned by create_eip, after create_eip, we get a FloatingIP object
    # get task_id by FloatingIP.task_id
    print(conn.anti_ddos.query_task_status(
        '4a4fefe7-34a1-40e2-a87c-16932af3ac4a'))


def get_eip_status(conn):
    print(conn.anti_ddos.get_eip_status(FLOATING_IP_ID))


def get_eip_daily(conn):
    for d in conn.anti_ddos.list_eip_daily(FLOATING_IP_ID):
        print(d)


def get_eip_log(conn):
    for l in conn.anti_ddos.list_eip_log(FLOATING_IP_ID):
        print(l)


def get_eip_weekly(conn):
    print(conn.anti_ddos.get_eip_weekly('1006510306'))


def get_alert_config(conn):
    # NOTEs: this is v2 api
    print(conn.anti_ddos.get_alert_config())
