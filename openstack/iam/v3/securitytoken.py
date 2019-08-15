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

from openstack.iam import iam_service
from openstack import resource2


class Securitytoken(resource2.Resource):
    resource_key = 'credential'
    resources_key = 'credentials'
    base_path = '/OS-CREDENTIAL/securitytokens'
    service = iam_service.IamService()

    #: The access key of the securitytoken.
    access = resource2.Body('access')
    #: The secret key of the securitytoken.
    secret = resource2.Body('secret')
    #: The expire time of the securitytoken.
    expires_at = resource2.Body('expires_at')
    #: The securitytoken of the securitytoken.
    securitytoken = resource2.Body('securitytoken')

    def create(self, session, **attrs):
        endpoint_override = self.service.get_endpoint_override()
        uri = self.base_path
        response = session.post(uri, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=attrs)
        self._translate_response(response)
        return self
