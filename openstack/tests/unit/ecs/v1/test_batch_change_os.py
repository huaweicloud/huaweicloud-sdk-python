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
from openstack.ecs.v1 import server

BATCH_CHANGE_OS_EXAMPLE = {
        "servers": [
            {
                "id": "server_id1"
            },
            {
                "id": "server_id2"
            }
        ],
        "keyname": "keyname",
        "imageid": "image_id"
}


class TestServerBathChangeOs(testtools.TestCase):
    def test_basic(self):
        obj = server.ChangeOs()
        self.assertEqual("/cloudservers/batch-changeos", obj.base_path)
        self.assertEqual("os-change", obj.os_change)
        self.assertEqual("ecs", obj.service.service_type)
        self.assertTrue(obj.allow_list)

    def test_make_it(self):
        obj = server.ChangeOs(**BATCH_CHANGE_OS_EXAMPLE)
        self.assertEqual(BATCH_CHANGE_OS_EXAMPLE["os-change"], obj.os_change)