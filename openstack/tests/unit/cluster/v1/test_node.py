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

import mock
import testtools

from openstack.cluster.v1 import node


FAKE_ID = '123d0955-0099-aabb-b8fa-6a44655ceeff'
FAKE_NAME = 'test_node'

FAKE = {
    'id': FAKE_ID,
    'cluster_id': 'clusterA',
    'metadata': {'key1': 'value1'},
    'name': FAKE_NAME,
    'profile_id': 'myserver',
    'user': '3747afc360b64702a53bdd64dc1b8976',
    'project': '42d9e9663331431f97b75e25136307ff',
    'index': 1,
    'role': 'main',
    'dependents': {},
    'created_at': '2015-10-10T12:46:36.000000',
    'updated_at': '2016-10-10T12:46:36.000000',
    'init_at': '2015-10-10T12:46:36.000000',
}


class TestNode(testtools.TestCase):

    def test_basic(self):
        sot = node.Node()
        self.assertEqual('node', sot.resource_key)
        self.assertEqual('nodes', sot.resources_key)
        self.assertEqual('/nodes', sot.base_path)
        self.assertEqual('clustering', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_instantiate(self):
        sot = node.Node(**FAKE)
        self.assertEqual(FAKE['id'], sot.id)
        self.assertEqual(FAKE['profile_id'], sot.profile_id)
        self.assertEqual(FAKE['cluster_id'], sot.cluster_id)
        self.assertEqual(FAKE['user'], sot.user_id)
        self.assertEqual(FAKE['project'], sot.project_id)
        self.assertEqual(FAKE['name'], sot.name)
        self.assertEqual(FAKE['index'], sot.index)
        self.assertEqual(FAKE['role'], sot.role)
        self.assertEqual(FAKE['metadata'], sot.metadata)
        self.assertEqual(FAKE['init_at'], sot.init_at)
        self.assertEqual(FAKE['created_at'], sot.created_at)
        self.assertEqual(FAKE['updated_at'], sot.updated_at)
        self.assertEqual(FAKE['dependents'], sot.dependents)

    def test_check(self):
        sot = node.Node(**FAKE)

        resp = mock.Mock()
        resp.json = mock.Mock(return_value='')
        sess = mock.Mock()
        sess.post = mock.Mock(return_value=resp)
        self.assertEqual('', sot.check(sess))
        url = 'nodes/%s/actions' % sot.id
        body = {'check': {}}
        sess.post.assert_called_once_with(url, endpoint_filter=sot.service,
                                          json=body)

    def test_recover(self):
        sot = node.Node(**FAKE)

        resp = mock.Mock()
        resp.json = mock.Mock(return_value='')
        sess = mock.Mock()
        sess.post = mock.Mock(return_value=resp)
        self.assertEqual('', sot.recover(sess))
        url = 'nodes/%s/actions' % sot.id
        body = {'recover': {}}
        sess.post.assert_called_once_with(url, endpoint_filter=sot.service,
                                          json=body)

    def test_operation(self):
        sot = node.Node(**FAKE)

        resp = mock.Mock()
        resp.json = mock.Mock(return_value='')
        sess = mock.Mock()
        sess.post = mock.Mock(return_value=resp)
        self.assertEqual('', sot.op(sess, 'dance', style='tango'))
        url = 'nodes/%s/ops' % sot.id
        sess.post.assert_called_once_with(url, endpoint_filter=sot.service,
                                          json={'dance': {'style': 'tango'}})


class TestNodeDetail(testtools.TestCase):

    def test_basic(self):
        sot = node.NodeDetail()
        self.assertEqual('/nodes/%(node_id)s?show_details=True', sot.base_path)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertFalse(sot.allow_list)
