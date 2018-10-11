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

import mock

from openstack.cts.v1 import _proxy
from openstack.cts.v1 import tracker as _tracker
from openstack.tests.unit import test_proxy_base2


class TestCTSProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestCTSProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_create_tracker(self):
        self.verify_create(self.proxy.create_tracker, _tracker.Tracker)

    def test_delete_tracker(self):
        self._verify2('openstack.proxy2.BaseProxy._delete',
                      self.proxy.delete_tracker,
                      method_args=['system'],
                      expected_args=[mock.ANY, 'system'],
                      expected_kwargs={'ignore_missing': True})

    def test_get_tracker(self):
        self._verify2('openstack.cts.v1.tracker.Tracker.list',
                      self.proxy.get_tracker,
                      method_args=['system'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'tracker_name': 'system'})

    def test_update_tracker(self):
        self.verify_update(self.proxy.update_tracker, _tracker.Tracker)

    def test_traces(self):
        self._verify2('openstack.cts.v1.trace.Trace.list',
                      self.proxy.traces,
                      method_args=['system'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'paginated': False,
                                       'tracker_name': 'system'})

    def test_traces_v2(self):
        self._verify2('openstack.cts.v1.trace.TraceV2.list',
                      self.proxy.traces_v2,
                      method_args=['system'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'paginated': False,
                                       'tracker_name': 'system'})
