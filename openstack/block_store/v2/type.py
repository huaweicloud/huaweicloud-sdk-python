# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
#      Huawei has modified this source file.
#     
#         Copyright 2018 Huawei Technologies Co., Ltd.
#         
#         Licensed under the Apache License, Version 2.0 (the "License"); you may not
#         use this file except in compliance with the License. You may obtain a copy of
#         the License at
#         
#             http://www.apache.org/licenses/LICENSE-2.0
#         
#         Unless required by applicable law or agreed to in writing, software
#         distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#         WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#         License for the specific language governing permissions and limitations under
#         the License.

from openstack.block_store import block_store_service
from openstack import resource2


class Type(resource2.Resource):
    resource_key = "volume_type"
    resources_key = "volume_types"
    base_path = "/types"
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_list = True

    # Properties
    #: A ID representing this type.
    id = resource2.Body("id")
    #: Name of the type.
    name = resource2.Body("name")
    #: A dict of extra specifications. "capabilities" is a usual key.
    extra_specs = resource2.Body("extra_specs", type=dict)
    #: List of cloud disk types returned by the query request
    #volume_types = resource2.Body("volue_types", type = list)
    #: Cinder backend cloud drive type name
    volume_backend_name = resource2.Body("volume_backend_name")
    #: Available partition
    availability_zone = resource2.Body("availability-zone")
    #: Error message returned when an error occurs
    message = resource2.Body("message")
    # the specific meaning refers to the list of return values below
    # 400 Bad Request
    # 401 Unauthorized
    # 403 Forbidden
    # 404 Not Found
    # 405 Method Not Allowed
    # 406 Not Acceptable
    # 407 Proxy Authentication Required
    # 408 Request Timeout
    # 409 Conflict
    # 500 Internal Server Error
    # 501 Not Implemented
    # 502 Bad Gateway
    # 503 Service Unavailable
    # 504 Gateway Timeout
    code = resource2.Body("code")
    #: Description of the cloud disk type
    description = resource2.Body("description")
    #: The id of the qos corresponding to the cloud drive type
    qos_specs_id = resource2.Body("qos_specs_id")
    #: Whether it is a public type
    is_public = resource2.Body("is_public", type= bool)
    #: Support AZ list of current cloud drive type
    RESKEY_availability_zone = resource2.Body("RESKEY:availability_zone")
    #: AZ list of current cloud drive types sold out
    sold_out_availability_zones = resource2.Body("os-vendor-extended:sold_out_availability_zones")



