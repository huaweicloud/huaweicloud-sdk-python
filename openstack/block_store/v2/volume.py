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
from openstack import format
from openstack import resource2


class Volume(resource2.Resource):
    resource_key = "volume"
    resources_key = "volumes"
    base_path = "/volumes"
    service = block_store_service.BlockStoreService()

    _query_mapping = resource2.QueryParameters(
            'all_tenants',
            'name',
            'status',
            'project_id',
            "sort_key",
            "offset",
            "availability_zone",
            "sort_dir",
            changes_since="changes-since",
            metadata_alias="metadata"
            )

    # capabilities
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_update = True
    allow_list = True

    # Properties
    #: A ID representing this volume.
    id = resource2.Body("id")
    #: The name of this volume.
    name = resource2.Body("name")
    #: A list of links associated with this volume. *Type: list*
    links = resource2.Body("links", type=list)

    #: The availability zone.
    availability_zone = resource2.Body("availability_zone")
    #: To create a volume from an existing volume, specify the ID of
    #: the existing volume. If specified, the volume is created with
    #: same size of the source volume.
    source_volume_id = resource2.Body("source_volid")
    #: The volume description.
    description = resource2.Body("description")
    #: To create a volume from an existing snapshot, specify the ID of
    #: the existing volume snapshot. If specified, the volume is created
    #: in same availability zone and with same size of the snapshot.
    snapshot_id = resource2.Body("snapshot_id")
    #: The size of the volume, in GBs. *Type: int*
    size = resource2.Body("size", type=int)
    #: The ID of the image from which you want to create the volume.
    #: Required to create a bootable volume.
    image_id = resource2.Body("imageRef")
    #: The name of the associated volume type.
    volume_type = resource2.Body("volume_type")
    #: Enables or disables the bootable attribute. You can boot an
    #: instance from a bootable volume. *Type: bool*
    is_bootable = resource2.Body("bootable", type=format.BoolStr)
    #: One or more metadata key and value pairs to associate with the volume.
    metadata = resource2.Body("metadata", type=dict)
    #: One of the following values: creating, available, attaching, in-use
    #: deleting, error, error_deleting, backing-up, restoring-backup,
    #: error_restoring. For details on these statuses, see the
    #: Block Storage API documentation.
    status = resource2.Body("status")
    #: TODO(briancurtin): This is currently undocumented in the API.
    attachments = resource2.Body("attachments", type=list)
    #: The timestamp of this volume creation.
    created_at = resource2.Body("created_at")
    # This parameter indicates that the cloud disk is created from the clone of the disk.
    # The current cloud disk service does not support this function.
    source_replica = resource2.Body("source_replica")
    # Consistency group ID. This parameter indicates that the cloud disk belongs to the consistency group. The current
    # cloud disk service does not support this function.
    consistencygroup_id = resource2.Body("consistencygroup_id")
    # Is it a shareable cloud drive
    shareable = resource2.Body("shareable", type=bool)
    # Share the cloud drive flag. The default is false.
    multiattach = resource2.Body("multiattach", type=bool)
    #: ``True`` if this volume is encrypted, ``False`` if not.
    #: *Type: bool*
    encrypted = resource2.Body("encrypted", type=bool)
    #: Status of replication on this volume.
    replication_status = resource2.Body("replication_status")
    # updated date
    updated_at = resource2.Body("updated_at")
    # user id
    user_id = resource2.Body("user_id")
    # If the cloud drive is created from the image, this field will be available, otherwise the field is empty.
    volume_image_metadata = resource2.Body("volume_image_metadata", type=dict)
    #: Extended replication status on this volume.
    extended_status = resource2.Body(
        "os-volume-replication:extended_status")
    #: The project ID associated with current back-end.
    tenant_id = resource2.Body("os-vol-tenant-attr:tenant_id")
    #: The status of this volume's migration (None means that a migration
    #: is not currently in progress).
    migstat = resource2.Body("os-vol-mig-status-attr:migstat")
    #: The volume ID that this volume's name on the back-end is based on.
    name_id = resource2.Body("os-vol-mig-status-attr:name_id")
    # message
    message = resource2.Body("message")
    # code
    code = resource2.Body("code")
    #: The volume's current back-end.
    host = resource2.Body("os-vol-host-attr:host")
    # The scheduling parameter currently supports the dedicated_storage_id field,
    # indicating that the cloud disk is created in the DSS storage pool.
    scheduler_hints = resource2.Body("OS-SCH-HNT:scheduler_hints", type =dict)
    # Mirror ID. Specifying the parameter to create a cloud disk is created from the image.
    # Description:
    # Creating a BMS system disk through BMS mirroring is not supported.
    imageRef = resource2.Body("imageRef")


class VolumeDetail(Volume):

    base_path = "/volumes/detail"
    #: The volume's current back-end.
    host = resource2.Body("os-vol-host-attr:host")
    #: The project ID associated with current back-end.
    project_id = resource2.Body("os-vol-tenant-attr:tenant_id")
    #: The status of this volume's migration (None means that a migration
    #: is not currently in progress).
    migration_status = resource2.Body("os-vol-mig-status-attr:migstat")
    #: The volume ID that this volume's name on the back-end is based on.
    migration_id = resource2.Body("os-vol-mig-status-attr:name_id")
    #: Status of replication on this volume.
    replication_status = resource2.Body("replication_status")
    #: Extended replication status on this volume.
    extended_replication_status = resource2.Body(
        "os-volume-replication:extended_status")
    #: ID of the consistency group.
    consistency_group_id = resource2.Body("consistencygroup_id")
    #: Data set by the replication driver
    replication_driver_data = resource2.Body(
        "os-volume-replication:driver_data")
    #: ``True`` if this volume is encrypted, ``False`` if not.
    #: *Type: bool*
    is_encrypted = resource2.Body("encrypted", type=format.BoolStr)
    # If the cloud drive is created from the image, this field will be available, otherwise the field is empty.
    volume_image_metadata = resource2.Body("volume_image_metadata", type=dict)
    # The cloud disk list queries the location tag, which is the same level as the volume in the response body.
    # If this query only returns part of the list information, it will return the url of the current disk mark tag,
    # and you can continue to use this url to query the remaining list information.
    volumes_links = resource2.Body("volumes_links", type=list)