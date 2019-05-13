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

username = "**********"
password = "**********"
userDomainId = "**********"
auth_url = "**********"
projectId = "**********"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    domain_id=userDomainId,
    username=username,
    password=password,
    verify=False,
)


def test_add_user_to_group(group_id, user_id):
    result = conn.identity.add_user_to_group(group_id, user_id)
    if result is True:
        print("Add user to group successfully")
    else:
        print("Add user to group failure")


def test_check_group_user(group_id, user_id):
    result = conn.identity.check_group_user(group_id, user_id)
    if result is True:
        print("The user is in the group")
    else:
        print("The user is not in the group")


def test_list_user_groups(user_id):
    groups = conn.identity.list_user_groups(user_id)
    for group in groups:
        print(group)


if __name__ == '__main__':
    group_id = "**********"
    user_id = "**********"
    # test_add_user_to_group(group_id, user_id)
    # test_check_group_user(group_id, user_id)
    # test_list_user_groups(user_id)
    pass
