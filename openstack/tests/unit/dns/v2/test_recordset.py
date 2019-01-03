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
from openstack.dns.v2 import recordset

DATA = {
    "id": "2c9eb155587228570158722b6ac30007",
    "name": "www.example.com.",
    "description": "This is an example record set.",
    "type": "A",
    "ttl": 300,
    "records": [
        "192.168.10.2",
        "192.168.10.1"
    ],
    "status": "PENDING_CREATE",
    "links": {
        "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149/recordsets/2c9eb155587228570158722b6ac30007"
    },
    "zone_id": "2c9eb155587194ec01587224c9f90149",
    "zone_name": "example.com.",
    "create_at": "2016-11-17T12:03:17.827",
    "update_at": "2016-11-17T12:03:18.827",
    "default": False,
    "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
    "tags": [],
}

class TestRecordSet(testtools.TestCase):
    def test_basic(self):
        obj = recordset.Recordset()
        self.assertEqual("/zones/%(zone_id)s/recordsets", obj.base_path)
        self.assertEqual("recordset", obj.resource_key)
        self.assertEqual("recordsets", obj.resources_key)
        self.assertTrue(obj.allow_get)
        self.assertTrue(obj.allow_list)
        self.assertTrue(obj.allow_delete)
        self.assertTrue(obj.allow_create)
        self.assertEqual("dns",obj.service.service_type)

    def test_make_it(self):
        obj = recordset.Recordset(**DATA)
        self.assertEqual(DATA["name"], obj.name)
        self.assertEqual(DATA["id"], obj.id)
        self.assertEqual(DATA["description"],obj.description)
        self.assertEqual(DATA["type"], obj.type)
        self.assertEqual(DATA["ttl"], obj.ttl)
        self.assertEqual(DATA["records"], obj.records)
        self.assertEqual(DATA["links"],obj.links)
        self.assertEqual(DATA["status"], obj.status)
        self.assertEqual(DATA["zone_id"], obj.zone_id)
        self.assertEqual(DATA["zone_name"],obj.zone_name)
        self.assertEqual(DATA["update_at"],obj.update_at)
        self.assertEqual(DATA["create_at"],obj.create_at)
        self.assertEqual(DATA["default"], obj.default)
        self.assertEqual(DATA["project_id"], obj.project_id)
        self.assertEqual(DATA["tags"], obj.tags)
