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
    'OS_VPCV2.0_ENDPOINT_OVERRIDE',
    'https://vpc.cn-north-1.myhuaweicloud.com:443/v2.0'
)


def test_get_network_ip_availability(_conn):
    network_id = 'e1471015-c8f0-487d-8426-eb7953b29130'
    print(_conn.vpc.get_network_ip_availability(network_id))


if __name__ == '__main__':
    # test_get_network_ip_availability(conn)
    pass
