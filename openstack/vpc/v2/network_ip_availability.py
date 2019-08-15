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

from openstack import exceptions
from openstack import resource2 as resource
from openstack.vpc import vpc_service


class NetworkIPAvailability(resource.Resource):
    resource_key = 'network_ip_availability'
    resources_key = None
    base_path = '/network-ip-availabilities'
    service = vpc_service.VpcService()

    # capabilities
    allow_get = True

    # Properties
    #: The network ID.
    network_id = resource.Body('network_id')
    #: The network name.
    network_name = resource.Body('network_name')
    #: The project ID.
    project_id = resource.Body('tenant_id')
    #: The total number of IP addresses on a network.
    total_ips = resource.Body('total_ips', type=int)
    #: The number of in-use IP addresses on a network.
    used_ips = resource.Body('used_ips', type=int)
    #: The subnet IP address usage object.
    subnet_ip_availability = resource.Body('subnet_ip_availability', type=list)

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

        request = self._prepare_request(requires_id=requires_id)
        endpoint_override = self.service.get_endpoint_override() if self.service.get_endpoint_override() \
            else self.get_endpoint_override(session)
        service = self.get_service_filter(self, session)
        response = session.get(request.uri, endpoint_filter=self.service,
                               microversion=service.microversion,
                               endpoint_override=endpoint_override)
        self._translate_response(response)
        return self

    def get_endpoint_override(self, session):
        endpoint = session.get_endpoint(
            interface=self.service.interface,
            service_type=self.service.service_type
        )
        endpoint_override = endpoint[0:endpoint.rindex('/')]
        return endpoint_override
