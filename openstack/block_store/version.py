# Copyright 2019 Huawei Technologies Co.,Ltd.
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

from openstack.block_store import block_store_service
from openstack import resource2
from openstack import exceptions


class Version(resource2.Resource):
    resource_key = 'version'
    resources_key = 'versions'
    base_path = '/'
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_list = True

    # Properties
    links = resource2.Body('links', type=list)
    status = resource2.Body('status')

    #: The minimum API version.
    min_version = resource2.Body('min_version')
    #: The request messages type of the API version.
    media_types = resource2.Body('media-types', type=list)
    #: The ID of the API version.
    id = resource2.Body('id')
    #: The last time when the API version is updated.
    updated = resource2.Body('updated')
    #: The sub-version of the API version.
    version = resource2.Body('version')

    @classmethod
    def list(cls, session, paginated=False, **params):
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
        if not cls.allow_list:
            raise exceptions.MethodNotSupported(cls, "list")

        more_data = True
        query_params = cls._query_mapping._transpose(params)
        uri = cls.get_list_uri(params)
        service = cls.get_service_filter(cls, session)
        while more_data:
            endpoint_override = cls.get_endpoint_override(session)
            resp = session.get(uri, endpoint_filter=cls.service,
                               microversion=service.microversion,
                               endpoint_override=endpoint_override,
                               headers={"Accept": "application/json"},
                               params=query_params)
            response_json = resp.json()
            if cls.resources_key:
                resources = cls.find_value_by_accessor(response_json,
                                                       cls.resources_key)
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

                value = cls.existing(**data)
                new_marker = value.id
                yielded += 1
                yield value

            query_params = dict(query_params)
            # if `next marker path` is explicit specified, use it as marker
            next_marker = cls.get_next_marker(response_json,
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
            if cls.query_limit_key in query_params:
                if yielded < query_params["limit"]:
                    return
            query_params[cls.query_limit_key] = yielded
            query_params[cls.query_marker_key] = new_marker

    @classmethod
    def get_endpoint_override(cls, session):
        endpoint = session.get_endpoint(
            interface=cls.service.interface,
            service_type=cls.service.service_type
        )
        endpoint_override = endpoint.split('/v')
        return endpoint_override[0]


class VersionV2(Version):
    base_path = '/v2'
