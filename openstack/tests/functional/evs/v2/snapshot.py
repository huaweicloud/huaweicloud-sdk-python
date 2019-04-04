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


def test_rollback_snapshot(_conn):
    snapshot_id = '2747d0cc-48d4-43b8-95b8-0f40c69174fb'
    data = {
        "volume_id": "fce0c143-fa29-47a8-965b-6cc5f32a0e74",
        "name": "volume-for-snapshot",
    }
    print(_conn.evs.rollback_snapshot(snapshot_id, **data))


if __name__ == '__main__':
    # test_rollback_snapshot(conn)
    pass
