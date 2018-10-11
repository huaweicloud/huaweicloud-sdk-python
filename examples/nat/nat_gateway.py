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

auth_url = 'https://iam.eu-de.otc.t-systems.com/v3'
userDomainId = 'cb06f3a9fa4e464ea62695b4dd26e5f0'
projectId = '054efa2069a64785a196efe56c05ee74'
username = 'zhanggaofeng'
password = 'Ok_1102$123'

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
    verify=False
)

# list nat_gateway
nat_gateways = conn.nat.nat_gateways()
for nat_gateway in nat_gateways:
    print(nat_gateway)

# update nat_gateway
id = '8d45f435-61f7-4a30-b955-ae40f3e3989b'
data = {
    'name': 'nat-test-update-x2',
    'description': 'a nat description',
    'spec': '3'
}
update_nat_gateway = conn.nat.update_nat_gateway(id, **data)
print(update_nat_gateway)

nat = conn.nat.create_nat_gateway(router_id='7c7d9bf6-9431-4366-9be2-e0caea8eb382',
                                  name='yyx-test-nat',
                                  description='dddd',
                                  internal_network_id='8719d692-a4e9-4dbc-bba1-15afd13c4ce5',
                                  spec='1')

print nat

print conn.nat.get_nat_gateway('8d45f435-61f7-4a30-b955-ae40f3e3989b')

print conn.nat.delete_nat_gateway('8d45f435-61f7-4a30-b955-ae40f3e3989b')
