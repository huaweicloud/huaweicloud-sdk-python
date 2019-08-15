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


class VPC(resource.Resource):
    resource_key = 'vpc'
    resources_key = 'vpcs'
    base_path = '/vpcs'
    service = vpc_service.VpcServiceV1()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource.QueryParameters('enterprise_project_id')

    #: The range of available subnets in the VPC.
    cidr = resource.Body('cidr')
    #: The status of the VPC. The value can be CREATING, OK, DOWN,
    # PENDING_UPDATE, PENDING_DELETE, or ERROR.
    status = resource.Body('status')
    #: The routing rules of the VPC.
    routes = resource.Body('routes', type=list)
    #: The enterprise project id of the VPC.
    enterprise_project_id = resource.Body('enterprise_project_id')
