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

def get_as_hook(conn):
    group_id = ''
    lifecycle_hook = 'lifecycle_hook_name'
    ff = conn.auto_scaling.get_lifecycle_hook(group_id, lifecycle_hook=lifecycle_hook)
    print ff


def get_as_hook_list(conn):
    group_id = ''
    ff = conn.auto_scaling.lifecycle_hooks(group_id)
    for i in ff:
        print i


def create_as_hook(conn):
    group_id = ''
    data = {
        "lifecycle_hook_name": "test-kFaas2",
        "default_result": "ABANDON",
        "default_timeout": 3600,
        "notification_topic_urn": "urn:smn:eu-de:054efa20ee69a64785a196efe56c05ee74:test_as",
        "lifecycle_hook_type": "INSTANCE_LAUNCHING"
    }
    ff = conn.auto_scaling.create_lifecycle_hook(group=group_id, **data)
    print ff


def modify_lifecycle_hook(conn):
    group_id = ''
    lifecycle_hook = 'lifecycle_hook_name'
    data = {'default_timeout': 15030}
    ff = conn.auto_scaling.update_lifecycle_hook(group=group_id, lifecycle_hook=lifecycle_hook, **data)
    print ff


def delete_lifecycle_hook(conn):
    group_id = ''
    lifecycle_hook = 'lifecycle_hook_name'
    ff = conn.auto_scaling.delete_lifecycle_hook(group_id, lifecycle_hook=lifecycle_hook)
    print ff


def get_instances(conn):
    group_id = ''
    ff = conn.auto_scaling.get_group_hanging_instance(group_id)
    for i in ff:
        print i


def call_back(conn):
    group_id = ''
    data = {
        "lifecycle_action_result": "EXTEND",
        "lifecycle_action_key": "your action key"
    }

    ff = conn.auto_scaling.call_back_instance(group_id, **data)
    print ff
