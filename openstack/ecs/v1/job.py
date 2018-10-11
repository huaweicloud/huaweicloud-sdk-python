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

from openstack import resource2
from openstack.ecs import ecs_service


class Job(resource2.Resource):
    base_path = '/jobs'
    service = ecs_service.EcsService()
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
