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

from openstack.csbs.v1 import resource

DATA_ResourceBackup = {
    "project_id": "Test project_id for URI and Response",
    "provider_id": "Test provider_id for URI",
    "resource_id": "Test resource_id for URI",

    "protect": {
        # Test protect for Request
    },

    "status": "Test status for Response",
    "created_at": "Test created_at for Response",
    "id": "Test id for Response",
    "resource_graph": "Test resource_graph for Response",
    "protection_plan": {
        # Test protection_plan for Response
    }
}

DATA_ResourceBackupCapability = {
    "project_id": "Test project_id for URI",
    "provider_id": "Test provider_id for URI",

    "check_protectable": [
        # Test check_protectable for Request
    ],

    "protectable": [
        # Test protectable for Response
    ]
}

DATA_ResourceRecoveryCapability = {
    "project_id": "Test project_id for URI",
    "provider_id": "Test provider_id for URI",

    "check_restorable": [
        # Test check_restorable for Request
    ],

    "restorable": [
        # Test restorable for Response
    ]
}


class TestResourceBackup(testtools.TestCase):

    def setUp(self):
        super(TestResourceBackup, self).setUp()

    def test_basic(self):
        resource_backup = resource.ResourceBackup()

        self.assertEqual("checkpoint", resource_backup.resource_key)
        self.assertEqual(None, resource_backup.resources_key)
        self.assertEqual(
            "/providers/%(provider_id)s/resources/%(resource_id)s/action",
            resource_backup.base_path
        )
        self.assertEqual("data-protect", resource_backup.service.service_type)
        self.assertEqual(True, resource_backup.service.requires_project_id)

        self.assertTrue(resource_backup.allow_create)

    def test_make_it(self):
        resource_backup = resource.ResourceBackup(**DATA_ResourceBackup)

        self.assertEqual(DATA_ResourceBackup["project_id"], resource_backup.project_id)
        self.assertEqual(DATA_ResourceBackup["provider_id"], resource_backup.provider_id)
        self.assertEqual(DATA_ResourceBackup["resource_id"], resource_backup.resource_id)

        self.assertEqual(DATA_ResourceBackup["protect"], resource_backup.protect)

        self.assertEqual(DATA_ResourceBackup["status"], resource_backup.status)
        self.assertEqual(DATA_ResourceBackup["created_at"], resource_backup.created_at)
        self.assertEqual(DATA_ResourceBackup["id"], resource_backup.id)
        self.assertEqual(DATA_ResourceBackup["resource_graph"], resource_backup.resource_graph)
        self.assertEqual(DATA_ResourceBackup["protection_plan"], resource_backup.protection_plan)


class TestResourceBackupCapability(testtools.TestCase):

    def setUp(self):
        super(TestResourceBackupCapability, self).setUp()

    def test_basic(self):
        resource_backup_capability = resource.ResourceBackupCapability()

        self.assertEqual(None, resource_backup_capability.resource_key)
        self.assertEqual(None, resource_backup_capability.resources_key)
        self.assertEqual("/providers/%(provider_id)s/resources/action", resource_backup_capability.base_path)
        self.assertEqual("data-protect", resource_backup_capability.service.service_type)
        self.assertEqual(True, resource_backup_capability.service.requires_project_id)

        self.assertTrue(resource_backup_capability.allow_create)

    def test_make_it(self):
        resource_backup_capability = resource.ResourceBackupCapability(**DATA_ResourceBackupCapability)

        self.assertEqual(DATA_ResourceBackupCapability["provider_id"], resource_backup_capability.provider_id)

        self.assertEqual(DATA_ResourceBackupCapability["check_protectable"], resource_backup_capability.check_protectable)

        self.assertEqual(DATA_ResourceBackupCapability["protectable"], resource_backup_capability.protectable)


class TestResourceRecoveryCapability(testtools.TestCase):

    def setUp(self):
        super(TestResourceRecoveryCapability, self).setUp()

    def test_basic(self):
        resource_recovery_capability = resource.ResourceRecoveryCapability()

        self.assertEqual(None, resource_recovery_capability.resource_key)
        self.assertEqual(None, resource_recovery_capability.resources_key)
        self.assertEqual("/providers/%(provider_id)s/resources/action", resource_recovery_capability.base_path)
        self.assertEqual("data-protect", resource_recovery_capability.service.service_type)
        self.assertEqual(True, resource_recovery_capability.service.requires_project_id)

        self.assertTrue(resource_recovery_capability.allow_create)

    def test_make_it(self):
        resource_recovery_capability = resource.ResourceRecoveryCapability(**DATA_ResourceRecoveryCapability)

        self.assertEqual(DATA_ResourceRecoveryCapability["provider_id"], resource_recovery_capability.provider_id)

        self.assertEqual(DATA_ResourceRecoveryCapability["check_restorable"], resource_recovery_capability.check_restorable)

        self.assertEqual(DATA_ResourceRecoveryCapability["restorable"], resource_recovery_capability.restorable)
