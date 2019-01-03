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

from openstack.csbs.v1 import policy as _policy

DATA = {
    "project_id": "Test project_id for URI and Response",
    "policy_id": "Test policy_id for URI",

    "description": "Test description for Request and Response",
    "name": "Test name for Request and Response",
    "parameters": {
        # Test parameters for Request and Response
    },
    "provider_id": "Test provider_id for Request and Response",
    "resources": [
        # Test resources for Request and Response
    ],
    "scheduled_operations": [
        # Test scheduled_operations for Request and Response
    ],

    "created_at": "Test created_at for Response",
    "id": "Test id for Response",
    "status": "Test status for Response"
}


class TestPolicy(testtools.TestCase):

    def setUp(self):
        super(TestPolicy, self).setUp()

    def test_basic(self):
        policy = _policy.Policy()

        self.assertEqual("policy", policy.resource_key)
        self.assertEqual("policies", policy.resources_key)
        self.assertEqual("/policies", policy.base_path)
        self.assertEqual("data-protect", policy.service.service_type)
        self.assertEqual(True, policy.service.requires_project_id)

        self.assertTrue(policy.allow_create)
        self.assertTrue(policy.allow_delete)
        self.assertTrue(policy.allow_update)
        self.assertTrue(policy.allow_get)
        self.assertTrue(policy.allow_list)

        self.assertDictEqual(
            {
                "limit": "limit",
                "marker": "marker",
                "sort": "sort",
                "name": "name",
                "all_tenants": "all_tenants",
                "offset": "offset"
            },
            policy._query_mapping._mapping
        )

    def test_make_it(self):
        policy = _policy.Policy(**DATA)

        self.assertEqual(DATA["project_id"], policy.project_id)

        self.assertEqual(DATA["description"], policy.description)
        self.assertEqual(DATA["name"], policy.name)
        self.assertEqual(DATA["parameters"], policy.parameters)
        self.assertEqual(DATA["provider_id"], policy.provider_id)
        self.assertEqual(DATA["resources"], policy.resources)
        self.assertEqual(DATA["scheduled_operations"], policy.scheduled_operations)

        self.assertEqual(DATA["created_at"], policy.created_at)
        self.assertEqual(DATA["id"], policy.id)
        self.assertEqual(DATA["status"], policy.status)
