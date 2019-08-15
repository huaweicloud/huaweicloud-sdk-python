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


def networks(_conn):
    query = {
        "limit": 2,
    }
    pts = _conn.network.networks(**query)
    for pt in pts:
        print(pt)


def get_network(_conn):
    print(_conn.network.get_network('008ce66f-ff4a-430c-ae7f-d9959ebcde00'))


def find_network(_conn):
    print(_conn.network.find_network('67d25236-9ff6-4a10-a913-ed759bcca882'))


def create_network(_conn):
    data = {
        "name": "network-test",
    }
    print(_conn.network.create_network(**data))


def update_network(_conn):
    data = {
        "name": "network-test-20181018",
    }
    print(_conn.network.update_network('85f1616e-fe9b-4eb0-8b91-83964a9ec7ed', **data))


def delete_network(_conn):
    print(_conn.network.delete_network('85f1616e-fe9b-4eb0-8b91-83964a9ec7ed'))


if __name__ == '__main__':
    networks(conn)
    get_network(conn)
    create_network(conn)
    update_network(conn)
    delete_network(conn)
    find_network(conn)

