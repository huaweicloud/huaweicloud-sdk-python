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


class Policy(resource2.Resource):
    resource_key = 'policy'
    resources_key = 'policies'
    base_path = '/policies'
    service = csbs_service.CsbsService()

    # Capabilities.
    allow_create = True
    allow_delete = True
    allow_update = True
    allow_get = True
    allow_list = True

    _query_mapping = resource2.QueryParameters(
        'limit',
        'marker',
        'sort',
        'name',
        'all_tenants',
        'offset'
    )

    # Description of backup policy.
    description = resource2.Body('description')
    # Name of backup policy.
    name = resource2.Body('name')
    # Parameter of backup policy.
    parameters = resource2.Body('parameters', type=dict)
    # Backup provider id.
    provider_id = resource2.Body('provider_id')
    # A list of backup objects.
    resources = resource2.Body('resources', type=list)
    # A list of scheduling periods.
    scheduled_operations = resource2.Body('scheduled_operations', type=list)
    # Create time.
    created_at = resource2.Body('created_at')
    # Id of backup policy.
    id = resource2.Body('id')
    # Id of project.
    project_id = resource2.Body('project_id')
    # Status of backup policy.
    status = resource2.Body('status')
