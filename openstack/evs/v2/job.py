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

import re

from openstack import resource2
from openstack.evs import evs_service
from openstack import exceptions

class Job(resource2.Resource):
    base_path = '/jobs'
    service = evs_service.EvsService()
    allow_get = True

    # job's status
    status = resource2.Body('status')
    # job's operation object
    entities = resource2.Body('entities', type=dict)
    # job's id
    job_id = resource2.Body('job_id')
    # job's type
    job_type = resource2.Body('job_type')
    # begin time
    begin_time = resource2.Body('begin_time')
    # end time
    end_time = resource2.Body('end_time')
    # the error code when the job execution failed
    error_code = resource2.Body('error_code')
    # the fail reason when the job execution failed
    fail_reason = resource2.Body('fail_reason')
    # the error message returned when an error occurs
    message = resource2.Body('message')
    # the error code returned when an error occurs
    code = resource2.Body('code')
    # number of subtasks
    sub_jobs_total = resource2.Body('sub_jobs_total', type=int)
    # execution information for each subtask
    sub_jobs = resource2.Body('sub_jobs', type=list)

    def get(self, session, requires_id=True):
        """Get a remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param boolean requires_id: A boolean indicating whether resource ID
                                    should be part of the requested URI.
        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_get` is not set to ``True``.
        """
        if not self.allow_get:
            raise exceptions.MethodNotSupported(self, "get")

        request = self._prepare_request(requires_id=requires_id)
        endpoint_override = self.get_endpoint_override(session)
        service = self.get_service_filter(self, session)
        response = session.get(request.uri, endpoint_filter = self.service,
                               microversion = service.microversion,
                               endpoint_override=endpoint_override)
        self._translate_response(response)
        return self


    def get_endpoint_override(self,session):
        endpoint = session.get_endpoint(
            interface=self.service.interface,
            service_type=self.service.service_type
        )
        endpoint_override = re.sub(r'/v+./', "/v1/", endpoint)
        return endpoint_override