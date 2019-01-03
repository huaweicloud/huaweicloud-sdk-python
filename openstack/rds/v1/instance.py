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
from openstack import utils


class Instance(_rdsresource.Resource):

    base_path = '/instances'
    resource_key = 'instance'
    resources_key = 'instances'
    service = rds_service.RDSService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_get = True
    allow_update = True
    allow_list = True

    # Properties
    #: Instance id
    id = resource.Body('id')
    #: Instance status
    status = resource.Body('status')
    #: Instance name
    name = resource.Body('name')
    #: Instance created time
    created = resource.Body('created')
    #: Host name of the instance
    hostname = resource.Body('hostname')
    #: Instance type readreplica/master/slave
    type = resource.Body('type')
    #: Region
    region = resource.Body('region')
    #: Instance updated time
    updated = resource.Body('updated')
    #: Availability Zone
    availabilityZone = resource.Body('availabilityZone')
    #: Private cloud id
    vpc = resource.Body('vpc')
    #: Nics interface list
    #: *Type:dict*
    nics = resource.Body('nics', type=dict)
    #: Security group
    #: *Type: dict*
    securityGroup = resource.Body('securityGroup', type=dict)
    #: Flavor information
    flavor = resource.Body('flavorRef')
    #: Volume information
    #: *Type: dict*
    volume = resource.Body('volume', type=dict)
    #: Data store information
    #: *Type: dict*
    dataStoreInfo = resource.Body('datastore', type=dict)
    #: Backup Strategy
    #: *Type: dict*
    backupStrategy = resource.Body('backupStrategy', type=dict)
    #: Id of the master
    replica_of = resource.Body('replica_of')
    #: HA information
    #: *Type: dict*
    ha = resource.Body('ha', type=dict)
    #: Restore Point, create new instance from restore
    #: *Type: dict*
    restorePoint = resource.Body("restorePoint", type=dict)
    #: Root password
    dbRtPd = resource.Body("dbRtPd")
    #: DB port
    dbPort = resource.Body("dbPort")

    def _action(self, session, body):
        """Perform instance action"""
        url = utils.urljoin(self.base_path, self._get_id(self), 'action')
        endpoint_override = self.service.get_endpoint_override()
        if endpoint_override is None:
            url = self._get_custom_url(session, url)
        else:
            endpoint_override = self._get_custom_override(endpoint_override)
        resp = session.post(url, endpoint_filter=self.service,
                            endpoint_override=endpoint_override,
                            json=body,
                            headers={"Accept": "application/json",
                                     "Content-type": "application/json",
                                     "X-Language": "en-us"})

        return resp.json()

    def resize(self, session, flavorRef):
        return self._action(session, {"resize": {"flavorRef": flavorRef}})

    def resize_volume(self, session, size):
        return self._action(session, {"resize": {"volume": {"size": size}}})

    def restart(self, session):
        return self._action(session, {"restart": {}})

    def restore(self, session, backupRef):
        return self._action(session, {"restore": {"backupRef": backupRef}})


class InstanceParameter(_rdsresource.Resource):

    base_path = 'instances/%(instanceId)s/parameters'

    service = rds_service.RDSService()
    # Properties
    #: These Parameters requires restart
    #: *Type: int*
    shouldRestart = resource.Body('shouldRestart', type=int)
    #: Set parameter result, 1, master success; 0; all success
    #: *Type: int*
    setParameteResult = resource.Body('setParameteResult', type=int)

    @classmethod
    def set_params(cls, session, **params):
        uri = cls.base_path % params
        params.pop('instanceId')
        body = {'values': params}
        endpoint_override = cls.service.get_endpoint_override()
        if endpoint_override is None:
            uri = cls._get_custom_url(session, uri)
        else:
            endpoint_override = cls._get_custom_override(endpoint_override)
        resp = session.put(uri, endpoint_filter=cls.service,
                           endpoint_override=endpoint_override,
                           headers={"Accept": "application/json",
                                    "Content-type": "application/json",
                                    "X-Language": "en-us"},
                           json=body)
        resp = resp.json()
        return cls.existing(**resp)

    @classmethod
    def reset_params(cls, session, **params):
        uri = utils.urljoin(cls.base_path % params, 'default')
        body = {}
        endpoint_override = cls.service.get_endpoint_override()

        if endpoint_override is None:
            uri = cls._get_custom_url(session, uri)
        else:
            endpoint_override = cls._get_custom_override(endpoint_override)
        resp = session.put(uri, endpoint_filter=cls.service,
                           endpoint_override=endpoint_override,
                           headers={"X-Language": "en-us"},
                           json=body)
        resp = resp.json()
        return cls.existing(**resp)


class InstanceErrorLog(_rdsresource.Resource):

    base_path = 'instances/%(instanceId)s/errorlog'
    resources_key = 'errorLogList'
    service = rds_service.RDSService()

    _query_mapping = resource.QueryParameters('startDate',
                                              'endDate',
                                              'curPage',
                                              'perPage')

    # capabilities
    allow_list = True
    # Properties
    # instanceId
    instanceId = resource.URI('instanceId')
    # Error log data time
    datetime = resource.Body('datetime')
    #: Error log content
    content = resource.Body('content')


class InstanceSlowLog(_rdsresource.Resource):

    base_path = 'instances/%(instanceId)s/slowlog'
    resources_key = 'slowLogList'
    service = rds_service.RDSService()

    _query_mapping = resource.QueryParameters('sftype',
                                              'top')

    # capabilities
    allow_list = True
    # Properties
    # instanceId
    instanceId = resource.URI('instanceId')
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
