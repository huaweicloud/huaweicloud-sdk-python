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
from openstack.rds.v3.rdsresource import ErrorResponse


class Backup(_rdsresource.Resource):

    base_path = '/backups'
    resource_key = 'backup'
    resources_key = 'backups'
    service = rds_service.RDSServiceV3()
    error_key = 'error_code'
    base_files_path = '/backup-files'

    _query_mapping = resource.QueryParameters('instance_id', 'backup_id', 'backup_type', 'offset',
                                              'limit', 'begin_time', 'end_time')

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

    def create(self, session, prepend_key=True):
        endpoint_override = self.service.get_endpoint_override()
        request = self._prepare_request(requires_id=False,
                                        prepend_key=False)
        if endpoint_override is None:
            request.uri = self._get_custom_url(session, request.uri)
        response = session.post(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=request.body, headers=request.headers, raise_exc=False)
        if response.status_code >= 400:
            return ErrorResponse.make_response(response)
        self._translate_response(response)
        return self


class BackupPolicy(_rdsresource.Resource):
    base_path = '/instances/%(instance_id)s/backups/policy'
    resource_key = 'backup_policy'
    service = rds_service.RDSServiceV3()

    # capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True

    # Properties
    #: instaceId
    instance_id = resource.URI('instance_id')
    #: Policy keep days
    #: *Type: int*
    keep_days = resource.Body('keep_days', type=int)
    #: Start time
    start_time = resource.Body('start_time')
    period = resource.Body('period')

    def create(self, session, prepend_key=True):
        endpoint_override = self.service.get_endpoint_override()
        request = self._prepare_request(requires_id=False,
                                        prepend_key=prepend_key)
        if endpoint_override is None:
            request.uri = self._get_custom_url(session, request.uri)
        response = session.put(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=request.body, headers=request.headers,
                               raise_exc=False)

        if response.status_code >= 400:
            return ErrorResponse.make_response(response)
        self._translate_response(response)
        return self
