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

from openstack.vpc.v1 import vpc

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    'id': IDENTIFIER,
    'name': 'vpc-name',
    'cidr': '192.168.0.0/16',
    'status': 'OK',
    'routes': [{'destination': '0.0.0.0/0', 'nexthop': '4.4.4.4'}],
    'enterprise_project_id': '0',
}


class TestVPC(testtools.TestCase):

    def test_basic(self):
        sot = vpc.VPC()
        self.assertEqual('vpc', sot.resource_key)
        self.assertEqual('vpcs', sot.resources_key)
        self.assertEqual('/vpcs', sot.base_path)
        self.assertEqual('vpc', sot.service.service_type)

        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

        self.assertDictEqual({'limit': 'limit', 'marker': 'marker',
                              'enterprise_project_id': 'enterprise_project_id'},
                             sot._query_mapping._mapping)

    def test_make_it(self):
        sot = vpc.VPC(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['cidr'], sot.cidr)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertItemsEqual(EXAMPLE['routes'], sot.routes)
        self.assertEqual(EXAMPLE['enterprise_project_id'],
                         sot.enterprise_project_id)
