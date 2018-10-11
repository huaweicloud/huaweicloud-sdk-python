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

from openstack.anti_ddos import anti_ddos_service
from openstack import resource2 as resource


class AlertConfig(resource.Resource):

    base_path = '/warnalert/alertconfig/query'
    service = anti_ddos_service.AntiDDosService()

    # capabilities
    allow_create = False
    allow_list = False
    allow_get = True
    allow_delete = False
    allow_update = False

    # Properties
    #: warn alert config information
    #: *Type: dict*
    warn_config = resource.Body('warn_config', type=dict)
    #: unique topic id
    topic_urn = resource.Body('topic_urn')
    #: warn alert group name
    display_name = resource.Body('display_name')

    # This overrides the default behavior of resource get
    def get(self, session, requires_id=False):
        return super(AlertConfig, self).get(session, requires_id=requires_id)
