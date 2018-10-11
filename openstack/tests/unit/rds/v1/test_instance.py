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

from openstack.rds.v1 import instance

INSTANCE_EXAMPLE = {
    "id": "252f11f1-2912-4c06-be55-1999bde659c5",
    "status": "BUILD",
    "name": "trove-instance-rep3",
    "created": "2016-06-18T21:21:50+0200",
    "hostname": "",
    "type": "master",
    "region": "eu-de",
    "updated": "2016-06-18T21:21:50+0200",
    "availabilityZone": "eu-de-01",
    "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
    "nics": {
        "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
    },
    "securityGroup": {
        "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
    },
    "flavor": {
        "id": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4"
    },
    "volume": {
        "type": "COMMON",
        "size": 100,
        "used": "14.99"
    },
    "dataStoreInfo": {
        "type": "MySQL",
        "version": "5.6.30"
    },
    "backupStrategy": {
        "startTime": "01:00:00",
        "keepDays": 3
    }
}

INSTANCE_PARA_EXAMPLE = {
    "shouldRestart": 0,
    "setParameteResult": 0
}

INSTANCE_ERR_LOG_EXAMPLE = {
    "datetime": "2016-08-30 09:55:39",
    "content": "[Warning] 'proxies_priv' entry '@ root@rds-bf83' ignored in"
}

INSTANCE_SLOW_LOG_EXAMPLE = {
    "count": " 409  (99.76%)",
    "time": "1.29",
    "lockTime": " 0 ",
    "rowsSent": " 0 ",
    "rowsExamined": " 0 ",
    "database": " ",
    "users": " \trdsBackup@localhost  : 100.00% (409) of query, 99.76% users",
    "querySample": "flush logs;"
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
        self.assertEqual(self.example['dataStoreInfo'], sot.dataStoreInfo)
        self.assertEqual(self.example['flavor'], sot.flavor)
        self.assertEqual(self.example['volume'], sot.volume)
        self.assertEqual(self.example['region'], sot.region)
        self.assertEqual(self.example['availabilityZone'],
                         sot.availabilityZone)
        self.assertEqual(self.example['vpc'], sot.vpc)
        self.assertEqual(self.example['nics'], sot.nics)
        self.assertEqual(self.example['securityGroup'], sot.securityGroup)
        self.assertEqual(self.example['backupStrategy'], sot.backupStrategy)


class TestInstanceParameter(testtools.TestCase):
    example = INSTANCE_PARA_EXAMPLE
    objcls = instance.InstanceParameter

    def test_basic(self):
        sot = instance.InstanceParameter()

        self.assertEqual('instances/%(instanceId)s/parameters', sot.base_path)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['shouldRestart'], sot.shouldRestart)
        self.assertEqual(self.example['setParameteResult'],
                         sot.setParameteResult)


class TestInstanceErrorLog(testtools.TestCase):
    example = INSTANCE_ERR_LOG_EXAMPLE
    objcls = instance.InstanceErrorLog

    def test_basic(self):
        sot = self.objcls()

        self.assertEqual('instances/%(instanceId)s/errorlog', sot.base_path)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = self.objcls(**self.example)

        self.assertEqual(self.example['datetime'], sot.datetime)
        self.assertEqual(self.example['content'], sot.content)


class TestInstanceSlowLog(testtools.TestCase):
    example = INSTANCE_SLOW_LOG_EXAMPLE
    objcls = instance.InstanceSlowLog

    def test_basic(self):
        sot = self.objcls()

        self.assertEqual('instances/%(instanceId)s/slowlog', sot.base_path)
        self.assertEqual('slowLogList', sot.resources_key)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = self.objcls(**self.example)

        self.assertEqual(self.example['count'], sot.count)
        self.assertEqual(self.example['time'], sot.time)
        self.assertEqual(self.example['lockTime'], sot.lockTime)
        self.assertEqual(self.example['rowsSent'], sot.rowsSent)
        self.assertEqual(self.example['rowsExamined'], sot.rowsExamined)
        self.assertEqual(self.example['database'], sot.database)
        self.assertEqual(self.example['users'], sot.users)
        self.assertEqual(self.example['querySample'], sot.querySample)
