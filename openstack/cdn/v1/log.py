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

from openstack.cdn import cdn_resource
from openstack.cdn import cdn_service
from openstack import resource2 as resource


class Log(cdn_resource.Resource):
    base_path = '/cdn/logs'
    resource_key = 'log'
    resources_key = 'logs'
    service = cdn_service.CDNService()

    allow_create = False
    allow_get = False
    allow_delete = False
    allow_list = True

    _query_mapping = cdn_resource.QueryParameters('query_date', 'domain_name', 'enterprise_project_id')

    #: The queried domain name.
    domain_name = resource.Body('domain_name')
    #: The start time of a query, which is expressed as milliseconds
    #: since 1970-01-01 00:00:00 UTC.
    start_time = resource.Body('start_time')
    #: The end time of a query, which is expressed as milliseconds
    #: since 1970-01-01 00:00:00 UTC.
    end_time = resource.Body('end_time')
    #: The name of a log file.
    name = resource.Body('name', alternate_id=True)
    #: The size (Byte) of a log file.
    size = resource.Body('size', type=int)
    #: The link to download.
    link = resource.Body('link')
