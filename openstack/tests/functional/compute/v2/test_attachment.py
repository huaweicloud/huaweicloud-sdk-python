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

import six
import  sys

from openstack.tests.functional import base
from openstack import utils
utils.enable_logging(debug=True,stream=sys.stdout)
from openstack.compute.v2.volume_attachment import VolumeAttachment

class TestDelVolumeAttachments(base.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(TestDelVolumeAttachments, cls).setUpClass()

    def test_create(self):
       self.conn.compute.create_volume_attachment("1658753f-8ab2-4650-be05-5ac8d353c56a", device = "/dev/sdb", volume_id = "fbacaf56-ec2f-4cbf-a9e2-06c36fc3b35a")
    # def test_update(self):
    #     self.conn.compute.update_volume_attachment("fbacaf56-ec2f-4cbf-a9e2-06c36fc3b35a","1658753f-8ab2-4650-be05-5ac8d353c56a", device = "/dev/sdb")

    def test_del_volume(self):
       self.conn.compute.delete_volume_attachment("fbacaf56-ec2f-4cbf-a9e2-06c36fc3b35a", "1658753f-8ab2-4650-be05-5ac8d353c56a",force_del = True)

    def test_volume_attachment(self):
        for attach in self.conn.compute.volume_attachments("1658753f-8ab2-4650-be05-5ac8d353c56a"):
            self.assertIsInstance(attach, VolumeAttachment)

    def test_get_one(self):
        res = self.conn.compute.get_volume_attachment("d6bc3c9c-077b-45a0-b9b0-05e4af99c3dd", "1658753f-8ab2-4650-be05-5ac8d353c56a")
        self.assertIsInstance(res, VolumeAttachment)


