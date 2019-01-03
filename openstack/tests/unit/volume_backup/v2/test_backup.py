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

from openstack.volume_backup.v2 import backup as _backup

DATA = {
    "backup_id": "Test backup_id for URI",

    "volume_id": "Test volume_id for Request and Response",
    "snapshot_id": "Test snapshot_id for Request and Response",
    "name": "Test name for Request and Response",
    "description": "Test description for Request and Response",
    "container": "Test container for Request and Response",
    "incremental": True,
    "force": True,
    "project_id": "Test project_id for Request",

    "id": "Test id for Response",
    "links": [
        # Test links for Response
    ],
    "status": "Test status for Response",
    "availability_zone": "Test availability_zone for Response",
    "fail_reason": "Test fail_reason for Response",
    "size": 6,
    "object_count": 6,
    "created_at": "Test created_at for Response",
    "tenant_id": "Test os-bak-tenant-attr:tenant_id for Response",
    "service_metadata": "Test service_metadata for Response",
    "updated_at": "Test updated_at for Response",
    "data_timestamp": "Test data_timestamp for Response",
    "has_dependent_backups": True,
    "is_incremental": True,
}


class TestBackup(testtools.TestCase):

    def setUp(self):
        super(TestBackup, self).setUp()

    def test_basic(self):
        backup = _backup.Backup()
        self.assertEqual("backup", backup.resource_key)
        self.assertEqual("backups", backup.resources_key)
        self.assertEqual("/backups", backup.base_path)
        self.assertEqual("volume-backup", backup.service.service_type)

        self.assertTrue(backup.allow_create)
        self.assertTrue(backup.allow_list)
        self.assertTrue(backup.allow_get)
        self.assertTrue(backup.allow_delete)

        self.assertDictEqual(
            {
                "name": "name",
                "status": "status",
                "volume_id": "volume_id",
                "offset": "offset",
                "limit": "limit",
                "marker": "marker"
            },
            backup._query_mapping._mapping
        )

    def test_make_it(self):
        backup = _backup.Backup(**DATA)

        self.assertEqual(DATA["tenant_id"], backup.tenant_id)

        self.assertEqual(DATA["volume_id"], backup.volume_id)
        self.assertEqual(DATA["snapshot_id"], backup.snapshot_id)
        self.assertEqual(DATA["name"], backup.name)
        self.assertEqual(DATA["description"], backup.description)
        self.assertEqual(DATA["container"], backup.container)
        self.assertEqual(DATA["incremental"], backup.incremental)
        self.assertEqual(DATA["force"], backup.force)
        self.assertEqual(DATA["project_id"], backup.project_id)

        self.assertEqual(DATA["id"], backup.id)
        self.assertEqual(DATA["links"], backup.links)
        self.assertEqual(DATA["status"], backup.status)
        self.assertEqual(DATA["availability_zone"], backup.availability_zone)
        self.assertEqual(DATA["fail_reason"], backup.fail_reason)
        self.assertEqual(DATA["size"], backup.size)
        self.assertEqual(DATA["object_count"], backup.object_count)
        self.assertEqual(DATA["created_at"], backup.created_at)
        self.assertEqual(DATA["tenant_id"], backup.tenant_id)
        self.assertEqual(DATA["service_metadata"], backup.service_metadata)
        self.assertEqual(DATA["updated_at"], backup.updated_at)
        self.assertEqual(DATA["data_timestamp"], backup.data_timestamp)
        self.assertEqual(DATA["has_dependent_backups"], backup.has_dependent_backups)
        self.assertEqual(DATA["is_incremental"], backup.is_incremental)
