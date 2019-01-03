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


def security_group_rules(_conn):
    query = {
        "direction": "egress",
    }
    sgrs = _conn.network.security_group_rules(**query)
    for sgr in sgrs:
        print(sgr)


def get_security_group_rule(_conn):
    print(_conn.network.get_security_group_rule('4f10a783-dc1a-4c5d-acae-b2ceb995b3b2').project_id)


def create_security_group_rule(_conn):
    data = {
        "security_group_id": "87798123-56cb-46de-a8f0-43a603d9d206",
        "direction": "egress",
        "protocol": "tcp"
    }
    print(_conn.network.create_security_group_rule(**data))


def delete_security_group_rule(_conn):
    print(_conn.network.delete_security_group_rule('4f10a783-dc1a-4c5d-acae-b2ceb995b3b2'))


if __name__ == '__main__':
    # security_group_rules(conn)
    # get_security_group_rule(conn)
    # create_security_group_rule(conn)
    # delete_security_group_rule(conn)
    pass
