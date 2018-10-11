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
from openstack.evs import evs_service


class Vloume(resource2.Resource):
    base_path = "/cloudvolumes"

    service = evs_service.EvsService()
    allow_create = True

    # string type volume name
    name = resource2.Body('name')
    # availability zone name
    availability_zone = resource2.Body('availability_zone')
    # project id
    project_id = resource2.Body('tenant_id')

    # created volume number
    count = resource2.Body('count', type=int)
    # volume type
    volume_type = resource2.Body('volume_type')
    # extend server info
    backup_id = resource2.Body('backup_id')
    snapshot_id = resource2.Body('snapshot_id')
    imageRef = resource2.Body('imageRef')
    metadata = resource2.Body('metadata')
    # volume size
    size = resource2.Body('size')
    # volume description
    description = resource2.Body('description')
    # whether this volume can be attached for many devices
    multiattach = resource2.Body('multiattach')
    # whether this device can be shared
    shareable = resource2.Body('shareable')
    volume = resource2.Body('volume')
    # task id
    job_id = resource2.Body('job_id')
    # order id
    order_id = resource2.Body('order_id')
    error = resource2.Body('error')
    message = resource2.Body('message')
    code = resource2.Body('code')


class ResizeVloume(Vloume):
    base_path = "/cloudvolumes/%(volume_id)s/action"

    volume_id = resource2.URI('volume_id')
    # extend vloume info
    extend = resource2.Body('os-extend', type=dict)

    # vloume new  size
    new_size = resource2.Body('new_size', type=int)
