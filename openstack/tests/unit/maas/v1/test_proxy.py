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

from openstack.maas.v1 import _proxy
from openstack.maas.v1 import task as _task
from openstack.maas.v1 import version as _version
from openstack.tests.unit import test_proxy_base2


class TestMaaSProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestMaaSProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_versions(self):
        self.verify_list(self.proxy.versions, _version.Version)

    def test_tasks(self):
        self.verify_list(self.proxy.tasks, _task.Task)

    def test_create_task(self):
        self.verify_create(self.proxy.create_task, _task.Task)

    def test_delete_task(self):
        self.verify_delete(self.proxy.delete_task, _task.Task, True)

    def test_get_task(self):
        self.verify_get(self.proxy.get_task, _task.Task)

    def test_start_task(self):
        # TODO
        pass

    def test_stop_task(self):
        # TODO
        pass

    def test_task_count(self):
        self._verify2('openstack.maas.v1.task.Task.task_count',
                      self.proxy.task_count,
                      method_args=['state'],
                      expected_args=[mock.ANY, 'state'])
