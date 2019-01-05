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
from openstack.deh import deh_service


class Host(resource2.Resource):
    """Define a Host class."""

    base_path = '/dedicated-hosts'
    resource_key = 'dedicated_host'
    resources_key = 'dedicated_hosts'
    service = deh_service.DehService()

    # Allow create/list/get/update/delete operation for this resource.
    allow_create = True
    allow_list = True
    allow_get = True
    allow_update = True
    allow_delete = True

    # Mapping of accepted query parameter names.
    _query_mapping = resource2.QueryParameters(
        'host_type',
        'host_type_name',
        'flavor',
        'dedicated_host_id',
        'state',
        'tenant',
        'availability_zone',
        'name',
        'limit',
        'marker',
        'sys_enterprise_project_id',
        changes_since='changes-since'
    )

    # Id of deh.
    dedicated_host_id = resource2.Body('dedicated_host_id')
    # Name of deh.
    name = resource2.Body('name')
    # Auto placement to deh.
    auto_placement = resource2.Body('auto_placement')
    # Availability zone.
    availability_zone = resource2.Body('availability_zone')
    # Tenant ID to which the dedicated host belongs.
    project_id = resource2.Body('project_id')
    # Properties of host.
    host_properties = resource2.Body('host_properties', type=dict)
    # State of deh.
    state = resource2.Body('state')
    # Available vcpu cores.
    available_vcpus = resource2.Body('available_vcpus', type=int)
    # Available memory size.
    available_memory = resource2.Body('available_memory', type=int)
    # Create time.
    allocated_at = resource2.Body('allocated_at')
    # Delete time.
    released_at = resource2.Body('released_at')
    # Count of instance.
    instance_total = resource2.Body('instance_total', type=int)
    # Uuids of instance.
    instance_uuids = resource2.Body('instance_uuids', type=list)
    # Type of host.
    host_type = resource2.Body('host_type')
    # Type name of host.
    host_type_name = resource2.Body('host_type_name')
    # Number of vcpu.
    vcpus = resource2.Body('vcpus', type=int)
    # The physical core of the dedicated host.
    cores = resource2.Body('cores', type=int)
    # The number of physical sockets for the dedicated host.
    sockets = resource2.Body('sockets', type=int)
    # The physical memory size of the dedicated host.
    memory = resource2.Body('memory', type=int)
    # Cloud server specifications created on a dedicated host.
    available_instance_capacities = resource2.Body('available_instance_capacities', type=list)
    # Indicates the number of specifications supported.
    flavor = resource2.Body('flavor')
    # The number of dedicated hosts to be assigned.
    quantity = resource2.Body('quantity', type=int)
    # Allocated exclusive host ID array.
    dedicated_host_ids = resource2.Body('dedicated_host_ids', type=list)
    # A dedicated host that meets the query criteria.
    dedicated_hosts = resource2.Body('dedicated_hosts', type=list)
    # Metadata of deh.
    metadata = resource2.Body('metadata', type=dict)
    # Tags of deh.
    tags = resource2.Body('tags', type=dict)
    # Sys_tags of deh.
    sys_tags = resource2.Body('sys_tags', type=dict)
    # The number of dedicated hosts that satisfy the query criteria.
    total = resource2.Body('total', type=int)


