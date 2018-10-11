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

from openstack.rds_os.v1 import configuration

CONFIGURATION_EXAMPLE = {
    'configuration': {
        "basedir": "/usr",
        "connect_timeout": "15",
        "datadir": "/var/lib/mysql",
        "default_storage_engine": "innodb",
        "innodb_buffer_pool_size": "600M",
        "innodb_data_file_path": "ibdata1:10M:autoextend",
        "innodb_file_per_table": "1"
    }
}

CONFIGURATIONS_EXAMPLE = {
    "id": "904ce226-bcc7-457d-b118-74ebdce59ba1",
    "name": "default-SQLServer-2014",
    "description": "Default parameter group for sqlserver 2014",
    "datastore_version_id": "4f71c5b5-8939-424e-8825-8e3816e4303d",
    "datastore_version_name": "2014",
    "datastore_name": "sqlserver",
    "created": "2017-01-01T10:00:00",
    "updated": "2017-01-01T10:00:00",
    "allowed_updated": 0,
    "instance_count": 0
}


class TestConfiguration(testtools.TestCase):
    example = CONFIGURATION_EXAMPLE
    objcls = configuration.Configuration

    def test_basic(self):
        sot = self.objcls()

        self.assertEqual('instances/%(instanceId)s/configuration',
                         sot.base_path)
        self.assertEqual('instance', sot.resource_key)

        self.assertTrue(sot.allow_get)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['configuration'], sot.configuration)


class TestConfigurations(testtools.TestCase):

    example = CONFIGURATIONS_EXAMPLE
    objcls = configuration.Configurations

    def test_basic(self):
        sot = self.objcls()

        self.assertEqual('configurations', sot.base_path)
        self.assertEqual('configuration', sot.resource_key)
        self.assertEqual('configurations', sot.resources_key)

        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_create)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['id'], sot.id)
        self.assertEqual(self.example['name'], sot.name)
        self.assertEqual(self.example['description'], sot.description)
        self.assertEqual(self.example['datastore_version_id'],
                         sot.datastore_version_id)
        self.assertEqual(self.example['datastore_version_name'],
                         sot.datastore_version_name)
        self.assertEqual(self.example['created'], sot.created)
        self.assertEqual(self.example['updated'], sot.updated)
        self.assertEqual(self.example['allowed_updated'], sot.allowed_updated)
        self.assertEqual(self.example['instance_count'], sot.instance_count)
