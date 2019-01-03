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


class DnatRule(resource2.Resource):
    resource_key = 'dnat_rule'
    resources_key = 'dnat_rules'
    base_path = '/dnat_rules'

    service = nat_service.NatService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = False
    allow_delete = True
    allow_list = True

    _query_mapping = resource2.QueryParameters(
        "id",
        "tenant_id",
        "port_id",
        "internal_service_port",
        "floating_ip_id",
        "floating_ip_address",
        "external_service_port",
        "protocol",
        "status",
        "created_at",
        "admin_state_up"
    )

    # RULE id
    id = resource2.Body("id")
    # tenant id
    tenant_id = resource2.Body("tenant_id")
    # nat gateway id
    nat_gateway_id = resource2.Body("nat_gateway_id")
    # Port ID of the virtual machine or bare metal(actually,this id is the ecs's  NIC ID)
    port_id = resource2.Body("port_id")
    # Protocol port number for external service of virtual machine or bare metal
    internal_service_port = resource2.Body("internal_service_port", type=int)
    # Floating IP ID
    floating_ip_id = resource2.Body("floating_ip_id")
    # Protocol port number for floating IP external exposure
    external_service_port = resource2.Body("external_service_port",type=int)
    # Floating IP address
    floating_ip_address = resource2.Body("floating_ip_address")
    # Currently, the input characters "TCP" and "UDP" are supported, and the specific protocol number is also supported, 6, 17. Protocol number query rule is not supported
    protocol = resource2.Body("protocol")
    # Status, which can be ACTIVE, ERROR, PENDING_CREATE, PENDING_UPDATE,PENDING_DELETE
    status = resource2.Body("status")
    # Rule creation time
    created_at = resource2.Body("created_at")
    # Administrator status, only the system administrator has permission to operate
    # Description:
    # True is the rule thawing state;
    # False is the rule freeze state
    admin_state_up = resource2.Body("admin_state_up", type = bool)