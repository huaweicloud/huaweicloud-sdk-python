# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
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

import testtools
from openstack.volume_backup.v2 import backup

DATA = {
        "volume_id": "0781095c",
        "snapshot_id": "0781095c-b8ab-4ce5-99f3-4c5f6ff75319",
        "name": "2016-12-03T06:24:34.467",
        "description": "2016-12-03T06:24:34.467",
        "job_id": "autobk_a61d",
        "tags": [],
        "key": "f47a4ab5-11f5-4509-97f5-80ce0dd74e37",
        "value": "f47a4ab5-11f5-4509-97f5-80ce0dd74e37"
}

class TestCloudBackup(testtools.TestCase):

    def test_basic(self):
        obj = backup.CloudBackup()
        self.assertEqual('/cloudbackups', obj.base_path)
        self.assertEqual("backup", obj.resource_key)
        self.assertEqual("backups", obj.resources_key)
        self.assertTrue(obj.allow_create)
        self.assertTrue(obj.allow_delete)

    def test_make_it(self):
        obj = backup.CloudBackup(**DATA)
        self.assertEqual(DATA['volume_id'],obj.volume_id)
        self.assertEqual(DATA['snapshot_id'],obj.snapshot_id)
        self.assertEqual(DATA["name"], obj.name)
        self.assertEqual(DATA['description'], obj.description)
        self.assertEqual(DATA['job_id'], obj.job_id)
        self.assertEqual(DATA['tags'], obj.tags)
        self.assertEqual(DATA['key'], obj.key)
        self.assertEqual(DATA['value'], obj.value)

