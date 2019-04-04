# Copyright 2018 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack import resource2 as resource
from openstack.vpc import vpc_service


class Port(resource.Resource):
    resource_key = 'port'
    resources_key = 'ports'
    base_path = '/ports'
    service = vpc_service.VpcServiceV1()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource.QueryParameters(
        'id', 'name', 'network_id', 'mac_address',
        'device_id', 'device_owner', 'status',
        is_admin_state_up='admin_state_up')

    #: The ID of the network to which the port belongs.
    network_id = resource.Body('network_id')
    #: The administrative state of the port.
    # The value can only be true, and the default value is true.
    is_admin_state_up = resource.Body(
        'admin_state_up', type=bool, default=True)
    #: The port MAC address.
    mac_address = resource.Body('mac_address')
    #: The port IP address.
    fixed_ips = resource.Body('fixed_ips', type=list)
    #: The ID of the device to which the port belongs.
    device_id = resource.Body('device_id')
    #: The owner type of the device to which the port belongs.
    device_owner = resource.Body('device_owner')
    #: The ID of the project(tenant).
    project_id = resource.Body('tenant_id')
    #: The status of the port.
    # The value can be ACTIVE, BUILD, or DOWN.
    status = resource.Body('status')
    #: The UUID of the security group.
    security_group_ids = resource.Body('security_groups', type=list)
    #: The set of zero or more allowed address pairs.
    allowed_address_pairs = resource.Body('allowed_address_pairs', type=list)
    #: The set of zero or more extra DHCP option pairs.
    extra_dhcp_opts = resource.Body('extra_dhcp_opts', type=list)
    #: The interface type of the port.
    # The value can be ovs, hw_veb, or others.It is visible to administrators.
    binding_vif_type = resource.Body('binding:vif_type')
    #: The VIF details.It is visible to administrators.
    binding_vif_details = resource.Body('binding:vif_details', type=dict)
    #: The host ID.It is visible to administrators.
    binding_host_id = resource.Body('binding:host_id')
    #: The configuration of customized data. It is visible to administrators.
    binding_profile = resource.Body('binding:profile', type=dict)
    #: The type of the bound vNIC.
    # The value can be normal or direct.
    binding_vnic_type = resource.Body('binding:vnic_type')
    #: Port security enable flag.
    port_security_enabled = resource.Body('port_security_enabled', type=bool, default=True)
    #: Extended attribute: The default intranet domain name information of the primary NIC.
    dns_assignment = resource.Body('dns_assignment', type=list)
    #: Extended attribute: The default intranet DNS name of the primary NIC.
    dns_name = resource.Body('dns_name')
