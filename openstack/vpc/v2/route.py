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


class Route(resource.Resource):
    resource_key = 'route'
    resources_key = 'routes'
    base_path = '/vpc/routes'
    service = vpc_service.VpcService()

    # capabilities
    allow_create = True
    allow_delete = True
    allow_get = True
    allow_list = True

    _query_mapping = resource.QueryParameters(
        'id',
        'vpc_id',
        'destination',
        'type',
        project_id='tenant_id',
    )

    # Properties
    #: The route ID.
    id = resource.Body('id')
    #: The destination IP address or CIDR block.
    destination = resource.Body('destination')
    #: The next hop. If the route type is peering,
    #: enter the VPC peering connection ID.
    nexthop = resource.Body('nexthop')
    #: The route type.
    type = resource.Body('type')
    #: The VPC for which a route is to be added.
    vpc_id = resource.Body('vpc_id')
    #: The project ID.
    project_id = resource.Body('tenant_id')

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

        endpoint_override = self.service.get_endpoint_override() if self.service.get_endpoint_override() \
            else self.get_endpoint_override(session)
        service = self.get_service_filter(self, session)
        if self.put_create:
            request = self._prepare_request(requires_id=True,
                                            prepend_key=prepend_key)
            response = session.put(request.uri, endpoint_filter=self.service,
                                   endpoint_override=endpoint_override,
                                   json=request.body, headers=request.headers,
                                   microversion=service.microversion)
        else:
            request = self._prepare_request(requires_id=False,
                                            prepend_key=prepend_key)
            response = session.post(request.uri, endpoint_filter=self.service,
                                    endpoint_override=endpoint_override,
                                    json=request.body, headers=request.headers,
                                    microversion=service.microversion)

        self._translate_response(response)
        return self

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

        request = self._prepare_request()
        service = self.get_service_filter(self, session)
        endpoint_override = self.service.get_endpoint_override() if self.service.get_endpoint_override() \
            else self.get_endpoint_override(session)
        response = session.delete(request.uri, endpoint_filter=self.service,
                                  microversion=service.microversion,
                                  endpoint_override=endpoint_override,
                                  headers={"Accept": ""},
                                  params=params)

        self._translate_response(response, has_body=has_body)
        return self

    def list(self, session, paginated=False, **params):
        """This method is a generator which yields resource objects.

        This resource object list generator handles pagination and takes query
        params for response filtering.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param bool paginated: ``True`` if a GET to this resource returns
                               a paginated series of responses, or ``False``
                               if a GET returns only one page of data.
                               **When paginated is False only one
                               page of data will be returned regardless
                               of the API's support of pagination.**
        :param dict params: These keyword arguments are passed through the
            :meth:`~openstack.resource2.QueryParamter._transpose` method
            to find if any of them match expected query parameters to be
            sent in the *params* argument to
            :meth:`~openstack.session.Session.get`. They are additionally
            checked against the
            :data:`~openstack.resource2.Resource.base_path` format string
            to see if any path fragments need to be filled in by the contents
            of this argument.

        :return: A generator of :class:`Resource` objects.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_list` is not set to ``True``.
        """
        if not self.allow_list:
            raise exceptions.MethodNotSupported(self, "list")

        more_data = True
        query_params = self._query_mapping._transpose(params)
        uri = self.get_list_uri(params)
        service = self.get_service_filter(self, session)
        while more_data:
            endpoint_override = self.service.get_endpoint_override() if self.service.get_endpoint_override() \
                else self.get_endpoint_override(session)
            resp = session.get(uri, endpoint_filter=self.service,
                               microversion=service.microversion,
                               endpoint_override=endpoint_override,
                               headers={"Accept": "application/json"},
                               params=query_params)
            response_json = resp.json()
            if self.resources_key:
                resources = self.find_value_by_accessor(response_json,
                                                        self.resources_key)
            else:
                resources = response_json

            if not resources:
                more_data = False

            # Keep track of how many items we've yielded. If we yielded
            # less than our limit, we don't need to do an extra request
            # to get back an empty data set, which acts as a sentinel.
            yielded = 0
            new_marker = None
            for data in resources:
                # Do not allow keys called "self" through. Glance chose
                # to name a key "self", so we need to pop it out because
                # we can't send it through cls.existing and into the
                # Resource initializer. "self" is already the first
                # argument and is practically a reserved word.
                data.pop("self", None)

                value = self.existing(**data)
                new_marker = value.id
                yielded += 1
                yield value

            query_params = dict(query_params)
            # if `next marker path` is explicit specified, use it as marker
            next_marker = self.get_next_marker(response_json,
                                               yielded,
                                               query_params)
            if next_marker:
                new_marker = next_marker if next_marker != -1 else None

            # if cls.next_marker_path:
            #     if isinstance(cls.next_marker_path, six.string_types):
            #         new_marker = cls.find_value_by_accessor(response_json,
            #                                                 cls.next_marker_path)
            #     elif callable(cls.next_marker_path):
            #         new_marker = cls.next_marker_path(response_json, yielded)

            if not new_marker:
                return
            if not paginated:
                return
            if self.query_limit_key in query_params:
                if yielded < query_params["limit"]:
                    return
            query_params[self.query_limit_key] = yielded
            query_params[self.query_marker_key] = new_marker

    def get_endpoint_override(self, session):
        endpoint = session.get_endpoint(
            interface=self.service.interface,
            service_type=self.service.service_type
        )
        endpoint_override = endpoint[0:endpoint.rindex('/')]
        return endpoint_override
