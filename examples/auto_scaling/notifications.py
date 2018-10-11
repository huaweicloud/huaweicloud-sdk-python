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

def test_create_notification(conn):
    group = '7f6fe6bd-6615-44e6-858a-b8b66507083a'
    data = {
        "topic_urn": "urn:smn:eu-de:054efa2069a64785a196efe56c05ee74:test_as",
        "topic_scene": [
            "SCALING_UP", "SCALING_UP_FAIL", "SCALING_DOWN", "SCALING_DOWN_FAIL", "SCALING_GROUP_ABNORMAL"
        ]
    }

    ff = conn.auto_scaling.create_notification(group=group, **data)
    print ff


def test_list_notifications(conn):
    group = '7f6fe6bd-6615-44e6-858a-b8b66507083a'

    ff = conn.auto_scaling.notifications(group=group)
    for i in ff:
        print i


def test_delete_notification(conn):
    group = '7f6fe6bd-6615-44e6-858a-b8b66507083a'
    topic = 'urn:smn:eu-de:054efa2069a64785a196efe56c05ee74:test_as'

    ff = conn.auto_scaling.delete_notification(group=group, topic=topic)
    print ff
