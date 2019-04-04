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
import warnings

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


def test_types(_conn):
    for index in _conn.block_store.types():
        print(index)


def test_get_type(_conn):
    type_id = '9318d869-8ccb-4cc7-8d7a-7fa205204bcf'
    print(_conn.block_store.get_type(type_id))


if __name__ == '__main__':
    # test_types(conn)
    # test_get_type(conn)
    pass
