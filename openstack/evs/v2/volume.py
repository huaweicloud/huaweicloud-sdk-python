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
from openstack.evs import evs_service


class Volume(resource2.Resource):
    base_path = "/cloudvolumes"
    resource_key = 'volume'

    service = evs_service.EvsService()
    allow_create = True
    allow_update = True
    allow_get = True

    # string type volume name
    name = resource2.Body('name')
    # availability zone name
    availability_zone = resource2.Body('availability_zone')
    # project id
    project_id = resource2.Body('tenant_id')
    # created volume number
    count = resource2.Body('count', type=int)
    # volume type
    volume_type = resource2.Body('volume_type')
    # extend server info
    backup_id = resource2.Body('backup_id')
    snapshot_id = resource2.Body('snapshot_id')
    imageRef = resource2.Body('imageRef')
    metadata = resource2.Body('metadata')
    # volume size
    size = resource2.Body('size')
    # volume description
    description = resource2.Body('description')
    # whether this volume can be attached for many devices
    multiattach = resource2.Body('multiattach')
    # whether this device can be shared
    shareable = resource2.Body('shareable')
    volume = resource2.Body('volume')
    # task id
    job_id = resource2.Body('job_id')
    # order id
    order_id = resource2.Body('order_id')
    error = resource2.Body('error')
    message = resource2.Body('message')
    code = resource2.Body('code')
    # Cloud hard disk uri self-description information
    links = resource2.Body("links", type=list)
    # status
    status = resource2.Body("status")
    # Mounting information of the cloud hard disk
    attachments = resource2.Body("attachments", type=list)
    # Source cloud hard disk ID, if it is created from the source cloud hard disk, there is value
    source_volid = resource2.Body("source_volid")
    # os tenant_id
    attr_tenant_id = resource2.Body("os-vol-tenant-attr:tenant_id")
    # Metadata for cloud disk image
    volume_image_metadata = resource2.Body("volume_image_metadata", type=dict)
    # created_at
    created_at = resource2.Body("created_at")
    # bootable
    bootable = resource2.Body("bootable")
    # Host where the cloud drive is located
    host = resource2.Body("os-vol-host-attr:host")
    # reserved
    encrypted = resource2.Body("encrypted", type=bool)
    # updated date
    updated_at = resource2.Body("updated_at")
    # reserved
    replica_status = resource2.Body("replication_status")
    # reserved
    migstat = resource2.Body("os-vol-mig-status-attr:migstat")
    # reserved
    consistencygroup_id = resource2.Body("consistencygroup_id")
    # reserved
    user_id = resource2.Body("user_id")
    # dedicated_storage_id
    dedicated_storage_id = resource2.Body("dedicated_storage_id")
    # dedicated_storage_name
    dedicated_storage_name = resource2.Body("dedicated_storage_name")
    # tags
    tags = resource2.Body("tags")
    # Unique identifier when the cloud drive is mounted
    wwn = resource2.Body("wwn")
    # enterprise_project_id
    enterprise_project_id = resource2.Body("enterprise_project_id")
    # service_type
    service_type = resource2.Body("service_type")
    # The cloud disk list queries the location tag, which is the same level as the volume in the response body.
    # If this query only returns part of the list information, it will return the url of the current disk mark tag,
    # and you can continue to use this url to query the remaining list information.
    volumes_links = resource2.Body("volumes_links", type=list)
    # reserved
    os_volume_replication_extended_status = resource2.Body("os-volume-replication:extended_status")
    # reserved
    os_vol_mig_status_attr_name_id = resource2.Body("os-vol-mig-status-attr:name_id")

class ResizeVolume(Volume):
    base_path = "/cloudvolumes/%(volume_id)s/action"
    resource_key = None

    volume_id = resource2.URI('volume_id')
    # extend volume info
    extend = resource2.Body('os-extend', type=dict)
    # volume new  size
    new_size = resource2.Body('new_size', type=int)

class VolumeDetail(Volume):
    base_path = "/cloudvolumes/detail"

    _query_mapping = resource2.QueryParameters(
            'marker',
            'name',
            'limit',
            'sort_key',
            'sort_dir',
            'offset',
            'status',
            'availability_zone',
            'multiattach',
            'service_type',
            'dedicated_storage_id',
            'dedicated_storage_name',
            'volume_type_id',
            'id',
            'ids',
            'enterprise_project_id',
            changes_since='changes-since',
            metadata_alias='metadata'
    )

    allow_list = True

    # The total number of lists of elastic cloud volumes.
    count = resource2.Body('count', type=int)
    # Elastic cloud volume details list.
    volumes = resource2.Body('volumes', type=list)
    # The cloud disk list queries the location tag, which is the same level as
    # the volume in the response body.If this query only returns part of the
    # list information, it will return the url of the current disk mark tag,and
    # you can continue to use this url to query the remaining list information.
    volumes_links = resource2.Body('volumes_links', type=list)



