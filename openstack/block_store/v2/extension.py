# Copyright 2019 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack.block_store import block_store_service
from openstack import resource2


class Extension(resource2.Resource):
    base_path = '/extensions'
    resources_key = 'extensions'
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_list = True

    # Properties
    #: The last update time
    updated = resource2.Body('updated')
    #: Description
    description = resource2.Body('description')
    #: The link for the disk transfer
    links = resource2.Body('links', type=list)
    #: The link associated with the extension
    namespace = resource2.Body('namespace')
    #: The alias of the extension
    alias = resource2.Body('alias')
    #: The name of the disk transfer
    name = resource2.Body('name')
