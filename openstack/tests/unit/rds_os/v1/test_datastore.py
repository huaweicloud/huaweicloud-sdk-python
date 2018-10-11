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

from openstack.rds.v1 import datastore

VERSION_EXAMPLE = {
    "id": "e8a8b8cc-63f8-4fb5-8d4a-24c502317a62",
    "name": "5.6.33",
    "datastore": "736270b9-27c7-4f03-823b-447d8245e1c2",
    "image": "988f7639-4bc9-4225-bdfe-f47bcde1a5f2",
    "packages": "MySQL-server-5.6.33",
    "active": 1
}

PARAMETER_EXAMPLE = {
    "name": "connect_timeout",
    "min": 2,
    "max": 31536000,
    "restart_required": False,
    "type": "integer",
    "description": "mysqld ...",
    "datastore_version_id": "f8e67741-e767-4137-b394-3fb8a3fafd2f"
}


class TestVersion(testtools.TestCase):
    example = VERSION_EXAMPLE
    objcls = datastore.Version

    def test_basic(self):
        sot = self.objcls()
        self.assertEqual(
            '/datastores/%(datastore_name)s/versions',
            sot.base_path)
        self.assertEqual('dataStores', sot.resources_key)

        self.assertTrue(sot.allow_list)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['id'], sot.id)
        self.assertEqual(self.example['name'], sot.name)
        self.assertEqual(self.example['datastore'], sot.datastore)
        self.assertEqual(self.example['image'], sot.image)
        self.assertEqual(self.example['packages'], sot.packages)
        self.assertEqual(self.example['active'], sot.active)


class TestParameter(testtools.TestCase):
    example = PARAMETER_EXAMPLE
    objcls = datastore.Parameter

    def test_basic(self):
        sot = self.objcls()

        self.assertEqual(
            '/datastores/versions/%(datastore_version_id)s/parameters/',
            sot.base_path)
        self.assertEqual('configuration-parameters', sot.resources_key)

        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['name'], sot.name)
        self.assertEqual(self.example['min'], sot.min)
        self.assertEqual(self.example['max'], sot.max)
        self.assertEqual(self.example['restart_required'],
                         sot.restart_required)
        self.assertEqual(self.example['type'], sot.type)
        self.assertEqual(self.example['description'], sot.description)
        self.assertEqual(self.example['datastore_version_id'],
                         sot.datastore_version_id)
