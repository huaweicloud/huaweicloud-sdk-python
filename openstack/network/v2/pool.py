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

class Pool(resource2.Resource):
    resource_key = 'pool'
    resources_key = 'pools'
    base_path = '/lbaas/pools'
    service = network_service.NetworkService()

    _query_mapping = resource2.QueryParameters(
        "limit",
        "marker",
        "page_reverse",
        "id",
        "name",
        "description",
        "healthmonitor_id",
        "loadbalancer_id",
        "protocol",
        "lb_algorithm",
        "member_address",
        "member_device_id"
    )

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # the pool id
    id = resource2.Body("id")
    # tenant id
    tenant_id = resource2.Body("tenant_id")
    # pool name
    name = resource2.Body("name")
    # pool description
    description = resource2.Body("description")
    # Back-end protocol
    # Instructions for use: Supports TCP, UDP, and HTTP.
    # When listener's protocol is TCP, the pool's protocol must be TCP,
    # and the listener's protocol is HTTP or TERMINATED_HTTPS.
    # The pool's protocol must be HTTP.
    protocol = resource2.Body("protocol")
    # The load balancing algorithm can be ROUND_ROBIN, LEAST_CONNECTIONS, SOURCE_IP.
    # Usage note: When the SOURCE_IP is configured, the back-end non-zero weight is invalid
    lb_algorithm = resource2.Body("lb_algorithm")
    # Backend member list
    members = resource2.Body("members", type=list)
    # Health monitor uuid
    healthmonitor_id = resource2.Body("healthmonitor_id")
    # Management status, true/false.
    # Instructions for use: Fixed to true
    admin_state_up = resource2.Body("admin_state_up", type=bool, default=True)
    # Pool associated listener ID
    listener_id = resource2.Body("listener_id")
    # Pool associated listerner list
    listeners = resource2.Body("listeners", type= list)
    # Session persistence
    session_persistence = resource2.Body("session_persistence", type=dict)
    # The loadbalancer id of the pool
    loadbalancer_id = resource2.Body("loadbalancer_id")
