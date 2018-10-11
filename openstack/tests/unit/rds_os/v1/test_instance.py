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

from openstack.rds_os.v1 import instance

INSTANCE_EXAMPLE = {
    "configurationStatus": "In-Sync",
    "paramsGroupId": "b89db814-6ba1-454f-a9ad-380064ef0c6f",
    "type": "MySQL",
    "subnetid": "0fb5d084-4e5d-463b-8920-fca10e6b4028",
    "role": "master",
    "internalSubnetId": "330a10fd-3962-44c5-b3a1-1d282617a183",
    "group": "1",
    "securegroup": "ca99fcef-502f-495f-b28d-85c9c6f4666e",
    "vpc": "292997f2-3bf7-4d60-86a5-4e9d593bc850",
    "azcode": "eu-de-01",
    "region": None,
    "created": "2017-05-12T02:18:46",
    "updated": "2017-05-12T02:18:46",
    "status": "ACTIVE",
    "name": "rds-MySQL-1-1",
    "links": [],
    "id": "e8faac23-8129-4c68-a231-480e46fc5f4f",
    "flavor": {
        "id": "31b2863c-0e15-44fd-a80d-1e83a7aca338"
    },
    "volume": {
        "type": "COMMON",
        "size": 210
    },
    "datastore": {
        "type": "MySQL",
        "version": "MySQL-5.7.17"
    },
    "fault": None,
    "configuration": None,
    "locality": None,
    "replicas": None,
    "dbuser": "root",
    "storageEngine": None,
    "payModel": 0,
    "cluster_id": "fb22f24c-0466-48f2-8275-70af04ef4935"
}


class TestInstance(testtools.TestCase):
    example = INSTANCE_EXAMPLE
    objcls = instance.Instance

    def test_basic(self):
        sot = instance.Instance()

        self.assertEqual('/instances', sot.base_path)
        self.assertEqual('instance', sot.resource_key)
        self.assertEqual('instances', sot.resources_key)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['id'], sot.id)
        self.assertEqual(self.example['status'], sot.status)
        self.assertEqual(self.example['name'], sot.name)
        self.assertEqual(self.example['created'], sot.created)
        self.assertEqual(self.example['updated'], sot.updated)
        self.assertEqual(self.example['type'], sot.type)
        self.assertEqual(self.example['datastore'], sot.datastore)
        self.assertEqual(self.example['flavor'], sot.flavor)
        self.assertEqual(self.example['volume'], sot.volume)
        self.assertEqual(self.example['region'], sot.region)
        self.assertEqual(self.example['vpc'], sot.vpc)
        self.assertEqual(self.example['role'], sot.role)
        self.assertEqual(self.example['internalSubnetId'],
                         sot.internalSubnetId)
        self.assertEqual(self.example['group'], sot.group)
        self.assertEqual(self.example['securegroup'], sot.securegroup)
        self.assertEqual(self.example['azcode'], sot.azcode)
        self.assertEqual(self.example['status'], sot.status)
        self.assertEqual(self.example['links'], sot.links)
        self.assertEqual(self.example['datastore'], sot.datastore)
        self.assertEqual(self.example['fault'], sot.fault)
        self.assertEqual(self.example['dbuser'], sot.dbuser)
        self.assertEqual(self.example['payModel'], sot.payModel)
        self.assertEqual(self.example['cluster_id'], sot.cluster_id)
