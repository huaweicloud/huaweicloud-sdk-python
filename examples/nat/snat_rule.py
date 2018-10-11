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
import time

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

rule_id = ''

# create snat_rule
print('create_snat_rule:')
data = {
    'nat_gateway_id': '8d45f435-61f7-4a30-b955-ae40f3e3989b',
    'network_id': '247e2ef9-4625-4cfd-870a-f128f6f38acf',
    'floating_ip_id': 'dd05c596-fde4-491f-bc1b-24f2d7e3e623'
}
snat_rule = conn.nat.create_snat_rule(**data)
print(snat_rule)
rule_id = snat_rule.id
print('rule_id: ' + rule_id)
print('>>>')

# get snat_rule
print('get_snat_rule:')
snat_rule = conn.nat.get_snat_rule(rule_id)
print(snat_rule)
print('>>>')

# list snat_rule
print('snat_rules:')
snat_rules = conn.nat.snat_rules()
for snat_rule in snat_rules:
    print(snat_rule)
print('>>>')

# delete snat_rule
print('delete_snat_rule:')
deleteObj = conn.nat.delete_snat_rule(rule_id)
print(deleteObj)
print('Deleting... Please wait 3 seconds.')
time.sleep(3)
print('>>>')

# list snat_rule
print('snat_rules:')
snat_rules = conn.nat.snat_rules()
for snat_rule in snat_rules:
    print(snat_rule)
