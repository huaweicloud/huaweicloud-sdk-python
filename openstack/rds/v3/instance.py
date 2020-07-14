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
from openstack import utils
from openstack.rds.v3.rdsresource import ErrorResponse


class Instance(_rdsresource.Resource):

    base_path = '/instances'
    # resource_key = 'instance'
    resources_key = 'instances'
    service = rds_service.RDSServiceV3()

    _query_mapping = resource.QueryParameters('id', 'name', 'type', 'datastore_type',
                                              'vpc_id', 'subnet_id', 'offset', 'limit')

    # capabilities
    allow_create = True
    allow_delete = True
    allow_get = True
    allow_update = True
    allow_list = True
    prepend_key = False

    # Properties
    #: Instance id
    id = resource.Body('id')
    name = resource.Body('name')
    status = resource.Body('status')
    #req
    region = resource.Body('region')
    availability_zone = resource.Body('availability_zone')
    engine = resource.Body('engine', type=dict)
    ha = resource.Body('ha', type=dict)
    # kmsKeyId = resource.Body('kmsKeyId')
    volume = resource.Body('volume', type=dict)
    flavor_ref = resource.Body('flavor_ref')
    vpc_id = resource.Body('vpc_id')
    subnet_id = resource.Body('subnet_id')
    security_group_id = resource.Body('security_group_id')
    backup_strategy = resource.Body('backup_strategy', type=dict)
    dataStoreInfo = resource.Body('datastore', type=dict)
    password = resource.Body('password')
    replica_of_id = resource.Body('replica_of_id')

    nodes = resource.Body('nodes')
    db_user_name = resource.Body('db_user_name')
    private_ips = resource.Body('private_ips', type=[])
    public_ips = resource.Body('public_ips', type=[])
    type = resource.Body('type')
    switch_strategy = resource.Body('switch_strategy')
    maintenance_window = resource.Body('maintenance_window')
    related_instance = resource.Body('related_instance', type=[])
    disk_encryption_id = resource.Body('disk_encryption_id')
    time_zone = resource.Body('time_zone')
    port = resource.Body('port')
    configuration_id = resource.Body('configuration_id')
    enterprise_project_id = resource.Body('enterprise_project_id')
    charge_info = resource.Body('charge_info')
    version = resource.Body('version')
    replication_mode = resource.Body('replication_mode')
    start_time = resource.Body('start_time')
    keep_days = resource.Body('keep_days')
    resize_flavor = resource.Body('resize_flavor', type=dict)

    restore_point = resource.Body('restore_point', type=dict)
    job_id = resource.Body("job_id")
    instance = resource.Body("instance")

    def _action(self, session, body, action="action"):
        """Perform instance action"""
        url = utils.urljoin(self.base_path, self._get_id(self), action)
        endpoint_override = self.service.get_endpoint_override()
        if endpoint_override is None:
            url = self._get_custom_url(session, url)
        else:
            endpoint_override = self._get_custom_override(endpoint_override)
        if action == "action":
            response = session.post(url, endpoint_filter=self.service,
                                    endpoint_override=endpoint_override,
                                    json=body,
                                    raise_exc=False,
                                    headers={"Accept": "application/json",
                                             "Content-type": "application/json",
                                             "X-Language": "en-us"})
        else:
            response = session.get(url, endpoint_filter=self.service,
                                   endpoint_override=endpoint_override,
                                   json=body,
                                   raise_exc=False,
                                   headers={"Accept": "application/json",
                                            "Content-type": "application/json",
                                            "X-Language": "en-us"})
        if response.status_code >= 400:
            return ErrorResponse.make_response(response)

        self._translate_response(response)
        return self

    def resize(self, session, flavor_ref):
        return self._action(session, {"resize_flavor": {"spec_code": flavor_ref}})

    def resize_volume(self, session, size):
        return self._action(session, {"enlarge_volume": {"size": size}})

    def restart(self, session):
        return self._action(session, {"restart": {}})

    def single_to_ha(self, session, **single_to_ha_param):
        new_az_code = single_to_ha_param.get("new_az_code")
        password = single_to_ha_param.get("password")
        if password is not None and password != '':
            single_to_ha_req = {"single_to_ha": {"az_code_new_node": new_az_code, "password": password}}
            return self._action(session, single_to_ha_req)
        else:
            single_to_ha_req = {"single_to_ha": {"az_code_new_node": new_az_code}}
            return self._action(session, single_to_ha_req)

    def recovery_instance(self, session, **params):
        endpoint_override = self.service.get_endpoint_override()
        if endpoint_override is None:
            url = self._get_custom_url(session, self.base_path)
        else:
            endpoint_override = self._get_custom_override(endpoint_override)
        response = session.post(url, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=params,
                                raise_exc=False,
                                headers={"Accept": "application/json",
                                         "Content-type": "application/json",
                                         "X-Language": "en-us"})
        if response.status_code >= 400:
            return ErrorResponse.make_response(response)

        self._translate_response(response)
        return self

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


