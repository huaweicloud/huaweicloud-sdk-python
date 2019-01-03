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
from openstack.csbs import csbs_service


class ResourceBackup(resource2.Resource):
    resource_key = 'checkpoint'
    resources_key = None
    base_path = '/providers/%(provider_id)s/resources/%(resource_id)s/action'
    service = csbs_service.CsbsService()

    # Capabilities.
    allow_create = True

    # Uri parameter.
    # Backup provider id.
    provider_id = resource2.URI('provider_id')
    # The id of the backup object.
    resource_id = resource2.URI('resource_id')

    # Request parameter.
    # Backup parameter.
    protect = resource2.Body('protect', type=dict)

    # Response parameter.
    # Status of backup.
    status = resource2.Body('status')
    # Create time.
    created_at = resource2.Body('created_at')
    # Backup record id.
    id = resource2.Body('id')
    # Resource graph.
    resource_graph = resource2.Body('resource_graph')
    # Id of project.
    project_id = resource2.Body('project_id')
    # Backup plan information.
    protection_plan = resource2.Body('protection_plan', type=dict)


class ResourceBackupCapability(resource2.Resource):
    resource_key = None
    resources_key = None
    base_path = '/providers/%(provider_id)s/resources/action'
    service = csbs_service.CsbsService()

    # Capabilities.
    allow_create = True

    # Uri parameter.
    # Backup provider id.
    provider_id = resource2.URI('provider_id')

    # Request parameter.
    # Query the parameter list.
    check_protectable = resource2.Body('check_protectable', type=list)

    # Response parameter.
    # Check parameter list.
    protectable = resource2.Body('protectable', type=list)


class ResourceRecoveryCapability(resource2.Resource):
    resource_key = None
    resources_key = None
    base_path = '/providers/%(provider_id)s/resources/action'
    service = csbs_service.CsbsService()

    # Capabilities.
    allow_create = True

    # Uri parameter.
    # Backup provider id.
    provider_id = resource2.URI('provider_id')

    # Request parameter.
    # Query the parameter list.
    check_restorable = resource2.Body('check_restorable', type=list)

    # Response parameter.
    # Check parameter list.
    restorable = resource2.Body('restorable', type=list)
