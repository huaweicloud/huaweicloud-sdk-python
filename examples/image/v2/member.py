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

import sys
import os

from openstack import connection
from openstack import utils

# Set debug info.
utils.enable_logging(debug=False, stream=sys.stdout)

# Create connection.
auth_url = "https://iam.example.com/v3"
projectId = "replace-with-your-projectId"
userDomainId = "replace-with-your-domainId"
username = "replace-with-your-username"
password = os.getenv('get_secret_code')

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


# Add member.
def add_member(_conn):
    member = conn.image.add_member(
        image='8a28af8c-e48c-4039-8495-bdea48193fd9',
        member='9c61004714024f9586705d090530f9fa'
    )
    print(member)


# Get member.
def show_member(_conn):
    member = conn.image.get_member(
        image='8a28af8c-e48c-4039-8495-bdea48193fd9',
        member='9c61004714024f9586705d090530f9fa'
    )
    print(member)


# List members.
def list_members(_conn):
    members = conn.image.members(image='8a28af8c-e48c-4039-8495-bdea48193fd9')
    for member in members:
        print(member)


# Delete member.
def remove_member(_conn):
    conn.image.remove_member(
        image='8a28af8c-e48c-4039-8495-bdea48193fd9',
        member='9c61004714024f9586705d090530f9fa'
    )


if __name__ == '__main__':
    # add_member(conn)
    # show_member(conn)
    # list_members(conn)
    # remove_member(conn)
    pass
