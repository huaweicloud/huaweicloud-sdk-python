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

from openstack.network import network_service
from openstack import resource2


class HealthMonitor(resource2.Resource):
    resource_key = 'healthmonitor'
    resources_key = 'healthmonitors'
    base_path = '/lbaas/healthmonitors'
    service = network_service.NetworkService()

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    # Health monitor ID
    id = resource2.Body("id")
    # tenant id
    tenant_id = resource2.Body("tenant_id")
    # Health monitor name
    name = resource2.Body("name")
    # Interval, unit seconds, value range [0,2147483647]
    delay = resource2.Body("delay", type=int)
    # The maximum number of failures, in the range [1,10]
    max_retries = resource2.Body("max_retries", type=int)
    # Pool id list
    pools = resource2.Body("pools", type=list)
    # Pool id
    pool_id = resource2.Body("pool_id")
    # Management status, true/false.
    # Instructions for use: Fixed to true
    admin_state_up = resource2.Body("admin_state_up", type=bool, default=True)
    # Timeout time, in seconds, in the range [0, 2147483647].
    # Instructions for use: It is recommended that this value be less than the value of delay
    timeout = resource2.Body("timeout", type=int)
    # Type, which can be TCP, UDP, or HTTP
    type = resource2.Body("type")
    # Health check port number, in the range [1,65535].
    # Usage note: The default is blank, which means the port of the back-end cloud server group is used
    monitor_port = resource2.Body("monitor_port", type=int)
    # Expect an HTTP response status code, specifying the following values:
    # Single value, such as 200;
    # List, for example 200,202;
    # Intervals, such as 200-204
    expected_codes = resource2.Body("expected_codes")
    # The health check tests the http request path sent when the member is healthy.
    # Instructions for use: begin with "/"
    url_path = resource2.Body("url_path")
    # HTTP methods, which can be GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS, CONNECT, PATCH
    http_method = resource2.Body("http_method")