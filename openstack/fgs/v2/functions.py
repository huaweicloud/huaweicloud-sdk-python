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

from openstack.fgs import fgs_service
from openstack import resource2 as resource
from openstack import exceptions


class Function(resource.Resource):
    resources_key = 'functions'
    base_path = '/fgs/functions'
    service = fgs_service.FGSService()

    # capabilities
    allow_create = True
    allow_list = True
    allow_get = False
    allow_update = False
    allow_delete = False

    # noinspection SpellCheckingInspection
    _query_mapping = resource.QueryParameters("maxitems")

    #: Properties
    #: Function name. 
    func_name = resource.Body('func_name')
    #:  Group to which the function belongs. This field is defined to group functions.
    package = resource.Body('package')
    #:  Function code type
    code_type = resource.Body('code_type')
    # Address of the function code package in OBS when CodeType is set to obs,
    #   or blank when CodeType is set to another value. ;
    code_url = resource.Body('code_url')
    #:  Description of the function.
    description = resource.Body('description')
    #:  Name of the function file.
    code_filename = resource.Body('code_filename')
    #:  Entry point of the function.
    handler = resource.Body('handler')
    #:  Memory size (MB) allocated to the function.
    memory_size = resource.Body('memory_size', type=int)
    #:  Environment for executing the function.
    runtime = resource.Body('runtime')
    #:  Timeout duration (3s to 900s) for executing the function.
    timeout = resource.Body('timeout', type=int)
    #:  Name/Value information defined for the function.
    user_data = resource.Body('user_data')
    #:  Agency used by the function.
    # noinspection SpellCheckingInspection,SpellCheckingInspection
    xrole = resource.Body('xrole')
    #:  Agency used by the function.
    # noinspection SpellCheckingInspection
    app_xrole = resource.Body('app_xrole')
    #:  The url address of the third-party software zip package used by the function on the obs.
    dependency_pkg = resource.Body('dependency_pkg')
    #:  Function code, need to be base64 encoded.
    func_code = resource.Body('func_code')
    #:  URN of a function.
    func_urn = resource.Body('func_urn')

    # name of tenant
    user_domain = resource.Body("user_domain")
    # project id of tenant
    domain_id = resource.Body("domain_id")
    # namespace of tenant
    namespace = resource.Body("namespace")
    # project name id of tenant
    project_name = resource.Body("project_name")
    # Cpu resource occupied by the function, the unit is millicore
    cpu = resource.Body("cpu", type=int)
    # Function size in bytes.
    code_size = resource.Body("code_size")
    #: Function digest .
    digest = resource.Body("digest")
    #: Function version .
    version = resource.Body('version')
    #: The internal ID of the function version.
    image_name = resource.Body('image_name')
    #: Function version description.
    version_description = resource.Body('version_description')
    #: Last update time of the function.
    last_modified = resource.Body('last_modified')
    #: Vpc configuration.
    func_vpc = resource.Body('func_vpc')
    #: Function enable flag
    concurrency = resource.Body('concurrency')
    #: Dependency package list
    depend_list = resource.Body('depend_list')
    #: Function policy configuration
    strategy_config = resource.Body('strategy_config')
    #: Function extension configuration
    extend_config = resource.Body('extend_config')
    #: Dependency code package
    dependencies = resource.Body('dependencies')
    #: Function initialization entry
    initializer_handler = resource.Body('initializer_handler')
    #: Function initialization time
    initializer_timeout = resource.Body('initializer_timeout')
    #: Function next_marker
    next_marker = resource.Body('next_marker')

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

        request = self._prepare_request(requires_id=False)

        endpoint_override = self.service.get_endpoint_override()
        response = session.delete(request.uri, endpoint_filter=self.service,
                                  endpoint_override=endpoint_override,
                                  headers={"Accept": ""},
                                  params=params)

        self._translate_response(response, has_body=has_body)
        return self

    def update(self, session, prepend_key=True, has_body=True):
        """Update the remote resource based on this instance.

        :param has_body: DELETE operations don't return a body, so only try to work
        with a body when has_body is True.
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
        # noinspection PyProtectedMember
        self._body._dirty.discard("id")
        id_mapping_name = self._body_mapping()["id"]
        self._body._dirty.discard(id_mapping_name)

        # Only try to update if we actually have anything to update.
        if not any([self._body.dirty, self._header.dirty]):
            return self

        if not self.allow_update:
            raise exceptions.MethodNotSupported(self, "update")

        request = self._prepare_request(requires_id=False, prepend_key=prepend_key)

        endpoint_override = self.service.get_endpoint_override()
        if self.patch_update:
            response = session.patch(request.uri, endpoint_filter=self.service,
                                     endpoint_override=endpoint_override,
                                     json=request.body,
                                     headers=request.headers)
        else:
            response = session.put(request.uri, endpoint_filter=self.service,
                                   endpoint_override=endpoint_override,
                                   json=request.body, headers=request.headers)

        self._translate_response(response, has_body=has_body)
        return self


class FunctionExpansion(Function):
    base_path = '/fgs/functions/%(function_urn)s'
    function_urn = resource.URI('function_urn')

    # capabilities
    allow_create = False
    allow_list = False
    allow_delete = True


class FunctionInvocations(Function):
    #: requestId for API2.0
    requestId = resource.Body('requestId')
    #: requestId for API1.0
    request_id = resource.Body('request_id')
    #: result of invocations
    result = resource.Body('result')
    #: log of invocations
    log = resource.Body('log')
    #: status of invocations
    status = resource.Body('status')

    base_path = '/fgs/functions/%(function_urn)s/invocations'
    function_urn = resource.URI('function_urn')

    # capabilities
    allow_list = False

    def create(self, session, prepend_key=True, **attrs):
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
        request.body = attrs
        request.headers = {"Accept": "*/*",
                           "Content-type": "application/json;charset=UTF-8",
                           "x-cf2-passthrough": "true",
                           "x-cff-log-type": "tail",
                           "x-cff-request-version": "v1"
                           }
        response = session.post(request.uri, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=request.body, headers=request.headers)

        self._translate_response(response)
        return self


class FunctionInvocationsAsync(FunctionInvocations):
    base_path = '/fgs/functions/%(function_urn)s/invocations-async'
    function_urn = resource.URI('function_urn')

    # capabilities
    allow_list = False


class FunctionMetadata(Function):
    base_path = '/fgs/functions/%(function_urn)s/config'
    function_urn = resource.URI('function_urn')

    # capabilities
    allow_create = False
    allow_list = False
    allow_get = True
    allow_update = True


class FunctionCode(Function):
    base_path = '/fgs/functions/%(function_urn)s/code'
    function_urn = resource.URI('function_urn')

    # capabilities
    allow_create = False
    allow_list = False
    allow_get = True
    allow_update = True


class FunctionVersion(Function):
    base_path = '/fgs/functions/%(function_urn)s/versions'
    function_urn = resource.URI('function_urn')
    resources_key = 'versions'

    # capabilities
    put_create = False

    #: Function version . 
    version = resource.Body('version')
    #: Function digest . 
    digest = resource.Body('digest')
    #: Function next_marker
    next_marker = resource.Body('next_marker')


class FunctionAliase(Function):
    base_path = '/fgs/functions/%(function_urn)s/aliases'
    function_urn = resource.URI('function_urn')
    resources_key = None

    # capabilities
    allow_get = True
    put_create = False

    #: Function alias. 
    name = resource.Body('name')
    #: Function version . 
    version = resource.Body('version')
    #: Function alias_urn .
    alias_urn = resource.Body('alias_urn')
    #: Function additional_version_weights .
    additional_version_weights = resource.Body('additional_version_weights')


class FunctionAliaseExpansion(FunctionAliase):
    base_path = '/fgs/functions/%(function_urn)s/aliases/%(alias_name)s'
    function_urn = resource.URI('function_urn')
    alias_name = resource.URI('alias_name')

    # capabilities
    allow_create = False
    allow_list = False
    allow_update = True
    allow_delete = True
