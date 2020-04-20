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


class Credential(resource2.Resource):
    resource_key = 'credential'
    resources_key = 'credentials'
    base_path = '/OS-CREDENTIAL/credentials'
    service = iam_service.IamService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource2.QueryParameters('user_id')

    # Properties
    #: The last_use_time of the credential.
    last_use_time = resource2.Body('last_use_time')
    #: The accesskey of the credential.
    access = resource2.Body('access')
    #: The create_time of the credential.
    create_time = resource2.Body('create_time')
    #: The user_id of the credential.
    user_id = resource2.Body('user_id')
    #: The description key of the credential.
    description = resource2.Body('description')
    #: The status key of the credential.
    status = resource2.Body('status')
    #: The secret key of the credential.
    secret = resource2.Body('secret')

    def get_credential(self, session, access_key):
        endpoint_override = self.service.get_endpoint_override()
        url = utils.urljoin(self.base_path, access_key)
        response = session.get(url, endpoint_filter=self.service,
                               endpoint_override=endpoint_override)
        self._translate_response(response)
        return self

    def update_credential(self, session, access_key, **attrs):
        endpoint_override = self.service.get_endpoint_override()
        url = utils.urljoin(self.base_path, access_key)
        response = session.put(url, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=attrs)
        self._translate_response(response)
        return self
