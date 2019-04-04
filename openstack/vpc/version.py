# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
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


class Version(resource.Resource):
    resource_key = 'version'
    resources_key = 'versions'
    base_path = '/'
    service = vpc_service.VpcService(
        version=vpc_service.VpcService.UNVERSIONED
    )

    # capabilities
    allow_list = True

    # Properties
    links = resource.Body('links')
    status = resource.Body('status')


class VersionV1(resource.Resource):
    resource_key = 'version'
    resources_key = 'versions'
    base_path = '/'
    service = vpc_service.VpcServiceV1(
        version=vpc_service.VpcServiceV1.UNVERSIONED
    )

    # capabilities
    allow_list = True

    # Properties
    links = resource.Body('links')
    status = resource.Body('status')
