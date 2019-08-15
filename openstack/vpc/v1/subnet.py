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

from openstack import exceptions
from openstack import resource2 as resource
from openstack import utils
from openstack.vpc.v1.private_ip import PrivateIP
from openstack.vpc import vpc_service


class Subnet(resource.Resource):
    resource_key = 'subnet'
    resources_key = 'subnets'
    base_path = '/subnets'
    # Note: The path for update and delete requests is different
    # from the base_path
    update_base_path = '/vpcs/%(vpc_id)s/subnets'
    delete_base_path = '/vpcs/%(vpc_id)s/subnets'
    service = vpc_service.VpcServiceV1()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource.QueryParameters('vpc_id')

    #: The subnet name.
    name = resource.Body('name')
    #: The network segment on which the subnet resides.
    cidr = resource.Body('cidr')
    #: The gateway of the subnet.
    gateway_ip = resource.Body('gateway_ip')
    #: Whether the DHCP function is enabled for the subnet. True by default
    is_dhcp_enabled = resource.Body('dhcp_enable', type=bool, default=True)
    #: The IP address of DNS server 1 on the subnet.
    primary_dns = resource.Body('primary_dns')
    #: The IP address of DNS server 2 on the subnet.
    secondary_dns = resource.Body('secondary_dns')
    #: The DNS server address list of a subnet.
    # This field is required if you need to use more than two DNS servers.
    dnsList = resource.Body('dnsList', type=list)
    #: The availability zone (AZ) to which the subnet belongs.
    availability_zone = resource.Body('availability_zone')
    #: The ID of the VPC to which the subnet belongs.
    vpc_id = resource.Body('vpc_id')
    #: The status of the subnet.
    # The value can be ACTIVE, DOWN, UNKNOWN, or ERROR.
    status = resource.Body('status')
    #: The network (Native OpenStack API) ID.
    neutron_network_id = resource.Body('neutron_network_id')
    #: The subnet (Native OpenStack API) ID.
    neutron_subnet_id = resource.Body('neutron_subnet_id')

    def update(self, session, prepend_key=True, has_body=True):
        """Update information about a subnet.

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`
        :param bool prepend_key: A boolean indicating whether the resource_key
            should be prepended in a resource update request.
            Default to True.
        :param bool has_body: should mapping response body to resource.
            Always be True.

        :returns: The subnet after updated
        :rtype: :class:`~openstack.vpc.v1.subnet.Subnet`
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

        request = self._prepare_request(prepend_key=prepend_key)
        # Note: Override the default subnet resource uri
        body_attrs = self._body.attributes
        uri = self.update_base_path % body_attrs
        request.uri = utils.urljoin(uri, self.id)

        endpoint_override = self.service.get_endpoint_override()
        response = session.put(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=request.body, headers=request.headers)

        self._translate_response(response)
        return self

    def delete(self, session, params=None, has_body=False):
        """Delete the remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param params: http params to be sent
        :type params: dict or None
        :param bool has_body: should mapping response body to resource

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_update` is not set to ``True``.
        """
        if not self.allow_delete:
            raise exceptions.MethodNotSupported(self, "delete")

        request = self._prepare_request()
        # Note: Override the default subnet resource uri
        body_attrs = self._body.attributes
        uri = self.delete_base_path % body_attrs
        request.uri = utils.urljoin(uri, self.id)

        endpoint_override = self.service.get_endpoint_override()
        response = session.delete(request.uri, endpoint_filter=self.service,
                                  endpoint_override=endpoint_override,
                                  headers={"Accept": ""},
                                  params=params)

        self._translate_response(response, has_body=has_body)
        return self

    def list_private_ips(self, session, **query):
        """Query private IP addresses in the subnet

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param dict query: Optional query parameters to be sent to limit
            the resources being returned. Valid parameters are:

            * ``limit``: The number of records returned on each page.
            * ``marker``: The resource ID of pagination query.
        :returns: A generator of resource type.
        :rtype: :class:`~openstack.vpc.v1.private_ip.PrivateIP`
        """
        params = query or {}
        params.update(subnet_id=self.id)
        return PrivateIP.list(session, paginated=True, **params)
