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


class WhiteList(resource2.Resource):
    resource_key = 'whitelist'
    resources_key = 'whitelists'
    base_path = '/lbaas/whitelists'
    service = network_service.NetworkService()

    _query_mapping = resource2.QueryParameters("listener_id",
                                               "id",
                                               "enable_whitelist",
                                               "whitelist"
                                               )

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    # white list id
    id = resource2.Body("id")
    # tenant id
    tenant_id = resource2.Body("tenant_id")
    # listener id
    listener_id = resource2.Body("listener_id")
    # Whether to open the access control switch
    enable_whitelist = resource2.Body("enable_whitelist", type=bool)
    # Whitelist IP list
    whitelist = resource2.Body("whitelist")
