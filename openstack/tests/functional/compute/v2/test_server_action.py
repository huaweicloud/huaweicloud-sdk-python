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

from openstack.compute.v2 import server as _server
from openstack.tests.functional import base
from openstack import utils
utils.enable_logging(debug=True, stream=sys.stdout)

class TestServerAction(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestServerAction, cls).setUpClass()
        for server in cls.conn.compute.servers():
            isinstance(server, _server.ServerDetail)
            cls.server = server
            break

    @classmethod
    def tearDownClass(cls):
        super(TestServerAction, cls).tearDownClass()

    def test_list(self):
        obj = None
        for o in self.conn.compute.get_server_actions("7be6ff3a-ac95-490f-aeff-fdd0eb982d5d"):
            obj = o
        self.assertIsInstance(obj, _server.ServerAction)

    def test_get_action_reqid(self):
        sot = self.conn.compute.get_server_action_reqid("7be6ff3a-ac95-490f-aeff-fdd0eb982d5d", "req-783116f0-c984-4e6c-a8b1-72358a273744")
        self.assertIsInstance(sot, _server.ServerActionReqID)

    def test_get_console_output(self):
        msg = self.conn.compute.get_server_console_output("1658753f-8ab2-4650-be05-5ac8d353c56a", 10)

    def test_reinstall(self):
        self.conn.compute.reinstall_server_os("7be6ff3a-ac95-490f-aeff-fdd0eb982d5d", adminpass = "test123!@#")

