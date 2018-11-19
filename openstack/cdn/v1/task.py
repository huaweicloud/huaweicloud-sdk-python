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

from openstack.cdn import cdn_resource
from openstack.cdn import cdn_service
from openstack import resource2 as resource
from openstack import utils


class Task(cdn_resource.Resource):
    base_path = '/cdn/historytasks'
    resource_key = 'task'
    resources_key = 'tasks'
    service = cdn_service.CDNService()

    allow_create = False
    allow_get = True
    allow_delete = False
    allow_list = True

    _query_mapping = cdn_resource.QueryParameters('status', 'start_date',
                                                  'end_date', 'order_field',
                                                  'order_type',
                                                  'user_domain_id')

    #: The type of a task. The value is either 'refresh' or 'preheating'.
    task_type = resource.Body('task_type')
    #: The status of a task after refreshing.
    #: 'task_done' indicates the refreshing task is completed successfully.
    #: 'task_inprocess' indicates that the refreshing task is being processed.
    status = resource.Body('status')
    #: The number of URLs being processing.
    processing = resource.Body('processing', type=int)
    #: The number of URLs processed successfully.
    succeeded = resource.Body('succeed', type=int)
    #: The number of URLs that failed to be processed.
    failed = resource.Body('failed', type=int)
    #: The total number of tasks.
    total = resource.Body('total', type=int)
    #: The time when the task is created.
    created_at = resource.Body('create_time')
    #: The URLs that need to be refreshed or preheated.
    urls = resource.Body('urls')

    @classmethod
    def list(cls, session, paginated=False, **params):
        """Override to mapping query parameters

        In order to be PEP8 compatible, we rename some attributes.
        When the query parameter 'order_field' is set to one of these
        attributes, we need map it back to the name on server side.

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

        :returns: A generator of :class:`Resource` objects.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_list` is not set to ``True``.
        """
        mapping = {
            'processing': 'process',
            'created_at': 'create_time',
            'succeeded': 'succeed'
        }
        if 'order_field' in params and params['order_field'] in mapping:
            params['order_field'] = mapping[params['order_field']]
        return super(Task, cls).list(session, paginated=paginated, **params)

    def get(self, session, requires_id=True):
        """Get a remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param boolean requires_id: A boolean indicating whether resource ID
                                    should be part of the requested URI.

        :returns: This :class:`Task` instance.
        :rtype: :class:`~openstack.cdn.v1.task.Task`
        """
        request = self._prepare_request(requires_id=requires_id)
        # NOTE(samsong8610): The URL for GET is not standard.
        request.uri = utils.urljoin(request.uri, 'detail')
        endpoint_override = self.service.get_endpoint_override()
        response = session.get(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override)

        self._translate_response(response)
        return self


class RefreshTask(Task):
    base_path = '/cdn/refreshtasks'
    resource_key = 'refreshTask'
    resources_key = 'refreshTasks'

    allow_create = True
    allow_get = False
    allow_delete = False
    allow_list = False

    #: The type of a task. The value is either 'refresh' or 'preheating'.
    task_type = resource.Body('taskType')
    #: The type of cache contents to be refreshed.
    #: The value is either 'file' or 'directory'. The default value is 'file'.
    # NOTE(samsong8610): This attribute is *ONLY* used in requests.
    type = resource.Body('type')

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

        endpoint_override = self.service.get_endpoint_override()
        if self.put_create:
            request = self._prepare_request(requires_id=True,
                                            prepend_key=prepend_key)
            response = session.put(request.uri, endpoint_filter=self.service,
                                   endpoint_override=endpoint_override,
                                   json=request.body, headers=request.headers)
        else:
            request = self._prepare_request(requires_id=False,
                                            prepend_key=prepend_key)
            response = session.post(request.uri, endpoint_filter=self.service,
                                    endpoint_override=endpoint_override,
                                    json=request.body, headers=request.headers, params={"enterprise_project_id": 'ALL'})

        self._translate_response(response)
        return self

class PreheatTask(Task):
    base_path = '/cdn/preheatingtasks'
    resource_key = 'preheatingTask'
    resources_key = 'preheatingTasks'

    allow_create = True
    allow_get = False
    allow_delete = False
    allow_list = False

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

        endpoint_override = self.service.get_endpoint_override()
        if self.put_create:
            request = self._prepare_request(requires_id=True,
                                            prepend_key=prepend_key)
            response = session.put(request.uri, endpoint_filter=self.service,
                                   endpoint_override=endpoint_override,
                                   json=request.body, headers=request.headers)
        else:
            request = self._prepare_request(requires_id=False,
                                            prepend_key=prepend_key)
            response = session.post(request.uri, endpoint_filter=self.service,
                                    endpoint_override=endpoint_override,
                                    json=request.body, headers=request.headers, params={"enterprise_project_id": 'ALL'})

        self._translate_response(response)
        return self