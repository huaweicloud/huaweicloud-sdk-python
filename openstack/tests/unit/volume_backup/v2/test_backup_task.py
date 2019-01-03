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
from openstack.volume_backup.v2 import backup_task

DATA = {
        "status": "RUNNING",
        "job_id": "0781095c-b8ab-4ce5-99f3-4c5f6ff75319",
        "created_at": "2016-12-03T06:24:34.467",
        "finished_at": "2016-12-03T06:24:34.467",
        "backup_name": "autobk_a61d",
        "resource_id": "f47a4ab5-11f5-4509-97f5-80ce0dd74e37",
        "resource_type": "f47a4ab5-11f5-4509-97f5-80ce0dd74e37",
        "vbs_job_id": "f47a4ab5-11f5-4509-97f5-80ce0dd74e37",
        "message": "volume",
        "code": 200
}

class TestBackupTask(testtools.TestCase):

    def test_basic(self):
        obj = backup_task.BackupTask()
        self.assertEqual('/backuppolicy/%(policy_id)s/backuptasks', obj.base_path)
        self.assertEqual(None, obj.resource_key)
        self.assertEqual("tasks", obj.resources_key)
        self.assertTrue(obj.allow_list)

    def test_make_it(self):
        obj = backup_task.BackupTask(**DATA)
        self.assertEqual(DATA['status'],obj.status)
        self.assertEqual(DATA['job_id'],obj.id)
        self.assertEqual(DATA["created_at"], obj.created_at)
        self.assertEqual(DATA['finished_at'], obj.finished_at)
        self.assertEqual(DATA['backup_name'], obj.backup_name)
        self.assertEqual(DATA['resource_id'], obj.resource_id)
        self.assertEqual(DATA['resource_type'], obj.resource_type)
        self.assertEqual(DATA['vbs_job_id'], obj.vbs_job_id)
        self.assertEqual(DATA['code'], obj.code)
        self.assertEqual(DATA['message'], obj.message)
