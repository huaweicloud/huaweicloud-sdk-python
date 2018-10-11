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

from openstack import resource2
from openstack.network import network_service


class Rule(resource2.Resource):
    resource_key = 'rule'
    resources_key = 'rules'
    base_path = '/lbaas/l7policies/%(policy_id)s/rules'
    service = network_service.NetworkService()

    _query_mapping = resource2.QueryParameters("id",
                                               "tenant_id",
                                               "admin_state_up",
                                               "type",
                                               "compare_type",
                                               "invert",
                                               "key",
                                               "value"
                                               )

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True
    # the rule id
    id = resource2.Body("id")
    # tenant id
    tenant_id = resource2.Body("tenant_id")
    # Management status: true/false.
    # Instructions for use: Fixed to true
    admin_state_up = resource2.Body("admin_state_up", type=bool, default=True)
    # Matching content: Can be HOST_NAME, PATH
    type = resource2.Body("type")
    # Matching method:
    # EQUAL_TO when type is HOST_NAME.
    # REGEX when the type is PATH, STARTS_WITH, EQUAL_TO
    compare_type = resource2.Body("compare_type")
    # Whether the match is reversed, true/false.
    # Instructions for use: Fixed to false. This field can be updated but will not take effect
    invert = resource2.Body("invert", type=bool, default=False)
    # Match the content key.
    # Usage note: When the current match is HOST_NAME and PATH, this field does not take effect.
    # This field can be updated but will not take effect
    key = resource2.Body("key")
    # The value of the matching content. Its value cannot contain spaces.
    # Usage note: When the type is HOST_NAME, the value range is String(100).
    # The string can only contain English letters, numbers, "-" or ".",
    # and must start with a letter or number.
    rule_value = resource2.Body("value")
    # policy id the rule belongs to
    policy_id = resource2.URI("policy_id")