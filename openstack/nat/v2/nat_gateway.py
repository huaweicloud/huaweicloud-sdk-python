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

from openstack.nat import nat_service
from openstack import resource2


class NatGateway(resource2.Resource):
    resource_key = 'nat_gateway'
    resources_key = 'nat_gateways'
    base_path = '/nat_gateways'

    service = nat_service.NatService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    _query_mapping = resource2.QueryParameters(
                                             "id",
                                             "name",
                                             "description",
                                             "router_id",
                                             "internal_network_id",
                                             "tenant_id",
                                             "status",
                                             "created_at",
                                             "admin_state_up"
                                              )

    # Properties
    # NAT gateway id
    id = resource2.Body("id")
    # NAT gateway name
    name = resource2.Body("name")
    # NAT gateway description
    description = resource2.Body("description")
    # The id of the route used by the NAT gateway.
    router_id = resource2.Body("router_id")
    # The id of the network used by the NAT gateway.
    internal_network_id = resource2.Body("internal_network_id")
    # Status, can be ACTIVE, ERROR, PENDING_CREATE, PENDING_UPDATE,
    # PENDING_DELETE
    status = resource2.Body("status")
    # Specifications can be:
    # "1": small
    # "2": medium
    # "3": large
    # "4": very large
    spec = resource2.Body("spec")
    # tenant id
    tenant_id = resource2.Body("tenant_id")
    # Gateway creation time
    created_at = resource2.Body("created_at")
    # Administrator status, only the system administrator has permission to operate
    # Description:
    # True is the thawing state of the gateway;
    # False is the gateway freeze state.
    admin_state_up = resource2.Body("admin_state_up",type =bool)
