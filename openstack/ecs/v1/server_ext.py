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
from openstack.ecs import ecs_service



class Servers(resource2.Resource):
    base_path = "/cloudservers"
    resources_key = 'servers'
    service = ecs_service.EcsServiceV1_1()
    allow_create = True

    # server detail
    server = resource2.Body('server', type=dict)
    # is dry run  True or False
    dry_run = resource2.Body('dry_run')
    # string type ECS server name
    name = resource2.Body('name')
    # availability zone name
    availability_zone = resource2.Body('availability_zone')
    # server size
    flavorRef = resource2.Body('flavorRef')
    # image id for create ecs server
    imageRef = resource2.Body('imageRef')
    # system volume
    root_volume = resource2.Body('root_volume', type=dict)
    # data volume
    data_volumes = resource2.Body('data_volumes', type=list)
    # file inspect for personal
    personality = resource2.Body('personality', type=list)
    # vpc id used for ecs server
    vpcid = resource2.Body('vpcid')
    # user data inspect to create ecs server
    user_data = resource2.Body('user_data')
    # project id
    project_id = resource2.Body('tenant_id')
    # subnet id used for ecs server
    nics = resource2.Body('nics')
    # eip configed for ecs server
    publicip = resource2.Body('publicip')
    # use Cloud-init or Cloudbase-init to set user password
    admin_password = resource2.Body('adminPass')
    # whether server name will be renamed
    isAutoRename = resource2.Body('isAutoRename')
    # ssh key name to login ecs server
    key_name = resource2.Body('key_name')
    # created server number
    count = resource2.Body('count', type=int)
    # metadata for ces server
    metadata = resource2.Body('metadata', type=dict)
    # extend server info
    extendparam = resource2.Body('extendparam', type=dict)
    # security groups id
    security_groups = resource2.Body('security_groups', type=list)
    # info for schedule server based host
    scheduler_hints = resource2.Body('os:scheduler_hints', type=dict)
    # tags for identify ecs servers
    tags = resource2.Body('tags')
    # server_tags
    server_tags = resource2.Body("server_tags", type=list)
    # task id
    job_id = resource2.Body('job_id')
    server_ids = resource2.Body('serverIds', type=list)
    # order id
    order_id = resource2.Body('order_id')
    error = resource2.Body('error')
    message = resource2.Body('message')
    code = resource2.Body('code')

    def create(self, session, headers=None, prepend_key=True):
        endpoint_override = self.service.get_endpoint_override()
        service = self.get_service_filter(self, session)
        request = self._prepare_request(requires_id=False,
                                        prepend_key=prepend_key)
        if headers:
            request.headers.update(headers)
        try:
            response = session.post(request.uri, endpoint_filter=self.service,
                                    endpoint_override=endpoint_override,
                                    json=request.body, headers=request.headers,
                                    microversion=service.microversion)
            if self.dry_run:
                return "dry_run finish"
            self._translate_response(response)
            return self
        except Exception as e:
            return e


class ResizeServer(resource2.Resource):
    base_path = "/cloudservers/%(server_id)s/resize"
    resource_key = "resize"
    service = ecs_service.EcsServiceV1_1()

    allow_create = True

    server_id = resource2.URI('server_id')
    # extend server info
    extendparam = resource2.Body('extendparam', type=dict)
    # optional only support dedicated type host
    dedicated_host_id = resource2.Body('dedicated_host_id')
    # server size
    flavorRef = resource2.Body('flavorRef')
    # task id
    job_id = resource2.Body('job_id')
    # order id
    order_id = resource2.Body('order_id')
    error = resource2.Body('error')
    message = resource2.Body('message')
    code = resource2.Body('code')
