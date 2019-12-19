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

from openstack.bssintl import bss_intl_service
from openstack import resource2


class SendVerificationcode(resource2.Resource):
    base_path = "%(domain_id)s/partner/common-mgr/verificationcode"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')

    # request
    receiverType = resource2.Body('receiverType', type=int)
    timeout = resource2.Body('timeout', type=int)
    # Email address.
    email = resource2.Body('email')
    mobilePhone = resource2.Body('mobilePhone')
    countryCode = resource2.Body('countryCode')
    # language
    lang = resource2.Body('lang')
    scene = resource2.Body('scene')
    # Customer ID.
    customerId = resource2.Body('customerId')

    def create(self, session, prepend_key=True):
        endpoint_override = self.service.get_endpoint_override()
        request = self._prepare_request(requires_id=False,
                                        prepend_key=prepend_key)
        response = session.post(request.uri, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=request.body, headers=request.headers)
        if (response.status_code == 204):
            return self
        self._translate_response(response)
        return self
