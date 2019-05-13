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
from openstack.ecs.v1 import server as _server
from openstack.ecs.v1 import server_ext as _server_ext
from openstack.ecs.v1 import job as _job
from openstack.ecs.v1 import flavors
from openstack.ecs.v1 import quotas


class Proxy(proxy2.BaseProxy):
    def create_server(self, **data):
        """
        post method to create ecs server
        :param data: data to create ecs server see more info from support website
        :return: :class:`~openstack.ecs.v1.server.Servers`
        """
        return self._create(_server.Servers, **data)

    def resize_server(self, server_id, **data):
        """
        post method to modify ecs server size
        :param server_id: ecs server id
        :param data: data to create ecs server see more info from support website
        :return: class:`~openstack.ecs.v1._server.ResizeServer`
        """
        return self._create(_server.ResizeServer, server_id=server_id, **data)

    def create_server_ext(self, **data):
        """
        post method to create ecs server
        :param data: data to create ecs server see more info from support website
        :return: :class:`~openstack.ecs.v1.server_ext.Servers`
        """
        return self._create(_server_ext.Servers, **data)

    def resize_server_ext(self, server_id, **data):
        """
        post method to modify ecs server size
        :param server_id: ecs server id
        :param data: data to create ecs server see more info from support website
        :return: class:`~openstack.ecs.v1.server_ext.ResizeServer`
        """
        return self._create(_server_ext.ResizeServer, server_id=server_id, **data)

    def start_server(self, **data):
        """
        post method to do server action ,such as batch start stop and restart server
        :param data: data to do action see more info from support website
        :return: :class:`~openstack.ecs.v1.server.ServerAction`
        """
        return self._create(_server.ServerAction, **data)

    def stop_server(self, **data):
        """
        post method to do server action ,such as batch start stop and restart server
        :param data: data to do action see more info from support website
        :return: :class:`~openstack.ecs.v1.server.ServerAction`
        """
        return self._create(_server.ServerAction, **data)

    def reboot_server(self, **data):
        """
        post method to do server action ,such as batch start stop and restart server
        :param data: data to do action see more info from support website
        :return: :class:`~openstack.ecs.v1.server.ServerAction`
        """
        return self._create(_server.ServerAction, **data)

    def delete_server(self, **data):
        """
        post method to batch delete server
        :param data: data to do delete server such as server id list
        :return: :class:`~openstack.ecs.v1.server.ServerAction`
        """
        return self._create(_server.DeleteServer, **data)

    def get_job(self, job_id):
        """
        get method to retrieve a task(job)
        :param job_id: id of job, that from a response
        :return: :class:`~openstack.ecs.v1.job.Job`
        """
        return self._get(_job.Job, job_id)

    def flavors(self, **query):
        """Retrieve a generator of flavors

        :param dict query: Optional query parameters to be sent to limit the
                      resources being returned.
            * ``availability_zone``: Zone name

        :returns: A generator of flavors (:class:`~openstack.ecs.v1.flavors.Flavor`)
                  instances
        """
        return self._list(flavors.Flavor, paginated=False, **query)

    def quotas(self):
        """Get a quotas
        :param None
        :rtype: :class:`~openstack.ecs.v1.quotas.Quota`
        """
        return self._get(quotas.Quota, requires_id=False)

    def get_server(self, server_id):
        """
        Get method to retrieve a ecs server.
        :param server_id: Id of ecs server.
        :return: :class:`~openstack.ecs.v1.server.Servers`
        """
        return self._get(_server.Servers, server_id)

    def servers(self, **query):
        """
        Retrieve a generator of servers.
        :param query: Query parameters.
        :return: A generator of server instances.
        """
        res = self._get_resource(_server.ServerDetail, value=None, **query)
        return res.list_by_offset(self._session, paginated=True, **query)

    # def get_autorecovery(self, server_id):
    #     '''
    #     :param server_id: server id
    #     :return: {"support_auto_recovery": "true/false"}
    #     '''
    #     return _server.Servers.autorecovery(self._session,server_id, None)
    #
    # def config_autorecovery(self, server_id, autorecovery):
    #     '''
    #     :param server_id: server id
    #     :param autorecovery: "true"/"false"
    #     :return: None
    #     '''
    #     _server.Servers.autorecovery(self._session,server_id, autorecovery)

    # def register_server_to_ces(self, server_id):
    #     '''
    #     :param server_id: server id
    #     :return: None
    #     '''
    #     _server.Servers.register_server_to_ces(self._session, server_id)
