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

from openstack.rds_os.v1 import flavor

FLAVOR_EXAMPLE = {
    "ram": 2,
    "id": 1,
    "links": [],
    "name": "rds.pg.c2.medium",
    "str_id": "9ff2a3a5-c859-bbc0-67f7-86ce59432b1d",
    "flavor_detail": [
        {
            "name": "cpu",
            "value": "1"}
    ],
    "price_detail": [],
    "flavor": {
        "ram": 2048,
        "id": 1,
        "links": [
            {
                "rel": "self",
                "href": ""
            },
        ],
        "name": "rds.pg.c2.medium",
        "str_id": "9ff2a3a5-c859-bbc0-67f7-86ce59432b1d"
    }
}


class TestFlavor(testtools.TestCase):
    example = FLAVOR_EXAMPLE
    objcls = flavor.Flavor

    def test_basic(self):
        sot = self.objcls()

        self.assertEqual('/flavors', sot.base_path)
        self.assertEqual('flavor', sot.resource_key)
        self.assertEqual('flavors', sot.resources_key)

        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['id'], sot.id)
        self.assertEqual(self.example['name'], sot.name)
        self.assertEqual(self.example['ram'], sot.ram)
        self.assertEqual(self.example['links'], sot.links)
        self.assertEqual(self.example['flavor_detail'], sot.flavor_detail)
        self.assertEqual(self.example['price_detail'], sot.price_detail)
        self.assertEqual(self.example['flavor'], sot.flavor)
