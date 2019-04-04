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


class Flavor(resource2.Resource):
    base_path = "/cloudservers/flavors"
    resource_key = "flavors"
    resources_key = "flavors"
    service = ecs_service.EcsService()

    _query_mapping = resource2.QueryParameters("availability_zone")

    allow_list = True
    # Cloud server specification name
    name = resource2.Body("name")
    # The number of CPU cores corresponding to the cloud server specification
    vcpus = resource2.Body("vcpus")
    # The size of the memory corresponding to the cloud server specification,
    # in MBThe size of the memory corresponding to the cloud server specification, in MB
    ram = resource2.Body("ram", type=int)
    # The cloud server specification corresponds to the required system disk size, and 0 is not limited.
    # This field is invalid in this system
    disk = resource2.Body("disk")
    # Unused
    swap = resource2.Body("swap")
    # Unused
    ephemeral = resource2.Body("OS-FLV-EXT-DATA:ephemeral", type=int)
    # Unused
    disabled = resource2.Body("OS-FLV-DISABLED:disabled", type=bool)
    # Unused
    factor = resource2.Body("rxtx_factor", type=int)
    # Unused
    rxtx_quota = resource2.Body("rxtx_quota")
    # Unused
    rxtx_cap = resource2.Body("rxtx_cap")
    # Unused
    is_public = resource2.Body("os-flavor-access:is_public", type=bool)
    # Specification related quick link address
    # rel: Quick link tag name
    # href: Corresponding quick link
    # type: Shortcut type
    links = resource2.Body("links", type=list)
    # Extension field for cloud server specifications
    specs = resource2.Body("os_extra_specs", type=dict)
