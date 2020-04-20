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

from openstack import proxy2
from openstack.eps.v1 import enterprise_project as _ep


class Proxy(proxy2.BaseProxy):
    def update_enterprise_project(self, enterpriseProjectId, **attrs):
        """Update a enterprise_project.
        """
        return self._update(_ep.EnterpriseProjectUpdate, enterprise_project_id = enterpriseProjectId, **attrs)

    def get_enterprise_project(self, enterpriseProjectId):
        """get a enterprise_project.
        """
        return self._get(_ep.EnterpriseProjectDetail, enterprise_project_id = enterpriseProjectId)

    def enterprise_project_quotas(self):
        """quert enterprise_projects quotas.
        """
        return self._get(_ep.EnterpriseProjectQuotas)

    def list_enterprise_projects(self, **query):
        """list enterprise_projects.
        """
        return self._list(_ep.EnterpriseProject, **query)

    def create_enterprise_project(self, **attrs):
        """create a enterprise_project.
        """
        return self._create(_ep.EnterpriseProject, **attrs)

    def operate_enterprise_project(self, enterpriseProjectId, **attrs):
        """operate a enterprise_project.
        """
        return self._create(_ep.EnterpriseProjectAction, enterprise_project_id = enterpriseProjectId, **attrs)

    def filter_resource_enterprise_project(self, enterpriseProjectId, **attrs):
        """filter a enterprise_project resource.
        """
        return self._create(_ep.EnterpriseProjectResourceFilter, enterprise_project_id = enterpriseProjectId, **attrs)

    def migrate_resource_enterprise_project(self, enterpriseProjectId, **attrs):
        """migrate a enterprise_project resource.
        """
        return self._create(_ep.EnterpriseProjectResourceMigrate, enterprise_project_id = enterpriseProjectId, **attrs)