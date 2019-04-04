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

import uuid
import sys

from openstack.compute.v2 import quota as _quota
from openstack.tests.functional import base
from openstack import utils

utils.enable_logging(debug=True, stream=sys.stdout)


class TestQuota(base.BaseFunctionalTest):
    @classmethod
    def setUpClass(cls):
        super(TestQuota, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestQuota, cls).tearDownClass()

    def test_query_quota(self):
        sot = self.conn.compute.query_quota("128a7bf965154373a7b73c89eb6b65aa")
        self.assertIsInstance(sot, _quota.Quota)
    def test_query_quotadefault(self):
        sot = self.conn.compute.query_quota_default("128a7bf965154373a7b73c89eb6b65aa")
        self.assertIsInstance(sot, _quota.QuotaDefault)