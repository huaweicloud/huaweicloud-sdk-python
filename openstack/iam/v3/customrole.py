# -*- coding:utf-8 -*-
# Copyright 2020 Huawei Technologies Co.,Ltd.
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

from openstack.iam import iam_service
from openstack import resource2
from openstack import utils


class Customrole(resource2.Resource):
    resource_key = 'role'
    resources_key = 'roles'
    base_path = '/OS-ROLE/roles'
    service = iam_service.IamService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    patch_update = True

    # Properties
    #: Unique role name, within the owning domain. *Type: string*
    name = resource2.Body('name')
    #: The links for the service resource.
    links = resource2.Body('links', type=dict)
    #: The id of the domain that the role belongs to. *Type: string*
    domain_id = resource2.Body('domain_id')
    #: The display type of the role. *Type: string*
    type = resource2.Body('type')
    #: The display name of the role. *Type: string*
    display_name = resource2.Body('display_name')
    #: The catalog of the role. *Type: string*
    catalog = resource2.Body('catalog')
    #: The policy of the role.
    policy = resource2.Body('policy', type=dict)
    #: The description of the role. *Type: string*
    description = resource2.Body('description')
    #: The flag of the role. *Type: string*
    flag = resource2.Body('flag')
    #: The description_cn of the role. *Type: string*
    description_cn = resource2.Body('description_cn')
    #: The id of the role. *Type: string*
    id = resource2.Body('id')
    #: The updated_time of the role. *Type: string*
    updated_time = resource2.Body('updated_time')
    #: The created_time of the role. *Type: string*
    created_time = resource2.Body('created_time')
    #: The references of the role. *Type: int*
    references = resource2.Body('references', type=int)
