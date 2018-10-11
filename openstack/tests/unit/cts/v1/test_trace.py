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

from openstack.cts.v1 import trace

EXAMPLE = {
    "time": 1472148708232,
    "user": "{\"name\":\"xxx\",\"domain\":{\"name\":\"xxx.................}",
    "response": "{\"code\":\"VPC.0514\",\"message\":\"Update port fail.\"}",
    "code": 200,
    "service_type": "VPC",
    "resource_type": "eip",
    "resource_name": "192.144.163.1",
    "resource_id": "d502809d-0d1d-41ce-9690-784282142ccc",
    "trace_name": "deleteEip",
    "trace_rating": "warning",
    "trace_type": "ConsoleAction",
    "api_version": "2.0",
    "record_time": 1481066128032,
    "trace_id": "e001ccb9-bc09-11e6-b00b-4b2a61338db6"
}

EXAMPLEV2 = {
    "time": 1472148708232,
    "user": {"name": "xxx", "id": "a2e899190fcd444084a68fc0ac2sc1e9",
             "domain": {"name": "xxx",
                        "id": "05b2598d69bc4a209f9ac5eeeb1f91ad"}},
    "response": {"code": "VPC.0514", "message": "Update port fail."},
    "code": 200,
    "service_type": "VPC",
    "resource_type": "eip",
    "resource_name": "192.144.163.1",
    "resource_id": "d502809d-0d1d-41ce-9690-784282142ccc",
    "trace_name": "deleteEip",
    "trace_status": "warning",
    "trace_type": "ConsoleAction",
    "api_version": "2.0",
    "record_time": 1481066128032,
    "trace_id": "e001ccb9-bc09-11e6-b00b-4b2a61338db6"
}


class TestTrace(testtools.TestCase):

    example = EXAMPLE
    objcls = trace.Trace

    def test_basic(self):
        sot = self.objcls()

        self.assertEqual('/%(tracker_name)s/trace', sot.base_path)

        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_list)
        self.assertFalse(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)

    def test_make_it(self):

        sot = self.objcls(**self.example)
        self.assertEqual(self.example['time'], sot.time)
        self.assertEqual(self.example['response'], sot.response)
        self.assertEqual(self.example['code'], sot.code)
        self.assertEqual(self.example['service_type'], sot.service_type)
        self.assertEqual(self.example['resource_name'], sot.resource_name)
        self.assertEqual(self.example['resource_id'], sot.resource_id)
        self.assertEqual(self.example['trace_name'], sot.trace_name)
        if 'trace_rating' in self.example:
            self.assertEqual(self.example['trace_rating'], sot.trace_rating)
        if 'trace_status' in self.example:
            self.assertEqual(self.example['trace_status'], sot.trace_status)
        self.assertEqual(self.example['trace_type'], sot.trace_type)
        self.assertEqual(self.example['api_version'], sot.api_version)
        self.assertEqual(self.example['record_time'], sot.record_time)
        self.assertEqual(self.example['trace_id'], sot.trace_id)


class TestTraceV2(TestTrace):

    example = EXAMPLEV2
    objcls = trace.TraceV2
