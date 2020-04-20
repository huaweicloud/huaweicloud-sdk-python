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


from openstack import exceptions
from openstack.bssintl import bss_intl_service
from openstack import resource2



class IndividualRealnameAuth(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/realname-auth/individual"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')

    # request
    # Customer ID.
    customerId = resource2.Body('customerId')
    # Authentication method.
    identifyType = resource2.Body('identifyType')
    # Certificate type.
    verifiedType = resource2.Body('verifiedType')
    # Attachment URL for individual certificate authentication. The URL must be entered in sequence.
    verifiedFileURL = resource2.Body('verifiedFileURL', type=list)
    # Real-name authentication name.
    name = resource2.Body('name')
    # Enterprise certificate number.
    verifiedNumber = resource2.Body('verifiedNumber')
    # Change type.
    changeType = resource2.Body('changeType')
    # Platform ID assigned by Huawei to a partner.
    xaccountType = resource2.Body('xaccountType')
    bankCardInfo = resource2.Body('bankCardInfo')
    # response
    # Whether to transfer to manual review.
    isReview = resource2.Body('isReview')
    # Error list.
    failCheckItems = resource2.Body('failCheckItems', type=list)
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')


class EnterpriseRealnameAuth(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/realname-auth/enterprise"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')

    # request
    # Customer ID.
    customerId = resource2.Body('customerId')
    # Authentication method.
    identifyType = resource2.Body('identifyType')
    # Enterprise certificate type.
    certificateType = resource2.Body('certificateType')
    # Attachment URL for individual certificate authentication. The URL must be entered in sequence.
    verifiedFileURL = resource2.Body('verifiedFileURL', type=list)
    # Organization name.
    corpName = resource2.Body('corpName')
    # Enterprise certificate number.
    verifiedNumber = resource2.Body('verifiedNumber')
    # Registration country entered for real-name authentication.
    regCountry = resource2.Body('regCountry')
    # Enterprise registration address for real-name authentication.
    regAddress = resource2.Body('regAddress')
    # Platform ID assigned by Huawei to a partner.
    xaccountType = resource2.Body('xaccountType')
    # Enterprise person information.
    enterprisePerson = resource2.Body('enterprisePerson')
    # response
    # Whether to transfer to manual review.
    isReview = resource2.Body('isReview')
    # Error list.
    failCheckItems = resource2.Body('failCheckItems', type=list)
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')


class ChangeEnterpriseRealnameAuth(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/realname-auth/enterprise"
    service = bss_intl_service.BssIntlService()
    allow_create = True
    put_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')
    # request
    # Customer ID.
    customerId = resource2.Body('customerId')
    # Authentication method.
    identifyType = resource2.Body('identifyType')
    # Enterprise certificate type.
    certificateType = resource2.Body('certificateType')
    # URL of the certificate attachment file used for enterprise certificate authentication.
    verifiedFileURL = resource2.Body('verifiedFileURL')
    # Organization name.
    corpName = resource2.Body('corpName')
    # Enterprise certificate number.
    verifiedNumber = resource2.Body('verifiedNumber')
    # Registration country entered for real-name authentication.
    regCountry = resource2.Body('regCountry')
    # Enterprise registration address for real-name authentication.
    regAddress = resource2.Body('regAddress')
    # Change type.
    changeType = resource2.Body('changeType')
    # Platform ID assigned by Huawei to a partner.
    xaccountType = resource2.Body('xaccountType')
    # Enterprise person information.
    enterprisePerson = resource2.Body('enterprisePerson')

    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')
    # Whether to transfer to manual review.
    isReview = resource2.Body('isReview')
    # Error list.
    failCheckItems = resource2.Body('failCheckItems', type=list)

    def create(self, session, prepend_key=True):
        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        request = self._prepare_request(requires_id=False,
                                        prepend_key=prepend_key)
        response = session.put(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=request.body, headers=request.headers,
                               microversion=service.microversion)
        self._translate_response(response)
        return self


class QueryRealnameAuth(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/realname-auth/result"
    service = bss_intl_service.BssIntlService()
    allow_get = True
    allow_list = True
    _query_mapping = resource2.QueryParameters(
        'customerId')

    # User domain ID
    domain_id = resource2.URI('domain_id')
    # request
    # Customer ID.
    customerId = resource2.Body('customerId')

    reviewResult = resource2.Body('reviewResult')
    opinion = resource2.Body('opinion', type=list)
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')

