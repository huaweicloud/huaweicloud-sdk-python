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

from openstack.identity import identity_service
from openstack import resource2
from openstack import utils


class PasswordConfig(resource2.Resource):
    resource_key = 'config'
    resources_key = None
    base_path = '/domains'
    service = identity_service.IdentityService()

    allow_get = True

    #: The endpoints of the catalog.
    security_compliance = resource2.Body('security_compliance')
    #: The type of the catalog.
    password_regex = resource2.Body('password_regex')
    #: The regex description of the password config
    password_regex_description = resource2.Body('password_regex_description')

    def get(self, session, domain_id):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin(self.base_path, domain_id, 'config', 'security_compliance')
        response = session.get(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        self._translate_response(response)
        return self

    def get_by_option(self, session, domain_id, option):
        endpoint_override = self.service.get_endpoint_override()
        uri = utils.urljoin(self.base_path, domain_id, 'config', 'security_compliance', option)
        response = session.get(uri, endpoint_filter=self.service,endpoint_override=endpoint_override)
        self._translate_response(response)
        return self
