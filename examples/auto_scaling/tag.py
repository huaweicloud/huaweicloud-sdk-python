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

def test_get_tags(conn):
    ff = conn.auto_scaling.get_tags()
    for i in ff:
        print i


def test_get_resource_tags(conn):
    group = '7f6fe6bd-6615-44e6-858a-b8b66507083a'
    ff = conn.auto_scaling.get_group_tags(group=group)
    for i in ff:
        print i


def test_update_tags(conn):
    group = '7f6fe6bd-6615-44e6-858a-b8b66507083a'
    data = {
        "tags": [
            {
                "key": "ENV15",
                "value": "ENV15"
            },
            {
                "key": "ENV151",
                "value": "ENV151"
            }
        ],
        "action": "delete"
    }

    ff = conn.auto_scaling.tag_action(group=group, **data)
    print ff

