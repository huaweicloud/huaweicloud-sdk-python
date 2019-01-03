# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
#      Huawei has modified this source file.
#     
#         Copyright 2018 Huawei Technologies Co., Ltd.
#         
#         Licensed under the Apache License, Version 2.0 (the "License"); you may not
#         use this file except in compliance with the License. You may obtain a copy of
#         the License at
#         
#             http://www.apache.org/licenses/LICENSE-2.0
#         
#         Unless required by applicable law or agreed to in writing, software
#         distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#         WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#         License for the specific language governing permissions and limitations under
#         the License.

from openstack.network import network_service

from openstack import resource2


class Listener(resource2.Resource):
    resource_key = 'listener'
    resources_key = 'listeners'
    base_path = '/lbaas/listeners'
    service = network_service.NetworkService()

    _query_mapping = resource2.QueryParameters(
        "id",
        "description",
        "name",
        "default_pool_id",
        "default_tls_container_id",
        "protocol",
        "protocol_port",
        "member_address",
        "member_device_id")

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    # the listener id
    id = resource2.Body("id")
    # tenant id
    tenant_id = resource2.Body("tenant_id")
    # the listener name
    name = resource2.Body("name")
    # the listener description
    description = resource2.Body("description")
    # Listening protocol number.
    # Instructions for use: Support TCP, HTTP, UDP, TERMINATED_HTTPS
    protocol = resource2.Body("protocol")
    # Listening port, value range [1, 65535]
    protocol_port = resource2.Body("protocol_port", type=int)
    # Associated Load Balancer ID
    loadbalancer_id = resource2.Body("loadbalancer_id")
    # Bound load balancer list
    loadbalancers = resource2.Body("loadbalancers", type=list)
    # Maximum number of connections, range of values [-1, 2147483647]
    connection_limit = resource2.Body("connection_limit", type=int, default=-1)
    # Management state is true/false.
    # Instructions for use: Fixed to true
    admin_state_up = resource2.Body("admin_state_up", type=bool, default=True)
    # Associated pool id
    default_pool_id = resource2.Body("default_pool_id")
    # Reference to the TLS secrets container.
    # Instructions for use: fill in the certificate ID
    default_tls_container_ref = resource2.Body("default_tls_container_ref")
    # List of TLS secrets container references.
    # Instructions for use: temporarily not supported
    sni_container_refs = resource2.Body("sni_container_refs")
    # Listener tag
    tags = resource2.Body("tags", type=list)