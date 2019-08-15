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


def subnets(_conn):
    query = {
        "limit": 2,
    }
    pts = _conn.network.subnets(**query)
    for pt in pts:
        print(pt)


def get_subnet(_conn):
    print(_conn.network.get_subnet('01f0c3f3-5d5e-4d0e-9e47-aaa5952fbad5'))


def get_subnet_ports(_conn):
    print(_conn.network.get_subnet_ports('01f0c3f3-5d5e-4d0e-9e47-aaa5952fbad5'))


def find_subnet(_conn):
    print(_conn.network.find_subnet('subnetUpdateDemo'))


def create_subnet(_conn):
    data = {
        "network_id": "0133cd73-34d4-4d4c-bf1f-e65b24603206",
        "cidr": "172.16.2.0/24"
    }
    print(_conn.network.create_subnet(**data))


def update_subnet(_conn):
    data = {
        "name": "subnet-test-20190422",
    }
    print(_conn.network.update_subnet('85f1616e-fe9b-4eb0-8b91-83964a9ec7ed', **data))


def delete_subnet(_conn):
    print(_conn.network.delete_subnet('85f1616e-fe9b-4eb0-8b91-83964a9ec7ed'))


if __name__ == '__main__':
    subnets(conn)
    get_subnet(conn)
    create_subnet(conn)
    update_subnet(conn)
    delete_subnet(conn)
    find_subnet(conn)
    get_subnet_ports(conn)

