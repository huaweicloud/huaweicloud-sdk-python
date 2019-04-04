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

from openstack.vpc.v1 import security_group

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "id": "16b6e77a-08fa-42c7-aa8b-106c048884e6",
    "name": "qq",
    "description": "qq",
    "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
    "security_group_rules": [
        {
            "direction": "egress",
            "ethertype": "IPv4",
            "id": "369e6499-b2cb-4126-972a-97e589692c62",
            "security_group_id": "16b6e77a-08fa-42c7-aa8b-106c048884e6"
        },
        {
            "direction": "ingress",
            "ethertype": "IPv4",
            "id": "0222556c-6556-40ad-8aac-9fd5d3c06171",
            "remote_group_id": "16b6e77a-08fa-42c7-aa8b-106c048884e6",
            "security_group_id": "16b6e77a-08fa-42c7-aa8b-106c048884e6"
        }
    ],
    "enterprise_project_id": "0",
}


class TestSecurityGroup(testtools.TestCase):

    def test_basic(self):
        sot = security_group.SecurityGroup()
        self.assertEqual('security_group', sot.resource_key)
        self.assertEqual('security_groups', sot.resources_key)
        self.assertEqual('/security-groups', sot.base_path)
        self.assertEqual('vpc', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertDictEqual(
            {'limit': 'limit', 'marker': 'marker', 'vpc_id': 'vpc_id',
             'enterprise_project_id': 'enterprise_project_id'},
            sot._query_mapping._mapping)

    def test_make_it(self):
        sot = security_group.SecurityGroup(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['vpc_id'], sot.vpc_id)
        self.assertItemsEqual(EXAMPLE['security_group_rules'],
                              sot.security_group_rules)
        self.assertEqual(dict, type(sot.security_group_rules[0]))
        self.assertEqual(EXAMPLE['enterprise_project_id'],
                         sot.enterprise_project_id)
