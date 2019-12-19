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
from openstack import utils
try:
    # Python3
    from urllib.parse import urlencode
except ImportError:
    # Python2
    from urllib import urlencode


# 查询客户预算
class QueryCredit(resource2.Resource):
    base_path = "%(domain_id)s/partner/account-mgr/credit"
    service = bss_intl_service.BssIntlService()
    allow_get = True

    # request
    # User domain ID
    domain_id = resource2.URI('domain_id')
    # customer ID
    customer_id = resource2.Body('customer_id')

    # response
    creditAmount = resource2.Body('creditAmount')
    # New budget, which can be accurate to two decimal places.
    usedAmount = resource2.Body('usedAmount')
    # Unit
    measureId = resource2.Body('measureId', type=int)
    # currency
    currency = resource2.Body('currency')
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')

    def get(self, session, requires_id=False):
        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        query_dict = {'customer_id': self.customer_id}
        query_str = urlencode(query_dict, doseq=True)
        url = request.uri + '?' + query_str
        response = session.get(url, endpoint_filter=self.service,
                               microversion=service.microversion,
                               endpoint_override=endpoint_override)
        self._translate_response(response)
        return self


# 设置客户预算
class SetCredit(resource2.Resource):
    base_path = "%(domain_id)s/partner/account-mgr/credit"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # request
    # User domain ID
    domain_id = resource2.URI('domain_id')
    # Customer ID.
    customerId = resource2.Body('customerId')
    adjustmentAmount = resource2.Body('adjustmentAmount')
    measureId = resource2.Body('measureId', type=int)
    # response
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')

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
