# -*- coding:utf-8 -*-
# Copyright 2020 Huawei Technologies Co.,Ltd.
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


from openstack.iam import iam_service
from openstack import resource2
from openstack import utils


class User(resource2.Resource):
    resource_key = 'user'
    resources_key = 'users'
    base_path = '/OS-USER/users'
    service = iam_service.IamService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    patch_update = True

    # Properties
    #: The areacode of mobile. *Type: string*
    areacode = resource2.Body('areacode')
    #: The create_time of user. *Type: string*
    create_time = resource2.Body('create_time')
    #: The default_project_id of user. *Type: string*
    default_project_id = resource2.Body('default_project_id')
    #: The description of user. *Type: string*
    description = resource2.Body('description')
    #: The domain_id of user. *Type: string*
    domain_id = resource2.Body('domain_id')
    #: The update_time of user. *Type: string*
    update_time = resource2.Body('update_time')
    #: The email of user. *Type: string*
    email = resource2.Body('email')
    #: The mobile of user. *Type: string*
    mobile = resource2.Body('mobile')
    #: The enabled of user. *Type: bool*
    is_enabled = resource2.Body('enabled', type=bool)
    #: The id of user. *Type: string*
    id = resource2.Body('id')
    #: The is_domain_owner of user. *Type: bool*
    is_domain_owner = resource2.Body('is_domain_owner', type=bool)
    #: The name of user. *Type: string*
    name = resource2.Body('name')
    #: The password_expires_at of user. *Type: string*
    password_expires_at = resource2.Body('password_expires_at')
    #: The phone of user. *Type: string*
    phone = resource2.Body('phone')
    #: The phone of user. *Type: dict*
    links = resource2.Body('links', type=dict)
    #: The pwd_status of user. *Type: bool*
    pwd_status = resource2.Body('pwd_status', type=bool)
    #: The status of user. *Type: int*
    status = resource2.Body('status', type=int)
    #: The xdomain_id of user. *Type: string*
    xdomain_id = resource2.Body('xdomain_id')
    #: The xdomain_type of user. *Type: string*
    xdomain_type = resource2.Body('xdomain_type')
    #: The xuser_id of user. *Type: string*
    xuser_id = resource2.Body('xuser_id')
    #: The xuser_type of user. *Type: string*
    xuser_type = resource2.Body('xuser_type')

    def query_user_details(self, session, user_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin(self.base_path, user_id)
        response = session.get(uri, endpoint_filter=self.service, endpoint_override=endpoint_override)
        self._translate_response(response)
        return self

    def create_user(self, session, **user):
        endpoint_override = self.service.get_endpoint_override()
        uri = self.base_path
        response = session.post(uri, endpoint_filter=self.service, endpoint_override=endpoint_override, json=user)
        self._translate_response(response)
        return self

    def update_user_information(self, session, user_id, **user):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin(self.base_path, user_id, 'info')
        response = session.put(uri, endpoint_filter=self.service, endpoint_override=endpoint_override, json=user)
        return response.status_code == 204

    def update_user_information_by_admin(self, session, user_id, **user):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin(self.base_path, user_id)
        response = session.put(uri, endpoint_filter=self.service, endpoint_override=endpoint_override, json=user)
        self._translate_response(response)
        return self
