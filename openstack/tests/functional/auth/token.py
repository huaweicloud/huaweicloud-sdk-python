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

from openstack import connection

import sys
import os
from openstack import connection
from openstack import utils

utils.enable_logging(debug=True, stream=sys.stdout)

username = "***"
userpassword = "***"
userDomainId = "***"
auth_url = "https://iam.xxx.yyy.com/v3"
projectId = "***"
domain = "yyy.com"
region = "xxx"
AK = "***"
SK = "***"

enterprise_username = "***"
enterprise_userpwd = "***"
domain_name = "***"
user_domain_name = "***"

# Get a domain-level token with a enterprise account
conn_pwd_domain = connection.Connection(
    auth_url=auth_url,
    username=enterprise_username,         # enterprise account username
    password=enterprise_userpwd,          # enterprise account password
    domain_name=domain_name,              # maybe enterprise account username
    user_domain_name=user_domain_name     # maybe enterprise account username
)
# Get a project-level token with a normal account
conn_pwd_project = connection.Connection(
    project_id=projectId,
    auth_url=auth_url,
    user_domain_id=userDomainId,
    username=username,         # normal account username
    password=userpassword      # normal account password
)

# The AKSK mode enterprise account is the same as the normal account authentication method.
# But the aksk is divided into ordinary and enterprise
conn_aksk = connection.Connection(
    project_id=projectId,
    domain=domain,
    region=region,
    ak=AK,                     # enterprise or normal
    sk=SK                      # enterprise or normal
)
