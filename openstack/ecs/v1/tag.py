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
from openstack.ecs import ecs_service


class ServerTag(resource2.Resource):
    resources_key = "tags"
    base_path = "/cloudservers/%(server_id)s/tags"

    service = ecs_service.EcsService()

    allow_list = True

    server_id = resource2.URI("server_id")
    key = resource2.Body("key")
    value = resource2.Body("value")


class ProjectTag(resource2.Resource):
    resources_key = "tags"
    base_path = "/cloudservers/tags"

    service = ecs_service.EcsService()

    allow_list = True

    key = resource2.Body("key")
    values = resource2.Body("values", type=list)


class ServerTagAction(resource2.Resource):
    base_path = "/cloudservers/%(server_id)s/tags/action"

    service = ecs_service.EcsService()

    allow_create = True

    server_id = resource2.URI("server_id")
    action = resource2.Body('action')
    tags = resource2.Body('tags', type=list)

    def create(self, session, prepend_key=True):
        """Create a remote resource based on this Server Tag Action.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param prepend_key: A boolean indicating whether the resource_key
                            should be prepended in a resource creation
                            request. Default to True.

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_create` is not set to ``True``.
        """

        endpoint_override = self.service.get_endpoint_override()
        request = self._prepare_request(requires_id=False,
                                        prepend_key=prepend_key)
        response = session.post(request.uri, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=request.body, headers=request.headers)

        self._translate_response(response, has_body=False)
        return self
