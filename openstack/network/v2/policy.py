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


class Policy(resource2.Resource):
    resource_key = 'l7policy'
    resources_key = 'l7policies'
    base_path = '/lbaas/l7policies'
    service = network_service.NetworkService()

    _query_mapping = resource2.QueryParameters("id",
                                               "tenant_id",
                                               "name",
                                               "admin_state_up",
                                               "description",
                                               "listener_id",
                                               "action",
                                               "position"
                                               )

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    id = resource2.Body("id")
    tenant_id = resource2.Body("tenant_id")
    name = resource2.Body("name")
    admin_state_up = resource2.Body("admin_state_up", type=bool, default=True)
    description = resource2.Body("description")
    listener_id = resource2.Body("listener_id")
    action = resource2.Body("action")
    redirect_pool_id = resource2.Body("redirect_pool_id")
    redirect_url = resource2.URI("redirect_url")
    rules = resource2.Body("rules", type=list)
    position = resource2.Body("position", type=int)