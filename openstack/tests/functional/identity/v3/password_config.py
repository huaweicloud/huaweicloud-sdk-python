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


def test_get_password_config(domain_id):
    password_config = conn.identity.get_password_config(domain_id)
    print(password_config)


def test_get_password_config_by_option(domain_id, option):
    password_config = conn.identity.get_password_config_by_option(domain_id, option)
    print(password_config)


if __name__ == '__main__':
    domain_id = "**********"
    option = "**********"
    test_get_password_config(domain_id)
    test_get_password_config_by_option(domain_id, option)
    pass
