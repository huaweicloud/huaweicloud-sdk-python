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


# Create a peering
def create_peering(_conn):
    data = {
        "name": "xxxxxx",
        "request_vpc_info": {
            "vpc_id": "xxxxxx"
        },
        "accept_vpc_info": {
            "vpc_id": "xxxxxx"
        },
    }
    print(_conn.vpc.create_peering(**data))


# Delete a peering
def delete_peering(_conn):
    peering_id = 'xxxxxx'
    print(_conn.vpc.delete_peering(peering_id))


# Update a peering
def update_peering(_conn):
    peering_id = 'xxxxxx'
    data = {
        "name": "xxxxxx"
    }
    print(_conn.vpc.update_peering(peering_id, **data))


# Get a peering
def get_peering(_conn):
    peering_id = 'xxxxxx'
    print(_conn.vpc.get_peering(peering_id))


# List peerings
def peerings(_conn):
    for index in _conn.vpc.peerings():
        print(index)


# Accept peering request
def accept_peering(_conn):
    peering_id = 'xxxxxx'
    print(_conn.vpc.accept_peering(peering_id))


# Reject peering request
def reject_peering(_conn):
    peering_id = 'xxxxxx'
    print(_conn.vpc.reject_peering(peering_id))


if __name__ == '__main__':
    create_peering(conn)
    delete_peering(conn)
    update_peering(conn)
    get_peering(conn)
    peerings(conn)
    accept_peering(conn)
    reject_peering(conn)
