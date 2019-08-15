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
from openstack.compute.v2 import tag
from openstack.tests.functional import base
from openstack import utils
utils.enable_logging(debug=True, stream=sys.stdout)



class TestTag(base.BaseFunctionalTest):
    @classmethod
    def setUpClass(cls):
        super(TestTag, cls).setUpClass()
        cls.server = cls.conn.compute.get_server("1658753f-8ab2-4650-be05-5ac8d353c56a")
        cls.conn.set_microversion("compute","2.26")
    @classmethod
    def tearDownClass(cls):
        super(TestTag, cls).tearDownClass()
        cls.conn.unset_microversion("compute")

    def test_create_tag(self):
        self.conn.compute.create_server_tag(self.server,tags = ["bar"])
    def test_add_server_tag(self):
        self.conn.compute.add_server_tag(self.server, "ddd")
    def test_list_server_tags(self):
        self.conn.compute.server_tags(self.server)
    def test_delete_tags(self):
        self.conn.compute.delete_server_tag(self.server, "ddd")
    def test_has_tag(self):
        self.conn.compute.check_server_tag(self.server, "ddd")
    def test_clean(self):
        self.conn.compute.clean_server_tags(self.server)
    def test_list_server_tags(self):
        self.conn.compute.server_tags(self.server)