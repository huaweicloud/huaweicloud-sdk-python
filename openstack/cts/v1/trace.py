# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
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

from openstack.cts import cts_service
from openstack.cts.v1 import ctsresource
from openstack import resource2 as resource


class Trace(ctsresource.Resource):

    base_path = '/%(tracker_name)s/trace'
    resources_key = 'traces'
    service = cts_service.CTSService()

    allow_list = True

    _query_mapping = resource.QueryParameters('service_type',
                                              'resource_type',
                                              'resource_id',
                                              'resource_name'
                                              'trace_name',
                                              'limit',
                                              'next',
                                              'from',
                                              'to',
                                              'trace_id',
                                              'trace_rating',
                                              'user')

    # Properties
    #: trace resource id
    resource_id = resource.Body('resource_id')
    #: name of the trace
    trace_name = resource.Body('trace_name')
    #: rating of the trace, normal, warning, incident
    trace_rating = resource.Body('trace_rating')
    #: trace source type
    trace_type = resource.Body('trace_type')
    #: trace request content
    request = resource.Body('request')
    #: trace response content
    response = resource.Body('response')
    #: trace http return code
    code = resource.Body('code')
    #: API version
    api_version = resource.Body('api_version')
    #: remark of the trace
    message = resource.Body('message')
    #: record time stampt
    #: *Type: int*
    record_time = resource.Body('record_time', type=int)
    #: metadata of the trace
    #: *Type: dict*
    meta_data = resource.Body('meta_data', type=dict)
    #: trace id
    trace_id = resource.Body('trace_id')
    #: trace event time
    #: *Type: int*
    time = resource.Body('time', type=int)
    #: trace user information
    user = resource.Body('user')
    #: trace service type
    service_type = resource.Body('service_type')
    #: trace resource type
    resource_type = resource.Body('resource_type')
    #: user ip of the trace
    source_ip = resource.Body('source_ip')
    #: resource name of the trace
    resource_name = resource.Body('resource_name')


class TraceV2(ctsresource.Resource):

    # Compared with v1.0, v2.0 change trace_rating to trace_status in request,
    # user/request/resource to dict in the response
    # FIXME: the doc says, v2.0 changes resource to dict, but the api response
    # example shows response changes to dict.
    base_path = '/%(tracker_name)s/trace'
    resources_key = 'traces'
    service = cts_service.CTSService()

    allow_list = True

    _query_mapping = resource.QueryParameters('service_type',
                                              'resource_type',
                                              'resource_id',
                                              'resource_name'
                                              'trace_name',
                                              'limit',
                                              'next',
                                              'from',
                                              'to',
                                              'trace_id',
                                              'trace_status',
                                              'user')

    # Properties
    #: trace resource id
    resource_id = resource.Body('resource_id')
    #: name of the trace
    trace_name = resource.Body('trace_name')
    #: rating of the trace, normal, warning, incident
    trace_status = resource.Body('trace_status')
    #: trace source type
    trace_type = resource.Body('trace_type')
    #: trace request content
    #: *Type: dict*
    request = resource.Body('request', type=dict)
    #: trace response content
    #: *Type: dict*
    response = resource.Body('response', type=dict)
    #: trace http return code
    code = resource.Body('code')
    #: API version
    api_version = resource.Body('api_version')
    #: remark of the trace
    message = resource.Body('message')
    #: record time stampt
    #: *Type: int*
    record_time = resource.Body('record_time', type=int)
    #: metadata of the trace
    #: *Type: dict*
    meta_data = resource.Body('meta_data', type=dict)
    #: trace id
    trace_id = resource.Body('trace_id')
    #: trace event time
    #: *Type: int*
    time = resource.Body('time', type=int)
    #: trace user information
    #: *Type: dict*
    user = resource.Body('user', type=dict)
    #: trace service type
    service_type = resource.Body('service_type')
    #: trace resource type
    resource_type = resource.Body('resource_type')
    #: user ip of the trace
    source_ip = resource.Body('source_ip')
    #: resource name of the trace
    resource_name = resource.Body('resource_name')
