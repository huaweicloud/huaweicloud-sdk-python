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


def routers(_conn):
    query = {
        "limit": 2,
    }
    pts = _conn.network.routers(**query)
    for pt in pts:
        print(pt)


def get_router(_conn):
    print(_conn.network.get_router('88959ff9-c0bf-400c-92ae-b5fd5d613455'))


def find_router(_conn):
    print(_conn.network.find_router('router-test-20190422'))


def create_router(_conn):
    data = {
        "name": "name",
        "admin_state_up": "true"
    }
    print(_conn.network.create_router(**data))


def add_interface_to_router(_conn):
    data = {
        "subnet_id": "ab78be2d-782f-42a5-aa72-35879f6890ff",
    }
    print(_conn.network.add_interface_to_router('88959ff9-c0bf-400c-92ae-b5fd5d613455',**data))


def remove_interface_from_router(_conn):
    data = {
        "subnet_id": "4b910a10-0860-428b-b463-d84dbc5e288e",
    }
    print(_conn.network.add_interface_to_router('88959ff9-c0bf-400c-92ae-b5fd5d613455',**data))


def update_router(_conn):
    data = {
        "name": "router-test-20190422",
    }
    print(_conn.network.update_router('88959ff9-c0bf-400c-92ae-b5fd5d613455', **data))


def delete_router(_conn):
    print(_conn.network.delete_router('85f1616e-fe9b-4eb0-8b91-83964a9ec7ed'))


if __name__ == '__main__':
    routers(conn)
    get_router(conn)
    create_router(conn)
    update_router(conn)
    delete_router(conn)
    find_router(conn)
    add_interface_to_router(conn)
    remove_interface_from_router(conn)
