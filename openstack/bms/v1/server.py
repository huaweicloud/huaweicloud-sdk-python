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
from openstack.bms import bms_service


class Servers(resource2.Resource):
    base_path = "/baremetalservers"
    resource_key = "server"
    resources_key = 'servers'
    service = bms_service.BmsService()
    allow_create = True
    allow_get = True
    allow_update = True

    # string type BMS server name
    name = resource2.Body('name')
    # availability zone name
    availability_zone = resource2.Body('availability_zone')
    # server size
    flavorRef = resource2.Body('flavorRef')
    # image id for create bms server
    imageRef = resource2.Body('imageRef')
    # system volume
    root_volume = resource2.Body('root_volume', type=dict)
    # data volume
    data_volumes = resource2.Body('data_volumes', type=list)
    # file inspect for personal
    personality = resource2.Body('personality', type=list)
    # vpc id used for bms server
    vpcid = resource2.Body('vpcid')
    # user data inspect to create bms server
    user_data = resource2.Body('user_data')
    # project id
    project_id = resource2.Body('tenant_id')
    # subnet id used for bms server
    nics = resource2.Body('nics')
    # eip configed for bms server
    publicip = resource2.Body('publicip')
    # use Cloud-init or Cloudbase-init to set user password
    admin_password = resource2.Body('adminPass')
    # whether server name will be renamed
    isAutoRename = resource2.Body('isAutoRename')
    # ssh key name to login bms server
    key_name = resource2.Body('key_name')
    # created server number
    count = resource2.Body('count', type=int)
    # metadata for bms server
    metadata = resource2.Body('metadata', type=dict)
    # extend server info
    extendparam = resource2.Body('extendparam', type=dict)
    # security groups id
    security_groups = resource2.Body('security_groups', type=list)
    # info for schedule server based host
    scheduler_hints = resource2.Body('os:scheduler_hints', type=dict)
    # tags for identify bms servers
    tags = resource2.Body('tags')
    # # task id
    # job_id = resource2.Body('job_id')
    # # order id
    # order_id = resource2.Body('order_id')
    # error = resource2.Body('error')
    # message = resource2.Body('message')
    # code = resource2.Body('code')

    # Get the properties of the server.
    # Bare metal server unique ID.
    id = resource2.Body('id')
    # Bare metal server current status information.
    status = resource2.Body('status')
    # Bare metal server creation time.
    created = resource2.Body('created')
    # Bare metal server last update time.
    updated = resource2.Body('updated')
    # The bare metal server corresponds to the bare metal server specification information
    flavor = resource2.Body('flavor', type=dict)
    # Bare metal server image information.
    image = resource2.Body('image', type=dict)
    # The tenant ID of the bare metal server.
    tenant_id = resource2.Body('tenant_id')
    # The user ID of the bare metal server.
    user_id = resource2.Body('user_id')
    # The host ID corresponding to the bare metal server.
    hostId = resource2.Body('hostId')
    # Network address information corresponding to the bare metal server.
    addresses = resource2.Body('addresses', type=dict)
    # Bare metal server related quick link information.
    links = resource2.Body('links', type=list)
    # Extended attributes, disk configuration.
    OS_DCF_diskConfig = resource2.Body('OS-DCF:diskConfig')
    # Extended attributes, available partition coding.
    OS_EXT_AZ_availability_zone = resource2.Body('OS-EXT-AZ:availability_zone')
    # Extended attributes, bare metal server service status.
    OS_EXT_SERVICE_service_state = resource2.Body('OS-EXT-SERVICE:service_state')
    # Extended attribute, bare metal server host name.
    OS_EXT_SRV_ATTR_host = resource2.Body('OS-EXT-SRV-ATTR:host')
    # Extended attributes, hypervisor host name, provided by the Nova virt driver.
    OS_EXT_SRV_ATTR_hypervisor_hostname = resource2.Body('OS-EXT-SRV-ATTR:hypervisor_hostname')
    # Extended attribute, bare metal server instance ID.
    OS_EXT_SRV_ATTR_instance_name = resource2.Body('OS-EXT-SRV-ATTR:instance_name')
    # Extended attributes, bare metal server power state.
    # eg:
    # 0: 'NO STATE', 1: 'RUNNING', 4: 'SHUTDOWN'.
    OS_EXT_STS_power_state = resource2.Body('OS-EXT-STS:power_state')
    # Extended attributes, bare metal server task status.
    # eg:
    # rebooting, reboot_started, reboot_started_hard,
    # powering-off, powering-on, rebuilding, scheduling, deleting.
    OS_EXT_STS_task_state = resource2.Body('OS-EXT-STS:task_state')
    # Extended attributes, bare metal server status.
    # eg:
    # RUNNING, SHUTOFF, SUSPENDED, REBOOT.
    OS_EXT_STS_vm_state = resource2.Body('OS-EXT-STS:vm_state')
    # Extended attributes, bare metal server startup time.
    OS_SRV_USG_launched_at = resource2.Body('OS-SRV-USG:launched_at')
    # Extended attributes, bare metal server shutdown time.
    OS_SRV_USG_terminated_at = resource2.Body('OS-SRV-USG:terminated_at')
    # The information about the cloud drive mounted on the bare metal server.
    os_extended_volumes_volumes_attached = resource2.Body(
        'os-extended-volumes:volumes_attached', type=list
    )
    # Reserved attribute.
    accessIPv4 = resource2.Body('accessIPv4')
    # Reserved attribute.
    accessIPv6 = resource2.Body('accessIPv6')
    # Optional returned attributes, the cause of the failure.
    fault = resource2.Body('fault', type=dict)
    # Reserved attribute.
    config_drive = resource2.Body('config_drive')
    # Reserved attribute.
    progress = resource2.Body('progress')
    # Bare metal server description.
    description = resource2.Body('description')
    # Nova-compute status: UP, UNKNOWN, DOWN, MAINTENANCE, Empty string.
    host_status = resource2.Body('host_status')
