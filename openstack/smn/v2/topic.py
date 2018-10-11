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

import json

from openstack import resource2 as resource
from openstack.smn import smn_service
from openstack.smn.v2 import smnresource as _smnresource
from openstack import utils


class Topic(_smnresource.Resource):

    resources_key = 'topics'
    base_path = '/notifications/topics'
    service = smn_service.SMNService()

    _query_mapping = resource.QueryParameters('offset', 'limit')

    # capabilities
    allow_create = True
    allow_delete = True
    allow_update = True
    allow_get = True
    allow_list = True

    # Properties
    #: topic urn
    topic_urn = resource.Body('topic_urn', alternate_id=True)
    #: Topic name
    name = resource.Body('name')
    #: Topic display name
    display_name = resource.Body('display_name')
    #: Request id of topic
    request_id = resource.Body('request_id')
    #: upate time
    update_time = resource.Body('update_time')
    #: create time
    create_time = resource.Body('create_time')
    #: push policy
    #: *Type: int*
    push_policy = resource.Body('push_policy', type=int)

    def _dict_to_str(self, dt):
        # dict to json string
        ret = json.dumps(dt)
        return ret

    def publish(self, session, **kwargs):
        url = utils.urljoin(self.base_path, self._get_id(self), 'publish')

        headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
            "Content-Length": str(len(str(kwargs)))
        }

        endpoint_override = self.service.get_endpoint_override()

        if 'message_structure' in kwargs:
            kwargs['message_structure'] = (
                self._dict_to_str(kwargs['message_structure']))

        resp = session.post(url, endpoint_filter=self.service,
                            endpoint_override=endpoint_override,
                            json=kwargs,
                            headers=headers)

        return resp.json()

    @classmethod
    def direct_publish(cls, session, **kwargs):
        url = '/notifications/sms'
        endpoint_override = cls.service.get_endpoint_override()

        headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
            "Content-Length": str(len(str(kwargs)))
        }

        resp = session.post(url, endpoint_filter=cls.service,
                            endpoint_override=endpoint_override,
                            json=kwargs,
                            headers=headers)
        return resp.json()


class TopicAttr(_smnresource.Resource):

    base_path = '/notifications/topics/%(topic_urn)s/attributes'

    service = smn_service.SMNService()
    _query_mapping = resource.QueryParameters('name')

    # Properties
    #: topic urn
    topic_urn = resource.URI('topic_urn')
    #: attribute name
    attributes_name = resource.Body('attributes_name', alternate_id=True)
    #: attribute value are string
    attr_value = resource.Body('value')
    #: attributes
    #: *Type: dict*
    attributes = resource.Body('attributes', type=dict)
    #: request_id
    request_id = resource.Body('request_id')

    # capabilities
    allow_update = True
    allow_delete = True

    @classmethod
    def list(cls, session, paginated=False, **params):
        query_params = cls._query_mapping._transpose(params)
        uri = cls.base_path % params

        endpoint_override = cls.service.get_endpoint_override()
        resp = session.get(uri, endpoint_filter=cls.service,
                           endpoint_override=endpoint_override,
                           headers={"Accept": "application/json",
                                    "Content-type": "application/json"},
                           params=query_params)
        resp = resp.json()
        # Notes, smn doesn't returen topic_urn, it's from URI
        resp.update({"topic_urn": params['topic_urn']})

        return cls.existing(**resp)

    @classmethod
    def delete_all(cls, session, **params):
        uri = cls.base_path % params

        endpoint_override = cls.service.get_endpoint_override()
        session.delete(uri,
                       endpoint_filter=cls.service,
                       endpoint_override=endpoint_override,
                       headers={"Accept": "",
                                "Content-type": "application/json"})
