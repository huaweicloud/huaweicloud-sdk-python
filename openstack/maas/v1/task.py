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

from openstack.maas import maas_service
from openstack.maas.v1 import maasresource as _maasresource
from openstack import resource2 as resource
from openstack import utils


class Task(_maasresource.Resource):

    base_path = '/objectstorage/task'
    service = maas_service.MaaSService()

    # capabilities
    allow_create = True
    allow_list = True
    allow_get = True
    allow_delete = True

    _query_mapping = resource.QueryParameters('start', 'limit', 'state')

    # Properties
    #: Task Id
    #: *Type: int*
    id = resource.Body('id', type=int)
    #: Task name
    name = resource.Body('name')
    #: Source node information
    #: *Type: dict*
    src_node = resource.Body('src_node', type=dict)
    #: Dest node information
    #: *Type: dict*
    dst_node = resource.Body('dst_node', type=dict)
    #: Thread number
    #: *Type: int*
    thread_num = resource.Body('thread_num', type=int)
    #: Task status, value could be 0-5
    #: *Type: int*
    status = resource.Body('status', type=int)
    #: Task migrate progress
    #: *Type: float*
    progress = resource.Body('progress', type=float)
    #: Migrate speed, byte/s
    #: *Type: int*
    migrate_speed = resource.Body('migrate_speed', type=int)
    #: Enable KMS
    #: *Type: bool*
    enableKMS = resource.Body('enableKMS', type=bool)
    #: Taskname
    task_name = resource.Body('task_name')
    #: Task description, empty if user does not set it
    description = resource.Body('description')
    #: Error reason
    #: *Type: dict*
    error_reason = resource.Body('error_reason', type=dict)
    #: Total size of the task
    #: *Type: int*
    total_size = resource.Body('total_size', type=int)
    #: Complete size of the task
    #: *Type: int*
    complete_size = resource.Body('complete_size', type=int)
    #: Task start time
    #: *Type: int*
    start_time = resource.Body('start_time', type=int)
    #: Task left time
    #: *Type: int*
    left_time = resource.Body('left_time', type=int)
    #: Task total time
    #: *Type: int*
    total_time = resource.Body('total_time', type=int)
    #: Task migration success object number
    #: *Type: int*
    success_num = resource.Body('success_num', type=int)
    #: Task migration failed object number
    #: *Type: int*
    fail_num = resource.Body('fail_num', type=int)
    #: Task migration total object number
    #: *Type: int*
    total_num = resource.Body('total_num', type=int)
    #: SMN information
    #: *Type: dict*
    smnInfo = resource.Body('smnInfo', type=dict)

    def _action(self, session, **kwargs):
        endpoint_override = self.service.get_endpoint_override()
        url = utils.urljoin(self.base_path, self._get_id(self))
        request = self._prepare_request(prepend_key=True)
        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           json=kwargs,
                           headers=request.headers)

        if resp is not None and resp.status_code == 200:
            return True

        return False

    def start(self, session, source_ak, source_sk, target_ak, target_sk):
        return self._action(session, operation='start',
                            source_ak=source_ak,
                            source_sk=source_sk,
                            target_ak=target_ak,
                            target_sk=target_sk)

    def stop(self, session):
        return self._action(session, operation='stop')

    @classmethod
    def task_count(cls, session, state):

        uri = cls.base_path
        query_params = {'totalcount': 'true'}

        if state is not None:
            query_params.update({'state': state})

        endpoint_override = cls.service.get_endpoint_override()
        resp = session.get(uri, endpoint_filter=cls.service,
                           endpoint_override=endpoint_override,
                           headers={"Accept": "application/json",
                                    "Content-type": "application/json"},
                           params=query_params)
        resp = resp.json()
        return resp.get('taskcount')

    # overwrite resource2.py get to add request.headers
    # if all maas API requres get to have headers move this
    # to maasresrouce.py
    def get(self, session, requires_id=True):

        request = self._prepare_request(requires_id=requires_id)

        endpoint_override = self.service.get_endpoint_override()
        response = session.get(request.uri, endpoint_filter=self.service,
                               headers=request.headers,
                               endpoint_override=endpoint_override)

        self._translate_response(response)
        return self

    # overwrite resource2.py delete to add request.headers
    # if all maas API requres delete to have headers move this
    # to maasresrouce.py
    def delete(self, session):

        request = self._prepare_request()

        endpoint_override = self.service.get_endpoint_override()
        response = session.delete(request.uri, endpoint_filter=self.service,
                                  endpoint_override=endpoint_override,
                                  headers=request.headers)

        self._translate_response(response, has_body=False)
        return self
