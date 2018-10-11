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

from openstack.smn.v2 import subscription

EXAMPLE = {
    "topic_urn": "urn:smn:regionId:762bdb3251034f268af0e395c53ea09b:test_t..",
    "protocol": "sms",
    "subscription_urn": "urn:smn:regionId:762bdb3251034f268af0e39cbc6d3c3..",
    "owner": "762bdb3251034f268af0e395c53ea09b",
    "endpoint": "xxxxxxxxxxx",
    "remark": "",
    "status": 0
}


class TestTopic(testtools.TestCase):

    def test_basic(self):
        sot = subscription.Subscription

        self.assertEqual('/notifications/subscriptions', sot.base_path)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertTrue(sot.allow_delete)

    def test_make_it(self):

        sot = subscription.Subscription(**EXAMPLE)
        self.assertEqual(EXAMPLE['subscription_urn'], sot.subscription_urn)
        self.assertEqual(EXAMPLE['protocol'], sot.protocol)
        self.assertEqual(EXAMPLE['remark'], sot.remark)
        self.assertEqual(EXAMPLE['endpoint'], sot.endpoint)
        self.assertEqual(EXAMPLE['topic_urn'], sot.topic_urn)
        self.assertEqual(EXAMPLE['owner'], sot.owner)
        self.assertEqual(EXAMPLE['status'], sot.status)
