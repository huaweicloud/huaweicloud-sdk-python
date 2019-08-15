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

from openstack import resource2 as resource
from openstack.smn import smn_service
from openstack.smn.v2 import smnresource as _smnresource


class MessageTemplate(_smnresource.Resource):

    base_path = '/notifications/message_template'
    resources_key = 'message_templates'
    service = smn_service.SMNService()

    _query_mapping = resource.QueryParameters('offset', 'limit',
                                              'message_template_name',
                                              'protocol',
                                              'locale')

    # capabilities
    allow_create = True
    allow_delete = True
    allow_get = True
    allow_update = True
    allow_list = True

    # Properties
    #: Template ID
    message_template_id = resource.Body('message_template_id',
                                        alternate_id=True)
    #: Template name
    message_template_name = resource.Body('message_template_name')
    #: Template language. e.g: zh-cn, en-us, de-de, pt-br
    locale = resource.Body('locale')
    #: Template tag list
    #: *Type: list*
    tag_names = resource.Body('tag_names', type=list)
    #: Created time
    create_time = resource.Body('create_time')
    #: Update time
    update_time = resource.Body('update_time')
    #: Template content
    content = resource.Body('content')
    #: Protocol
    protocol = resource.Body('protocol')
