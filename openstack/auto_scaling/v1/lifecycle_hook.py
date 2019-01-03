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


class LifecycleHookBase(resource.Resource):
    resource_key = 'lifecycle_hook'
    resources_key = 'lifecycle_hooks'
    base_path = '/scaling_lifecycle_hook/%(scaling_group_id)s'
    service = auto_scaling_service.AutoScalingService()

    # capabilities
    allow_create = True
    allow_list = True
    allow_get = True
    allow_delete = True
    allow_update = True

    name = resource.Body("lifecycle_hook_name")
    scaling_group_id = resource.URI('scaling_group_id')
    lifecycle_hook_type = resource.Body('lifecycle_hook_type')
    default_result = resource.Body('default_result')
    default_timeout = resource.Body('default_timeout')
    notification_topic_urn = resource.Body('notification_topic_urn')
    notification_topic_name = resource.Body('notification_topic_name')
    notification_metadata = resource.Body('notification_metadata')
    create_time = resource.Body('create_time')


class LifecycleHookList(LifecycleHookBase):
    '''
    life_cycle_state,health_status,start_number,limit
    '''
    base_path = '/scaling_lifecycle_hook/%(scaling_group_id)s/list'


class InstanceHook(resource.Resource):
    resource_key = 'scaling_instance_hook'
    resources_key = 'scaling_instance_hooks'
    base_path = '/scaling_instance_hook/%(scaling_group_id)s/callback'

    allow_update = True
    service = auto_scaling_service.AutoScalingService()
    scaling_group_id = resource.URI('scaling_group_id')
    lifecycle_action_key = resource.Body('lifecycle_action_key')
    instance_id = resource.Body('instance_id')
    lifecycle_hook_name = resource.Body('lifecycle_hook_name')
    lifecycle_action_result = resource.Body('lifecycle_action_result')

    def call_back(self, session, **attrs):
        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()

        response = session.put(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=attrs, headers=request.headers)
        ## http 返回码若成功为204
        if not response.status_code == 204:
            _logger.debug('request AS service lifecycle hook call back url is %s response code is %s ' % (response.url, response.status_code))
            raise exceptions.InvalidRequest(
                "Request AS service lifecycle hook call back %s failed" % request.uri)
        else:
            return self


class InstanceHookList(resource.Resource):
    resource_key = 'instance_hanging_info'
    resources_key = 'instance_hanging_info'
    base_path = '/scaling_instance_hook/%(scaling_group_id)s/list'
    allow_list = True
    service = auto_scaling_service.AutoScalingService()

    _query_mapping = resource.QueryParameters(
        'instance_id')

    lifecycle_action_key = resource.Body('lifecycle_action_key')
    instance_id = resource.Body('instance_id')
    lifecycle_hook_name = resource.Body('lifecycle_hook_name')
    scaling_group_id = resource.Body('scaling_group_id')
    lifecycle_hook_status = resource.Body('lifecycle_hook_status')
    timeout = resource.Body('timeout')
    default_result = resource.Body('default_result')
