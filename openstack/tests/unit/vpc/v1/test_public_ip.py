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

import mock
import testtools

from openstack.vpc.v1 import public_ip

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    'id': IDENTIFIER,
    'profile': {'user_id': 'useruuid', 'product_id': 'productuuid'},
    'status': 'ACTIVE',
    'type': '5_bgp',
    "public_ip_address": "161.17.101.12",
    "public_ipv6_address": "",
    "ip_version": 4,
    "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
    "private_ip_address": "192.168.10.5",
    "create_time": "2015-07-16 04:32:50",
    "port_id": "f588ccfa-8750-4d7c-bf5d-2ede24414706",
    "bandwidth_id": "49c8825b-bed9-46ff-9416-704b96d876a2",
    "bandwidth_share_type": "PER",
    "bandwidth_size": 10,
    "bandwidth_name": "bandwidth-test",
    "enterprise_project_id": "0",
}


class TestPublicIP(testtools.TestCase):

    def test_basic(self):
        sot = public_ip.PublicIP()
        self.assertEqual('publicip', sot.resource_key)
        self.assertEqual('publicips', sot.resources_key)
        self.assertEqual('/publicips', sot.base_path)
        self.assertEqual('vpc', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertDictEqual({'limit': 'limit', 'marker': 'marker',
                              'ip_version': 'ip_version'},
                             sot._query_mapping._mapping)

    def test_make_it(self):
        sot = public_ip.PublicIP(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertDictEqual(EXAMPLE['profile'], sot.profile)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['type'], sot.type)
        self.assertEqual(EXAMPLE['public_ip_address'],
                         sot.public_ip_address)
        self.assertEqual(EXAMPLE['public_ipv6_address'],
                         sot.public_ipv6_address)
        self.assertEqual(EXAMPLE['ip_version'], sot.ip_version)
        self.assertEqual(EXAMPLE['public_ip_address'], sot.name)
        self.assertEqual(EXAMPLE['private_ip_address'], sot.private_ip_address)
        self.assertEqual(EXAMPLE['port_id'], sot.port_id)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
        self.assertEqual(EXAMPLE['create_time'], sot.create_time)
        self.assertEqual(EXAMPLE['bandwidth_id'], sot.bandwidth_id)
        self.assertEqual(EXAMPLE['bandwidth_name'], sot.bandwidth_name)
        self.assertEqual(EXAMPLE['bandwidth_share_type'],
                         sot.bandwidth_share_type)
        self.assertEqual(EXAMPLE['bandwidth_size'], sot.bandwidth_size)
        self.assertEqual(EXAMPLE['enterprise_project_id'],
                         sot.enterprise_project_id)
