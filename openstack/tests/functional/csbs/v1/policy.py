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

import sys
import warnings
import os

from openstack import utils
from openstack import connection

utils.enable_logging(debug=False, stream=sys.stdout)
warnings.filterwarnings('ignore')

auth_url = '******'
userDomainId = '******'
projectId = '******'
username = '******'
password = '******'

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
    verify=False
)

os.environ.setdefault(
    'OS_DATA_PROTECT_ENDPOINT_OVERRIDE',
    'https://******/v1/%(project_id)s'
)


def test_create_backup_policy(_conn):
    data = {
        "description": "description-test_create_backup_policy-sdk",
        "name": "name-test_create_backup_policy-sdk-20181101",
        "parameters": {
            "common": {
                # ***Extra params or wrong params. app_consistency
                # "app_consistency": 0
            }
        },
        "provider_id": "fc4d5750-22e7-4798-8a46-f48f62c4c1da",
        "resources": [
            {
                "id": "5a06b9f2-02e9-4c8e-a55d-00c8f6b5347a",
                "type": "OS::Nova::Server",
                "name": "ecs-cena-20181101",
                # "extra_info": {
                #     "exclude_volumes": [
                #         "volume_id"
                #     ]
                # }
            }
        ],
        "scheduled_operations": [
            {
                "description": "description-scheduled_operation-sdk",
                "enabled": False,
                "name": "name-scheduled_operation-sdk-20181101",
                "operation_type": "backup",
                "operation_definition": {
                    "max_backups": 3,
                    "retention_duration_days": 2,
                    "permanent": False,
                    # ***Extra params or wrong params. plan_id
                    # "plan_id": "",
                    # ***Extra params or wrong params. provider_id
                    # "provider_id": "",
                    # "destination_region": "",
                    # "destination_project_id": "",
                    # "enable_acceleration": False
                },
                "trigger": {
                    "properties": {
                        "pattern": "BEGIN:VEVENT\nRRULE:FREQ=WEEKLY;BYDAY=TH;BYHOUR=10;BYMINUTE=39\nEND:VEVENT"
                    }
                }
            }
        ]
    }
    backup_policy = _conn.csbs.create_backup_policy(**data)
    print(backup_policy)


def test_delete_backup_policy(_conn):
    policy_id = 'd2aee8b1-0954-4af1-8d05-fac6b805487e'
    backup_policy = _conn.csbs.delete_backup_policy(policy_id)
    print(backup_policy)


def test_update_backup_policy(_conn):
    policy_id = 'a0af62ea-13bf-40d6-810b-c834ce151f82'
    data = {
        "description": "description-test_create_backup_policy-sdk",
        "name": "name-test_create_backup_policy-sdk-20181101",
        "parameters": {
            "common": {
                # ***Extra params or wrong params. app_consistency
                # "app_consistency": 0
            }
        },
        "resources": [
            {
                "id": "5a06b9f2-02e9-4c8e-a55d-00c8f6b5347a",
                "type": "OS::Nova::Server",
                "name": "ecs-cena-20181101",
                # "extra_info": {
                #     "exclude_volumes": [
                #         "volume_id"
                #     ]
                # }
            }
        ],
        "scheduled_operations": [
            {
                "description": "description-scheduled_operation-sdk",
                "enabled": False,
                "name": "name-scheduled_operation-sdk-20181101",
                "operation_type": "backup",
                "operation_definition": {
                    "max_backups": 3,
                    "retention_duration_days": 2,
                    "permanent": False,
                    # ***Extra params or wrong params. plan_id
                    # "plan_id": "",
                    # ***Extra params or wrong params. provider_id
                    # "provider_id": "",
                    # "destination_region": "",
                    # "destination_project_id": "",
                    # "enable_acceleration": False
                },
                "trigger": {
                    "properties": {
                        "pattern": "BEGIN:VEVENT\nRRULE:FREQ=WEEKLY;BYDAY=TH;BYHOUR=10;BYMINUTE=39\nEND:VEVENT"
                    }
                },
                "id": "3b6e62ce-3476-471f-af73-b00c9803a459"
            }
        ]
    }
    backup_policy = _conn.csbs.update_backup_policy(policy_id, **data)
    print(backup_policy)


def test_get_backup_policy(_conn):
    policy_id = 'a0af62ea-13bf-40d6-810b-c834ce151f82'
    backup_policy = _conn.csbs.get_backup_policy(policy_id)
    print(backup_policy)


def test_backup_policys(_conn):
    query = {
        "limit": 10,
        "name": "name-test_create_backup_policy-sdk-20181101"
    }
    backup_policys = _conn.csbs.backup_policys(**query)
    for backup_policy in backup_policys:
        print(backup_policy)


if __name__ == '__main__':
    # test_create_backup_policy(conn)
    # test_delete_backup_policy(conn)
    # test_update_backup_policy(conn)
    # test_get_backup_policy(conn)
    # test_backup_policys(conn)
    pass
