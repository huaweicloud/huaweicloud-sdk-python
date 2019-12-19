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
# under the License is distributed on an "AS I@daiS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack.bss import bss_service
from openstack import resource2

try:
    # Python3
    from urllib.parse import urlencode
except ImportError:
    # Python2
    from urllib import urlencode



class QueryBillMonthlySum(resource2.Resource):
    base_path = "%(domain_id)s/customer/account-mgr/bill/monthly-sum"
    service = bss_service.BssService()
    allow_get = True

    # User domain ID
    domain_id = resource2.URI('domain_id')
    # request
    # Expenditure month.
    cycle = resource2.Body('cycle')
    # Cloud service type code. For example, the cloud service type code of ECS is hws.service.type.ec2.
    cloud_service_type_code = resource2.Body('cloud_service_type_code')
    account_type = resource2.Body('type')
    # Enterprise project ID.
    enterpriseProjectId = resource2.Body('enterpriseProjectId')

    # response
    # Currency unit.
    currency = resource2.Body('currency')
    # Number of result sets.
    total_count = resource2.Body('total_count')
    # Record information.
    bill_sums = resource2.Body('bill_sums', type=list)
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')

    def get(self, session, requires_id=False):
        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        xstr = lambda s: '' if s is None else str(s)
        query_dict = {'cycle': xstr(self.cycle), 'cloud_service_type_code': xstr(self.cloud_service_type_code), 'type': xstr(self.account_type),
                      'enterpriseProjectId': xstr(self.enterpriseProjectId)}
        query_str = urlencode(query_dict, doseq=True)
        url = request.uri + "?" + query_str
        response = session.get(url, endpoint_filter=self.service,
                               microversion=service.microversion,
                               endpoint_override=endpoint_override)
        self._translate_response(response)
        return self


class QueryBillResRecords(resource2.Resource):
    base_path = "%(domain_id)s/customer/account-mgr/bill/res-records"
    service = bss_service.BssService()
    allow_get = True

    # User domain ID
    domain_id = resource2.URI('domain_id')
    # request

    # Expenditure month.
    cycle = resource2.Body('cycle')
    # Cloud service type code.
    cloudServiceTypeCode = resource2.Body('cloudServiceTypeCode')
    # Resource type code. For example, the VM resource type code of ECS is hws.resource.type.vm.
    resourceTypeCode = resource2.Body('resourceTypeCode')
    # Cloud service region code, for example, cn-north-1.
    regionCode = resource2.Body('regionCode')
    # Resource instance ID.
    resInstanceId = resource2.Body('resInstanceId')
    # Billing mode.
    payMethod = resource2.Body('payMethod')
    # Enterprise project ID.
    enterpriseProjectId = resource2.Body('enterpriseProjectId')
    offset = resource2.Body('offset')
    limit = resource2.Body('limit')

    # response
    # currency
    currency = resource2.Body('currency')
    totalCount = resource2.Body('totalCount')
    monthlyRecords = resource2.Body('monthlyRecords', type=list)
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')

    def get(self, session, requires_id=False):
        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        xstr = lambda s: '' if s is None else str(s)
        query_dict = {'cycle': xstr(self.cycle), 'cloudServiceTypeCode': xstr(self.cloudServiceTypeCode),
                      'resourceTypeCode': xstr(self.resourceTypeCode), 'regionCode': xstr(self.regionCode),
                      'resInstanceId': xstr(self.resInstanceId), 'payMethod': xstr(self.payMethod),
                      'enterpriseProjectId': xstr(self.enterpriseProjectId),
                      'offset': xstr(self.offset), 'limit': xstr(self.limit)}
        query_str = urlencode(query_dict, doseq=True)
        url = request.uri + "?" + query_str
        response = session.get(url, endpoint_filter=self.service,
                               microversion=service.microversion,
                               endpoint_override=endpoint_override)
        self._translate_response(response)
        return self


class QueryResFeeRecords(resource2.Resource):
    base_path = "%(domain_id)s/customer/account-mgr/bill/res-fee-records"
    service = bss_service.BssService()
    allow_get = True

    # User domain ID
    domain_id = resource2.URI('domain_id')
    # request
    startTime = resource2.Body('startTime')
    endTime = resource2.Body('endTime')
    # Cloud service type code.
    cloudServiceTypeCode = resource2.Body('cloudServiceTypeCode')
    # Cloud service region code, for example, cn-north-1.
    regionCode = resource2.Body('regionCode')
    # Order ID.
    orderId = resource2.Body('orderId')
    # Billing mode.
    payMethod = resource2.Body('payMethod')
    # Queries resource IDs in batches.
    resourceId = resource2.Body('resourceId')
    # Enterprise project ID.
    enterpriseProjectId = resource2.Body('enterpriseProjectId')
    offset = resource2.Body('offset')
    limit = resource2.Body('limit')

    # response
    # currency
    currency = resource2.Body('currency')
    totalCount = resource2.Body('totalCount')
    # Resource usage record.
    feeRecords = resource2.Body('feeRecords', type=list)
    #  Status code.
    error_code = resource2.Body('error_code')
    # Error description.
    error_msg = resource2.Body('error_msg')

    def get(self, session, requires_id=False):
        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        xstr = lambda s: '' if s is None else str(s)
        query_dict = {'startTime': xstr(self.startTime), 'endTime': xstr(self.endTime),
                      'cloudServiceTypeCode': xstr(self.cloudServiceTypeCode), 'regionCode': xstr(self.regionCode),
                      'orderId': xstr(self.orderId), 'payMethod': xstr(self.payMethod),
                      'resourceId': xstr(self.resourceId), 'enterpriseProjectId': xstr(self.enterpriseProjectId),
                      'offset': xstr(self.offset), 'limit': xstr(self.limit)}
        query_str = urlencode(query_dict, doseq=True)
        url = request.uri + "?" + query_str
        response = session.get(url, endpoint_filter=self.service,
                               microversion=service.microversion,
                               endpoint_override=endpoint_override)
        self._translate_response(response)
        return self
