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

import logging

from openstack import exceptions
from openstack import resource2 as resource
from openstack.auto_scaling import auto_scaling_service

_logger = logging.getLogger(__name__)


class BaseTag(resource.Resource):
    resource_key = 'tag'
    resources_key = 'tags'
    base_path = 'scaling_group_tag/tags'
    service = auto_scaling_service.AutoScalingService()
    # allow_get = True
    allow_list = True
    tag = resource.Body('tags')
    key = resource.Body("key")
    value = resource.Body('value')


class GroupTag(BaseTag):
    base_path = '/scaling_group_tag/%(group_id)s/tags'
    group_id = resource.URI('group_id')


class TagAction(GroupTag):
    allow_create = True
    action = resource.Body('action')
    base_path = '/scaling_group_tag/%(group_id)s/tags/action'

    def tag_action(self, session, **attrs):
        if not self.allow_create:
            raise exceptions.MethodNotSupported(self, "create")

        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()
        #super(TagAction, self).create(session, )
        response = session.post(request.uri, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=attrs, headers=request.headers)

        if not response.status_code == 204:
            _logger.debug(
                'request AS service tag action url is %s response code is %s ' % (response.url, response.status_code))
            raise exceptions.InvalidRequest(
                "Request AS service tag action %s failed" % request.uri)
        else:
            return self
