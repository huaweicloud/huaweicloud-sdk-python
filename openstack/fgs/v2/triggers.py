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

from openstack.fgs import fgs_service
from openstack import resource2 as resource
from openstack import exceptions


class Trigger(resource.Resource):
    """FGS reverse record resource"""
    resources_key = 'triggers'
    base_path = '/fgs/triggers/%(function_urn)s'
    service = fgs_service.FGSService()

    function_urn = resource.URI('function_urn')

    # capabilities
    allow_create = True
    allow_get = False
    allow_update = False
    allow_list = True
    allow_delete = True

    #: Trigger type.
    trigger_type_code = resource.Body('trigger_type_code')
    #:  Event type.
    event_type_code = resource.Body('event_type_code')
    #: Event message.
    event_data = resource.Body('event_data')
    #: trigger_id.
    trigger_id = resource.Body('trigger_id')
    #: trigger_status.
    trigger_status = resource.Body('trigger_status')
    #: last_updated_time.
    last_updated_time = resource.Body('last_updated_time')
    #: created_time.
    created_time = resource.Body('created_time')

    def delete(self, session, params=None, has_body=False):
        """Delete the remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param params: http params to be sent
        :param bool has_body: should mapping response body to resource

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_update` is not set to ``True``.
        """
        if not self.allow_delete:
            raise exceptions.MethodNotSupported(self, "delete")

        request = self._prepare_request(requires_id=False)

        endpoint_override = self.service.get_endpoint_override()
        response = session.delete(request.uri, endpoint_filter=self.service,
                                  endpoint_override=endpoint_override,
                                  headers={"Accept": ""},
                                  params=params)

        self._translate_response(response, has_body=has_body)
        return self


class TriggerExpansion(Trigger):
    base_path = '/fgs/triggers/%(function_urn)s/%(tg_type)s/%(tg_id)s'
    function_urn = resource.URI('function_urn')
    tg_type = resource.URI('tg_type')
    tg_id = resource.URI('tg_id')

    # capabilities
    allow_create = False
    allow_list = False
    allow_get = True
