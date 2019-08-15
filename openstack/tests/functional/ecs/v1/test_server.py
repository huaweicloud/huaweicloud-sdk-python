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

import os
import sys

from openstack.ecs.v1 import server as _server
from openstack.tests.functional import base
from openstack import utils
utils.enable_logging(debug=True, stream=sys.stdout)

# os.environ.setdefault(
#     'OS_ECS_ENDPOINT_OVERRIDE',
#     'https://ecs.cn-north-1.myhuaweicloud.com/v1.0'
# )

class TestServerAction(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestServerAction, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestServerAction, cls).tearDownClass()

    def test_recoveryauto(self):
        res = self.conn.ecs.get_autorecovery("faed6c66-6915-4fe4-b1e2-5c88170319ce")
        print(res)
    def test_setrecoveryauto(self):
        res = self.conn.ecs.config_autorecovery("6662221e-5046-44a9-8da0-0f92d32cad43", True)
        print(res)

    # def test_register(self):
    #     self.conn.ecs.register_server_to_ces("53faa6af-7429-4acb-981f-6cca7918bb67")