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

from openstack.compute.v2 import quota

IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    "cores": 20,
    "fixed_ips": 40,
    "floating_ips": 10,
    "id": "d9ebe43510414ef590a4aa158605329e",
    "injected_file_content_bytes": 10240,
    "injected_file_path_bytes": 255,
    "injected_files": 5,
    "instances": 20,
    "key_pairs": 100,
    "metadata_items": 128,
    "ram": 51200,
    "security_group_rules": 20,
    "security_groups": 50,
    "server_group_members": 10,
    "server_groups": 10
}


class TestQuota(testtools.TestCase):

    def test_basic(self):
        sot = quota.Quota()
        self.assertEqual('quota_set', sot.resource_key)
        self.assertEqual('/os-quota-sets', sot.base_path)
        self.assertEqual('compute', sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertDictEqual({
            "limit": "limit",
            "marker": "marker",
            "user_id": "user_id"
        },
        sot._query_mapping._mapping)

    def test_make_basic(self):
        sot = quota.Quota(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['cores'], sot.cores)
        self.assertEqual(BASIC_EXAMPLE['fixed_ips'], sot.fixed_ips)
        self.assertEqual(BASIC_EXAMPLE['floating_ips'], sot.floating_ips)
        self.assertEqual(BASIC_EXAMPLE['id'], sot.id)
        self.assertEqual(BASIC_EXAMPLE['injected_file_content_bytes'], sot.injected_file_content_bytes)
        self.assertEqual(BASIC_EXAMPLE['injected_files'], sot.injected_files)
        self.assertEqual(BASIC_EXAMPLE['instances'], sot.instances)
        self.assertEqual(BASIC_EXAMPLE['key_pairs'], sot.key_pairs)
        self.assertEqual(BASIC_EXAMPLE['metadata_items'], sot.metadata_items)
        self.assertEqual(BASIC_EXAMPLE['ram'], sot.ram)
        self.assertEqual(BASIC_EXAMPLE['security_group_rules'], sot.security_group_rules)
        self.assertEqual(BASIC_EXAMPLE['security_groups'], sot.security_groups)
        self.assertEqual(BASIC_EXAMPLE['server_group_members'], sot.server_group_members)
        self.assertEqual(BASIC_EXAMPLE['server_groups'], sot.server_groups)



