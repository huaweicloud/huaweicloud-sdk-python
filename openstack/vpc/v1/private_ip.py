# Copyright 2018 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack import exceptions
from openstack import resource2 as resource
from openstack.vpc import vpc_service


class PrivateIP(resource.Resource):
    resource_key = 'privateip'
    resources_key = 'privateips'
    base_path = '/privateips'
    # Note: The uri for listing is different from base_path
    list_base_path = '/subnets/%(subnet_id)s/privateips'
    service = vpc_service.VpcServiceV1()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    #: The status of the private IP address.
    status = resource.Body('status')
    #: The ID of the subnet from which the IP address is allocated.
    subnet_id = resource.Body('subnet_id')
    #: The project(tenant) ID of the operator.
    project_id = resource.Body('tenant_id')
    #: The VM or network device using the private IP address.
    device_owner = resource.Body('device_owner')
    #: The private IP address obtained.
    ip_address = resource.Body('ip_address')

    @classmethod
    def get_list_uri(cls, params):
        return cls.list_base_path % params

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
        request = self._prepare_request(requires_id=False,
                                        prepend_key=prepend_key)
        # Note: The creation request body is a list of private
        # ip address objects with 'privateips' as the key. This is not
        # identical to the normal API request.
        # The 'subnet_id' attribute is mandatory in the creation request Body
        # but is an URI attribute in the updating and deleting requests. So
        # we add it into the creation request body manually.
        if prepend_key:
            body = request.body[self.resource_key]
            body['subnet_id'] = self.subnet_id
            request.body = {'privateips': [body]}
        else:
            request.body['subnet_id'] = self.subnet_id
            request.body = {'privateips': [request.body]}

        response = session.post(request.uri, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=request.body, headers=request.headers)

        body = response.json()
        if self.resource_key and self.resource_key in body:
            body = body[self.resource_key]
        if self.resources_key and self.resources_key in body:
            private_ips = body[self.resources_key]
            # Note: We only support to create private ips one
            # by one.
            body = private_ips[0] if len(private_ips) > 0 else {}

        body = self._filter_component(body, self._body_mapping())
        self._body.attributes.update(body)
        self._body.clean()

        headers = self._filter_component(response.headers,
                                         self._header_mapping())
        self._header.attributes.update(headers)
        self._header.clean()
        return self

    @classmethod
    def batch_create(cls, session, private_ips):
        """Create the given private ips in batch

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param private_ips: A list of dict defined private ip.

        :returns: A list of the created private ips.
        """
        uri = cls.base_path
        body = {'privateips': private_ips}
        endpoint_override = cls.service.get_endpoint_override()
        response = session.post(uri, endpoint_filter=cls.service,
                                endpoint_override=endpoint_override,
                                json=body)
        body = response.json()
        result = []
        for each in body[cls.resources_key]:
            result.append(cls.new(**each))
        return result
