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

from openstack.bss import bss_service
from openstack import resource2


class QueryRating(resource2.Resource):
    base_path = "%(domain_id)s/customer/product-mgr/query-rating"
    service = bss_service.BssService()
    allow_create = True

    # User domain ID
    domain_id = resource2.URI('domain_id')
    # request

    cloudServiceType = resource2.Body('cloudServiceType')
    resourceType = resource2.Body('resourceType')
    resourceSpecCode = resource2.Body('resourceSpecCode')
    resourceSize = resource2.Body('resourceSize', type=int)
    resouceSizeMeasureId = resource2.Body('resouceSizeMeasureId', type=int)
    usageFactor = resource2.Body('usageFactor')
    usageValue = resource2.Body('usageValue')
    usageMeasureId = resource2.Body('usageMeasureId', type=int)
    extendParams = resource2.Body('extendParams')

    tenantId = resource2.Body('tenantId')
    regionId = resource2.Body('regionId')
    avaliableZoneId = resource2.Body('avaliableZoneId')
    chargingMode = resource2.Body('chargingMode', type=int)
    periodType = resource2.Body('periodType', type=int)
    periodNum = resource2.Body('periodNum', type=int)
    periodEndDate = resource2.Body('periodEndDate')
    relativeResourceId = resource2.Body('relativeResourceId')
    relativeResourcePeriodType = resource2.Body('relativeResourcePeriodType', type=int)
    subscriptionNum = resource2.Body('subscriptionNum', type=int)
    inquiryTime = resource2.Body('inquiryTime')
    productInfos = resource2.Body('productInfos', type=list)

    # response
    id = resource2.Body('id')
    productId = resource2.Body('productId')
    amount = resource2.Body('amount')
    originalAmount = resource2.Body('originalAmount')
    discountAmount = resource2.Body('discountAmount')
    # Unit
    measureId = resource2.Body('measureId')
    extendParams = resource2.Body('extendParams')

    amount = resource2.Body('amount')
    discountAmount = resource2.Body('discountAmount')
    originalAmount = resource2.Body('originalAmount')
    # Unit
    measureId = resource2.Body('measureId')
    # currency
    currency = resource2.Body('currency')
    productRatingResult = resource2.Body('productRatingResult')

    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')
    extendParams = resource2.Body('extendParams')
    ratingResult = resource2.Body('ratingResult')
