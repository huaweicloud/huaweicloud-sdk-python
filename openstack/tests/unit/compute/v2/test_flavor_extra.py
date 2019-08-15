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

from openstack.compute.v2 import flavor

IDENTIFIER = 'IDENTIFIER'
BASIC_EXAMPLE = {
    'cond:operation:status': "test",
    'cond:operation:az': '2',
    'cond:operation:roles': '3'
}


class TestFlavorExtra(testtools.TestCase):

    def test_basic(self):
        sot = flavor.ExtraSpecs()
        self.assertEqual('extra_specs', sot.resource_key)
        self.assertEqual('extra_specss', sot.resources_key)
        self.assertEqual('/flavors/%(flavor_id)s/os-extra_specs', sot.base_path)
        self.assertEqual('compute', sot.service.service_type)
        self.assertTrue(sot.allow_get)

    def test_make_basic(self):
        sot = flavor.ExtraSpecs(**BASIC_EXAMPLE)
        self.assertEqual(BASIC_EXAMPLE['cond:operation:status'], sot.status)
        self.assertEqual(BASIC_EXAMPLE['cond:operation:az'], sot.az)
        self.assertEqual(BASIC_EXAMPLE['cond:operation:roles'], sot.roles)

