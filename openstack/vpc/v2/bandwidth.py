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

from openstack import exceptions
from openstack import resource2
from openstack.vpc import vpc_service


class Bandwidths(resource2.Resource):
    base_path = "/bandwidths/%(bandwidth_id)s"

    service = vpc_service.VpcService()
    allow_create = True
    put_create = True

    # bandwidth id
    bandwidth_id = resource2.URI('bandwidth_id')
    bandwidth = resource2.Body('bandwidth', type=dict)
    # extend param to apply bandwidth
    extendParam = resource2.Body('extendParam', type=dict)

    # string type bandwidth name
    name = resource2.Body('name')
    # string type bandwidth size
    size = resource2.Body('size')
    # optional whether auto pay order
    isAutoPay = resource2.Body('isAutoPay')
    # order id
    order_id = resource2.Body('order_id')
    message = resource2.Body('message')
    code = resource2.Body('code')
    id = resource2.Body('id')
    # share type PER or WHOLE
    share_type = resource2.Body('share_type')
    # bandwidth type
    bandwidth_type = resource2.Body('bandwidth_type')
    tenant_id = resource2.Body('tenant_id')
    # charge mode as bandwidth or traffic default is bandwidth
    charge_mode = resource2.Body('charge_mode')
    # public ip info
    publicip_info = resource2.Body('publicip_info')
    # public ip id
    publicip_id = resource2.Body('publicip_id')
    # public ip address
    publicip_address = resource2.Body('publicip_address')
    # public ip type
    publicip_type = resource2.Body('publicip_type')
    # project id
    project_id = resource2.Body('tenant_id')

    def create(self, session, prepend_key=True):
        """Create a remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param prepend_key: A boolean indicating whether the resource_key
                            should be prepended in a resource creation
                            request. Default to True.

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_create` is not set to ``True``.
        """
        if not self.allow_create:
            raise exceptions.MethodNotSupported(self, "create")

        if not self.put_create:
            raise exceptions.MethodNotSupported(self, "put create")

        endpoint_override = self.service.get_endpoint_override()

        request = self._prepare_request(requires_id=False,
                                        prepend_key=prepend_key)
        response = session.put(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=request.body, headers=request.headers)

        self._translate_response(response)
        return self
