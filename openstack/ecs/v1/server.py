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
from openstack import utils
from openstack.ecs import ecs_service


class Servers(resource2.Resource):
    base_path = "/cloudservers"
    resource_key = "server"
    resources_key = 'servers'
    service = ecs_service.EcsService()
    allow_create = True
    allow_get = True

    # string type ECS server name
    name = resource2.Body('name')
    # availability zone name
    availability_zone = resource2.Body('availability_zone')
    # server size
    flavorRef = resource2.Body('flavorRef')
    # image id for create ecs server
    imageRef = resource2.Body('imageRef')
    # system volume
    root_volume = resource2.Body('root_volume', type=dict)
    # data volume
    data_volumes = resource2.Body('data_volumes', type=list)
    # file inspect for personal
    personality = resource2.Body('personality', type=list)
    # vpc id used for ecs server
    vpcid = resource2.Body('vpcid')
    # user data inspect to create ecs server
    user_data = resource2.Body('user_data')
    # project id
    project_id = resource2.Body('tenant_id')
    # subnet id used for ecs server
    nics = resource2.Body('nics')
    # eip configed for ecs server
    publicip = resource2.Body('publicip')
    # use Cloud-init or Cloudbase-init to set user password
    admin_password = resource2.Body('adminPass')
    # whether server name will be renamed
    isAutoRename = resource2.Body('isAutoRename')
    # ssh key name to login ecs server
    key_name = resource2.Body('key_name')
    # created server number
    count = resource2.Body('count', type=int)
    # metadata for ces server
    metadata = resource2.Body('metadata', type=dict)
    # extend server info
    extendparam = resource2.Body('extendparam', type=dict)
    # security groups id
    security_groups = resource2.Body('security_groups', type=list)
    # info for schedule server based host
    scheduler_hints = resource2.Body('os:scheduler_hints', type=dict)
    # tags for identify ecs servers
    tags = resource2.Body('tags', type=list)
    # task id
    job_id = resource2.Body('job_id')
    # order id
    order_id = resource2.Body('order_id')
    error = resource2.Body('error')
    message = resource2.Body('message')
    code = resource2.Body('code')

    # Add fields for get/list server(s).
    # Status of ecs server.
    status = resource2.Body('status')
    # Update time.
    updated = resource2.Body('updated')
    # Host ID of the host where the ECS is located.
    hostId = resource2.Body('hostId')
    # Host name of the host where the ECS is located.
    OS_EXT_SRV_ATTR_host = resource2.Body('OS-EXT-SRV-ATTR:host')
    # Network infomation of ecs server.
    addresses = resource2.Body('addresses', type=dict)
    # The state of the current task of the Elastic Cloud Server.
    OS_EXT_STS_task_state = resource2.Body('OS-EXT-STS:task_state')
    # The current state of the ECS.
    OS_EXT_STS_vm_state = resource2.Body('OS-EXT-STS:vm_state')
    # Elastic cloud server alias.
    OS_EXT_SRV_ATTR_instance_name = resource2.Body('OS-EXT-SRV-ATTR:instance_name')
    # The virtualized host name where the ECS is located.
    OS_EXT_SRV_ATTR_hypervisor_hostname = resource2.Body('OS-EXT-SRV-ATTR:hypervisor_hostname')
    # Elastic cloud server specification information.
    flavor = resource2.Body('flavor', type=dict)
    # Id of ecs server.
    id = resource2.Body('id')
    # The name of the available partition where the ECS is located.
    OS_EXT_AZ_availability_zone = resource2.Body('OS-EXT-AZ:availability_zone')
    # Create a user ID for the ECS.
    user_id = resource2.Body('user_id')
    # Create time.
    created = resource2.Body('created')
    # Type of disk config.
    OS_DCF_diskConfig = resource2.Body('OS-DCF:diskConfig')
    # Reserve attributes.
    accessIPv4 = resource2.Body('accessIPv4')
    # Reserve attributes.
    accessIPv6 = resource2.Body('accessIPv6')
    # Elastic cloud server progress.
    progress = resource2.Body('progress', type=int)
    # Elastic cloud server power status.
    OS_EXT_STS_power_state = resource2.Body('OS-EXT-STS:power_state', type=int)
    # Config drive information.
    config_drive = resource2.Body('config_drive')
    # Elastic cloud server startup time.
    OS_SRV_USG_launched_at = resource2.Body('OS-SRV-USG:launched_at')
    # Elastic cloud server delete time.
    OS_SRV_USG_terminated_at = resource2.Body('OS-SRV-USG:terminated_at')
    # Mount the disk to the Elastic Cloud Server.
    os_extended_volumes_volumes_attached = resource2.Body('os-extended-volumes:volumes_attached', type=list)
    # Description of ecs server.
    description = resource2.Body('description')
    # Nova compute status.
    host_status = resource2.Body('host_status')
    # The host name of the ECS.
    OS_EXT_SRV_ATTR_hostname = resource2.Body('OS-EXT-SRV-ATTR:hostname')
    # The reserved ID of the ECS.
    OS_EXT_SRV_ATTR_reservation_id = resource2.Body('OS-EXT-SRV-ATTR:reservation_id')
    # The startup sequence of the elastic cloud server.
    OS_EXT_SRV_ATTR_launch_index = resource2.Body('OS-EXT-SRV-ATTR:launch_index', type=int)
    # If the image in AMI format is used, it indicates the UUID of the kernel image.
    OS_EXT_SRV_ATTR_kernel_id = resource2.Body('OS-EXT-SRV-ATTR:kernel_id')
    # If the AMI format image is used, it indicates the UUID of the ramdisk image.
    OS_EXT_SRV_ATTR_ramdisk_id = resource2.Body('OS-EXT-SRV-ATTR:ramdisk_id')
    # Device name of the ECS system disk.
    OS_EXT_SRV_ATTR_root_device_name = resource2.Body('OS-EXT-SRV-ATTR:root_device_name')
    # User_data specified when creating an ECS.
    OS_EXT_SRV_ATTR_user_data = resource2.Body('OS-EXT-SRV-ATTR:user_data')
    # Whether the ECS is locked.
    locked = resource2.Body('locked', type=bool)
    # Enterprise project ID to which the ECS belongs.
    enterprise_project_id = resource2.Body('enterprise_project_id')
    # Elastic cloud server system label.
    sys_tags = resource2.Body('sys_tags', type=list)
    # server_tags
    server_tags = resource2.Body("server_tags", type=list)
    # If you need to use a password to log in to the cloud server, you can use the adminPass field to specify the
    # initial login password for the cloud server administrator account. The Linux administrator account is root
    # and the Windows administrator account is Administrator.
    # Password complexity requirements:
    # The length is 8-26 digits.
    # The password must contain at least three of uppercase letters, lowercase letters, numbers,
    # and special characters (!@$%^-_=+[{}]:, ./?).
    # The password cannot contain the reverse of the username or username.
    # The Windows system password cannot contain the reverse order of the username or username, and cannot contain
    # more than two consecutive characters in the username.
    adminPass = resource2.Body("adminPass")

    @classmethod
    def autorecovery(cls, session, server_id, autorecovery):
        url = utils.urljoin(cls.base_path, server_id, 'autorecovery')
        headers = {'Accept': ''}
        endpoint_override = cls.service.get_endpoint_override()
        service = cls.get_service_filter(cls, session)
        session.put(
            url, endpoint_filter=cls.service,
            microversion=service.microversion,
            headers=headers,
            json = {"support_auto_recovery": autorecovery},
            endpoint_override=endpoint_override)

    @classmethod
    def register_server_to_ces(cls, session , server_id):
        url = utils.urljoin("servers", server_id, 'action')
        headers = {'Accept': ''}
        endpoint_override = cls.service.get_endpoint_override()
        service = cls.get_service_filter(cls, session)
        session.post(
            url, endpoint_filter=cls.service,
            microversion=service.microversion,
            headers=headers,
            json={"monitorMetrics": None},
            endpoint_override=endpoint_override)


