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
from openstack import connection

# create connection
username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


def create_server_tags():
    server_id = "b0a9d2b4-2cae-4b66-a6ba-6af70f3bd7f8"
    data = {
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    conn.ecs.create_server_tags(server_id, **data)


def delete_server_tags():
    server_id = "b0a9d2b4-2cae-4b66-a6ba-6af70f3bd7f8"
    data = {
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            }
        ]
    }
    conn.ecs.delete_server_tags(server_id, **data)


def get_server_tags():
    server_id = "b0a9d2b4-2cae-4b66-a6ba-6af70f3bd7f8"
    tags = conn.ecs.get_server_tags(server_id)
    for tag in tags:
        print(tag.key, tag.value)


def get_project_tags():
    tags = conn.ecs.get_project_tags()
    for tag in tags:
        print(tag.key, tag.values)
