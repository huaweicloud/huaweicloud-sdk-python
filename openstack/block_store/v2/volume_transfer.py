# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
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

from openstack import resource2 as resource
from openstack.block_store import block_store_service


class VolumeTransfer(resource.Resource):
    resource_key = 'transfer'
    resources_key = 'transfers'
    base_path = '/os-volume-transfer'
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_get = True
    allow_list = True

    _query_mapping = resource.QueryParameters(
        'offset'
    )

    # Properties
    #: The disk ID.
    volume_id = resource.Body('volume_id')
    #: The name of the disk transfer.
    name = resource.Body('name')
    #: The authentication key of the disk transfer.
    auth_key = resource.Body('auth_key')
    #: The links of the disk transfer.
    links = resource.Body('links', type=list)
    #: he time when the disk transfer was created.
    created_at = resource.Body('created_at')
    #: The disk transfer ID.
    id = resource.Body('id')


class VolumeTransferDetail(VolumeTransfer):
    resource_key = None
    resources_key = 'transfers'
    base_path = '/os-volume-transfer/detail'

    # capabilities
    allow_create = False
    allow_delete = False
    allow_get = False
    allow_list = True


class VolumeTransferAccept(VolumeTransfer):
    resource_key = 'transfer'
    resources_key = None
    base_path = '/os-volume-transfer/%(transfer_id)s/accept'
    transfer_id = resource.URI('transfer_id')

    # capabilities
    allow_create = True
    allow_delete = False
    allow_get = False
    allow_list = False

    #: The tag accepts the cloud disk transfer operation.
    accept = resource.Body('accept', type=dict)
