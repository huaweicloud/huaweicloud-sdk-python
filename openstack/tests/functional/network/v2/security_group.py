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


def security_groups(_conn):
    query = {
        "limit": 3,
        "name": "sg-name",
        "description": "sg-description"
    }
    sgs = _conn.network.security_groups(**query)
    for sg in sgs:
        print(sg)


def get_security_group(_conn):
    print(_conn.network.get_security_group('87798123-56cb-46de-a8f0-43a603d9d206'))


def create_security_group(_conn):
    data = {
        "name": "sg-test-20180x0x"
    }
    print(_conn.network.create_security_group(**data))


def update_security_group(_conn):
    data = {
        "name": "sg-test-20180x0x",
        "description": "test sg description again."
    }
    print(_conn.network.update_security_group('e1073c2d-2b04-4ff2-8c87-4a60bc43f717', **data))


def delete_security_group(_conn):
    print(_conn.network.delete_security_group('d37db748-8eb7-4461-a105-413727f324b0'))


if __name__ == '__main__':
    # security_groups(conn)
    # get_security_group(conn)
    # create_security_group(conn)
    # update_security_group(conn)
    # delete_security_group(conn)
    pass
