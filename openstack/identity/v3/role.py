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


class Role(resource.Resource):
    resource_key = 'role'
    resources_key = 'roles'
    base_path = '/roles'
    service = identity_service.IdentityService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource.QueryParameters(
        'name', 'domain_id')

    # Properties
    #: Unique role name, within the owning domain. *Type: string*
    name = resource.Body('name')
    #: The links for the service resource.
    links = resource.Body('links', type=dict)
    #: The id of the domain that the role belongs to. *Type: string*
    domain_id = resource.Body('domain_id')
    #: The display type of the role. *Type: string*
    type = resource.Body('type')
    #: The display name of the role. *Type: string*
    display_name = resource.Body('display_name')
    #: The catalog of the role. *Type: string*
    catalog = resource.Body('catalog')
    #: The policy of the role.
    policy = resource.Body('policy', type=dict)
    #: The description of the role. *Type: string*
    description = resource.Body('description')

    def grant_domain_group_role(self, session, domain_id, group_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin('domains', domain_id, 'groups',group_id, 'roles', role_id)
        response = session.put(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        return response.status_code == 204

    def grant_project_group_role(self, session, project_id, group_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin('projects', project_id, 'groups',group_id, 'roles', role_id)
        response = session.put(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        return response.status_code == 204

    def delete_domain_group_role(self, session, domain_id, group_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin('domains', domain_id, 'groups',group_id, 'roles', role_id)
        response = session.delete(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        return response.status_code == 204

    def delete_project_group_role(self, session, project_id, group_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin('projects', project_id, 'groups',group_id, 'roles', role_id)
        response = session.delete(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        return response.status_code == 204

    def check_domain_group_role(self, session, domain_id, group_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin('domains', domain_id, 'groups',group_id, 'roles', role_id)
        response = session.head(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        return response.status_code == 204

    def check_project_group_role(self, session, project_id, group_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin('projects', project_id, 'groups', group_id, 'roles', role_id)
        response = session.head(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        return response.status_code == 204


class DomainGroupRole(Role):
    base_path = "/domains/%(domain_id)s/groups/%(group_id)s/roles"


class ProjectGroupRole(Role):
    base_path = "/projects/%(project_id)s/groups/%(group_id)s/roles"