class ServerAction(resource2.Resource):
    base_path = "/cloudservers/action"

    service = ecs_service.EcsService()

    allow_create = True
    # action name
    os_start = resource2.Body('os-start', type=dict)
    # action name
    reboot = resource2.Body('reboot', type=dict)
    # action name
    os_stop = resource2.Body('os-stop', type=dict)
    # server reboot type like soft hard
    type = resource2.Body('type')
    # ecs server id list
    servers = resource2.Body('servers')
    # ecs server id
    id = resource2.Body('id')

    # task id
    job_id = resource2.Body('job_id')
    order_id = resource2.Body('order_id')
    error = resource2.Body('error')
    message = resource2.Body('message')
    code = resource2.Body('code')


class DeleteServer(resource2.Resource):
    base_path = "/cloudservers/delete"

    service = ecs_service.EcsService()

    allow_create = True
    # whether delete server eip
    delete_publicip = resource2.Body('delete_publicip')
    # whether delete server volume disk
    delete_volume = resource2.Body('delete_volume')
    # ecs server id list
    servers = resource2.Body('servers', type=list)
    # ecs server id
    id = resource2.Body('id')

    # task id
    job_id = resource2.Body('job_id')
    # order id
    order_id = resource2.Body('order_id')
    error = resource2.Body('error')
    message = resource2.Body('message')
    code = resource2.Body('code')


class ResizeServer(resource2.Resource):
    base_path = "/cloudservers/%(server_id)s/resize"
    resource_key = "resize"
    service = ecs_service.EcsService()

    allow_create = True

    server_id = resource2.URI('server_id')
    # # extend server info
    # extendparam = resource2.Body('extendparam', type=dict)
    # optional only support dedicated type host
    dedicated_host_id = resource2.Body('dedicated_host_id')
    # server size
    flavorRef = resource2.Body('flavorRef')
    # task id
    job_id = resource2.Body('job_id')
    # order id
    order_id = resource2.Body('order_id')
    error = resource2.Body('error')
    message = resource2.Body('message')
    code = resource2.Body('code')


class ServerDetail(Servers):
    base_path = '/cloudservers/detail'

    # capabilities
    allow_create = False
    allow_get = False
    allow_list = True

    _query_mapping = resource2.QueryParameters(
        'name',
        'status',
        'limit',
        'offset',
        'reservation_id',
        'enterprise_project_id',
        'tags',
        not_tags='not-tags',
        flavor_id='flavor'
    )

    # The total number of lists of elastic cloud servers.
    count = resource2.Body('count', type=int)
    # Elastic cloud server details list.
    servers = resource2.Body('servers', type=list)
