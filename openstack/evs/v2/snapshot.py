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

from openstack.evs import evs_service
from openstack import resource2


class SnapshotRollback(resource2.Resource):
    resource_key = 'rollback'
    resources_key = None
    base_path = '/os-vendor-snapshots/%(snapshot_id)s/rollback'
    snapshot_id = resource2.URI('snapshot_id')
    service = evs_service.EvsService()

    allow_create = True

    #: The UUID of the EVS disk to be rolled back.
    volume_id = resource2.Body('volume_id')
    #: The name of the EVS disk to be rolled back.
    name = resource2.Body('name')
