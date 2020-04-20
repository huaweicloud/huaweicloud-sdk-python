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
from openstack.eps import eps_service
from openstack import exceptions


class EnterpriseProject(resource2.Resource):
    """Define a EnterpriseProject class. list and create EP"""

    base_path = '/enterprise-projects'
    service = eps_service.EpsService()

    # Allow operation for this resource.
    # capabilities
    allow_create = True
    allow_list = True
    allow_get = False
    allow_update = False
    allow_delete = False

    # Mapping of accepted query parameter names.
    _query_mapping = resource2.QueryParameters(
        'name',
        'status',
        'id'
    )
    enterprise_projects = resource2.Body("enterprise_projects", type= list)
    total_count = resource2.Body("total_count", type= int)

    @classmethod
    def list(cls, session, paginated=False, **params):
        if not cls.allow_list:
            raise exceptions.MethodNotSupported(cls, "list")
        query_params = cls._query_mapping._transpose(params)
        uri = cls.get_list_uri(params)
        service = cls.get_service_filter(cls, session)

        endpoint_override = cls.service.get_endpoint_override()
        resp = session.get(uri, endpoint_filter=cls.service,
                           microversion=service.microversion,
                           endpoint_override=endpoint_override,
                           headers={"Accept": "application/json"},
                           params=query_params)
        response_json = resp.json()
        value = cls.existing(**response_json)
        return value

class EnterpriseProjectQuotas(resource2.Resource):
    """Define a EnterpriseProject class. get quotas of EP"""

    base_path = '/enterprise-projects/quotas'
    service = eps_service.EpsService()

    # Allow operation for this resource.
    # capabilities
    allow_create = False
    allow_list = False
    allow_get = True
    allow_update = False
    allow_delete = False

    quotas = resource2.Body("quotas", type=list)
    type = resource2.Body("type")
    used = resource2.Body("used", type=int)
    quota = resource2.Body("quota", type=int)

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

class EnterpriseProjectDetail(resource2.Resource):
    """Define a EnterpriseProject class. get detail and update EP"""

    base_path = '/enterprise-projects/%(enterprise_project_id)s'
    service = eps_service.EpsService()

    # Allow operation for this resource.
    # capabilities
    allow_create = False
    allow_list = False
    allow_get = True
    allow_update = False
    allow_delete = False
    enterprise_project_id = resource2.URI("enterprise_project_id")
    enterprise_project = resource2.Body("enterprise_project")
    id = resource2.Body("id")
    name = resource2.Body("name")
    description = resource2.Body("description")
    status = resource2.Body("status", type=int)
    created_at = resource2.Body("created_at")
    updated_at = resource2.Body("updated_at")

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
class EnterpriseProjectUpdate(resource2.Resource):
    """Define a EnterpriseProject class. get detail and update EP"""

    base_path = '/enterprise-projects/%(enterprise_project_id)s'
    service = eps_service.EpsService()

    # Allow operation for this resource.
    # capabilities
    allow_create = False
    allow_list = False
    allow_get = True
    allow_update = True
    allow_delete = False
    enterprise_project_id = resource2.URI("enterprise_project_id")
    enterprise_project = resource2.Body("enterprise_project")
    name = resource2.Body("name")
    description = resource2.Body("description")
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

        self._translate_response(response, has_body=True)
        return self

class EnterpriseProjectAction(resource2.Resource):
    """Define a EnterpriseProject class. get detail and update EP"""

    base_path = '/enterprise-projects/%(enterprise_project_id)s/action'
    service = eps_service.EpsService()

    # Allow operation for this resource.
    # capabilities
    allow_create = True
    allow_list = False
    allow_get = False
    allow_update = False
    allow_delete = False
    enterprise_project_id = resource2.URI("enterprise_project_id")
    action = resource2.Body("action")

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

class EnterpriseProjectResourceFilter(resource2.Resource):
    """Define a EnterpriseProject class. get detail and update EP"""

    base_path = '/enterprise-projects/%(enterprise_project_id)s/resources/filter'
    service = eps_service.EpsService()

    # Allow operation for this resource.
    # capabilities
    allow_create = True
    allow_list = False
    allow_get = False
    allow_update = False
    allow_delete = False
    enterprise_project_id = resource2.URI("enterprise_project_id")
    projects = resource2.Body("projects")
    resource_types = resource2.Body("resource_types")
    resources = resource2.Body("resources")
    errors = resource2.Body("errors")
    total_count = resource2.Body("total_count")
class EnterpriseProjectResourceMigrate(resource2.Resource):
    """Define a EnterpriseProject class. get detail and update EP"""

    base_path = '/enterprise-projects/%(enterprise_project_id)s/resources-migrate'
    service = eps_service.EpsService()

    # Allow operation for this resource.
    # capabilities
    allow_create = True
    allow_list = False
    allow_get = False
    allow_update = False
    allow_delete = False
    enterprise_project_id = resource2.URI("enterprise_project_id")
    project_id = resource2.Body("project_id")
    cloud_resource_type = resource2.Body("resource_type")
    resource_id = resource2.Body("resource_id")

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
