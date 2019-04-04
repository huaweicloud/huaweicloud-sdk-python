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

from openstack.vpc.v1 import quota

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {"type": "vpc", "used": 4, "quota": 150, "min": 0}


class TestQuota(testtools.TestCase):

    def test_basic(self):
        sot = quota.Quota()
        self.assertEqual('quota', sot.resource_key)
        self.assertEqual('quotas.resources', sot.resources_key)
        self.assertEqual('/quotas', sot.base_path)
        self.assertEqual('vpc', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertDictEqual(
            {'limit': 'limit', 'marker': 'marker', 'type': 'type'},
            sot._query_mapping._mapping)

    def test_make_it(self):
        sot = quota.Quota(**EXAMPLE)
        self.assertEqual(EXAMPLE['type'], sot.type)
        self.assertEqual(EXAMPLE['used'], sot.used)
        self.assertEqual(EXAMPLE['quota'], sot.quota)
        self.assertEqual(EXAMPLE['min'], sot.min)
