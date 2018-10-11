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
from openstack import resource2 as resource


# NOTE: The VPN service is unmaintained, need to consider remove it

class VPNService(resource.Resource):
    resource_key = 'vpnservice'
    resources_key = 'vpnservices'
    base_path = '/vpn/vpnservices'
    service = network_service.NetworkService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # Properties
    #: Human-readable description for the vpnservice.
    description = resource.Body('description')
    #: The external IPv4 address that is used for the VPN service.
    external_v4_ip = resource.Body('external_v4_ip')
    #: The external IPv6 address that is used for the VPN service.
    external_v6_ip = resource.Body('external_v6_ip')
    #: The administrative state of the vpnservice, which is up ``True`` or
    #: down ``False``. *Type: bool*
    is_admin_state_up = resource.Body('admin_state_up', type=bool)
    #: The vpnservice name.
    name = resource.Body('name')
    #: ID of the router into which the VPN service is inserted.
    router_id = resource.Body('router_id')
    #: The ID of the project this vpnservice is associated with.
    project_id = resource.Body('tenant_id')
    #: The vpnservice status.
    status = resource.Body('status')
    #: The ID of the subnet on which the tenant wants the vpnservice.
    subnet_id = resource.Body('subnet_id')


class IPSecPolicy(resource.Resource):
    resource_key = 'ipsecpolicy'
    resources_key = 'ipsecpolicies'
    base_path = '/vpn/ipsecpolicies'
    service = network_service.NetworkService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    name = resource.Body('name')
    transform_protocol = resource.Body('transform_protocol')
    auth_algorithm = resource.Body('auth_algorithm')
    pfs = resource.Body('pfs')
    description = resource.Body('description')
    encapsulation_mode = resource.Body('encapsulation_mode')
    encryption_algorithm = resource.Body('encryption_algorithm')
    lifetime = resource.Body('lifetime')
    tenant_id = resource.Body('project_id')
    value = resource.Body('value')
    units = resource.Body('units')


class IKEPolicy(resource.Resource):
    resource_key = 'ikepolicy'
    resources_key = 'ikepolicies'
    base_path = 'vpn/ikepolicies'
    service = network_service.NetworkService()

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    name = resource.Body('name')
    auth_algorithm = resource.Body('auth_algorithm')
    description = resource.Body('description')
    encryption_algorithm = resource.Body('encryption_algorithm')
    ike_version = resource.Body('ike_version')
    lifetime = resource.Body('lifetime')
    pfs = resource.Body('pfs')
    phase1_negotiation_mode = resource.Body('phase1_negotiation_mode')
    value = resource.Body('value')
    units = resource.Body('units')
    tenant_id = resource.Body('project_id')


class EndPointGroup(resource.Resource):
    resource_key = 'endpoint_group'
    resources_key = 'endpoint_groups'
    base_path = 'vpn/endpoint-groups'
    service = network_service.NetworkService()

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    name = resource.Body('name')
    endpoints = resource.Body('endpoints')
    type = resource.Body('type')
    description = resource.Body('description')
    tenant_id = resource.Body('project_id')


class VPNConnetion(resource.Resource):
    resource_key = 'ipsec_site_connection'
    resources_key = 'ipsec_site_connections'
    base_path = 'vpn/ipsec-site-connections'
    service = network_service.NetworkService()

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    name = resource.Body('name')
    description = resource.Body('description')
    tenant_id = resource.Body('project_id')
    dpd = resource.Body('dpd')
    timeout = resource.Body('timeout')
    action = resource.Body('action')
    local_id = resource.Body('local_id')
    psk = resource.Body('psk')
    initiator = resource.Body('initiator')
    ipsecpolicy_id = resource.Body('ipsecpolicy_id')
    admin_state_up = resource.Body('admin_state_up', type=bool)
    mtu = resource.Body('mtu')
    peer_ep_group_id = resource.Body('peer_ep_group_id')
    ikepolicy_id = resource.Body('ikepolicy_id')
    vpnservice_id = resource.Body('vpnservice_id')
    local_ep_group_id = resource.Body('local_ep_group_id')
    peer_address = resource.Body('peer_address')
    peer_id = resource.Body('peer_id')
    auth_mode = resource.Body('auth_mode')
    peer_cidrs = resource.Body('peer_cidrs')
    interval = resource.Body('interval')
    route_mode = resource.Body('route_mode')
    status = resource.Body('status')
    type = resource.Body('type')
