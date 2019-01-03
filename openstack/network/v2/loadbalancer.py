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

from openstack.network import network_service
from openstack import resource2

class LoadBalancer(resource2.Resource):
    resource_key = 'loadbalancer'
    resources_key = 'loadbalancers'
    base_path = '/lbaas/loadbalancers'
    service = network_service.NetworkService()

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource2.QueryParameters(
        "id",
        "description",
        "name",
        "operating_status",
        "provisioning_status",
        "vip_address",
        "vip_port_id",
        "vip_subnet_id",
        "member_address",
        "member_device_id"
    )
    # loadbalancer id
    id = resource2.Body("id")
    # tenant id
    tenant_id = resource2.Body("tenant_id")
    # loadbalancer name
    name = resource2.Body("name")
    # loadbalancer description
    description = resource2.Body("description")
    # Assign the subnet id for vip.
    # Instructions for use: only supports intranet types
    vip_subnet_id = resource2.Body("vip_subnet_id")
    # Vip port id
    vip_port_id = resource2.Body("vip_port_id")
    # Supplier.
    # Instructions for use: only support vlb
    provider = resource2.Body("provider")
    # VIP's ip address
    vip_address = resource2.Body("vip_address")
    # Associated listener list
    listeners = resource2.Body("listeners", type=list)
    # Provisioning state, which can be ACTIVE, PENDING_CREATE, or ERROR
    provisioning_status = resource2.Body("provisioning_status")
    # Operating state, which can be ONLINE, OFFLINE, DEGRADED, DISABLED, or NO_MONITOR
    operating_status = resource2.Body("operating_status")
    # Management status: true/false.
    # Instructions for use: Fixed to true
    admin_state_up = resource2.Body("admin_state_up", default=True, type=bool)
    # The id of the flavor.
    # Instructions for use: temporarily not supported
    flavor_id = resource2.Body("flavor_id")
    # Load balanced tags
    tags = resource2.Body("tags", type=list)