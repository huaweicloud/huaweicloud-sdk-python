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

from openstack import proxy2
from openstack.deh.v1 import dedicated_host as _host


class Proxy(proxy2.BaseProxy):
    def create_dedicated_host(self, **data):
        """Create dedicated host(s).

        :param data: Used to create a host.
        :return: Dedicated host(s).
        """
        return self._create(_host.Host, prepend_key=False, **data)

    def dedicated_hosts(self, **query):
        """List dedicated hosts.

        :param query: Query conditions.
        :return: A generator of dedicated host.
        """
        return self._list(_host.Host, **query)

    def get_dedicated_host(self, dedicated_host_id):
        """Get a dedicated host.

        :param dedicated_host_id: Id of dedicated host.
        :return: Dedicated host.
        """
        return self._get(_host.Host, dedicated_host_id)

    def update_dedicated_host(self, dedicated_host_id, **data):
        """Update a dedicated host.

        :param dedicated_host_id: Id of dedicated host.
        :param data: Used to update a host.
        :return: Dedicated host.
        """
        return self._update(_host.Host, dedicated_host_id, has_body=False, **data)

    def delete_dedicated_host(self, dedicated_host_id):
        """Delete a dedicated host.

        :param dedicated_host_id: Id of dedicated host.
        :return: None.
        """
        return self._delete(_host.Host, dedicated_host_id)

    def host_servers(self, dedicated_host_id, **query):
        """Query the cloud server on the dedicated host.

        :param dedicated_host_id: Id of dedicated host.
        :param query: Query conditions.
        :return: A generator of servers from host.
        """
        return self._list(_host.HostServer, dedicated_host_id=dedicated_host_id, **query)

    def host_types(self, availability_zone):
        """Query available proprietary host types.

        :param availability_zone: Availability zone.
        :return: A generator of available types from host.
        """
        return self._list(_host.HostType, availability_zone=availability_zone)

    def host_quotas(self, tenant_id, **query):
        """Query the tenant's exclusive host quota.

        :param tenant_id: Id of tenant.
        :param query: Query conditions.
        :return: A generator of host quota.
        """
        return self._list(_host.HostQuota, tenant_id=tenant_id, **query)
