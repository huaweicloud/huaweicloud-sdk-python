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


class Backup(_rdsresource.Resource):

    base_path = '/backups'
    resource_key = 'backup'
    resources_key = 'backups'
    service = rds_service.RDSService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True

    # Properties
    #: Backup id
    id = resource.Body('id')
    #: Instance id
    instance_id = resource.Body('instance_id')
    #: Instance id alt
    instance = resource.Body('instance')
    #: Backup created time
    created = resource.Body('created')
    #: Data store information
    #: *Type: dict*
    dataStore = resource.Body('dataStore', type=dict)
    #: Data backup description
    description = resource.Body('description')
    #: Back file name
    name = resource.Body('name')
    #: Back file size in GB
    #: *Type:int*
    size = resource.Body('size', type=int)
    #: Backup status
    status = resource.Body('status')
    #: Finished time
    updated = resource.Body('updated')
    #: Backup type
    backuptype = resource.Body('backuptype')


class BackupPolicy(_rdsresource.Resource):

    base_path = '/instances/%(instanceId)s/backups/policy'
    resource_key = 'policy'
    service = rds_service.RDSService()

    # capabilities
    allow_create = True
    allow_get = True

    # Properties
    #: instaceId
    instanceId = resource.URI('instanceId')
    #: Policy keep days
    #: *Type: int*
    keepday = resource.Body('keepday', type=int)
    #: Start time
    starttime = resource.Body('starttime')

    # use put to create, but we don't require id
    def create(self, session, prepend_key=True):
        endpoint_override = self.service.get_endpoint_override()
        request = self._prepare_request(requires_id=False,
                                        prepend_key=prepend_key)
        if endpoint_override is None:
            request.uri = self._get_custom_url(session, request.uri)
        response = session.put(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=request.body, headers=request.headers)

        self._translate_response(response)
        return self
