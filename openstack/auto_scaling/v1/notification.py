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


class Notification(resource.Resource):
    resource_key = 'topic'
    resources_key = 'topics'
    base_path = '/scaling_notification/%(scaling_group_id)s'
    service = auto_scaling_service.AutoScalingService()

    allow_list = True

    scaling_group_id = resource.URI('scaling_group_id')
    topic_name = resource.Body('topic_name')
    topic_urn = resource.Body('topic_urn')
    topic_scene = resource.Body("topic_scene")
    topics = resource.Body('topics')


class CreateNotification(Notification):
    base_path = '/scaling_notification/%(scaling_group_id)s'

    def create_notification(self, session, **attrs):
        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()

        response = session.put(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=attrs, headers=request.headers)

        if not response.status_code == 200:
            _logger.debug('failed request AS service create notification url is %s response code is %s ' % (
                response.url, response.status_code))
            raise exceptions.InvalidRequest(
                "Request AS service create notification %s failed" % request.uri)
        else:
            return self


class DeleteNotification(resource.Resource):
    service = auto_scaling_service.AutoScalingService()
    allow_delete = True
    topic_urn = resource.URI('topic_urn')
    scaling_group_id = resource.URI('scaling_group_id')
    base_path = '/scaling_notification/%(scaling_group_id)s/%(topic_urn)s'

    def delete_notification(self, session):
        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()

        response = session.delete(request.uri, endpoint_filter=self.service,
                                  endpoint_override=endpoint_override, headers=request.headers)

        if not response.status_code == 204:
            _logger.debug('failed request AS service delete notification url is %s response code is %s ' % (
                response.url, response.status_code))
            raise exceptions.InvalidRequest(
                "Request AS service delete notification %s failed" % request.uri)
        else:
            return self
