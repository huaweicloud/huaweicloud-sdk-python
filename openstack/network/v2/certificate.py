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

from openstack.network import network_service
from openstack import resource2


class Certificate(resource2.Resource):

    resource_key = 'certificate'
    resources_key = 'certificates'
    base_path = '/lbaas/certificates'
    service = network_service.NetworkService()

    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource2.QueryParameters(
        'page_reverse',
        'id',
        'name',
        'description',
        'type',
        'domain',
        'private_key',
        'certificate',
        'create_time',
        'update_time'
    )

    # SSL certificate ID
    id = resource2.Body("id")
    # SSL certificate name.
    # Value range: a string of 0-64 characters in length,
    # consisting of Chinese, English letters, numbers, "_" or "-"
    name = resource2.Body("name")
    # SSL certificate description.
    # Value range: A string of 0-128 characters in length.
    # The string cannot contain two characters, "<" and ">".
    # Chinese characters must be UTF-8 or unicode encoded
    description = resource2.Body("description")
    # Certificate type.
    # Ranges:
    # server
    # client: The value is reserved. It is not enabled yet.
    # Default: server
    type = resource2.Body("type")
    # The domain name signed by the server certificate.
    # Value range: A string of 0-100 characters in length.
    # A string can only contain English letters, digits, "-", or ".".
    # It must begin or end with a letter or number.
    # This field is valid only when type is server.
    domain = resource2.Body("domain")
    # Server-side private key in PEM format.
    # Format: The private key is in PEM format.
    # This field is valid only when type is server and is mandatory
    private_key = resource2.Body("private_key")
    # Server-side public key in PEM format
    certificate = resource2.Body("certificate")
    # creat time
    create_time = resource2.Body("create_time")
    # update time
    update_time = resource2.Body("update_time")

    def _translate_response(self, response, has_body=True):
        """Given a KSA response, inflate this instance with its data
        DELETE operations don't return a body, so only try to work
        with a body when has_body is True.
        This method updates attributes that correspond to headers
        and body on this instance and clears the dirty set.
        """
        if has_body:
            body = response.json()
            if self.resource_key and self.resource_key in body and isinstance(body[self.resource_key], dict):
                body = body[self.resource_key]

            body = self._filter_component(body, self._body_mapping())
            self._body.attributes.update(body)
            self._body.clean()

        headers = self._filter_component(response.headers,
                                         self._header_mapping())
        self._header.attributes.update(headers)
        self._header.clean()
