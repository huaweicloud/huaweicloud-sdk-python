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


class QueryCustomerResource(resource2.Resource):
    base_path = "%(domain_id)s/partner/customer-mgr/customer-resource/query-resources"
    service = bss_intl_service.BssIntlService()
    allow_create = True

    domain_id = resource2.URI('domain_id')

    # Customer resource ID.
    customerResourceId = resource2.Body('customerResourceId')
    # Customer ID.
    customerId = resource2.Body('customerId')
    # Cloud service region code, for example, cn-north-1.
    regionCode = resource2.Body('regionCode')
    # Cloud service type code.
    cloudServiceTypeCode = resource2.Body('cloudServiceTypeCode')
    # Resource type code. For example, the VM resource type code of ECS is hws.resource.type.vm.
    resourceTypeCode = resource2.Body('resourceTypeCode')
    # Queries resource IDs in batches.
    resourceIds = resource2.Body('resourceIds')
    # Resource name.
    resourceName = resource2.Body('resourceName')
    # Start time of the validity period.
    startTimeBegin = resource2.Body('startTimeBegin')
    # End time of the validity period.
    startTimeEnd = resource2.Body('startTimeEnd')
    # Current page.
    pageNo = resource2.Body('pageNo')
    # Number of records displayed on each page.
    pageSize = resource2.Body('pageSize')

    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')
    # Customer resources.
    customerResources = resource2.Body('customerResources')
    # Total number of query records.
    totalCount = resource2.Body('totalCount')
