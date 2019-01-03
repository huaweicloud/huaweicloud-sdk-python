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
from openstack.bms.v1 import server as _server
from openstack.bms.v1 import job as _job
from openstack.bms.v1 import volume as _volume

class Proxy(proxy2.BaseProxy):
    def create_server(self, **data):
        """
        post method to create bms server
        :param data: data to create bms server see more info from support website
        :return: :class:`~openstack.bms.v1.server.Servers`
        """
        return self._create(_server.Servers, **data)

    def get_server(self, server_id):
        """Get method to retrieve a bare metal server details.

        :param server_id: Id of bare metal server.
        :return: :class:`~openstack.bms.v1.server.Servers`
        """
        return self._get(_server.Servers, server_id)

    def update_server_name(self, server_id, **data):
        """Rename the server name.

        :param server_id: Id of bare metal server.
        :param data: Name if bms.
        :return: :class:`~openstack.bms.v1.server.Servers`
        """
        return self._update(_server.Servers, server_id, **data)

    def create_volume_attachment(self, server_id, **data):
        """Mount a cloud drive to the bms.

        :param server_id: Id of bare metal server.
        :param data: Information of cloud drive.
        :return: None
        """
        return self._create(_volume.VolumeAttach, server_id=server_id, **data)

    def delete_volume_attachment(self, server_id, attachment_id):
        """Unmount a cloud drive from the bms.

        :param server_id: Id of bare metal server.
        :param attachment_id: Id of cloud drive.
        :return: None
        """
        return self._delete(_volume.VolumeDetach, server_id=server_id, id=attachment_id)

    def get_job(self, job_id):
        """Get method to retrieve a task(job).

        :param job_id: Id of job, that from a response.
        :return: :class:`~openstack.bms.v1.job.Job`
        """
        return self._get(_job.Job, job_id)
