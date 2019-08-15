# Copyright 2018 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

import testtools

from openstack.vpc.v1 import security_group_rule

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "id": "2bc0accf-312e-429a-956e-e4407625eb62",
    "description": "about the rule",
    "security_group_id": "a7734e61-b545-452d-a3cd-0189cbd9747a",
    "direction": "ingress",
    "ethertype": "IPv4",
    "protocol": "tcp",
    "port_range_max": 80,
    "port_range_min": 80,
    "remote_ip_prefix": "",
    "remote_group_id": "85cc3048-abc3-43cc-89b3-377341426ac5",
    "tenant_id": "e4f50856753b4dc6afee5fa6b9b6c550"
}


class TestSecurityGroupRule(testtools.TestCase):

    def test_basic(self):
        sot = security_group_rule.SecurityGroupRule()
        self.assertEqual('security_group_rule', sot.resource_key)
        self.assertEqual('security_group_rules', sot.resources_key)
        self.assertEqual('/security-group-rules', sot.base_path)
        self.assertEqual('vpc', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = security_group_rule.SecurityGroupRule(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['security_group_id'], sot.security_group_id)
        self.assertEqual(EXAMPLE['direction'], sot.direction)
        self.assertEqual(EXAMPLE['ethertype'], sot.ether_type)
        self.assertEqual(EXAMPLE['protocol'], sot.protocol)
        self.assertEqual(EXAMPLE['port_range_min'], sot.port_range_min)
        self.assertEqual(EXAMPLE['port_range_max'], sot.port_range_max)
        self.assertEqual(EXAMPLE['remote_ip_prefix'], sot.remote_ip_prefix)
        self.assertEqual(EXAMPLE['remote_group_id'], sot.remote_group_id)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
