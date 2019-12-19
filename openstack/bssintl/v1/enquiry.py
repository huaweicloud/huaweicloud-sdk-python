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


class QueryRating(resource2.Resource):
    base_path = "%(domain_id)s/customer/product-mgr/query-rating"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')
    # request
    # Cloud service type code.
    cloudServiceType = resource2.Body('cloudServiceType')
    # Resource type code.
    resourceType = resource2.Body('resourceType')
    resourceSpecCode = resource2.Body('resourceSpecCode')
    # Resource size
    resourceSize = resource2.Body('resourceSize', type=int)
    # Resource capacity measurement ID.
    resouceSizeMeasureId = resource2.Body('resouceSizeMeasureId', type=int)
    # Usage factor.
    usageFactor = resource2.Body('usageFactor')
    # Usage value.
    usageValue = resource2.Body('usageValue')
    # Resource capacity measurement ID.
    usageMeasureId = resource2.Body('usageMeasureId', type=int)
    extendParams = resource2.Body('extendParams')

    # Project ID.
    tenantId = resource2.Body('tenantId')
    # Region ID.
    regionId = resource2.Body('regionId')
    # AZ ID.
    avaliableZoneId = resource2.Body('avaliableZoneId')
    # Billing mode.
    chargingMode = resource2.Body('chargingMode', type=int)
    # Order period type.
    periodType = resource2.Body('periodType', type=int)
    # Number of subscription periods.
    periodNum = resource2.Body('periodNum', type=int)
    # Expiration date.
    periodEndDate = resource2.Body('periodEndDate')
    # Associated resource ID.
    relativeResourceId = resource2.Body('relativeResourceId')
    # Period type of the associated resource.
    relativeResourcePeriodType = resource2.Body('relativeResourcePeriodType', type=int)
    # Number of subscriptions.
    subscriptionNum = resource2.Body('subscriptionNum', type=int)
    # Inquiry date.
    inquiryTime = resource2.Body('inquiryTime')
    # Product information.
    productInfos = resource2.Body('productInfos', type=list)

    # response
    # ID, which comes from the ID in the request.
    queryRatingId = resource2.Body('id')
    # Product ID
    productId = resource2.Body('productId')
    # Total amount (final amount after discount).
    amount = resource2.Body('amount')
    # Original total amount.
    originalAmount = resource2.Body('originalAmount')
    # Discounted amount.
    discountAmount = resource2.Body('discountAmount')
    # Unit
    measureId = resource2.Body('measureId')
    # Extended parameter.
    extendParams = resource2.Body('extendParams')

    # currency
    currency = resource2.Body('currency')
    # Product price inquiry result.
    productRatingResult = resource2.Body('productRatingResult')

    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')
    ratingResult = resource2.Body('ratingResult')
