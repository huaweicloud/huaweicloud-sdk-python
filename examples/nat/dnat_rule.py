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
import os
from openstack import connection
from openstack import utils

utils.enable_logging(debug = True, stream = sys.stdout)

username = "***"
password = "***"
projectId = "054efa2069a64785a196efe56c05ee74"
userDomainId = "cb06f3a9fa4e464ea62695b4dd26e5f0"
auth_url = "https://iam.eu-de.otc.t-systems.com/v3"

conn = connection.Connection(
                             auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password,
                             verify=False
                             )

nats = conn.nat.create_dnat_rule(nat_gateway_id = "8d45f435-61f7-4a30-b955-ae40f3e3989b",
                                     floating_ip_id = "dd05c596-fde4-491f-bc1b-24f2d7e3e623",
                                     protocol = "TCP",
                                     external_service_port = 6000,
                                     internal_service_port = 5000,
                                     port_id = "66db34af-2eba-4356-b7b8-9e5f71b3a5dd"
                                     )
print nats


print conn.nat.get_dnat_rule('5e465a4f-30ec-4f73-8ec7-5820fda6930c')
print conn.nat.delete_dnat_rule("5e465a4f-30ec-4f73-8ec7-5820fda6930c")
nats = conn.nat.dnat_rules()
for dnat in  nats:
    print dnat