class InstanceParameter(_rdsresource.Resource):

    base_path = 'instances/%(instance_id)s/configurations'
    resources_key = "restart_required"
    service = rds_service.RDSServiceV3()
    restart_required = resource.Body('restart_required')

    def set_params(self, session, **params):
        uri = self.base_path % params
        params.pop('instance_id')
        body = {'values': params}
        endpoint_override = self.service.get_endpoint_override()
        if endpoint_override is None:
            uri = self._get_custom_url(session, uri)
        else:
            endpoint_override = self._get_custom_override(endpoint_override)
        response = session.put(uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               raise_exc=False,
                               headers={"Accept": "application/json",
                                    "Content-type": "application/json",
                                    "X-Language": "en-us"},
                               json=body)
        if response.status_code >= 400:
            return ErrorResponse.make_response(response)

        self._translate_response(response)
        return self


class InstanceErrorLog(_rdsresource.Resource):

    base_path = 'instances/%(instance_id)s/errorlog'
    resources_key = 'error_log_list'
    service = rds_service.RDSServiceV3()

    _query_mapping = resource.QueryParameters('start_date',
                                              'end_date',
                                              'offset',
                                              'limit',
                                              'level')

    # capabilities
    allow_list = True
    # Properties
    # instanceId
    instanceId = resource.URI('instance_id')
    # Error log data time
    datetime = resource.Body('datetime')
    #: Error log content
    content = resource.Body('content')


class InstanceSlowLog(_rdsresource.Resource):

    base_path = 'instances/%(instance_id)s/slowlog'
    resources_key = 'slow_log_list'
    service = rds_service.RDSServiceV3()

    _query_mapping = resource.QueryParameters('start_date',
                                              'end_date',
                                              'offset',
                                              'limit',
                                              'type')

    # capabilities
    allow_list = True
    # Properties
    # instanceId
    instanceId = resource.URI('instance_id')
    # Execuation count
    count = resource.Body('count')
    # Average time
    time = resource.Body('time')
    # Average time for waiting lock
    lockTime = resource.Body('lockTime')
    # Average sent rows
    rowsSent = resource.Body('rowsSent')
    # Average examined rows
    rowsExamined = resource.Body('rowsExamined')
    # Database belonged
    database = resource.Body('database')
    # User account
    users = resource.Body('users')
    # Query sample
    querySample = resource.Body('querySample')


class InstanceRestoreTime(_rdsresource.Resource):

    base_path = 'instances/%(instance_id)s/restore-time'
    resources_key = 'errorLogList'
    service = rds_service.RDSServiceV3()

    _query_mapping = resource.QueryParameters('date')

    # capabilities
    allow_list = True
    # Properties
    # instanceId
    instanceId = resource.URI('instanceId')
    # Error log data time
    datetime = resource.Body('datetime')
    #: Error log content
    content = resource.Body('content')
