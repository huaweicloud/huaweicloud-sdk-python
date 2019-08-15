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

from openstack.compute import compute_service
from openstack import resource2


class Flavor(resource2.Resource):
    resource_key = 'flavor'
    resources_key = 'flavors'
    base_path = '/flavors'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource2.QueryParameters("sort_key", "sort_dir",
                                               min_disk="minDisk",
                                               min_ram="minRam")

    # Properties
    #: Links pertaining to this flavor. This is a list of dictionaries,
    #: each including keys ``href`` and ``rel``.
    links = resource2.Body('links')
    #: The name of this flavor.
    name = resource2.Body('name')
    #: Size of the disk this flavor offers. *Type: int*
    disk = resource2.Body('disk', type=int)
    #: ``True`` if this is a publicly visible flavor. ``False`` if this is
    #: a private image. *Type: bool*
    is_public = resource2.Body('os-flavor-access:is_public', type=bool)
    #: The amount of RAM (in MB) this flavor offers. *Type: int*
    ram = resource2.Body('ram', type=int)
    #: The number of virtual CPUs this flavor offers. *Type: int*
    vcpus = resource2.Body('vcpus', type=int)
    #: Size of the swap partitions.
    swap = resource2.Body('swap')
    #: Size of the ephemeral data disk attached to this server. *Type: int*
    ephemeral = resource2.Body('OS-FLV-EXT-DATA:ephemeral', type=int)
    #: ``True`` if this flavor is disabled, ``False`` if not. *Type: bool*
    is_disabled = resource2.Body('OS-FLV-DISABLED:disabled', type=bool)
    #: The bandwidth scaling factor this flavor receives on the network.
    rxtx_factor = resource2.Body('rxtx_factor', type=float)

class FlavorResize(Flavor):
    allow_list = True
    allow_create = False
    allow_get = False
    allow_delete = False

    base_path = '/resize_flavors'

    _query_mapping = resource2.QueryParameters("instance_uuid",
                                               "source_flavor_id",
                                               "source_flavor_name",
                                               "sort_key",
                                               "sort_dir",
                                               )

    # Properties
    #: Links pertaining to this flavor. This is a list of dictionaries,
    #: each including keys ``href`` and ``rel``.
    links = resource2.Body('links', type=list)
    # Extension field for cloud server specifications
    extra_specs = resource2.Body("extra_specs", type=list)



class FlavorDetail(Flavor):
    base_path = '/flavors/detail'

    allow_create = False
    allow_get = False
    allow_update = False
    allow_delete = False
    allow_list = True


class ExtraSpecs(resource2.Resource):
    resource_key = 'extra_specs'
    resources_key = 'extra_specss'
    base_path = '/flavors/%(flavor_id)s/os-extra_specs'

    service = compute_service.ComputeService()
    # capabilities
    allow_get = True

    # This parameter is a Region level configuration. When an AZ is not configured in the cond:operation:az parameter,
    # the value of this parameter is used by default. Not configured or without this parameter is equivalent to "normal". Ranges:
    # Normal: normal commercial
    # Abandon: offline (ie not displayed)
    # Sellout: sold out
    # Obt: public beta
    # Promotion: recommended (equivalent to normal, also commercial)
    status = resource2.Body("cond:operation:status")
    # This parameter is an AZ level configuration. When an AZ is not configured in this parameter,
    # the value of the cond:operation:status parameter is used by default.
    # The configuration format of this parameter is "az(xx)". () is the flavor state of a certain AZ.
    # () must be filled with the status, not filled in as invalid configuration.
    # The range of values is the same as the cond:operation:status parameter.
    # For example, if the flavor is sold out in a region of az0, az1 is not displayed,
    # and other az is displayed normally, which can be configured as:
    # "cond:operation:status" is set to "normal"
    # "cond:operation:az" is set to "az0(sellout), az1(abandon)"
    # Description:
    # This parameter must be configured if the state of the flavor under a certain AZ is different from the state of the cond:operation:status configuration.
    az = resource2.Body("cond:operation:az")
    # This parameter is used to configure the beta tag of the flavor.
    # If there is a beta AZ in a region, this property must be configured.
    # For example: flavor only starts beta at az1, other az is not visible, can be configured as:
    # "cond:operation:status" is configured as "abandon"
    # "cond:operation:az" is configured as "az1(obt)"
    # "cond:operation:roles" is configured as "op_gated_ecs_c3ne"
    roles = resource2.Body("cond:operation:roles")
    # flavor id used in the uri
    flavor_id = resource2.URI("flavor_id")
