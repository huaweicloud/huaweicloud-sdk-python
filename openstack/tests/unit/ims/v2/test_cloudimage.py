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
      "__sequence_num": "test",
      "__root_origin": "test",
      "enterprise_project_id": "test",
      "__system_support_market": True,
      "__support_xen_gpu_type": True,
      "__data_origin": "test",
      "__support_highperformance": "test",
      "__support_diskintensive": "test",
      "__support_xen": "test",
      "__support_kvm": "test",
      "__image_size": "test",
      "__productcode": "test",
      "__backup_id": "test",
      "__originalimagename": "test",
      "deleted_at":"TEST",
      "__description": "test",
      "max_ram": "test",
      "deleted": True,
      "schema": "/v2/schemas/image",
      "min_disk": 100,
      "created_at": "2018-09-06T14:03:27Z",
      "__image_source_type": "uds",
      "container_format": "bare",
      "file": "/v2/images/bc6bed6e-ba3a-4447-afcc-449174a3eb52/file",
      "updated_at": "2018-09-06T15:17:33Z",
      "protected": True,
      "checksum": "d41d8cd98f00b204e9800998ecf8427e",
      "__support_kvm_fpga_type": "VU9P",
      "id": "bc6bed6e-ba3a-4447-afcc-449174a3eb52",
      "__isregistered": "true",
      "min_ram": 2048,
      "__lazyloading": True,
      "owner": "1bed856811654c1cb661a6ca845ebc77",
      "__os_type": "Linux",
      "__imagetype": "gold",
      "visibility": "public",
      "virtual_env_type": "FusionCompute",
      "tags": [],
      "__platform": "CentOS",
      "size": 0,
      "__os_bit": "64",
      "__os_version": "CentOS 7.3 64bit",
      "name": "CentOS 7.3 64bit vivado",
      #"self": "/v2/images/bc6bed6e-ba3a-4447-afcc-449174a3eb52",
      "disk_format": "zvhd2",
      "virtual_size": None,
      "status": "active",
    }

class TestCloudImage(testtools.TestCase):

    def setUp(self):
        super(TestCloudImage, self).setUp()

    def test_basic(self):
        sot = cloudimage.CloudImage()
        self.assertIsNone(sot.resource_key)
        self.assertEqual('images', sot.resources_key)
        self.assertEqual('/cloudimages', sot.base_path)
        self.assertEqual('ims', sot.service.service_type)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.patch_update)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = cloudimage.CloudImage(**EXAMPLE)
        self.assertEqual(EXAMPLE["id"], sot.id)
        self.assertEqual(EXAMPLE["__sequence_num"], sot._CloudImage__sequence_num)
        self.assertEqual(EXAMPLE["__root_origin"], sot._CloudImage__root_origin)
        self.assertEqual(EXAMPLE["enterprise_project_id"], sot.enterprise_project_id)
        self.assertEqual(EXAMPLE["__system_support_market"], sot._CloudImage__system_support_market)
        self.assertEqual(EXAMPLE["__support_xen_gpu_type"], sot._CloudImage__support_xen_gpu_type)
        self.assertEqual(EXAMPLE["__data_origin"], sot._CloudImage__data_origin)
        self.assertEqual(EXAMPLE["__support_highperformance"], sot._CloudImage__support_highperformance)
        self.assertEqual(EXAMPLE["__support_diskintensive"], sot._CloudImage__support_diskintensive)
        self.assertEqual(EXAMPLE["__support_xen"], sot._CloudImage__support_xen)
        self.assertEqual(EXAMPLE["__support_kvm"], sot._CloudImage__support_kvm)
        self.assertEqual(EXAMPLE["__image_size"], sot._CloudImage__image_size)
        self.assertEqual(EXAMPLE["__productcode"], sot._CloudImage__productcode)
        self.assertEqual(EXAMPLE["__backup_id"], sot._CloudImage__backup_id)
        self.assertEqual(EXAMPLE["__originalimagename"], sot._CloudImage__originalimagename)
        self.assertEqual(EXAMPLE["deleted_at"], sot.deleted_at)
        self.assertEqual(EXAMPLE["__description"], sot._CloudImage__description)
        self.assertEqual(EXAMPLE["max_ram"], sot.max_ram)
        self.assertEqual(EXAMPLE["deleted"], sot.deleted)
        self.assertEqual(EXAMPLE["schema"], sot.schema)
        self.assertEqual(EXAMPLE["min_disk"], sot.min_disk)
        self.assertEqual(EXAMPLE["created_at"], sot.created_at)
        self.assertEqual(EXAMPLE["__image_source_type"], sot._CloudImage__image_source_type)
        self.assertEqual(EXAMPLE["container_format"], sot.container_format)
        self.assertEqual(EXAMPLE["file"], sot.file)
        self.assertEqual(EXAMPLE["updated_at"], sot.updated_at)
        self.assertEqual(EXAMPLE["protected"], sot.protected)
        self.assertEqual(EXAMPLE["checksum"], sot.checksum)
        self.assertEqual(EXAMPLE["__support_kvm_fpga_type"], sot._CloudImage__support_kvm_fpga_type)
        self.assertEqual(EXAMPLE["__isregistered"], sot._CloudImage__isregistered)
        self.assertEqual(EXAMPLE["min_ram"], sot.min_ram)
        self.assertEqual(EXAMPLE["__lazyloading"], sot._CloudImage__lazyloading)
        self.assertEqual(EXAMPLE["owner"], sot.owner)
        self.assertEqual(EXAMPLE["__os_type"], sot._CloudImage__os_type)
        self.assertEqual(EXAMPLE["__imagetype"], sot._CloudImage__imagetype)
        self.assertEqual(EXAMPLE["visibility"], sot.visibility)
        self.assertEqual(EXAMPLE["virtual_env_type"], sot.virtual_env_type)
        self.assertEqual(EXAMPLE["tags"], sot.tags)
        self.assertEqual(EXAMPLE["__platform"], sot._CloudImage__platform)
        self.assertEqual(EXAMPLE["size"], sot.size)
        self.assertEqual(EXAMPLE["__os_bit"], sot._CloudImage__os_bit)
        self.assertEqual(EXAMPLE["__os_version"], sot._CloudImage__os_version)
        self.assertEqual(EXAMPLE["name"], sot.name)
        #self.assertEqual(EXAMPLE["self"], sot._self)
        self.assertEqual(EXAMPLE["disk_format"], sot.disk_format)
        self.assertEqual(EXAMPLE["virtual_size"], sot.virtual_size)
        self.assertEqual(EXAMPLE["status"], sot.status)