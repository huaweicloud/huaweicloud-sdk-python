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

utils.enable_logging(debug=True, stream=sys.stdout)
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
print('endpoint: ' + os.environ.get('OS_DATA_PROTECT_ENDPOINT_OVERRIDE'))


def create_checkpoint(_conn):
    provider_id = 'fc4d5750-22e7-4798-8a46-f48f62c4c1da'
    data = {
        "parameters": {
            "auto_trigger": False,
            "resources": ["7cab506f-bd7f-406f-807a-4916de5db737"]
        },
        "plan_id": "853fe072-444a-419f-b808-b4111badb05d"
    }
    resource = _conn.csbs.create_checkpoint(provider_id, **data)
    print(resource)


def delete_checkpoint(_conn):
    checkpoint_id = '2e3f50c9-c8f8-4ec4-8ac7-3db7fb151f86'
    provider_id = 'fc4d5750-22e7-4798-8a46-f48f62c4c1da'
    data = {
        "checkpoint_items": "1928cb8c-90b2-4f93-9373-ea18209d7593"
    }
    resource = _conn.csbs.delete_checkpoint(checkpoint_id, provider_id, **data)
    print(resource)


if __name__ == '__main__':
    # create_checkpoint(conn)
    # delete_checkpoint(conn)
    pass
