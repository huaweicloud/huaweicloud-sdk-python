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

from openstack.iam.v3 import securitytoken

IDENTIFIER = "IDENTIFIER"
EXAMPLE = {
    "access": IDENTIFIER,
    "secret": IDENTIFIER,
    "expires_at": "2017-04-17T07:55:18.575000Z",
    "securitytoken": IDENTIFIER
  }


class TestSecuritytoken(testtools.TestCase):
    def test_basic(self):
        obj = securitytoken.Securitytoken()
        self.assertEqual("/OS-CREDENTIAL/securitytokens", obj.base_path)
        self.assertEqual("credential", obj.resource_key)
        self.assertEqual("credentials", obj.resources_key)
        self.assertEqual("iam", obj.service.service_type)

    def test_make_it(self):
        obj = securitytoken.Securitytoken(**EXAMPLE)
        self.assertEqual(EXAMPLE["access"], obj.access)
        self.assertEqual(EXAMPLE["secret"], obj.secret)
        self.assertEqual(EXAMPLE["expires_at"], obj.expires_at)
        self.assertEqual(EXAMPLE["securitytoken"], obj.securitytoken)