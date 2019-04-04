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


class SecurityGroup(resource.Resource):
    resource_key = 'security_group'
    resources_key = 'security_groups'
    base_path = '/security-groups'
    service = vpc_service.VpcServiceV1()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = False
    allow_delete = True
    allow_list = True

    _query_mapping = resource.QueryParameters('vpc_id',
                                              'enterprise_project_id')

    # Properties
    #: The security group name.
    name = resource.Body('name')
    #: The security group description.
    description = resource.Body('description')
    #: The ID of the VPC this security group belongs to.
    vpc_id = resource.Body('vpc_id')
    #: A list of
    #: :class:`~openstack.vpc.v1.security_group_rule.SecurityGroupRule`
    #: objects. *Type: list*
    security_group_rules = resource.Body('security_group_rules', type=list)
    #: The enterprise project id of the VPC.
    enterprise_project_id = resource.Body('enterprise_project_id')
