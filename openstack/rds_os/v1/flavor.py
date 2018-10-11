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

from openstack.rds import rds_service as rds_service
from openstack.rds_os.v1 import rdsresource as _rdsresource
from openstack import resource2 as resource


class Flavor(_rdsresource.Resource):

    base_path = '/flavors'
    resource_key = 'flavor'
    resources_key = 'flavors'
    service = rds_service.RDSService()

    # capabilities
    allow_get = True
    allow_list = True

    # Properties
    #: Flavor id
    id = resource.Body('id')
    #: Flavor name
    name = resource.Body('name')
    #: Ram size in MB.
    #: *Type:int*
    ram = resource.Body('ram', type=int)
    #: Instance created time
    specCode = resource.Body('specCode')
    #: Links
    #: *Type:list*
    links = resource.Body('links', type=list)
    #: String id
    str_id = resource.Body('str_id')
    #: Flavor detail
    #: *Type:list*
    flavor_detail = resource.Body('flavor_detail', type=list)
    #: Flavor
    #: *Type:dict*
    flavor = resource.Body('flavor', type=dict)
    #: Price detail
    #: *Type:list*
    price_detail = resource.Body('price_detail', type=list)
