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
from openstack import exceptions


class ShareBandwidth(resource2.Resource):
    service = vpc_service.VpcService()

    base_path = '/bandwidths'
    resource_key = 'bandwidth'

    # Allowed operations on this resource.
    allow_create = True
    allow_delete = True

    # Resource key.
    bandwidth = resource2.Body('bandwidth', type=dict)
    # Name of bandwidth.
    name = resource2.Body('name')
    # Size of bandwidth.
    size = resource2.Body('size', type=int)
    # Id of enterprise project.
    enterprise_project_id = resource2.Body('enterprise_project_id')
    # Id of bandwidth.
    id = resource2.Body('id')
    # Share type of bandwidth.
    share_type = resource2.Body('share_type')
    # Flexible public network IP information corresponding to bandwidth.
    publicip_info = resource2.Body('publicip_info', type=list)
    # Unique identifier of the flexible public network IP.
    publicip_id = resource2.Body('publicip_id')
    # The address of the flexible public network IP.
    publicip_address = resource2.Body('publicip_address')
    # Type of flexible public network IP.
    publicip_type = resource2.Body('publicip_type')
    # Id of tenant.
    tenant_id = resource2.Body('tenant_id')
    # Type of bandwidth.
    bandwidth_type = resource2.Body('bandwidth_type')
    # Charge mode as bandwidth or traffic default is bandwidth.
    charge_mode = resource2.Body('charge_mode')
    # Infomation of billing.
    billing_info = resource2.Body('billing_info')


class BatchShareBandwidth(resource2.Resource):
    service = vpc_service.VpcService()

    base_path = '/batch-bandwidths'
    resource_key = 'bandwidth'
    resources_key = 'bandwidths'

    # Allowed operations on this resource.
    allow_create = True

    # Resource key.
    bandwidth = resource2.Body('bandwidth', type=dict)
    # Resources key.
    bandwidths = resource2.Body('bandwidths', type=list)
    # Name of bandwidth.
    name = resource2.Body('name')
    # Size of bandwidth.
    size = resource2.Body('size', type=int)
    # Count of bandwidth.
    count = resource2.Body('count', type=int)
    # Id of bandwidth.
    id = resource2.Body('id')
    # Share type of bandwidth.
    share_type = resource2.Body('share_type')
    # Flexible public network IP information corresponding to bandwidth.
    publicip_info = resource2.Body('publicip_info', type=list)
    # Unique identifier of the flexible public network IP.
    publicip_id = resource2.Body('publicip_id')
    # The address of the flexible public network IP.
    publicip_address = resource2.Body('publicip_address')
    # Type of flexible public network IP.
    publicip_type = resource2.Body('publicip_type')
    # Id of tenant.
    tenant_id = resource2.Body('tenant_id')
    # Type of bandwidth.
    bandwidth_type = resource2.Body('bandwidth_type')
    # Charge mode as bandwidth or traffic default is bandwidth.
    charge_mode = resource2.Body('charge_mode')
    # Infomation of billing.
    billing_info = resource2.Body('billing_info')


class InsertIpToBandwidth(resource2.Resource):
    service = vpc_service.VpcService()

    base_path = '/bandwidths/%(bandwidth_id)s/insert'
    resource_key = 'bandwidth'

    # Allowed operations on this resource.
    allow_create = True

    # Resource key.
    bandwidth = resource2.Body('bandwidth', type=dict)
    # Id of bandwidth.
    bandwidth_id = resource2.URI('bandwidth_id')
    # Flexible public network IP information corresponding to bandwidth.
    publicip_info = resource2.Body('publicip_info', type=list)
    # Unique identifier of the flexible public network IP.
    publicip_id = resource2.Body('publicip_id')
    # The address of the flexible public network IP.
    publicip_address = resource2.Body('publicip_address')
    # Type of flexible public network IP.
    publicip_type = resource2.Body('publicip_type')
    # Name of bandwidth.
    name = resource2.Body('name')
    # Size of bandwidth.
    size = resource2.Body('size', type=int)
    # Id of bandwidth.
    id = resource2.Body('id')
    # Share type of bandwidth.
    share_type = resource2.Body('share_type')
    # Id of tenant.
    tenant_id = resource2.Body('tenant_id')
    # Type of bandwidth.
    bandwidth_type = resource2.Body('bandwidth_type')
    # Charge mode as bandwidth or traffic default is bandwidth.
    charge_mode = resource2.Body('charge_mode')
    # Infomation of billing.
    billing_info = resource2.Body('billing_info')


class RemoveIpFromBandwidth(resource2.Resource):
    service = vpc_service.VpcService()

    base_path = '/bandwidths/%(bandwidth_id)s/remove'
    resource_key = 'bandwidth'

    # Allowed operations on this resource.
    allow_create = True

    # Resource key.
    bandwidth = resource2.Body('bandwidth', type=dict)
    # Id of bandwidth.
    bandwidth_id = resource2.URI('bandwidth_id')
    # Flexible public network IP information corresponding to bandwidth.
    publicip_info = resource2.Body('publicip_info', type=list)
    # Unique identifier of the flexible public network IP.
    publicip_id = resource2.Body('publicip_id')
    # Charge mode as bandwidth or traffic default is bandwidth.
    charge_mode = resource2.Body('charge_mode')
    # Size of bandwidth.
    size = resource2.Body('size', type=int)

    def create(self, session, prepend_key=True, has_body=False):
        """Create a remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param prepend_key: A boolean indicating whether the resource_key
                            should be prepended in a resource creation
                            request. Default to True.
        :param bool has_body: should mapping response body to resource.

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_create` is not set to ``True``.
        """
        if not self.allow_create:
            raise exceptions.MethodNotSupported(self, "create")

        endpoint_override = self.service.get_endpoint_override()
        if self.put_create:
            request = self._prepare_request(requires_id=True,
                                            prepend_key=prepend_key)
            response = session.put(request.uri, endpoint_filter=self.service,
                                   endpoint_override=endpoint_override,
                                   json=request.body, headers=request.headers)
        else:
            request = self._prepare_request(requires_id=False,
                                            prepend_key=prepend_key)
            response = session.post(request.uri, endpoint_filter=self.service,
                                    endpoint_override=endpoint_override,
                                    json=request.body, headers=request.headers)

        self._translate_response(response, has_body=has_body)
        return self
