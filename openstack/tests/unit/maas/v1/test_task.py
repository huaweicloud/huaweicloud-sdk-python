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

from openstack.maas.v1 import task

EXAMPLE = {
    "id": 1,
    "name": "bucket3-bucket3-20161027211637786_544",
    "src_node": {
        "region": "us-east-1",
        "bucket": "bucket3",
        "object_key": "/"
    },
    "dst_node": {
        "region": "eastchina",
        "bucket": "bucket3",
        "object_key": "/"
    },
    "thread_num": 5,
    "status": 5,
    "progress": 1,
    "migrate_speed": 7213154,
    "enableKMS": True,
    "description": "ZXCZCZXCDVXVC",
    "error_reason": {},
    "total_size": 2000000000,
    "complete_size": 2000000000,
    "start_time": 1477574224062,
    "left_time": 0,
    "total_time": 88124
}


class TestTask(testtools.TestCase):

    def test_basic(self):
        sot = task.Task()

        self.assertEqual('/objectstorage/task', sot.base_path)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)

    def test_make_it(self):

        sot = task.Task(**EXAMPLE)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['src_node'], sot.src_node)
        self.assertEqual(EXAMPLE['dst_node'], sot.dst_node)
        self.assertEqual(EXAMPLE['thread_num'], sot.thread_num)
        self.assertEqual(EXAMPLE['status'], sot.status)
        self.assertEqual(EXAMPLE['progress'], sot.progress)
        self.assertEqual(EXAMPLE['migrate_speed'], sot.migrate_speed)
        self.assertEqual(EXAMPLE['enableKMS'], sot.enableKMS)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['error_reason'], sot.error_reason)
        self.assertEqual(EXAMPLE['total_size'], sot.total_size)
        self.assertEqual(EXAMPLE['complete_size'], sot.complete_size)
        self.assertEqual(EXAMPLE['start_time'], sot.start_time)
        self.assertEqual(EXAMPLE['left_time'], sot.left_time)
        self.assertEqual(EXAMPLE['total_time'], sot.total_time)
