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
from openstack.dns.v2 import zone

DATA = {
    "id": "2c9eb155587194ec01587224c9f90149",
    "name": "example.com.",
    "description": "This is an example zone.",
    "email": "xx@example.com",
    "ttl": 300,
    "serial": 0,
    "masters": [],
    "status": "ACTIVE",
    "links": {
        "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149"
    },
    "pool_id": "00000000570e54ee01570e9939b20019",
    "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
    "zone_type": "public",
    "created_at": "2016-11-17T11:56:03.439",
    "updated_at": "2016-11-17T11:56:05.528",
    "record_num": 2,
    "tags":[]

}

class TestZone(testtools.TestCase):
    def test_basic(self):
        obj = zone.Zone()
        self.assertEqual("/zones", obj.base_path)
        self.assertEqual("zone", obj.resource_key)
        self.assertEqual("zones", obj.resources_key)
        self.assertTrue(obj.allow_get)
        self.assertTrue(obj.allow_list)
        self.assertTrue(obj.allow_delete)
        self.assertTrue(obj.allow_create)
        self.assertEqual("dns",obj.service.service_type)

    def test_make_it(self):
        obj = zone.Zone(**DATA)
        self.assertEqual(DATA["name"], obj.name)
        self.assertEqual(DATA["id"], obj.id)
        self.assertEqual(DATA["description"],obj.description)
        self.assertEqual(DATA["email"], obj.email)
        self.assertEqual(DATA["ttl"], obj.ttl)
        self.assertEqual(DATA["serial"], obj.serial)
        self.assertEqual(DATA["masters"],obj.masters)
        self.assertEqual(DATA["status"], obj.status)
        self.assertEqual(DATA["links"], obj.links)
        self.assertEqual(DATA["pool_id"],obj.pool_id)
        self.assertEqual(DATA["project_id"],obj.project_id)
        self.assertEqual(DATA["updated_at"],obj.updated_at)
        self.assertEqual(DATA["created_at"],obj.created_at)
        self.assertEqual(DATA["zone_type"], obj.zone_type)
        self.assertEqual(DATA["tags"], obj.tags)
        self.assertEqual(DATA["record_num"], obj.record_num)
        self.assertEqual(DATA["tags"], obj.tags)

