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

from openstack.rds import rds_service
from openstack.rds.v1 import rdsresource as _rdsresource
from openstack import resource2 as resource


class Version(_rdsresource.Resource):
    base_path = '/datastores/%(datastore_name)s/versions'
    resources_key = 'dataStores'
    service = rds_service.RDSService()

    # capabilities
    allow_list = True

    # Properties
    #: Data store name
    datastore_name = resource.URI("datastore_name")
    #: Datastore version id
    id = resource.Body('id')
    #: Datastore name
    name = resource.Body('name')
    #: Datastore id
    datastore = resource.Body('datastore')
    #: Datastore image id
    image = resource.Body('image')
    #: Datastore version packages
    packages = resource.Body('packages')
    #: Active status, 1/0
    #: *Type: int*
    active = resource.Body('active', type=int)


class Parameter(_rdsresource.Resource):

    base_path = '/datastores/versions/%(datastore_version_id)s/parameters'
    resources_key = 'configuration-parameters'
    service = rds_service.RDSService()

    # capabilities
    allow_list = True
    allow_get = True

    # Properties
    #: Parameter name
    name = resource.Body('name', alternate_id=True)
    #: Minimum value of the parameter
    #: *Type: int*
    min = resource.Body('min', type=int)
    #: Maximum value of the parameter
    #: *Type: int*
    max = resource.Body('max', type=int)
    #: Parameter type
    type = resource.Body('type')
    #: Value range
    value_range = resource.Body('value_range')
    #: Description
    description = resource.Body('description')
    #: Require restart or not
    #: *Type: bool*
    restart_required = resource.Body('restart_required', type=bool)
    #: Datastore version id
    datastore_version_id = resource.URI('datastore_version_id')
