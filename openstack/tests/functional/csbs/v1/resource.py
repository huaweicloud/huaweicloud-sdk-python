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


def test_create_resource_backup(_conn):
    provider_id = 'fc4d5750-22e7-4798-8a46-f48f62c4c1da'
    resource_id = '5a06b9f2-02e9-4c8e-a55d-00c8f6b5347a'
    data = {
        "protect": {
            "backup_name": "backup_name-test_create_resource_backup-sdk-20181101",
            "description": "backup_name-test_create_resource_backup-sdk",
            "resource_type": "OS::Nova::Server",
            # "extra_info": {
            #     "exclude_volumes": [
            #         ""
            #     ]
            # }
        }
    }
    resource_backup = _conn.csbs.create_resource_backup(provider_id, resource_id, **data)
    print(resource_backup)


def test_query_resource_backup_capability(_conn):
    provider_id = 'fc4d5750-22e7-4798-8a46-f48f62c4c1da'
    data = {
        "check_protectable": [
            {
                "resource_id": "2759d3b3-87e2-4121-b499-047eff7f0dc5",
                "resource_type": "OS::Nova::Server"
            },
            {
                "resource_id": "5a06b9f2-02e9-4c8e-a55d-00c8f6b5347a",
                "resource_type": "OS::Nova::Server"
            }
        ]
    }
    resource_backup_capability = _conn.csbs.query_resource_backup_capability(provider_id, **data)
    print(resource_backup_capability)


def test_query_resource_recovery_capability(_conn):
    provider_id = 'fc4d5750-22e7-4798-8a46-f48f62c4c1da'
    data = {
        "check_restorable": [
            {
                "checkpoint_item_id": "138d004d-1612-4ae9-9f00-eb8193121a1d",
                "target": {
                    "resource_id": "5a06b9f2-02e9-4c8e-a55d-00c8f6b5347a",
                    "resource_type": "OS::Nova::Server",
                    "volumes": [
                        {
                            "backup_id": "4ebe012f-c2c2-4066-a7d4-4d90516d5d65",
                            "volume_id": "9427293a-be22-49f9-8f13-f7ba5ed25385"
                        }
                    ]
                }
            },
            {
                "checkpoint_item_id": "5f00ef90-f271-41da-8ff5-f1607d5c4934",
                "target": {
                    "resource_id": "2759d3b3-87e2-4121-b499-047eff7f0dc5",
                    "resource_type": "OS::Nova::Server",
                    "volumes": [
                        {
                            "backup_id": "f45dcd3f-b507-48f8-a814-b3c836cc6489",
                            "volume_id": "5451c0b2-2d72-4b5f-93a6-9fd27b439f1c"
                        }
                    ]
                }
            }
        ]
    }
    resource_recovery_capability = _conn.csbs.query_resource_recovery_capability(provider_id, **data)
    print(resource_recovery_capability)


if __name__ == '__main__':
    # test_create_resource_backup(conn)
    # test_query_resource_backup_capability(conn)
    # test_query_resource_recovery_capability(conn)
    pass
