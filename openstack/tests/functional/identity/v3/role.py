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


def test_list_domain_user_group_role(domain_id, group_id):
    roles = conn.identity.list_domain_user_group_role(domain_id, group_id)
    for role in roles:
        print(role)


def test_list_project_user_group_role(project_id, group_id):
    roles = conn.identity.list_project_user_group_role(project_id, group_id)
    for role in roles:
        print(role)


def test_grant_domain_user_group_role(domain_id, group_id, role_id):
    result = conn.identity.grant_domain_group_role(domain_id, group_id, role_id)
    if result is True:
        print("Grant permission to a user group of domain successfully")
    else:
        print("Grant permission to a user group of domain failure")


def test_grant_project_user_group_role(project_id, group_id, role_id):
    result = conn.identity.grant_project_group_role(project_id, group_id, role_id)
    if result is True:
        print("Grant permission to a user group of project successfully")
    else:
        print("Grant permission to a user group of project failure")


def test_check_domain_user_group_role(domain_id, group_id, role_id):
    result = conn.identity.check_domain_group_role(domain_id, group_id, role_id)
    if result is True:
        print("The group of domain has this permission")
    else:
        print("The group of domain doesn't have this permission")


def test_check_project_user_group_role(project_id, group_id, role_id):
    result = conn.identity.check_project_group_role(project_id, group_id, role_id)
    if result is True:
        print("The group of project has this permission")
    else:
        print("The group of project doesn't have this permission")


def test_delete_domain_user_group_role(domain_id, group_id, role_id):
    result = conn.identity.delete_domain_group_role(domain_id, group_id, role_id)
    if result is True:
        print("Delete permission to a user group of domain successfully")
    else:
        print("Delete permission to a user group of domain failure")


def test_delete_project_user_group_role(project_id, group_id, role_id):
    result = conn.identity.delete_project_group_role(project_id, group_id, role_id)
    if result is True:
        print("Delete permission to a user group of project successfully")
    else:
        print("Delete permission to a user group of project failure")


if __name__ == '__main__':
    domain_id = "**********"
    project_id = "**********"
    group_id = "**********"
    role_id = "**********"
    # test_list_domain_user_group_role(domain_id, group_id)
    # test_list_project_user_group_role(project_id, group_id)
    # test_grant_domain_user_group_role(domain_id, group_id, role_id)
    # test_grant_project_user_group_role(project_id, group_id, role_id)
    # test_check_domain_user_group_role(domain_id, group_id, role_id)
    # test_check_project_user_group_role(project_id, group_id, role_id)
    # test_delete_domain_user_group_role(domain_id, group_id, role_id)
    # test_delete_project_user_group_role(project_id, group_id, role_id)
    pass
