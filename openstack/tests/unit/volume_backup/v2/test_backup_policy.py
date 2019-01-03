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
from openstack.volume_backup.v2 import backup_policy

DATA = {
        "backup_policy_id" : "XX",
        "backup_policy_name": "plan01",
        "scheduled_policy" : {
            "remain_first_backup_of_curMonth" : "Y",
            "rentention_num" : 10,
            "frequency" : 1,
            "start_time" : "12:00",
            "status" : "ON",
            "week_frequency": ["test"],
            "rentention_day": 100,
            },
        "policy_resource_count": 0,
        "code": 123,
        "message": "test",
        "tags": [{
                  "key":"key",
                  "value":"value"}
                ],
        "time_zone": "test"
}

class TestBackupPolicy(testtools.TestCase):

    def test_basic(self):
        obj = backup_policy.BackupPolicy()
        self.assertEqual('/backuppolicy', obj.base_path)
        self.assertEqual(None, obj.resource_key)
        self.assertEqual("backup_policies", obj.resources_key)
        self.assertTrue(obj.allow_create)
        self.assertTrue(obj.allow_list)
        self.assertTrue(obj.allow_delete)
        self.assertTrue(obj.allow_update)

    def test_make_it(self):
        obj = backup_policy.BackupPolicy(**DATA)
        self.assertEqual(DATA['backup_policy_id'],obj.id)
        self.assertEqual(DATA['backup_policy_name'],obj.name)
        self.assertIsInstance(obj.scheduled_policy, backup_policy.SchedulePolicy)
        self.assertEqual(DATA['policy_resource_count'], obj.policy_resource_count)
        self.assertEqual(DATA['code'], obj.code)
        self.assertEqual(DATA['message'], obj.message)
        self.assertEqual(DATA['tags'], obj.tags)
        self.assertEqual(DATA['time_zone'], obj.time_zone)
