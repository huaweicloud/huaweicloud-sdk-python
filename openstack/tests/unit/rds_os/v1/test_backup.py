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

from openstack.rds.v1 import backup

BACKUP_EXAMPLE = {
    "created": "2016-09-12T01:17:05",
    "dataStore": {
        "type": "MySQL",
        "version": "5.6.30",
        "version_id": "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61"
    },
    "description": "123",
    "id": "2f4ddb93-b901-4b08-93d8-1d2e472f30fe",
    "instance_id": "0bc7300c-dc63-45d4-aa3b-d85bf577baac",
    "locationRef": None,
    "name": "test011111",
    "size": None,
    "status": "BUILDING",
    "updated": None,
    "backuptype": "1"
}

BACKUP_POLICY = {
    "keepday": 7,
    "starttime": "00:00:00"
}


class TestBackup(testtools.TestCase):
    example = BACKUP_EXAMPLE
    objcls = backup.Backup

    def test_basic(self):
        sot = self.objcls()

        self.assertEqual('/backups', sot.base_path)
        self.assertEqual('backup', sot.resource_key)
        self.assertEqual('backups', sot.resources_key)

        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['id'], sot.id)
        self.assertEqual(self.example['name'], sot.name)
        self.assertEqual(self.example['instance_id'], sot.instance_id)
        self.assertEqual(self.example['description'], sot.description)
        self.assertEqual(self.example['dataStore'], sot.dataStore)
        self.assertEqual(self.example['size'], sot.size)
        self.assertEqual(self.example['status'], sot.status)
        self.assertEqual(self.example['updated'], sot.updated)
        self.assertEqual(self.example['backuptype'], sot.backuptype)


class TestBackupPolicy(testtools.TestCase):
    example = BACKUP_POLICY
    objcls = backup.BackupPolicy

    def test_basic(self):
        sot = self.objcls()

        self.assertEqual('/instances/%(instanceId)s/backups/policy',
                         sot.base_path)
        self.assertEqual('policy', sot.resource_key)

        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['keepday'], sot.keepday)
        self.assertEqual(self.example['starttime'], sot.starttime)
