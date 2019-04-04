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

from openstack.vpc.v1 import private_ip

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    'id': IDENTIFIER,
    'status': 'ACTIVE',
    'subnet_id': '531dec0f-3116-411b-a21b-e612e42349fd',
    "ip_address": "192.168.1.11",
    "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
    "device_owner": ""
}


class TestPrivateIP(testtools.TestCase):

    def test_basic(self):
        sot = private_ip.PrivateIP()
        self.assertEqual('privateip', sot.resource_key)
        self.assertEqual('privateips', sot.resources_key)
        self.assertEqual('/privateips', sot.base_path)
        self.assertEqual('/subnets/%(subnet_id)s/privateips',
                         sot.list_base_path)
        self.assertEqual('vpc', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertDictEqual({'limit': 'limit', 'marker': 'marker'},
                             sot._query_mapping._mapping)

    def test_make_it(self):
        sot = private_ip.PrivateIP(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['subnet_id'], sot.subnet_id)
        self.assertEqual(EXAMPLE['ip_address'], sot.ip_address)
        self.assertEqual(EXAMPLE['tenant_id'], sot.project_id)
        self.assertEqual(EXAMPLE['device_owner'], sot.device_owner)

    def test_create(self):
        response = mock.Mock()
        response.json.return_value = {'privateips': [EXAMPLE]}
        response.headers = {}
        sess = mock.Mock()
        sess.post.return_value = response
        sess.get_project_id.return_value = 'uuid'

        sot = private_ip.PrivateIP(subnet_id='subnet_id',
                                   ip_address='192.168.0.3')
        sot.create(sess)

        uri = sot.base_path
        expected_body = {
            'privateips': [{'subnet_id': 'subnet_id',
                            'ip_address': '192.168.0.3'}]
        }
        sess.post.assert_called_once_with(
            uri,
            endpoint_filter=sot.service,
            endpoint_override=sot.service.get_endpoint_override(),
            json=expected_body,
            headers={}
        )

    def test_batch_create(self):
        response = mock.Mock()
        response.json.return_value = {'privateips': [EXAMPLE]}
        response.headers = {}
        sess = mock.Mock()
        sess.post.return_value = response

        param = ({'subnet_id': 'subnet_id',
                  'ip_address': '192.168.0.3'},)
        expected_body = {
            'privateips': param
        }
        result = private_ip.PrivateIP.batch_create(sess, param)
        clz = private_ip.PrivateIP
        sess.post.assert_called_once_with(
            clz.base_path,
            endpoint_filter=clz.service,
            endpoint_override=clz.service.get_endpoint_override(),
            json=expected_body)
        self.assertEqual(list, type(result))
        self.assertEqual(1, len(result))
