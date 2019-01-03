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
from openstack.vpc.v2 import eip

DATA = {
    "order_id": "test",
    "publicip": {

    },
    "publicip_id": "test",
}

class TestEip(testtools.TestCase):

    def test_basic(self):
        obj = eip.EIP()
        self.assertEqual('/publicips', obj.base_path)
        self.assertTrue(obj.allow_create)

    def test_make_it(self):
        obj = eip.EIP(**DATA)
        self.assertEqual(DATA['order_id'],obj.order_id)
        self.assertEqual(DATA['publicip'],obj.publicip)
        self.assertEqual(DATA['publicip_id'], obj.publicip_id)