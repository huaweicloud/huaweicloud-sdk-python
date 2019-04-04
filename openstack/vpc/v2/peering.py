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

from openstack import resource2 as resource
from openstack.vpc import vpc_service
from openstack import exceptions


class Peering(resource.Resource):
    resource_key = 'peering'
    resources_key = 'peerings'
    base_path = '/vpc/peerings'
    service = vpc_service.VpcService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_update = True
    allow_get = True
    allow_list = True

    _query_mapping = resource.QueryParameters(
        'id',
        'name',
        'status',
        'vpc_id',
        project_id='tenant_id',
    )

    # Properties
    #: The VPC peering connection ID.
    id = resource.Body('id')
    #: The name of the VPC peering connection. The value can contain 1 to 64 characters.
    name = resource.Body('name')
    #: The VPC peering connection status.
    #: The value can be PENDING_ACCEPTANCE, REJECTED, EXPIRED, DELETED, or ACTIVE.
    status = resource.Body('status')
    #: The information about the local VPC.
    request_vpc_info = resource.Body('request_vpc_info', type=dict)
    #: The information about the peer VPC.
    accept_vpc_info = resource.Body('accept_vpc_info', type=dict)


class PeeringAccept(Peering):
    resource_key = None
    resources_key = None
    base_path = '/vpc/peerings/%(peering_id)s/accept'

    # capabilities
    allow_create = False
    allow_delete = False
    allow_update = True
    allow_get = False
    allow_list = False

    peering_id = resource.URI('peering_id')

    def update(self, session, prepend_key=True, has_body=True):
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

        if not self.allow_update:
            raise exceptions.MethodNotSupported(self, "update")

        request = self._prepare_request(requires_id=False, prepend_key=prepend_key)
        request.body = None
        service = self.get_service_filter(self, session)
        endpoint_override = self.service.get_endpoint_override()
        response = session.put(request.uri, endpoint_filter=self.service,
                               microversion=service.microversion,
                               endpoint_override=endpoint_override,
                               json=request.body, headers=request.headers)

        self._translate_response(response, has_body=has_body)
        return self


class PeeringReject(PeeringAccept):
    base_path = '/vpc/peerings/%(peering_id)s/reject'
