# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
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

from openstack import resource2 as resource
from openstack.vpc import vpc_service


class Route(resource.Resource):
    resource_key = 'route'
    resources_key = 'routes'
    base_path = '/vpc/routes'
    service = vpc_service.VpcService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_get = True
    allow_list = True

    _query_mapping = resource.QueryParameters(
        'id',
        'vpc_id',
        'destination',
        'type',
        project_id='tenant_id',
    )

    # Properties
    #: The route ID.
    id = resource.Body('id')
    #: The destination IP address or CIDR block.
    destination = resource.Body('destination')
    #: The next hop. If the route type is peering,
    #: enter the VPC peering connection ID.
    nexthop = resource.Body('nexthop')
    #: The route type.
    type = resource.Body('type')
    #: The VPC for which a route is to be added.
    vpc_id = resource.Body('vpc_id')
    #: The project ID.
    project_id = resource.Body('tenant_id')
