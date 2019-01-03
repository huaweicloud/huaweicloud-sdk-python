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

import json

import mock
import testtools

from openstack import exceptions
from openstack.ims.v2 import cloudimage

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
      "name": "ims_test_file",
      "description": "OBS",
      "instance_id": "test",
      "data_images": [],
      "image_url": "ims-image:centos70.qcow2",
      "os_version": " CentOS 7.0 64bit",
      "is_config_init":True,
      "min_disk": 40,
      "is_config":True,
      "tags":[
            "aaa.111",
            "bbb.333",
            "ccc.444"
        ],
      "enterprise_project_id": "test",
      "cmk_id": "test",
      "type": "test",
      "job_id": "123",
      "max_ram": 1,
      "min_ram": 2,
      "image_tags": [],
    }

class TestCloudImageAction(testtools.TestCase):

    def setUp(self):
        super(TestCloudImageAction, self).setUp()

    def test_basic(self):
        sot = cloudimage.CloudImageAction()
        self.assertIsNone(sot.resource_key)
        self.assertIsNone(sot.resources_key)
        self.assertEqual('/cloudimages/action', sot.base_path)
        self.assertEqual('ims', sot.service.service_type)
        self.assertTrue(sot.allow_create)

    def test_make_it(self):
        sot = cloudimage.CloudImageAction(**EXAMPLE)
        self.assertEqual(EXAMPLE["name"], sot.name)
        self.assertEqual(EXAMPLE["description"], sot.description)
        self.assertEqual(EXAMPLE["instance_id"], sot.instance_id)
        self.assertEqual(EXAMPLE["data_images"], sot.data_images)
        self.assertEqual(EXAMPLE["image_url"], sot.image_url)
        self.assertEqual(EXAMPLE["os_version"], sot.os_version)
        self.assertEqual(EXAMPLE["is_config_init"], sot.is_config_init)
        self.assertEqual(EXAMPLE["min_disk"], sot.min_disk)
        self.assertEqual(EXAMPLE["is_config"], sot.is_config)
        self.assertEqual(EXAMPLE["tags"], sot.tags)
        self.assertEqual(EXAMPLE["enterprise_project_id"], sot.enterprise_project_id)
        self.assertEqual(EXAMPLE["cmk_id"], sot.cmk_id)
        self.assertEqual(EXAMPLE["type"], sot.type)
        self.assertEqual(EXAMPLE["job_id"], sot.job_id)
        self.assertEqual(EXAMPLE["max_ram"], sot.max_ram)
        self.assertEqual(EXAMPLE["min_ram"], sot.min_ram)
        self.assertEqual(EXAMPLE["image_tags"], sot.image_tags)

