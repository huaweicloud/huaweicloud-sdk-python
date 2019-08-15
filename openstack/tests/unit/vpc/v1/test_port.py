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

from openstack.vpc.v1 import port

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    "id": "d00f9c13-412f-4855-8af3-de5d8c24cd60",
    "name": "test",
    "status": "DOWN",
    "admin_state_up": True,
    "fixed_ips": [
            {
                "subnet_id": "70f2e74b-e660-410a-b754-0ca46744348a",
                "ip_address": "10.128.1.10"
            }
    ],
    "mac_address": "fa:16:3e:d7:f2:6c",
    "network_id": "5b808927-13c9-4e60-a4f4-ed6ffe225167",
    "tenant_id": "43f2d1cca56a40729dcb17212482f34d",
    "device_id": "",
    "device_owner": "",
    "security_groups": [
        "02b4e8ee-74fa-4a31-802e-5490df11245e"
    ],
    "extra_dhcp_opts": [],
    "allowed_address_pairs": [],
    "binding:vnic_type": "normal",
    "binding:vif_type": "ovs",
    "binding:vif_details": {},
    "binding:host_id": "02b4e8ee-74fa-4a31-802e-5490df11245e",
    "binding:profile": {},
    "port_security_enabled": True,
    "dns_assignment": [],
    "dns_name": ""
}


class TestPort(testtools.TestCase):

    def test_basic(self):
        sot = port.Port()
        self.assertEqual('port', sot.resource_key)
        self.assertEqual('ports', sot.resources_key)
        self.assertEqual('/ports', sot.base_path)
        self.assertEqual('vpc', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

        self.assertDictEqual(
            {
                'limit': 'limit',
                'marker': 'marker',
                'id': 'id',
                'name': 'name',
                'is_admin_state_up': 'admin_state_up',
                'network_id': 'network_id',
                'mac_address': 'mac_address',
                'device_id': 'device_id',
                'device_owner': 'device_owner',
                'status': 'status'
            },
            sot._query_mapping._mapping)

    def test_make_it(self):
        sot = port.Port(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertTrue(sot.is_admin_state_up)
        self.assertEqual(EXAMPLE['fixed_ips'], sot.fixed_ips)
        self.assertEqual(EXAMPLE['mac_address'], sot.mac_address)
        self.assertEqual(EXAMPLE['network_id'], sot.network_id)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
        self.assertEqual(EXAMPLE['device_id'], sot.device_id)
        self.assertEqual(EXAMPLE['device_owner'], sot.device_owner)
        self.assertEqual(EXAMPLE['security_groups'], sot.security_group_ids)
        self.assertEqual(EXAMPLE['extra_dhcp_opts'], sot.extra_dhcp_opts)
        self.assertEqual(EXAMPLE['allowed_address_pairs'],
                         sot.allowed_address_pairs)
        self.assertEqual(EXAMPLE['binding:host_id'], sot.binding_host_id)
        self.assertEqual(EXAMPLE['binding:profile'], sot.binding_profile)
        self.assertEqual(EXAMPLE['binding:vif_details'],
                         sot.binding_vif_details)
        self.assertEqual(EXAMPLE['binding:vif_type'], sot.binding_vif_type)
        self.assertEqual(EXAMPLE['binding:vnic_type'], sot.binding_vnic_type)
        self.assertTrue(sot.port_security_enabled)
        self.assertEqual(EXAMPLE['dns_assignment'], sot.dns_assignment)
        self.assertEqual(EXAMPLE['dns_name'], sot.dns_name)
