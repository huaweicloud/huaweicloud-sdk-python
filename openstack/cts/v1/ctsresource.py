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
from openstack import resource2 as resource
from openstack import utils


class Resource(resource.Resource):
    # overwrite resource2._prepare_request as maas requires header
    # to have Content-type
    def _prepare_request(self, requires_id=True, prepend_key=False):
        body = self._body.dirty
        if prepend_key and self.resource_key is not None:
            body = {self.resource_key: body}

        headers = self._header.dirty

        headers.update({'Content-type': 'application/json'})
        # Notes: take cares for create/put, need Content-Length in headers
        if requires_id is False or len(body) == 0:
            headers.update({'Content-Length': str(len(str(body)))})
        uri = self.base_path % self._uri.attributes
        if requires_id:
            if self.id is None:
                raise exceptions.InvalidRequest(
                    "Request requires an ID but none was found")

            uri = utils.urljoin(uri, self.id)

        return resource._Request(uri, body, headers)
