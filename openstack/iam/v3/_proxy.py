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

from openstack import proxy2
from openstack.iam.v3 import securitytoken as _securitytoken
from openstack.iam.v3 import user as _user
from openstack.iam.v3 import project as _project
from openstack.iam.v3 import credential as _credential
from openstack.iam.v3 import customrole as _customrole
from openstack.iam.v3 import agency as _agency


class Proxy(proxy2.BaseProxy):

    # def create_securitytoken(self, **attrs):
    #     """Create a new securitytoken
    #
    #     :param dict attrs: Keyword arguments which will be used to create
    #                        a :class:`~openstack.iam.v3.securitytoken.Securitytoken`.
    #                        Please follow the API reference to get the request body.
    #
    #     :returns: The results of securitytoken creation
    #     :rtype: :class:`~openstack.iam.v3.iam.Securitytoken`
    #     """
    #     return self._create(_securitytoken.Securitytoken, **attrs)

    def create_securitytoken(self, **attrs):
        """
        Retrieve a generator of servers.
        :param attrs: An Auth entity
        :return: A generator of server instances.
        """
        res = self._get_resource(_securitytoken.Securitytoken, None)
        return res.create(self._session, **attrs)

    def update_project_status(self, project_id, attrs):
        """
        Update status of the project.
        :param attrs: An project entity.
        :return: A boolean indicator.
        """
        res = self._get_resource(_project.Project, None)
        return res.update_project_status(self._session, project_id, attrs)

    def get_project_details_and_status(self, project_id):
        """
        get project details and status.
        :param attrs: An project id.
        :returns: One :class:`~openstack.iam.v3.project.Project`
        """
        res = self._get_resource(_project.Project, None)
        return res.get_project_details_and_status(self._session, project_id)

    def query_user_details(self, user_id):
        """
        get user details.
        :param user_id: a user id.
        :returns: One :class:`~openstack.iam.v3.user.User`
        """
        res = self._get_resource(_user.User, None)
        return res.query_user_details(self._session, user_id)

    def create_user(self, **user):
        """
        create user.
        :param user: a user entity.
        :returns: One :class:`~openstack.iam.v3.user.User`
        """
        res = self._get_resource(_user.User, None)
        return res.create_user(self._session, **user)

    def update_user_information(self, user_id, **user):
        """
        update user information.
        :param user_id: a user id.
        :param user: a user entity.
        :return: A boolean indicator.
        """
        res = self._get_resource(_user.User, None)
        return res.update_user_information(self._session, user_id, **user)

    def update_user_information_by_admin(self, user_id, **user):
        """
        update user information by admin.
        :param user_id: a user id.
        :param user: a user entity.
        :returns: One :class:`~openstack.iam.v3.user.User`
        """
        res = self._get_resource(_user.User, None)
        return res.update_user_information_by_admin(self._session, user_id, **user)

    def create_credential(self, **attrs):
        """Create a new credential

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.iam.v3.credential.Credential`,
                           comprised of the properties on the Credential class.

        :returns: The results of credential creation.
        :rtype: :class:`~openstack.iam.v3.credential.Credential`
        """
        return self._create(_credential.Credential, **attrs)

    def credentials(self, **query):
        """Retrieve a generator of credentials

        :return: A generator of credential instances.
        :rtype: :class:`~openstack.iam.v3.credential.Credential`
        """
        return self._list(_credential.Credential, **query)

    def get_credential(self, access_key):
        """Get a single credential

        :param access_key: the access_key.

        :returns: One :class:`~openstack.iam.v3.credential.Credential`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no matching credential can be found.
        """
        res = self._get_resource(_credential.Credential, None)
        return res.get_credential(self._session, access_key)

    def update_credential(self, access_key, **attrs):
        """Update a credential

        :param access_key: the access_key

        :returns: The updated credential.
        :rtype: :class:`~openstack.iam.v3.credential.Credential`
        """
        res = self._get_resource(_credential.Credential, None)
        return res.update_credential(self._session, access_key, **attrs)

    def delete_credential(self, access_key):
        """Delete a credential

        :param access_key: the access_key

        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the role does not exist.
                    When set to ``True``, no exception will be thrown when
                    attempting to delete a nonexistent credential.

        :returns: ``None``
        """
        self._delete(_credential.Credential, access_key, ignore_missing=True)

    def custom_roles(self):
        """Retrieve a generator of custom roles

        :return: A generator of customrole instances.
        :rtype: :class:`~openstack.iam.v3.customrole.Customrole`
        """
        return self._list(_customrole.Customrole, paginated=False)

    def get_custom_role(self, role_id):
        """Get a single custom role

        :param role_id: The ID of a custom role

        :returns: One :class:`~openstack.iam.v3.customrole.Customrole`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no matching customrole can be found.
        """
        return self._get(_customrole.Customrole, role_id)

    def create_custom_role(self, **attrs):
        """Create a new customrole from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.iam.v3.customrole.customrole`,
                           comprised of the properties on the Customrole class.

        :returns: The results of customrole creation.
        :rtype: :class:`~openstack.iam.v3.customrole.customrole`
        """
        return self._create(_customrole.Customrole, **attrs)

    def update_custom_role(self, role_id, **attrs):
        """Update a customrole

        :param customrole_id: Either the ID of a customrole.
        :param dict kwargs: The attributes to update on the customrole represented
                       by ``value``. Only name can be updated

        :returns: The updated customrole.
        :rtype: :class:`~openstack.iam.v3.customrole.Customrole`
        """
        return self._update(_customrole.Customrole, role_id, **attrs)

    def delete_custom_role(self, role_id, ignore_missing=True):
        """Delete a customrole

        :param customrole_id: Te ID of a customrole
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the customrole does not exist.
                    When set to ``True``, no exception will be thrown when
                    attempting to delete a nonexistent customrole.

        :returns: ``None``
        """
        self._delete(_customrole.Customrole, role_id, ignore_missing=ignore_missing)

    def agencies(self, **query):
        """Retrieve a generator of agencies

        :return: A generator of agency instances.
        :rtype: :class:`~openstack.iam.v3.agency.Agency`
        """
        return self._list(_agency.Agency, **query)

    def get_agency(self, agency_id):
        """Get a single agency

        :param agency_id: the agency_id.

        :returns: One :class:`~openstack.iam.v3.agency.Agency`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no matching agency can be found.
        """
        return self._get(_agency.Agency, agency_id)

    def create_agency(self, **attrs):
        """Create a new agency

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.iam.v3.agency.Agency`,
                           comprised of the properties on the Agency class.

        :returns: The results of agency creation.
        :rtype: :class:`~openstack.iam.v3.agency.Agency`
        """
        return self._create(_agency.Agency, **attrs)

    def update_agency(self, agency_id, **attrs):
        """Update an agency

        :param agency_id: the id of agency

        :returns: The updated agency.
        :rtype: :class:`~openstack.iam.v3.agency.Agency`
        """
        res = self._get_resource(_agency.Agency, None)
        return res.update_agency(self._session, agency_id, **attrs)

    def delete_agency(self, agency_id):
        """Delete an agency

        :param agency_id: the id of agency

        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the role does not exist.
                    When set to ``True``, no exception will be thrown when
                    attempting to delete a nonexistent agency.

        :returns: ``None``
        """
        self._delete(_agency.Agency, agency_id, ignore_missing=True)

    def list_domain_agency_role(self, domain_id, agency_id):
        """Querying domain permissions of an agency.

        :param domain_id: the id of the domain.
        :param agency_id: the id of the agency.

        :return: A generator of role instances.
        """
        return self._list(_agency.DomainAgencyRole, domain_id=domain_id, agency_id=agency_id)

    def list_project_agency_role(self, project_id, agency_id):
        """Querying  project permissions of an agency.

        :param project_id: the id of the project.
        :param agency_id: the id of the agency.

        :return: A generator of role instances.
        """
        return self._list(_agency.ProjectAgencyRole, project_id=project_id, agency_id=agency_id)

    def grant_domain_agency_role(self, domain_id, agency_id, role_id):
        """Granting permissions to a user agency of a domain.

        :param domain_id: the id of the domain.
        :param agency_id: the id of the agency.
        :param role_id: the id of the role.

        :return: A boolean indicator.
        """
        res = self._get_resource(_agency.Agency, None)
        return res.grant_domain_agency_role(self._session, domain_id, agency_id, role_id)

    def grant_project_agency_role(self, project_id, agency_id, role_id):
        """Granting permissions to a user agency of a project.

        :param project_id: the id of the project.
        :param agency_id: the id of the agency.
        :param role_id: the id of the role.

        :return: A boolean indicator.
        """
        res = self._get_resource(_agency.Agency, None)
        return res.grant_project_agency_role(self._session, project_id, agency_id, role_id)

    def check_domain_agency_role(self, domain_id, agency_id, role_id):
        """Querying whether a user agency under a domain has specific permissions.

        :param domain_id: the id of the domain.
        :param agency_id: the id of the agency.
        :param role_id: the id of the role.

        :return: A boolean indicator.
        """
        res = self._get_resource(_agency.Agency, None)
        return res.check_domain_agency_role(self._session, domain_id, agency_id, role_id)

    def check_project_agency_role(self, project_id, agency_id, role_id):
        """Querying whether a user agency under a project has specific permissions.

        :param project_id: the id of the project.
        :param agency_id: the id of the agency.
        :param role_id: the id of the role.

        :return: A boolean indicator.
        """
        res = self._get_resource(_agency.Agency, None)
        return res.check_project_agency_role(self._session, project_id, agency_id, role_id)

    def delete_domain_agency_role(self, domain_id, agency_id, role_id):
        """Deleting Permissions of a User Group of a Domain.

        :param domain_id: the id of the domain.
        :param agency_id: the id of the agency.
        :param role_id: the id of the role.

        :return: A boolean indicator.
        """
        res = self._get_resource(_agency.Agency, None)
        return res.delete_domain_agency_role(self._session, domain_id, agency_id, role_id)

    def delete_project_agency_role(self, project_id, agency_id, role_id):
        """Deleting permissions to a user agency of a project.

        :param project_id: the id of the project.
        :param agency_id: the id of the agency.
        :param role_id: the id of the role.

        :return: A boolean indicator.
        """
        res = self._get_resource(_agency.Agency, None)
        return res.delete_project_agency_role(self._session, project_id, agency_id, role_id)
