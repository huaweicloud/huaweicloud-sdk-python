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

from openstack.cts import cts_service
from openstack.cts.v1 import ctsresource
from openstack import resource2 as resource


class Tracker(ctsresource.Resource):

    base_path = '/tracker'
    service = cts_service.CTSService()

    _query_mapping = resource.QueryParameters('tracker_name')

    # capabilities
    allow_create = True
    allow_update = True

    # Properties
    #: tracker name
    tracker_name = resource.Body('tracker_name', alternate_id=True)
    #: bucket name
    bucket_name = resource.Body('bucket_name')
    #: file prefix name in a bucket
    file_prefix_name = resource.Body('file_prefix_name')
    #: Status of the tracker
    status = resource.Body('status')
    #: Detail of the tracker, only validate if exception happens
    detail = resource.Body('detail')

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

        return cls.existing(**resp)

    def delete(self, session, params=None, has_body=False):

        params = {'tracker_name': self.tracker_name}

        endpoint_override = self.service.get_endpoint_override()
        session.delete(self.base_path,
                       endpoint_filter=self.service,
                       endpoint_override=endpoint_override,
                       headers={"Accept": "",
                                "Content-type": "application/json"},
                       params=params)
