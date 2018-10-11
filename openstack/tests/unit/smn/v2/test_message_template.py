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

from openstack.smn.v2 import message_template

EXAMPLE = {
    "message_template_name": "confirm_message",
    "protocol": "https",
    "update_time": "2016-08-02T08:22:25Z",
    "create_time": "2016-08-02T08:22:20Z",
    "locale": "en-us",
    "tag_names": [
        "topic_id_id4"
    ],
    "content": "(1/24)You are invited to subscribe to topic({topic_id_i ....",
    "message_template_id": "57ba8dcecda844878c5dd5815b65d10f"
}


class TestMessateTemplate(testtools.TestCase):

    def test_basic(self):
        sot = message_template.MessageTemplate()

        self.assertEqual('/notifications/message_template', sot.base_path)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)

    def test_make_it(self):

        sot = message_template.MessageTemplate(**EXAMPLE)
        self.assertEqual(EXAMPLE['message_template_id'],
                         sot.message_template_id)
        self.assertEqual(EXAMPLE['message_template_name'],
                         sot.message_template_name)
        self.assertEqual(EXAMPLE['protocol'], sot.protocol)
        self.assertEqual(EXAMPLE['update_time'], sot.update_time)
        self.assertEqual(EXAMPLE['create_time'], sot.create_time)
        self.assertEqual(EXAMPLE['locale'], sot.locale)
        self.assertEqual(EXAMPLE['tag_names'], sot.tag_names)
        self.assertEqual(EXAMPLE['content'], sot.content)
