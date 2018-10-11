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

import sys
from openstack import connection
from openstack import utils

utils.enable_logging(debug=False, stream=sys.stdout)
auth_url = 'xxxxxx'
userDomainId = 'xxxxxx'
projectId = 'xxxxxx'
username = 'xxxxxx'
password = 'xxxxxx'

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
    verify=False
)


def get_job(_conn):
    job_id = 'ff808082643a7d4801643f09c4a13be0'
    job = _conn.ecs.get_job(job_id)
    print(job)


# get_job(conn)
