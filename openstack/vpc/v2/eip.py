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
from openstack.vpc import vpc_service


class EIP(resource2.Resource):
    base_path = "/publicips"

    service = vpc_service.VpcService()

    allow_create = True
    # object of public ip
    publicip = resource2.Body('publicip', type=dict)
    # object of bandwidth
    bandwidth = resource2.Body('bandwidth', type=dict)
    # object of extend params
    extendParam = resource2.Body('extendParam', type=dict)
    # public ip type such as telcom union bgp or sbgp
    type = resource2.Body('type')
    # public ip name
    name = resource2.Body('name')
    # public ip size
    size = resource2.Body('size')
    # public ip id
    id = resource2.Body('id')
    # public ip share type such as PRE or WHOLE
    share_type = resource2.Body('share_type')
    # charge mode as bandwidth or traffic default is bandwidth
    charge_mode = resource2.Body('charge_mode')

    # project id
    project_id = resource2.Body('tenant_id')

    chargingMode = resource2.Body('chargingMode')
    # period of public ip like year or month
    periodType = resource2.Body('periodType')
    # period count
    periodNum = resource2.Body('count', type=int)
    # optional whether public ip auto pay order
    isAutoPay = resource2.Body('isAutoPay')
    # optional whether public ip auto renew
    isAutoRenew = resource2.Body('isAutoRenew')

    # order id
    order_id = resource2.Body('order_id')
    message = resource2.Body('message')
    code = resource2.Body('code')
    # status of public ip
    status = resource2.Body('status')
    # public ip address
    public_ip_address = resource2.Body('public_ip_address')
    # create time
    create_time = resource2.Body('create_time')
    # bandwidth size
    bandwidth_size = resource2.Body('bandwidth_size')
    # tenant id
    tenant_id = resource2.Body('tenant_id')
    #publicip id
    publicip_id = resource2.Body("publicip_id")