class HostServer(resource2.Resource):
    """Define a HostServer class."""

    base_path = '/dedicated-hosts/%(dedicated_host_id)s/servers'
    resource_key = 'server'
    resources_key = 'servers'
    service = deh_service.DehService()

    # Allow list operation for this resource.
    allow_list = True

    # Mapping of accepted query parameter names.
    _query_mapping = resource2.QueryParameters(
        'limit',
        'marker'
    )

    # Id of deh.
    dedicated_host_id = resource2.URI('dedicated_host_id')
    # Name of ecs.
    name = resource2.Body('name')
    # Id of ecs.
    id = resource2.Body('id')
    # Status of ecs.
    status = resource2.Body('status')
    # Create time.
    created = resource2.Body('created')
    # Update time.
    updated = resource2.Body('updated')
    # Flavor of ecs.
    flavor = resource2.Body('flavor', type=dict)
    # Image of ecs.
    image = resource2.Body('image')
    # Tenant id
    tenant_id = resource2.Body('tenant_id')
    # Key name of ecs.
    key_name = resource2.Body('key_name')
    # User id of ecs.
    user_id = resource2.Body('user_id')
    # Metadata of ecs.
    metadata = resource2.Body('metadata', type=dict)
    # Host id of ecs.
    hostId = resource2.Body('hostId')
    # Network infomation of ecs.
    addresses = resource2.Body('addresses', type=dict)
    # Security groups of ecs.
    security_groups = resource2.Body('security_groups', type=list)
    # Links of ecs.
    links = resource2.Body('links', type=list)
    # Extended attribute, type of diskConfig.
    OS_DCF_diskConfig = resource2.Body('OS-DCF:diskConfig')
    # The name of the available partition where the ECS is located.
    OS_EXT_AZ_availability_zone = resource2.Body('OS-EXT-AZ:availability_zone')
    # Host name of ecs.
    OS_EXT_SRV_ATTR_host = resource2.Body('OS-EXT-SRV-ATTR:host')
    # The virtualized host name where the ECS is located.
    OS_EXT_SRV_ATTR_hypervisor_hostname = resource2.Body('OS-EXT-SRV-ATTR:hypervisor_hostname')
    # Alias of ecs.
    OS_EXT_SRV_ATTR_instance_name = resource2.Body('OS-EXT-SRV-ATTR:instance_name')
    # Power state of ecs.
    OS_EXT_STS_power_state = resource2.Body('OS-EXT-STS:power_state', type=int)
    # Current state of ecs's task.
    OS_EXT_STS_task_state = resource2.Body('OS-EXT-STS:task_state')
    # Current state of ecs.
    OS_EXT_STS_vm_state = resource2.Body('OS-EXT-STS:vm_state')
    # Start time.
    OS_SRV_USG_launched_at = resource2.Body('OS-SRV-USG:launched_at')
    # Delete time.
    OS_SRV_USG_terminated_at = resource2.Body('OS-SRV-USG:terminated_at')
    # Disk of ecs.
    os_extended_volumes_volumes_attached = resource2.Body('os-extended-volumes:volumes_attached', type=list)
    # Elastic cloud server label.
    tags = resource2.Body('tags', type=list)
    # Reserve attributes.
    accessIPv4 = resource2.Body('accessIPv4')
    # Reserve attributes.
    accessIPv6 = resource2.Body('accessIPv6')
    # Config of drive.
    config_drive = resource2.Body('config_drive')
    # evsOpts = resource2.Body('evsOpts', type=int)
    # hyperThreadAffinity = resource2.Body('hyperThreadAffinity')
    # numaOpts = resource2.Body('numaOpts', type=int)
    # Progress of ecs.
    progress = resource2.Body('progress', type=int)
    # vcpuAffinity = resource2.Body('vcpuAffinity', type=list)
    # Description of ecs.
    description = resource2.Body('description')
    # Nove compute status.
    host_status = resource2.Body('host_status')
    # Host name of ecs.
    OS_EXT_SRV_ATTR_hostname = resource2.Body('OS-EXT-SRV-ATTR:hostname')
    # Create a scenario in batches and reserve the ID of the ECS.
    OS_EXT_SRV_ATTR_reservation_id = resource2.Body('OS-EXT-SRV-ATTR:reservation_id')
    # Create scenarios in batches and start the elastic cloud server.
    OS_EXT_SRV_ATTR_launch_index = resource2.Body('OS-EXT-SRV-ATTR:launch_index', type=int)
    # UUID of kernel image.
    OS_EXT_SRV_ATTR_kernel_id = resource2.Body('OS-EXT-SRV-ATTR:kernel_id')
    # UUID of ramdisk image.
    OS_EXT_SRV_ATTR_ramdisk_id = resource2.Body('OS-EXT-SRV-ATTR:ramdisk_id')
    # Device name of the ECS system disk.
    OS_EXT_SRV_ATTR_root_device_name = resource2.Body('OS-EXT-SRV-ATTR:root_device_name')
    # User_data specified when creating an ECS.
    OS_EXT_SRV_ATTR_user_data = resource2.Body('OS-EXT-SRV-ATTR:user_data')
    # Locked status.
    locked = resource2.Body('locked')
    # Elastic cloud server scheduling information.
    os_scheduler_hints = resource2.Body('os:scheduler_hints')
    # Enterprise project ID to which the ECS belongs.
    enterprise_project_id = resource2.Body('enterprise_project_id')
    # Elastic cloud server system label.
    sys_tags = resource2.Body('sys_tags')


class HostType(resource2.Resource):
    """Define a HostType class."""

    base_path = '/availability-zone/%(availability_zone)s/dedicated-host-types'
    resource_key = 'dedicated_host_type'
    resources_key = 'dedicated_host_types'
    service = deh_service.DehService()

    # Allow list operation for this resource.
    allow_list = True

    # Availability zone.
    availability_zone = resource2.URI('availability_zone')
    # Type of host.
    host_type = resource2.Body('host_type')
    # Type name of host.
    host_type_name = resource2.Body('host_type_name')


class HostQuota(resource2.Resource):
    """Define a HostQuota class."""

    base_path = '/quota-sets/%(tenant_id)s'
    resources_key = 'quota_set'
    service = deh_service.DehService()

    # Allow list operation for this resource.
    allow_list = True

    # Mapping of accepted query parameter names.
    _query_mapping = resource2.QueryParameters(
        'resource'
    )

    # Id of tenan.
    tenant_id = resource2.URI('tenant_id')
    # Type of resource.
    resource = resource2.Body('resource')
    # Maximum quota limit.
    hard_limit = resource2.Body('hard_limit', type=int)
    # Number of quotas used.
    used = resource2.Body('used', type=int)
