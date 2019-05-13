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

from openstack.identity.v3 import password_config

EXAMPLE = {
    'security_compliance': {
      'password_regex': '(?=.*\\d)(?=.*[a-zA-Z]).{7,}$',
      'password_regex_description': 'Passwords must contain at least 1 letter, 1 digit, and be a minimum length of 7 characters.'
    },
    'password_regex': '^(?=.*\\d)(?=.*[a-zA-Z]).{7,}$',
    'password_regex_description': 'Passwords must contain at least 1 letter, 1 digit, and be a minimum length of 7 characters.'
}


class TestGroup(testtools.TestCase):

    def test_basic(self):
        sot = password_config.PasswordConfig()
        self.assertEqual('config', sot.resource_key)
        self.assertEqual(None, sot.resources_key)
        self.assertEqual('/domains', sot.base_path)
        self.assertEqual('identity', sot.service.service_type)
        self.assertTrue(sot.allow_get)

    def test_make_it(self):
        sot = password_config.PasswordConfig(**EXAMPLE)
        self.assertEqual(EXAMPLE['security_compliance']['password_regex'], sot.security_compliance['password_regex'])
        self.assertEqual(EXAMPLE['security_compliance']['password_regex_description'], sot.security_compliance['password_regex_description'])
        self.assertEqual(EXAMPLE['password_regex'], sot.password_regex)
        self.assertEqual(EXAMPLE['password_regex_description'], sot.password_regex_description)