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

from openstack.kms.v1 import key

KEY_EXAMPLE = {
    "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
    "domain_id": "b168fe00ff56492495a7d22974df2d0b",
    "key_alias": "kms_test",
    "realm": "cn-north-1eu-deaaa",
    "key_description": "",
    "creation_date": "1472442386000",
    "scheduled_deletion_date": "",
    "key_state": "2",
    "default_key_flag": "0",
    "key_type": "1"
}

DATAKEY_EXAMPLE = {
    "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
    "plain_text": "0000000000000000000000000000000000000000000.........",
    "cipher_text": "020098009EEAFCE122CAA5927D2E020086F9548BA1675FDB022E4EC..."
}

RANDOM_EXAMPLE = {
    "random_data": "5791C223E87124AB9FC29B5A8AC60BE4B98D168F47A58BB2A88833E4"
}

INSTANCE_NUMBER = {
    "instance_num": 10,
    "error_code": "KMS.xxx",
    "error_msg": "xxx"
}


class TestKey(testtools.TestCase):

    example = KEY_EXAMPLE
    objcls = key.Key

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['key_id'], sot.key_id)
        self.assertEqual(self.example['domain_id'], sot.domain_id)
        self.assertEqual(self.example['key_alias'], sot.key_alias)
        self.assertEqual(self.example['realm'], sot.realm)
        self.assertEqual(self.example['key_description'], sot.key_description)
        self.assertEqual(self.example['creation_date'], sot.creation_date)
        self.assertEqual(self.example['scheduled_deletion_date'],
                         sot.scheduled_deletion_date)
        self.assertEqual(self.example['key_state'], sot.key_state)
        self.assertEqual(self.example['default_key_flag'],
                         sot.default_key_flag)
        self.assertEqual(self.example['key_type'], sot.key_type)


class TestDataKey(testtools.TestCase):

    example = DATAKEY_EXAMPLE
    objcls = key.DataKey

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['key_id'], sot.key_id)
        self.assertEqual(self.example['plain_text'], sot.plain_text)
        self.assertEqual(self.example['cipher_text'],
                         sot.cipher_text)


class TestRandom(testtools.TestCase):

    example = RANDOM_EXAMPLE
    objcls = key.Random

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['random_data'], sot.random_data)


class TestInstanceNumber(testtools.TestCase):

    example = INSTANCE_NUMBER
    objcls = key.InstanceNumber

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['instance_num'], sot.instance_num)
        self.assertEqual(self.example['error_code'], sot.error_code)
        self.assertEqual(self.example['error_msg'], sot.error_msg)
