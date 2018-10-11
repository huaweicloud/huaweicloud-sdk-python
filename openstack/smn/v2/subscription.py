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


class SubscriptionMin(_smnresource.Resource):

    resources_key = 'subscriptions'
    service = smn_service.SMNService()

    _query_mapping = resource.QueryParameters('offset', 'limit')

    # capabilities
    allow_list = True

    # Properties
    #: endpoint publish protocol
    protocol = resource.Body('protocol')
    #: subscription urn
    subscription_urn = resource.Body('subscription_urn', alternate_id=True)
    #: Topic creator id
    owner = resource.Body('owner')
    #: Message endpoint
    endpoint = resource.Body('endpoint')
    #: Remark
    remark = resource.Body('remark')
    #: Status: 0, 1, 3.
    #: *Type: int*
    status = resource.Body('status', type=int)
    #: Request id
    request_id = resource.Body('request_id')


class Subscription(SubscriptionMin):
    base_path = '/notifications/subscriptions'

    # capabilities
    allow_list = True
    allow_delete = True

    # Properties
    #: topic urn
    topic_urn = resource.Body('topic_urn')

    def confirm(self, session, token):
        url = '/notifications/confirmation'
        endpoint_override = self.service.get_endpoint_override()

        body = {"token": token}

        # use topic_urn or endpoint
        if self.topic_urn is not None:
            body.update({'topic_urn': self.topic_urn})
        else:
            body.update({'endpoint': self.endpoint})

        headers = {"Accept": "application/json",
                   "Content-type": "application/json",
                   "Content-Length": str(len(str(body)))}

        resp = session.put(url, endpoint_filter=self.service,
                           endpoint_override=endpoint_override,
                           headers=headers,
                           json=body)
        return resp.json()


class TopicSubscription(SubscriptionMin):
    base_path = '/notifications/topics/%(topic_urn)s/subscriptions'

    # capabilities
    allow_list = True
    allow_create = True

    # Properties
    #: topic urn
    topic_urn = resource.URI('topic_urn')
