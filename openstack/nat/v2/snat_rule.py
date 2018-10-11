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
from openstack.nat import nat_service


class SnatRule(resource2.Resource):
    """Define a SnatRule class."""

    resource_key = 'snat_rule'
    resources_key = 'snat_rules'
    base_path = '/snat_rules'

    service = nat_service.NatService()

    # Allow create/list/get/delete operation for this resource.
    allow_create = True
    allow_list = True
    allow_get = True
    allow_delete = True

    # Mapping of accepted query parameter names.
    _query_mapping = resource2.QueryParameters(
        'id',
        'tenant_id',
        'nat_gateway_id',
        'network_id',
        'floating_ip_id',
        'floating_ip_address',
        'status',
        'created_at',
        'admin_state_up'
    )

    # Properties.
    # id of rule
    id = resource2.Body('id')
    # id of tenant
    tenant_id = resource2.Body('tenant_id')
    # id of the owning NAT gateway
    nat_gateway_id = resource2.Body('nat_gateway_id')
    # network id used by the rule
    network_id = resource2.Body('network_id')
    # floating IP id
    floating_ip_id = resource2.Body('floating_ip_id')
    # floating IP address
    floating_ip_address = resource2.Body('floating_ip_address')
    # status: ACTIVE, ERROR, PENDING_CREATE, PENDING_UPDATE, PENDING_DELETE
    status = resource2.Body('status')
    # rule creation time
    created_at = resource2.Body('created_at')
    # administrator status
    admin_state_up = resource2.Body('admin_state_up')
