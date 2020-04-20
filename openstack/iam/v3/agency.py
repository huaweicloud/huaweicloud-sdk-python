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

from openstack.identity.v3 import role
from openstack.iam import iam_service
from openstack import resource2
from openstack import utils


class Agency(resource2.Resource):
    resource_key = 'agency'
    resources_key = 'agencies'
    base_path = '/OS-AGENCY/agencies'
    service = iam_service.IamService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource2.QueryParameters(
        'name', 'domain_id', "trust_domain_id")

    # Properties
    #: The create_time of the agency. *Type: string*
    create_time = resource2.Body('create_time')
    #: The description of the agency. *Type: string*
    description = resource2.Body('description')
    #: The domain_id of the agency. *Type: string*
    domain_id = resource2.Body('domain_id')
    #: The duration of the agency. *Type: string*
    duration = resource2.Body('duration')
    #: The expire_time of the agency. *Type: string*
    expire_time = resource2.Body('expire_time')
    #: The id of the agency. *Type: string*
    id = resource2.Body('id')
    #: The name of the agency. *Type: string*
    name = resource2.Body('name')
    #: The trust_domain_id of the agency. *Type: string*
    trust_domain_id = resource2.Body('trust_domain_id')
    #: The trust_domain_name of the agency. *Type: string*
    trust_domain_name = resource2.Body('trust_domain_name')

    def update_agency(self, session, agency_id, **attrs):
        endpoint_override = self.service.get_endpoint_override()
        url = utils.urljoin(self.base_path, agency_id)
        response = session.put(url, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=attrs)
        self._translate_response(response)
        return self

    def grant_domain_agency_role(self, session, domain_id, agency_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin("OS-AGENCY", 'domains', domain_id, 'agencies', agency_id, 'roles', role_id)
        response = session.put(uri, endpoint_filter=self.service, endpoint_override=endpoint_override, raise_exc=False)
        return response.status_code == 204

    def grant_project_agency_role(self, session, project_id, agency_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin("OS-AGENCY", 'projects', project_id, 'agencies', agency_id, 'roles', role_id)
        response = session.put(uri, endpoint_filter=self.service, endpoint_override=endpoint_override, raise_exc=False)
        return response.status_code == 204

    def check_domain_agency_role(self, session, domain_id, agency_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin("OS-AGENCY", 'domains', domain_id, 'agencies', agency_id, 'roles', role_id)
        response = session.head(uri, endpoint_filter=self.service, endpoint_override=endpoint_override, raise_exc=False)
        return response.status_code == 204

    def check_project_agency_role(self, session, project_id, agency_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin("OS-AGENCY", 'projects', project_id, 'agencies', agency_id, 'roles', role_id)
        response = session.head(uri, endpoint_filter=self.service, endpoint_override=endpoint_override, raise_exc=False)
        return response.status_code == 204

    def delete_domain_agency_role(self, session, domain_id, agency_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin("OS-AGENCY", 'domains', domain_id, 'agencies', agency_id, 'roles', role_id)
        response = session.delete(uri, endpoint_filter=self.service, endpoint_override=endpoint_override,
                                  raise_exc=False)
        return response.status_code == 204

    def delete_project_agency_role(self, session, project_id, agency_id, role_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin("OS-AGENCY", 'projects', project_id, 'agencies', agency_id, 'roles', role_id)
        response = session.delete(uri, endpoint_filter=self.service, endpoint_override=endpoint_override,
                                  raise_exc=False)
        return response.status_code == 204


class DomainAgencyRole(role.Role):
    base_path = "/OS-AGENCY/domains/%(domain_id)s/agencies/%(agency_id)s/roles"
    service = iam_service.IamService()


class ProjectAgencyRole(role.Role):
    base_path = "/OS-AGENCY/projects/%(project_id)s/agencies/%(agency_id)s/roles"
    service = iam_service.IamService()
