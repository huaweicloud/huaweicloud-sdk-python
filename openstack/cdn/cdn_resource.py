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

from openstack.cdn.exceptions import CDNException
from openstack import exceptions
from openstack import resource2 as resource


class QueryParameters(resource.QueryParameters):
    def __init__(self, *names, **mappings):
        """Create a dict of accepted query parameters

        :param names: List of strings containing client-side query parameter
                      names. Each name in the list maps directly to the name
                      expected by the server.

        :param mappings: Key-value pairs where the key is the client-side
                         name we'll accept here and the value is the name
                         the server expects, e.g, changes_since=changes-since

        By default, both limit and marker are included in the initial mapping
        as they're the most common query parameters used for listing resources.
        """
        self._mapping = {'page_size': 'page_size',
                         'page_number': 'page_number'}
        self._mapping.update(dict({name: name for name in names}, **mappings))


class StatisticParameters(resource.QueryParameters):
    def __init__(self, *names, **mappings):
        """Create a dict of accepted query parameters

        :param names: List of strings containing client-side query parameter
                      names. Each name in the list maps directly to the name
                      expected by the server.

        :param mappings: Key-value pairs where the key is the client-side
                         name we'll accept here and the value is the name
                         the server expects, e.g, changes_since=changes-since

        By default, both limit and marker are included in the initial mapping
        as they're the most common query parameters used for listing resources.
        """
        self._mapping = {'start_time': 'start_time',
                         'end_time': 'end_time',
                         'domain_name': 'domain_name',
                         'enterprise_project_id': 'enterprise_project_id'}
        self._mapping.update(dict({name: name for name in names}, **mappings))


class Resource(resource.Resource):
    """Base class for all CDN resources.

    CDN service defines a different paginating method and a resource body
    structure when any error occurs, so we need override the base
    :class:`~openstack.resource2.Resource` to treat these differences.
    """

    #: dotted json path to get total resource numbers.
    total_path = 'total'
    #: The query key for the number of the queried page.
    query_page_number_key = 'page_number'
    #: The query key for the size of each page.
    query_page_size_key = 'page_size'

    _query_mapping = QueryParameters(page_size=query_page_size_key,
                                     page_number=query_page_number_key)

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
        if cls.query_page_size_key and \
                cls.query_page_size_key not in query_params:
            raise exceptions.InvalidRequest('query parameter %s is required.'
                                            % cls.query_page_size_key)
        if cls.query_page_number_key and \
                cls.query_page_number_key not in query_params:
            raise exceptions.InvalidRequest('query parameter %s is required.'
                                            % cls.query_page_number_key)
        uri = cls.get_list_uri(params)

        while more_data:
            endpoint_override = cls.service.get_endpoint_override()
            resp = session.get(uri, endpoint_filter=cls.service,
                               endpoint_override=endpoint_override,
                               headers={"Accept": "application/json"},
                               params=query_params)
            response_json = resp.json()
            cls.check_error(response_json)
            if cls.resources_key:
                resources = cls.find_value_by_accessor(response_json,
                                                       cls.resources_key)
            else:
                resources = response_json
            if resources is None:
                resources = []

            if not resources:
                return

            for data in resources:
                value = cls.existing(**data)
                yield value

            if not paginated:
                return
            more_data, next_page_num = cls.get_next_pagination(response_json,
                                                               query_params)
            query_params[cls.query_page_number_key] = next_page_num

    @classmethod
    def get_next_pagination(cls, response, query_params):
        total = cls.find_value_by_accessor(response, cls.total_path) or 0
        page_size = int(query_params.get(cls.query_page_size_key))
        page_number = int(query_params.get(cls.query_page_number_key))
        if total > page_size * page_number:
            return True, page_number + 1
        return False, page_number

    def _translate_response(self, response, has_body=True):
        """Override this method to check if the response is an error"""
        if has_body:
            body = response.json()
            self.check_error(body)
            if self.resource_key and self.resource_key in body:
                body = body[self.resource_key]

            body = self._filter_component(body, self._body_mapping())
            self._body.attributes.update(body)
            self._body.clean()

        headers = self._filter_component(response.headers,
                                         self._header_mapping())
        self._header.attributes.update(headers)
        self._header.clean()

    @classmethod
    def check_error(cls, response):
        """Raises exception when the response returns an error body"""
        if 'error' in response:
            e = response['error']
            raise CDNException(code=e['error_code'], message=e['error_msg'])
