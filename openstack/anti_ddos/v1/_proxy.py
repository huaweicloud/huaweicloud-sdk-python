# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack.anti_ddos.v1 import antiddos as _antiddos
from openstack.anti_ddos.v1 import warnalert as _warnalert
from openstack import proxy2


class Proxy(proxy2.BaseProxy):

    def query_config_list(self):
        """Get the config list of anti-ddos

        :returns: The config list
        :rtype: :class:`~openstack.anti_ddos.v1.antiddos.QueryConfigList`
        """
        return self._get(_antiddos.QueryConfigList, requires_id=False)

    def create_floating_ip(self, floating_ip_id, **kwargs):
        """Enable anti-ddos

        :param floating_ip_id: The EIP id or an instance of
                               :class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`
        :param dict kwargs: Keyword arguments which will be used to create a
                            :class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`

        :rtype: :class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`
        """
        return self._create(_antiddos.FloatingIP,
                            floating_ip_id=floating_ip_id, **kwargs)

    def get_floating_ip(self, floating_ip):
        """Get detail about an EIP policy

        :param floating_ip: The EIP id or an instance of
                           :class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`

        :rtype: :class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`
        """
        return self._get(_antiddos.FloatingIP, floating_ip)

    def delete_floating_ip(self, floating_ip, ignore_missing=True):
        """Disable an EIP

        :param floating_ip_id: The EIP id or an instance of
                           :class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the EIP floating ip does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to disable an EIP.
        :returns: ``None``
        """

        self._delete(_antiddos.FloatingIP, floating_ip,
                     ignore_missing=ignore_missing)

    def update_floating_ip(self, floating_ip, **attrs):
        """update anti-ddos EIP

        :param floating_ip: The EIP id or an instance of
                           :class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`
        :param dict attrs: Keyword arguments which will be used to create a
                           :class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`

        :rtype: :class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`
        """

        return self._update(_antiddos.FloatingIP,
                            floating_ip, **attrs)

    def query_task_status(self, task_id):
        """Query sepcific task status by id

        :param task_ip: The EIP id or an instance of
        :returns: The status of a task
        :rtype: :class:`~openstack.anti_ddos.v1.antiddos.TaskStatus`
        """

        return _antiddos.TaskStatus.list(self._session, task_id=task_id)

    def floating_ips(self, **query):
        """Get the list of anti-ddos EIPs

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of TemplateMessage object
        :rtype: class:`~openstack.anti_ddos.v1.antiddos.FloatingIP`
        """

        return self._list(_antiddos.FloatingIP, paginated=False, **query)

    def get_eip_status(self, floating_ip_id):
        """Get specific eip status by floating ip id.

        :param floating_ip_id: The EIP id
        :returns: The status of EIP
        :rtype: :class:`~openstack.anti_ddos.v1.antiddos.EIPStatus`
        """
        return self._get(_antiddos.EIPStatus, requires_id=False,
                         floating_ip_id=floating_ip_id)

    def list_eip_daily(self, floating_ip_id, **query):
        """List specific eip daily by floating ip id.

        :param floating_ip_id: The EIP id
        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of TemplateMessage object
        :rtype: :class:`~openstack.anti_ddos.v1.antiddos.EIPDaily`
        """
        return self._list(_antiddos.EIPDaily, paginated=False,
                          floating_ip_id=floating_ip_id, **query)

    def list_eip_log(self, floating_ip_id, **query):
        """List specific eip logs by floating ip id.

        :param floating_ip_id: The EIP id
        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of TemplateMessage object
        :rtype: :class:`~openstack.anti_ddos.v1.antiddos.EIPLog`
        """
        return self._list(_antiddos.EIPLog, paginated=False,
                          floating_ip_id=floating_ip_id, **query)

    def get_eip_weekly(self, period_start_date):
        """Get weekly stats

        :param period_start_date: start time of a week

        :returns: The config list
        :rtype: :class:`~openstack.anti_ddos.v1.antiddos.EIPWeekly`
        """
        return _antiddos.EIPWeekly.list(self._session,
                                        period_start_date=period_start_date)

    def get_alert_config(self):
        """Get alert config

        :returns: The alert configuration
        :rtype: :class:`~openstack.anti_ddos.v1.warnalert.AlertConfig`
        """
        return self._get(_warnalert.AlertConfig, requires_id=False)
