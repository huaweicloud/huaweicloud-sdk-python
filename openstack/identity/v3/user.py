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


class User(resource.Resource):
    resource_key = 'user'
    resources_key = 'users'
    base_path = '/users'
    service = identity_service.IdentityService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    patch_update = True

    # Properties
    #: References the user's default project ID against which to authorize,
    #: if the API user does not explicitly specify one when creating a token.
    #: Setting this attribute does not grant any actual authorization on the
    #: project, and is merely provided for the user's convenience.
    #: Therefore, the referenced project does not need to exist within the
    #: user's domain.
    #:
    #: *New in version 3.1* If the user does not have authorization to
    #: their default project, the default project will be ignored at token
    #: creation. *Type: string*
    default_project_id = resource.Body('default_project_id')
    #: The description of this user. *Type: string*
    description = resource.Body('description')
    #: References the domain ID which owns the user; if a domain ID is not
    #: specified by the client, the Identity service implementation will
    #: default it to the domain ID to which the client's token is scoped.
    #: *Type: string*
    domain_id = resource.Body('domain_id')
    #: The email of this user. *Type: string*
    email = resource.Body('email')
    #: Setting this value to ``False`` prevents the user from authenticating or
    #: receiving authorization. Additionally, all pre-existing tokens held by
    #: the user are immediately invalidated. Re-enabling a user does not
    #: re-enable pre-existing tokens. *Type: bool*
    is_enabled = resource.Body('enabled', type=bool)
    #: The links for the user resource.
    links = resource.Body('links' ,type=dict)
    #: Unique user name, within the owning domain. *Type: string*
    name = resource.Body('name')
    #: The default form of credential used during authentication. *Type: string*
    password = resource.Body('password')
    #: The date and time when the pasword expires. The time zone is UTC.
    #: A None value means the password never expires.
    #: This is a response object attribute, not valid for requests.
    #: *New in version 3.7*
    password_expires_at = resource.Body('password_expires_at')
    #: The status of the password, true: need modify, false: normal. *Type: bool*
    pwd_status = resource.Body('pwd_status', type=bool)
    #: The password strength of the user. *Type: string*
    pwd_strength = resource.Body('pwd_strength')
    #: The mobile number of the user. *Type: string*
    mobile = resource.Body('mobile')
    #: The flag indicates whether the user should reset the password when login next time. *Type: bool*
    force_reset_pwd = resource.Body('forceResetPwd', type=bool)
    #: The id of the project that the user request before log out. *Type: string*
    last_project_id = resource.Body('last_project_id')

    def change_password(self, session, user_id, **attrs):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin(self.base_path, user_id, 'password')
        response = session.post(uri, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=attrs)
        return response.status_code == 204

    def remove_user_from_group(self, session, group_id, user_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin('groups', group_id, 'users', user_id)
        response = session.delete(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        return response.status_code == 204


class GroupUser(User):
    base_path = "/groups/%(group_id)s/users"
