# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

import mock
import testtools
from openstack.ecs.v1 import tag


SERVER_TAG_EXAMPLE = {
    "key": "key1",
    "value": "value1"
}

PROJECT_TAG_EXAMPLE = {
    "key": "key1",
    "values": [
        "value1",
        "value2"
    ]
}

CREATE_TAG_EXAMPLE = {
    "server_id": "05184ba3-00ba-4fbc-b7a2-03b62b884931",
    "action": "create",
    "tags": [
        {
            "key": "key1",
            "value": "value1"
        }
    ]
}

DELETE_TAG_EXAMPLE = {
    "server_id": "05184ba3-00ba-4fbc-b7a2-03b62b884931",
    "action": "delete",
    "tags": [
        {
            "key": "key1",
            "value": "value1"
        }
    ]
}


class TestServerTag(testtools.TestCase):
    def test_basic(self):
        obj = tag.ServerTag()
        self.assertEqual("/cloudservers/%(server_id)s/tags", obj.base_path)
        self.assertEqual("tags", obj.resources_key)
        self.assertEqual("ecs", obj.service.service_type)
        self.assertTrue(obj.allow_list)

    def test_make_it(self):
        obj = tag.ServerTag(**SERVER_TAG_EXAMPLE)
        self.assertEqual(SERVER_TAG_EXAMPLE["key"], obj.key)
        self.assertEqual(SERVER_TAG_EXAMPLE["value"], obj.value)


class TestProjectTag(testtools.TestCase):
    def test_basic(self):
        obj = tag.ProjectTag()
        self.assertEqual("/cloudservers/tags", obj.base_path)
        self.assertEqual("tags", obj.resources_key)
        self.assertEqual("ecs", obj.service.service_type)
        self.assertTrue(obj.allow_list)

    def test_make_it(self):
        obj = tag.ProjectTag(**PROJECT_TAG_EXAMPLE)
        self.assertEqual(PROJECT_TAG_EXAMPLE["key"], obj.key)
        self.assertEqual(PROJECT_TAG_EXAMPLE["values"], obj.values)


class TestServerTagAction(testtools.TestCase):
    def setUp(self):
        super(TestServerTagAction, self).setUp()
        self.resp = mock.Mock()
        self.resp.body = None
        self.resp.headers = {}
        self.sess = mock.Mock()
        self.sess.post = mock.Mock(return_value=self.resp)

    def test_basic(self):
        obj = tag.ServerTagAction()
        self.assertEqual("/cloudservers/%(server_id)s/tags/action", obj.base_path)
        self.assertEqual("ecs", obj.service.service_type)
        self.assertTrue(obj.allow_create)

    def test_create_server_tags(self):
        sot = tag.ServerTagAction(**CREATE_TAG_EXAMPLE)
        self.assertIsInstance(sot.create(self.sess), tag.ServerTagAction)

        url = '/cloudservers/05184ba3-00ba-4fbc-b7a2-03b62b884931/tags/action'
        headers = {}
        CREATE_TAG_EXAMPLE.pop("server_id")
        self.sess.post.assert_called_with(
            url, endpoint_filter=sot.service, endpoint_override=None, json=CREATE_TAG_EXAMPLE, headers=headers)

    def test_delete_server_tags(self):
        sot = tag.ServerTagAction(**DELETE_TAG_EXAMPLE)
        self.assertIsInstance(sot.create(self.sess), tag.ServerTagAction)

        url = '/cloudservers/05184ba3-00ba-4fbc-b7a2-03b62b884931/tags/action'
        headers = {}
        DELETE_TAG_EXAMPLE.pop("server_id")
        self.sess.post.assert_called_with(
            url, endpoint_filter=sot.service, endpoint_override=None, json=DELETE_TAG_EXAMPLE, headers=headers)
