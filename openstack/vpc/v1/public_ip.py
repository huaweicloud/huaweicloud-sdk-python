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

from openstack import exceptions
from openstack import resource2 as resource
from openstack.vpc import vpc_service


class PublicIP(resource.Resource):
    name_attribute = "public_ip_address"
    resource_name = "public ip"
    resource_key = 'publicip'
    resources_key = 'publicips'
    base_path = '/publicips'
    service = vpc_service.VpcServiceV1()

    _query_mapping = resource.QueryParameters('ip_version')

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    #: Public network IP information.
    publicip = resource.Body('publicip', type=dict)
    #: Bandwidth information.
    bandwidth = resource.Body('bandwidth', type=dict)
    #: The status of the elastic IP address. The value can be FREEZED,
    # BIND_ERROR, BINDING, PENDING_DELETE, PENDING_CREATE, NOTIFYING,
    # NOTIFY_DELETE, PENDING_UPDATE, DOWN, ACTIVE, ELB, ERROR, or UNKNOWN.
    status = resource.Body('status')
    #: The extra infomation about the public ip.
    profile = resource.Body('profile', type=dict)
    #: The type of the elastic IP address.
    type = resource.Body('type')
    #: The obtained elastic IP address.
    public_ip_address = resource.Body('public_ip_address')
    #: The obtained elastic v6 version IP address.
    public_ipv6_address = resource.Body('public_ipv6_address')
    #: The IP address version, 4 or 6
    ip_version = resource.Body('ip_version', int)
    #: The alternative name for public_ip_address.
    # Note: We need this attribute because the creation request
    # uses this attribute name.
    ip_address = resource.Body('ip_address')
    #: The private IP address bound to the elastic IP address.
    private_ip_address = resource.Body('private_ip_address')
    #: The port ID.
    port_id = resource.Body('port_id')
    #: The project(tenant) ID of the operator.
    project_id = resource.Body('tenant_id')
    #: The time for applying for the elastic IP address.
    create_time = resource.Body('create_time')
    #: The bandwidth ID of the elastic IP address.
    bandwidth_id = resource.Body('bandwidth_id')
    #: The bandwidth size.
    bandwidth_size = resource.Body('bandwidth_size', type=int)
    #: The type of the bandwidth sharing.
    bandwidth_share_type = resource.Body('bandwidth_share_type')
    #: The bandwidth name.
    bandwidth_name = resource.Body('bandwidth_name')
    #: The bandwidth charge mode.
    # Note: This attribute only exists in the creation request.
    bandwidth_charge_mode = resource.Body('bandwidth_charge_mode')
    #: The enterprise project id of the VPC.
    enterprise_project_id = resource.Body('enterprise_project_id')
