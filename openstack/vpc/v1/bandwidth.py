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


class Bandwidth(resource.Resource):
    resource_key = 'bandwidth'
    resources_key = 'bandwidths'
    base_path = '/bandwidths'
    service = vpc_service.VpcServiceV1()

    # capabilities
    allow_create = False
    allow_get = True
    allow_update = True
    allow_delete = False
    allow_list = True

    # Properties
    #: The bandwidth size, in unit Mbits/s.
    size = resource.Body('size', type=int)
    #: The bandwidth sharing type.The value can be PER or WHOLE.
    share_type = resource.Body('share_type')
    #: A list of elastic IP addresses of the bandwidth. Each element is a dict
    # containing `publicip_id`, `publicip_address`, `publicip_type`.
    publicip_info = resource.Body('publicip_info', type=list)
    #: The project(tenant) ID of the user.
    project_id = resource.Body('tenant_id')
    #: The bandwidth type.The value can be bgp, union, double, or telcom.
    bandwidth_type = resource.Body('bandwidth_type')
    #: The charging mode.The value can be bandwidth or traffic.
    charge_mode = resource.Body('charge_mode')
    #: The billing information when charging by period.
    billing_info = resource.Body('billing_info')
    #: The enterprise project id of the VPC.
    enterprise_project_id = resource.Body('enterprise_project_id')
