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

from openstack.vpc.v1 import subnet

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    'id': IDENTIFIER,
    'name': 'subnet',
    'cidr': '192.168.20.0/24',
    'dnsList': ['114.114.114.114', '114.114.115.115'],
    'status': 'ACTIVE',
    'vpc_id': '3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85',
    'gateway_ip': '192.168.20.1',
    'dhcp_enable': True,
    'primary_dns': '114.114.114.114',
    'secondary_dns': '114.114.115.115',
    'availability_zone': 'aa-bb-cc',
    'neutron_network_id': '4779ab1c-7c1a-44b1-a02e-93dfc361b32d',
    'neutron_subnet_id': '213cb9d-3122-2ac1-1a29-91ffc1231a12',
}


class TestSubnet(testtools.TestCase):

    def setUp(self):
        super(TestSubnet, self).setUp()
        self.subnet_result = {
            'subnet': {
                'name': 'subnetqq',
                'dhcp_enable': False,
                'primary_dns': '114.114.114.115',
                'secondary_dns': '114.114.115.116',
                'dnsList': ['114.114.114.115', '114.114.115.116'],
            }
        }

    def test_basic(self):
        sot = subnet.Subnet()
        self.assertEqual('subnet', sot.resource_key)
        self.assertEqual('subnets', sot.resources_key)
        self.assertEqual('/subnets', sot.base_path)
        self.assertEqual('/vpcs/%(vpc_id)s/subnets',
                         sot.update_base_path)
        self.assertEqual('/vpcs/%(vpc_id)s/subnets',
                         sot.delete_base_path)
        self.assertEqual('vpc', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

        self.assertDictEqual(
            {'limit': 'limit', 'marker': 'marker', 'vpc_id': 'vpc_id'},
            sot._query_mapping._mapping)

    def test_make_it(self):
        sot = subnet.Subnet(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['cidr'], sot.cidr)
        self.assertItemsEqual(EXAMPLE['dnsList'], sot.dnsList)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['vpc_id'], sot.vpc_id)
        self.assertEqual(EXAMPLE['gateway_ip'], sot.gateway_ip)
        self.assertTrue(sot.is_dhcp_enabled)
        self.assertEqual(EXAMPLE['primary_dns'], sot.primary_dns)
        self.assertEqual(EXAMPLE['secondary_dns'], sot.secondary_dns)
        self.assertEqual(EXAMPLE['availability_zone'], sot.availability_zone)
        self.assertEqual(EXAMPLE['neutron_network_id'], sot.neutron_network_id)
        self.assertEqual(EXAMPLE['neutron_subnet_id'], sot.neutron_subnet_id)

    def test_update(self):
        response = mock.Mock()
        response.json.return_value = {'id': IDENTIFIER, 'status': 'ACTIVE'}
        response.headers = {}
        sess = mock.Mock()
        sess.put.return_value = response
        sess.get_project_id.return_value = 'uuid'

        sot = subnet.Subnet(**EXAMPLE)
        sot._body.clean()
        sot.name = self.subnet_result['subnet']['name']
        sot.is_dhcp_enabled = self.subnet_result['subnet']['dhcp_enable']
        sot.primary_dns = self.subnet_result['subnet']['primary_dns']
        sot.secondary_dns = self.subnet_result['subnet']['secondary_dns']
        sot.dnsList = self.subnet_result['subnet']['dnsList']
        sot.update(sess)

        uri = 'vpcs/%(vpc_id)s/subnets/%(id)s' % EXAMPLE
        sess.put.assert_called_once_with(
            uri,
            headers={},
            json=self.subnet_result,
            endpoint_override=sot.service.get_endpoint_override(),
            endpoint_filter=sot.service)
        self.assertEqual('ACTIVE', sot.status)

    def test_delete(self):
        response = mock.Mock()
        response.code = 204
        response.headers = {}
        sess = mock.Mock()
        sess.delete.return_value = response
        sess.get_project_id.return_value = 'uuid'

        sot = subnet.Subnet(**EXAMPLE)
        sot.delete(sess)

        uri = 'vpcs/%(vpc_id)s/subnets/%(id)s' % EXAMPLE
        sess.delete.assert_called_once_with(
            uri,
            headers={'Accept': ''},
            endpoint_override=sot.service.get_endpoint_override(),
            params=None,
            endpoint_filter=sot.service
        )
