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

from openstack import resource2
from openstack.bms import bms_service


class VolumeAttach(resource2.Resource):
    """Define a VolumeAttach class."""

    base_path = '/baremetalservers/%(server_id)s/attachvolume'
    resource_key = 'volumeAttachment'
    service = bms_service.BmsService()
    allow_create = True

    # The id of the server to operate on.
    server_id = resource2.URI('server_id')
    # The volume ID of the volume to be mounted.
    volumeId = resource2.Body('volumeId')
    # Disk mount point.
    device = resource2.Body('device')


class VolumeDetach(resource2.Resource):
    """Define a VolumeDetach class."""

    base_path = '/baremetalservers/%(server_id)s/detachvolume'
    service = bms_service.BmsService()
    allow_delete = True

    # The id of the server to operate on.
    server_id = resource2.URI('server_id')
