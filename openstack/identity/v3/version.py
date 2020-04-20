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
from openstack import resource2 as resource


class Version(resource.Resource):
    resource_key = 'version'
    service = identity_service.IdentityService()

    # capabilities
    allow_get = True

    # Properties
    #: The media_types of version. *Type: list*
    media_types = resource.Body('media-types', type=list)
    #: The status of version. *Type: string*
    status = resource.Body('status')
    #: The updated of version. *Type: string*
    updated = resource.Body('updated')
    #: The updated of version. *Type: dict*
    links = resource.Body('links', type=dict)
    #: The id of version. *Type: id*
    id = resource.Body('id')

    def get_version3_of_keystone(self, session):
        endpoint_override = self.service.get_endpoint_override()
        endpoint = session.get_endpoint(service_type=self.service.service_type)
        response = session.get(url=endpoint, endpoint_filter=self.service, endpoint_override=endpoint_override)
        self._translate_response(response)
        return self


class Versions(resource.Resource):
    resource_key = 'versions'
    service = identity_service.IdentityService()

    # capabilities
    allow_get = True

    # Properties
    #: The values of version. *Type: list*
    values = resource.Body('values', type=list)

    def get_version_of_keystone(self, session):
        endpoint = session.get_endpoint(service_type=self.service.service_type).rstrip("v3")
        endpoint_override = self.service.get_endpoint_override()
        response = session.get(url=endpoint, endpoint_filter=self.service, endpoint_override=endpoint_override)
        self._translate_response(response)
        return self
