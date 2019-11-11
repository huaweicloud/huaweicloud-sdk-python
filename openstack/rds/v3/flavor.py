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

from openstack.rds import rds_service
from openstack.rds.v3 import rdsresource as _rdsresource
from openstack import resource2 as resource


class Flavor(_rdsresource.Resource):

    base_path = '/flavors/%(database_name)s'
    resource_key = 'flavor'
    resources_key = 'flavors'
    service = rds_service.RDSServiceV3()

    _query_mapping = resource.QueryParameters('version_name')

    # capabilities
    allow_get = True
    allow_list = True

    # Properties
    ram = resource.Body('ram', type=int)
    vcpus = resource.Body('vcpus')
    instance_mode = resource.Body('instance_mode')
    spec_code = resource.Body('spec_code')