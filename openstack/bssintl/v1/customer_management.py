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


class CheckCustomerRegisterInfo(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/check-user"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')

    # request
    # The options are email, mobile, or name.
    searchType = resource2.Body('searchType')
    # Mobile number, email address, or account name.
    searchKey = resource2.Body('searchKey')

    # response
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')
    #  0: The account name, mobile number, or email address does not exist.
    #  1: The account name, mobile number, or email address already exists.
    status = resource2.Body('status')
    # Whether the number of verification code sending times reaches the upper limit (15 times per hour, 60 times per day)
    uplimit = resource2.Body('uplimit')


class CreateCustomer(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/customer"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')

    # request
    # Account name.
    domainName = resource2.Body('domainName')
    # Email address.
    email = resource2.Body('email')
    mobilePhone = resource2.Body('mobilePhone')
    countryCode = resource2.Body('countryCode')
    # Verification code.
    verificationCode = resource2.Body('verificationCode')
    # Unique ID of the user on the third-party system, which is assigned by the partner.
    xAccountId = resource2.Body('xAccountId')
    # Platform ID assigned by Huawei to a partner.
    xAccountType = resource2.Body('xAccountType')
    password = resource2.Body('password')
    # Two-letter ID representing the country/region of the customer.
    domainArea = resource2.Body('domainArea')
    # Indicates whether to disable the marketing message sending function.
    isCloseMarketMs = resource2.Body('isCloseMarketMs')
    # Association type. 1: Referral.Only value 1 is supported. If the value is not transferred, the customer is associated with the partner in Reseller mode.
    cooperationType = resource2.Body('cooperationType')
    # response
    domainId = resource2.Body('domainId')
    # Account name.
    domainName = resource2.Body('domainName')
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')


class QueryCustomerList(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/query"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')

    # request
    # Account name.
    domainName = resource2.Body('domainName')
    # Real-name authentication name.
    name = resource2.Body('name')
    # Page to be queried.
    offset = resource2.Body('offset', type=int)
    # Number of records on each page.
    limit = resource2.Body('limit', type=int)
    # Tag. Fuzzy search is supported.
    label = resource2.Body('label')
    cooperationType = resource2.Body('cooperationType')
    #  Start time of the association time range (UTC time).The value is in "yyyy-MM-dd 'T' HH:mm:ss 'Z'" format, such as 2019-05-06T08:05:01Z.
    cooperationTimeStart = resource2.Body('cooperationTimeStart')
    # End time of the association time range (UTC time). The value is in "yyyy-MM-dd 'T' HH:mm:ss 'Z'" format, such as 2019-05-06T08:05:01Z.
    cooperationTimeEnd = resource2.Body('cooperationTimeEnd')
    # response
    # Total number of records.
    count = resource2.Body('count')
    # Customer list.
    customerInfoList = resource2.Body('customerInfoList', type=list)
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')
    # Whether to freeze the account. 0: No 1: Yes
    isFrozen = resource2.Body('isFrozen')


# Freeze Customer Account
class FreezeCustomer(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/frozens"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')
    # request
    customerIds = resource2.Body('customerIds', type=list)
    reason = resource2.Body('reason')
    # response
    failNum = resource2.Body('failNum')
    successNum = resource2.Body('successNum')
    failDetail = resource2.Body('failDetail', type=list)
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')


# Unfreeze Customer  Account
class UnfreezeCustomer(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/unfrozens"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')
    # request
    customerIds = resource2.Body('customerIds', type=list)
    reason = resource2.Body('reason')
    # response
    failNum = resource2.Body('failNum')
    successNum = resource2.Body('successNum')
    failDetail = resource2.Body('failDetail', type=list)
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')
