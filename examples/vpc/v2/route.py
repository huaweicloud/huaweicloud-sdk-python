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


# Create a Route
def create_route(_conn):
    data = {
        "destination": "xxx.xxx.xxx.xxx/xx",
        "nexthop": "xxxxxx",
        "type": "peering",
        "vpc_id": "xxxxxx",
    }
    print(_conn.vpc.create_route(**data))


# Delete a Route
def delete_route(_conn):
    route_id = 'xxxxxx'
    print(_conn.vpc.delete_route(route_id))


# Get a Route
def get_route(_conn):
    route_id = 'xxxxxx'
    print(_conn.vpc.get_route(route_id))


# List all Route
def routes(_conn):
    for index in _conn.vpc.routes():
        print(index)


# List Routes paginated
def routes_paginated(_conn):
    for index in _conn.vpc.routes(paginated=False):
        print(index)


if __name__ == '__main__':
    create_route(conn)
    delete_route(conn)
    get_route(conn)
    routes(conn)
