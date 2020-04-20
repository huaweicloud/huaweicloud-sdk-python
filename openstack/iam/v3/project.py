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

from openstack.iam import iam_service
from openstack import resource2
from openstack import utils


class Project(resource2.Resource):
    resource_key = 'project'
    resources_key = 'projects'
    base_path = '/v3-ext/projects'
    service = iam_service.IamService()

    # capabilities
    allow_get = True
    allow_update = True

    _query_mapping = resource2.QueryParameters('domain_id', 'enabled', 'is_domain', 'name', 'page', 'parent_id',
                                               'per_page')
    # Properties
    #: The description of the project. *Type: string*
    description = resource2.Body('description')
    #: References the domain ID which owns the project; if a domain ID is not
    #: specified by the client, the Identity service implementation will
    #: default it to the domain ID to which the client's token is scoped.
    #: *Type: string*
    domain_id = resource2.Body('domain_id', type=bool)
    #: Indicates whether the project also acts as a domain. If set to True,
    #: the project acts as both a project and a domain. Default is False.
    #: New in version 3.6
    is_domain = resource2.Body('is_domain', type=bool)
    #: Setting this attribute to ``False`` prevents users from authorizing
    #: against this project. Additionally, all pre-existing tokens authorized
    #: for the project are immediately invalidated. Re-enabling a project
    #: does not re-enable pre-existing tokens. *Type: bool*
    is_enabled = resource2.Body('enabled', type=bool)
    #: Unique project name, within the owning domain. *Type: string*
    name = resource2.Body('name')
    #: The ID of the parent of the project.
    #: New in version 3.4
    parent_id = resource2.Body('parent_id')
    #: The links of the parent of the project.
    links = resource2.Body('links', type=dict)
    #: The ID of the of the project.
    id = resource2.Body('id')
    #: The status of the of the project.
    status = resource2.Body('status')

    def update_project_status(self, session, project_id, project):
        endpoint = session.get_endpoint(service_type=self.service.service_type).rstrip("v3.0")
        url = utils.urljoin(endpoint, self.base_path, project_id)
        endpoint_override = self.service.get_endpoint_override()
        resp = session.put(url, endpoint_filter=self.service, endpoint_override=endpoint_override, json=project)
        if resp.status_code == 204:
            return True
        return False

    def get_project_details_and_status(self, session, project_id):
        endpoint = session.get_endpoint(service_type=self.service.service_type).rstrip("v3.0")
        url = utils.urljoin(endpoint, self.base_path, project_id)
        endpoint_override = self.service.get_endpoint_override()
        resp = session.get(url, endpoint_filter=self.service, endpoint_override=endpoint_override)
        self._translate_response(resp)
        return self
