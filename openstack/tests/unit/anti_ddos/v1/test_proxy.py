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

from openstack.anti_ddos.v1 import _proxy
from openstack.anti_ddos.v1 import antiddos as _antiddos
from openstack.anti_ddos.v1 import warnalert as _warnalert
from openstack.tests.unit import test_proxy_base2


class TestAntiDDosProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestAntiDDosProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_query_config_list(self):
        self._verify2('openstack.proxy2.BaseProxy._get',
                      self.proxy.query_config_list,
                      method_args=[],
                      expected_args=[_antiddos.QueryConfigList],
                      expected_kwargs={'requires_id': False})

    def test_create_floating_ip(self):
        self._verify2('openstack.proxy2.BaseProxy._create',
                      self.proxy.create_floating_ip,
                      method_args=["id"],
                      method_kwargs={"enable_L7": True},
                      expected_args=[_antiddos.FloatingIP],
                      expected_kwargs={"floating_ip_id": "id",
                                       "enable_L7": True})

    def test_get_floating_ip(self):
        self.verify_get(self.proxy.get_floating_ip, _antiddos.FloatingIP)

    def test_delete_floating_ip(self):
        self.verify_delete(self.proxy.delete_floating_ip,
                           _antiddos.FloatingIP,
                           True)

    def test_update_floating_ip(self):
        self.verify_update(self.proxy.update_floating_ip,
                           _antiddos.FloatingIP)

    def test_query_task_status(self):
        self._verify2('openstack.anti_ddos.v1.antiddos.AntiDDosMin.list',
                      self.proxy.query_task_status,
                      method_args=['task_id'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'task_id': 'task_id'})

    def test_floating_ips(self):
        self.verify_list(self.proxy.floating_ips,
                         _antiddos.FloatingIP)

    def test_get_eip_status(self):
        self._verify2('openstack.proxy2.BaseProxy._get',
                      self.proxy.get_eip_status,
                      method_args=['value'],
                      expected_args=[_antiddos.EIPStatus],
                      expected_kwargs={'requires_id': False,
                                       'floating_ip_id': 'value'})

    def test_list_eip_daily(self):
        self.verify_list(self.proxy.list_eip_daily, _antiddos.EIPDaily,
                         paginated=False, method_args=['floating_ip_id'],
                         expected_kwargs={'floating_ip_id': 'floating_ip_id'})

    def test_list_eip_log(self):
        self.verify_list(self.proxy.list_eip_log, _antiddos.EIPLog,
                         paginated=False, method_args=['floating_ip_id'],
                         expected_kwargs={'floating_ip_id': 'floating_ip_id'})

    def test_list_eip_weekly(self):
        self._verify2('openstack.anti_ddos.v1.antiddos.AntiDDosMin.list',
                      self.proxy.get_eip_weekly,
                      method_args=['date'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'period_start_date': 'date'})

    def test_get_alert_config(self):
        self._verify2('openstack.proxy2.BaseProxy._get',
                      self.proxy.get_alert_config,
                      method_args=[],
                      expected_args=[_warnalert.AlertConfig],
                      expected_kwargs={'requires_id': False})
