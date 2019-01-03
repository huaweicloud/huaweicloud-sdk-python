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
    'OS_VOLUME_BACKUP_ENDPOINT_OVERRIDE',
    'https://******/v2/%(project_id)s'
)


def create_native_backup(_conn):
    data = {
        "volume_id": "000f0c09-5ae5-4f3f-8ba3-86679719a31a",
        "snapshot_id": "a7ce69f6-7087-4ca2-95d2-4079a5397292",
        "name": "vbs-test-20181018",
        "description": "vbs-test-20181018-desc"
    }
    print(_conn.volume_backup.create_native_backup(**data))


def backups(_conn):
    query = {
        "limit": "5"
    }
    bks = _conn.volume_backup.backups(details=True, **query)
    for bk in bks:
        print(bk)


def get_backup(_conn):
    print(_conn.volume_backup.get_backup('e4d91214-4317-4b9c-a31d-369d0b227d38'))


def delete_backup(_conn):
    print(_conn.volume_backup.delete_backup('e4d91214-4317-4b9c-a31d-369d0b227d38'))


if __name__ == '__main__':
    # create_native_backup(conn)
    # backups(conn)
    # get_backup(conn)
    # delete_backup(conn)
    pass
