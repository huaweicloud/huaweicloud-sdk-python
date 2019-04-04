# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from openstack.compute.v2.server import ServerAction
from openstack.compute.v2.server import ServerActionReqID


IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    'action': "test",
    'instance_uuid': '2',
    'message': '3',
    'project_id': '3',
    'request_id': '3',
    'updated_at': '3',
    'start_time': '3',
    'user_id': '3'
}

DATA = {
    'action': "test",
    'instance_uuid': '2',
    'message': '3',
    'project_id': '3',
    'request_id': '3',
    'start_time': '3',
    'user_id': '3',
    'events': [{}]
}


class TestServerActione(testtools.TestCase):

    def test_basic(self):
        sot = ServerAction()
        #self.assertEqual('instanceAction', sot.resource_key)
        self.assertEqual('instanceActions', sot.resources_key)
        self.assertEqual('/servers/%(server_id)s/os-instance-actions', sot.base_path)
        self.assertEqual('compute', sot.service.service_type)
        self.assertTrue(sot.allow_list)

    def test_make_basic(self):
        sot = ServerAction(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['action'], sot.action)
        self.assertEqual(BASIC_EXAMPLE['instance_uuid'], sot.instance_uuid)
        self.assertEqual(BASIC_EXAMPLE['message'], sot.message)
        self.assertEqual(BASIC_EXAMPLE['project_id'], sot.project_id)
        self.assertEqual(BASIC_EXAMPLE['request_id'], sot.request_id)
        self.assertEqual(BASIC_EXAMPLE['updated_at'], sot.updated_at)
        self.assertEqual(BASIC_EXAMPLE['start_time'], sot.start_time)
        self.assertEqual(BASIC_EXAMPLE['user_id'], sot.user_id)

class TestServerActionByReqID(testtools.TestCase):
    def test_basic(self):
        sot = ServerActionReqID()
        self.assertEqual('instanceAction', sot.resource_key)
        #self.assertEqual('instanceActions', sot.resources_key)
        self.assertEqual('/servers/%(server_id)s/os-instance-actions', sot.base_path)
        self.assertEqual('compute', sot.service.service_type)
        self.assertTrue(sot.allow_get)

    def test_make_basic(self):
        sot = ServerActionReqID(**DATA)
        self.assertEqual(DATA['action'], sot.action)
        self.assertEqual(DATA['instance_uuid'], sot.instance_uuid)
        self.assertEqual(DATA['message'], sot.message)
        self.assertEqual(DATA['project_id'], sot.project_id)
        self.assertEqual(DATA['request_id'], sot.id)
        self.assertEqual(DATA['start_time'], sot.start_time)
        self.assertEqual(DATA['user_id'], sot.user_id)
        self.assertEqual(DATA['events'], sot.events)
