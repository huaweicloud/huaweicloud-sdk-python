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

from openstack import resource2
from openstack.tms import tms_service
from openstack import exceptions


class PredefineTag(resource2.Resource):
    """Define a EnterpriseProject class. list and create EP"""

    base_path = '/predefine_tags'
    service = tms_service.TmsService()

    # Allow operation for this resource.
    # capabilities
    allow_create = False
    allow_list = False
    allow_get = True
    allow_update = True
    allow_delete = False

    # Mapping of accepted query parameter names.
    _query_mapping = resource2.QueryParameters(
        'key',
        'value',
        'limit',
        'marker',
        'order_field',
        'order_method'
    )

    tags = resource2.Body("tags", type=list)
    total_count = resource2.Body("total_count", type=int)
    marker = resource2.Body("marker", type=int)
    new_tag = resource2.Body("new_tag")
    old_tag = resource2.Body("old_tag")

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

        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        response = session.get(request.uri, endpoint_filter = self.service,
                               microversion = service.microversion,
                               endpoint_override=endpoint_override)
        self._translate_response(response)
        return self

    def update(self, session, prepend_key=True, has_body=False):
        """Update the remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param prepend_key: A boolean indicating whether the resource_key
                            should be prepended in a resource update request.
                            Default to True.

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_update` is not set to ``True``.
        """
        # The id cannot be dirty for an update
        self._body._dirty.discard("id")
        id_mapping_name = self._body_mapping()["id"]
        self._body._dirty.discard(id_mapping_name)

        # Only try to update if we actually have anything to update.
        if not any([self._body.dirty, self._header.dirty]):
            return self

        if not self.allow_update:
            raise exceptions.MethodNotSupported(self, "update")

        request = self._prepare_request(requires_id=False, prepend_key=prepend_key)
        service = self.get_service_filter(self, session)
        endpoint_override = self.service.get_endpoint_override()
        if self.patch_update:
            response = session.patch(request.uri, endpoint_filter=self.service,
                                     microversion = service.microversion,
                                     endpoint_override=endpoint_override,
                                     json=request.body,
                                     headers=request.headers)
        else:
            response = session.put(request.uri, endpoint_filter=self.service,
                                   microversion=service.microversion,
                                   endpoint_override=endpoint_override,
                                   json=request.body, headers=request.headers)

        self._translate_response(response, has_body=False)
        return self

class PredefineTagAction(resource2.Resource):
    """Define a EnterpriseProject class. get quotas of EP"""

    base_path = '/predefine_tags/action'
    service = tms_service.TmsService()

    # Allow operation for this resource.
    # capabilities
    allow_create = True
    allow_list = False
    allow_get = False
    allow_update = True
    allow_delete = False

    action = resource2.Body("action")
    tags = resource2.Body("tags")


    def create(self, session, prepend_key=True):
        """Create a remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param prepend_key: A boolean indicating whether the resource_key
                            should be prepended in a resource creation
                            request. Default to True.

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_create` is not set to ``True``.
        """
        if not self.allow_create:
            raise exceptions.MethodNotSupported(self, "create")

        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        if self.put_create:
            request = self._prepare_request(requires_id=True,
                                            prepend_key=prepend_key)
            response = session.put(request.uri, endpoint_filter=self.service,
                                   endpoint_override=endpoint_override,
                                   json=request.body, headers=request.headers,
                                   microversion = service.microversion)
        else:
            request = self._prepare_request(requires_id=False,
                                            prepend_key=prepend_key)
            response = session.post(request.uri, endpoint_filter=self.service,
                                    endpoint_override=endpoint_override,
                                    json=request.body, headers=request.headers,
                                    microversion=service.microversion)

        self._translate_response(response, False)
        return self