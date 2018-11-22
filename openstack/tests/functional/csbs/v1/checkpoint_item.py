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
print('endpoint: ' + os.environ.get('OS_DATA_PROTECT_ENDPOINT_OVERRIDE'))


def get_checkpoint_item(_conn):
    print('test get_checkpoint_item >>>')
    item = _conn.csbs.get_checkpoint_item('7f240f10-e358-4356-b3dc-fa125ee355dd')
    print(item)


def checkpoint_items(_conn):
    print('test checkpoint_items >>>')
    data = {
        # "name": "bk-zgf",
        # "limit": "2"
    }
    items = _conn.csbs.checkpoint_items(**data)
    for item in items:
        print(item)


def get_checkpoint_item_count(_conn):
    print('test get_checkpoint_item_count >>>')
    data = {
        # "name": "bk-zgf",
        # 'limit': "2"
    }
    count = _conn.csbs.get_checkpoint_item_count(**data)
    print(count)


if __name__ == '__main__':
    # get_checkpoint_item(conn)
    # checkpoint_items(conn)
    # get_checkpoint_item_count(conn)
    pass
