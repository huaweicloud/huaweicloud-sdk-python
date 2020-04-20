# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
#      Huawei has modified this source file.
#     
#         Copyright 2020 Huawei Technologies Co., Ltd.
#         
#         Licensed under the Apache License, Version 2.0 (the "License"); you may not
#         use this file except in compliance with the License. You may obtain a copy of
#         the License at
#         
#             http://www.apache.org/licenses/LICENSE-2.0
#         
#         Unless required by applicable law or agreed to in writing, software
#         distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#         WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#         License for the specific language governing permissions and limitations under
#         the License.

from openstack.identity import identity_service
from openstack import resource2 as resource, exceptions


class Authtoken(resource.Resource):
    resource_key = 'token'
    base_path = '/auth/tokens'
    service = identity_service.IdentityService()

    # capabilities
    allow_create = True
    allow_get = True

    x_subject_token = resource.Header("X-Subject-Token")

    _query_mapping = resource.QueryParameters("nocatalog")

    # Properties
    #: The identity of this token. *Type: dict*
    identity = resource.Body("identity", type=dict)
    #: The scope of this token. *Type: dict*
    scope = resource.Body("scope", type=dict)
    #: The catalog of this token. *Type: list*
    catalog = resource.Body("catalog", type=list)
    #: The domain of this token. *Type: dict*
    domain = resource.Body("domain", type=dict)
    #: The expires_at of this token. *Type: string*
    expires_at = resource.Body("expires_at")
    #: The issued_at of this token. *Type: string*
    issued_at = resource.Body("issued_at")
    #: The methods of this methods. *Type: list*
    methods = resource.Body("methods", type=list)
    #: The project of this token. *Type: dict*
    project = resource.Body("project", type=dict)
    #: The roles of this token. *Type: list*
    roles = resource.Body("roles", type=list)
    #: The user of this token. *Type: dict*
    user = resource.Body("user", type=dict)
    #: The assumed_by of this agency token. *Type: dict*
    assumed_by = resource.Body("assumed_by", type=dict)

    def create_authtoken(self, session, attr, nocatalog):
        endpoint_override = self.service.get_endpoint_override()
        if nocatalog is None:
            uri = self.base_path
        else:
            uri = self.base_path + "?nocatalog=" + nocatalog
        response = session.post(uri, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=attr)
        self._translate_response(response)
        return self

    def validate_authtoken(self, session, x_subject_token, nocatalog):
        if not self.allow_get:
            raise exceptions.MethodNotSupported(self, "get")

        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        if nocatalog is None:
            uri = self.base_path
        else:
            uri = self.base_path + "?nocatalog=" + nocatalog
        response = session.get(uri, endpoint_filter=self.service,
                               microversion=service.microversion, headers={"X-Subject-Token": x_subject_token},
                               endpoint_override=endpoint_override)
        self._translate_response(response)
        return self
