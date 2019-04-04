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
password = os.getenv('get_secret_code')

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
    verify=False
)


def test_security_group_rules(_conn):
    query = {
        # "": ""
    }
    objs = _conn.vpcv1.security_group_rules(**query)
    for obj in objs:
        print(obj)


def test_get_security_group_rule(_conn):
    print(_conn.vpcv1.get_security_group_rule('d5470e53-0092-4271-b25b-fc8962c513a2'))


def test_create_security_group_rule(_conn):
    data = {
        "security_group_id": "7236365d-7341-4d94-ae11-7ce0360bf155",
        "direction": "ingress",
    }
    print(_conn.vpcv1.create_security_group_rule(**data))


def test_delete_security_group_rule(_conn):
    print(_conn.vpcv1.delete_security_group_rule('d5470e53-0092-4271-b25b-fc8962c513a2'))


def test_find_security_group_rule(_conn):
    print(_conn.vpcv1.find_security_group_rule('d5470e53-0092-4271-b25b-fc8962c513a2'))


if __name__ == '__main__':
    # test_security_group_rules(conn)
    # test_get_security_group_rule(conn)
    # test_create_security_group_rule(conn)
    # test_delete_security_group_rule(conn)
    # test_find_security_group_rule(conn)
    pass
