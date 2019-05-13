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


def security_group_rules(_conn):
    query = {
        "direction": "egress",
    }
    sgrs = _conn.network.security_group_rules(**query)
    for sgr in sgrs:
        print(sgr)


def get_security_group_rule(_conn):
    print(_conn.network.get_security_group_rule('fe5d01e3-aeb2-4f46-be7b-250007f55247'))


def find_security_group_rule(_conn):
    print(_conn.network.find_security_group_rule('fe5d01e3-aeb2-4f46-be7b-250007f55247'))


def create_security_group_rule(_conn):
    data = {
        "security_group_id": "87798123-56cb-46de-a8f0-43a603d9d206",
        "direction": "egress",
        "protocol": "tcp"
    }
    print(_conn.network.create_security_group_rule(**data))


def security_group_allow_ping(_conn):

    print(_conn.network.security_group_allow_ping("ddc2af6f-516b-4463-8422-7c432de282e2"))


def security_group_open_port(_conn):

    print(_conn.network.security_group_open_port("ddc2af6f-516b-4463-8422-7c432de282e2", 2222))


def delete_security_group_rule(_conn):
    print(_conn.network.delete_security_group_rule('9e6b78ee-02ff-4aee-b528-76fb7f197834'))


if __name__ == '__main__':
    security_group_rules(conn)
    get_security_group_rule(conn)
    create_security_group_rule(conn)
    delete_security_group_rule(conn)
    find_security_group_rule(conn)
    security_group_allow_ping(conn)
    security_group_open_port(conn)
