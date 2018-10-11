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

from openstack.cts.v1 import tracker

EXAMPLE = {
    "bucket_name": "my_created_bucket",
    "tracker_name": "system",
    "detail": "noBucket",
    "file_prefix_name": "some_folder",
    "status": "disabled"
}


class TestTask(testtools.TestCase):

    def test_basic(self):

        sot = tracker.Tracker()
        self.assertEqual('/tracker', sot.base_path)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_update)

    def test_make_it(self):

        sot = tracker.Tracker(**EXAMPLE)
        self.assertEqual(EXAMPLE['bucket_name'], sot.bucket_name)
        self.assertEqual(EXAMPLE['tracker_name'], sot.tracker_name)
        self.assertEqual(EXAMPLE['detail'], sot.detail)
        self.assertEqual(EXAMPLE['file_prefix_name'], sot.file_prefix_name)
        self.assertEqual(EXAMPLE['status'], sot.status)
