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
from openstack.network import network_service


class Member(resource2.Resource):
    resource_key = 'member'
    resources_key = 'members'
    base_path = '/lbaas/pools/%(pool_id)s/members'
    service = network_service.NetworkService()

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource2.QueryParameters()
    # member id
    id = resource2.Body("id")
    # tenant id
    tenant_id = resource2.Body("tenant_id")
    # member name
    name = resource2.Body("name")
    # IP address corresponding to member, for example, 192.168.3.11
    # Instructions for use: only the IP address of the main network card
    address = resource2.Body("address")
    # Back-end protocol number, value range [1,65535]
    protocol_port = resource2.Body("protocol_port", type=int)
    # Subnet id
    subnet_id = resource2.Body("subnet_id")
    # Management status, true/false.
    # Instructions for use: Fixed to true
    admin_state_up = resource2.Body("admin_state_up", type=bool, default=True)
    # Weight, ranging from [0,100].
    # Usage note: The backend with zero weight no longer accepts new requests
    weight = resource2.Body("weight", type=int, default=1)
    # The health status of the backend cloud server can be ONLINE or OFFLINE
    operating_status = resource2.Body("operating_status")
    # The pool id to which this member belongs
    pool_id = resource2.URI("pool_id")