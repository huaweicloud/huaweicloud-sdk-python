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

from openstack.vpc.v1 import bandwidth

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "id": "a79fd11a-047b-4f5b-8f12-99c178cc780a",
    "name": "ddddd",
    "size": 5,
    "share_type": "PER",
    "publicip_info": [
        {
            "publicip_id": "80d5b82e-43b9-4f82-809a-37bec5793bd4",
            "publicip_address": "161.17.101.10",
            "publicip_type": "5_bgp"
        }
    ],
    "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
    "bandwidth_type": "bgp",
    "charge_mode": "bandwidth",
    "billing_info": "billing",
    "enterprise_project_id": "0",
}


class TestBandwidth(testtools.TestCase):

    def test_basic(self):
        sot = bandwidth.Bandwidth()
        self.assertEqual('bandwidth', sot.resource_key)
        self.assertEqual('bandwidths', sot.resources_key)
        self.assertEqual('/bandwidths', sot.base_path)
        self.assertEqual('vpc', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)

        self.assertDictEqual(
            {
                'limit': 'limit',
                'marker': 'marker',
            },
            sot._query_mapping._mapping)

    def test_make_it(self):
        sot = bandwidth.Bandwidth(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['size'], sot.size)
        self.assertEqual(EXAMPLE['share_type'], sot.share_type)
        self.assertEqual(EXAMPLE['publicip_info'], sot.publicip_info)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
        self.assertEqual(EXAMPLE['bandwidth_type'], sot.bandwidth_type)
        self.assertEqual(EXAMPLE['charge_mode'], sot.charge_mode)
        self.assertEqual(EXAMPLE['billing_info'], sot.billing_info)
        self.assertEqual(EXAMPLE['enterprise_project_id'],
                         sot.enterprise_project_id)
