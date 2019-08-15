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


def ports(_conn):
    query = {
        "admin_state_up": False,
    }
    pts = _conn.network.ports(**query)
    for pt in pts:
        print(pt)


def get_port(_conn):
    print(_conn.network.get_port('016ed520-3cfb-4e2c-919d-ce5eb1071aac'))


def find_port(_conn):
    print(_conn.network.find_port('123'))


def create_port(_conn):
    data = {
        "network_id": "0aed2b44-b846-4d15-8047-84bbc6aaf46c",
    }
    print(_conn.network.create_port(**data))


def update_port(_conn):
    data = {
        "name": "port-test-20181018",
    }
    print(_conn.network.update_port('f0bd0b3e-4230-4734-92a7-e92f58c2fe5d', **data))


def delete_port(_conn):
    print(_conn.network.delete_port('f0bd0b3e-4230-4734-92a7-e92f58c2fe5d'))


if __name__ == '__main__':
    ports(conn)
    get_port(conn)
    create_port(conn)
    update_port(conn)
    delete_port(conn)
    find_port(conn)

