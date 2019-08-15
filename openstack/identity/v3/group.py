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
#         Copyright 2018 Huawei Technologies Co., Ltd.
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
from openstack import utils


class Group(resource.Resource):
    resource_key = 'group'
    resources_key = 'groups'
    base_path = '/groups'
    service = identity_service.IdentityService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    patch_update = True

    # Properties
    #: The description of this group. *Type: string*
    description = resource.Body('description')
    #: References the domain ID which owns the group; if a domain ID is not
    #: specified by the client, the Identity service implementation will
    #: default it to the domain ID to which the client's token is scoped.
    #: *Type: string*
    domain_id = resource.Body('domain_id')
    #: Unique group name, within the owning domain. *Type: string*
    name = resource.Body('name')
    #: The links for the service resource.
    links = resource.Body('links', type=dict)
    #: The time that the group created. *Type: string*
    create_time = resource.Body('create_time')

    def add_user_to_group(self, session, group_id, user_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin(self.base_path, group_id, 'users',user_id)
        response = session.put(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        return response.status_code == 204

    def check_group_user(self, session, group_id, user_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin(self.base_path, group_id, 'users', user_id)
        response = session.head(uri, endpoint_filter=self.service, endpoint_override=endpoint_override)
        return response.status_code == 204


class UserGroup(Group):
    base_path = "/users/%(user_id)s/groups"


