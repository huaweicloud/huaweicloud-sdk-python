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


class rdsverion(_rdsresource.Resource):

    resource_key = 'version'
    resources_key = 'versions'
    base_path = '/'
    _version_str = '/rds'
    _need_project_id = False
    service = rds_service.RDSService()



    # capabilities
    allow_get = True
    allow_list = True

    

    # Properties
    id = resource.Body('id')
    links = resource.Body('links', type=dict)
    status = resource.Body('status')
    updated = resource.Body('updated')

    @classmethod
    def _get_custom_url(cls, session, url):
        key = (cls.service.service_type, cls.service.interface)

        #if key in session.endpoint_cache:
        #    base_url = session.endpoint_cache[key]
        #else:
        base_url = session.get_endpoint(
            interface=cls.service.interface,
            service_type=cls.service.service_type)

        # IAM only returns rds base url, as we need to hack
        # this to support both hw rds and openstack rds
        # provide custom url per resource type
        return base_url.rsplit('/', 2)[0]

    @classmethod
    def _get_custom_override(cls, endpoint_override):
        if cls._need_project_id:
            return endpoint_override
        else:
            return endpoint_override.rsplit('/', 2)[0]
