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
#         Copyright 2019 Huawei Technologies Co., Ltd.
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

from openstack.block_store.v2 import snapshot as _snapshot
from openstack.block_store.v2 import type as _type
from openstack.block_store.v2 import volume as _volume
# from openstack.block_store.v2 import extension as _extension
# from openstack.block_store.v2 import availability_zone as _availability_zone
# from openstack.block_store.v2 import volume_transfer as _volume_transfer
# from openstack.block_store import version as _version
from openstack import proxy2


class Proxy(proxy2.BaseProxy):

    def get_snapshot(self, snapshot):
        """Get a single snapshot

        :param snapshot: The value can be the ID of a snapshot or a
                         :class:`~openstack.volume.v2.snapshot.Snapshot`
                         instance.

        :returns: One :class:`~openstack.volume.v2.snapshot.Snapshot`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_snapshot.Snapshot, snapshot)

    def snapshots(self, details=True, **query):
        """Retrieve a generator of snapshots

        :param bool details: When set to ``False``
                    :class:`~openstack.block_store.v2.snapshot.Snapshot`
                    objects will be returned. The default, ``True``, will cause
                    :class:`~openstack.block_store.v2.snapshot.SnapshotDetail`
                    objects to be returned.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
            the snapshots being returned.  Available parameters include:

            * name: Name of the snapshot as a string.
            * all_tenants: Whether return the snapshots of all tenants.
            * volume_id: volume id of a snapshot.
            * status: Value of the status of the snapshot so that you can
                      filter on "available" for example.

        :returns: A generator of snapshot objects.
        """
        snapshot = _snapshot.SnapshotDetail if details else _snapshot.Snapshot
        return self._list(snapshot, paginated=True, **query)

    def create_snapshot(self, **attrs):
        """Create a new snapshot from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.volume.v2.snapshot.Snapshot`,
                           comprised of the properties on the Snapshot class.

        :returns: The results of snapshot creation
        :rtype: :class:`~openstack.volume.v2.snapshot.Snapshot`
        """
        return self._create(_snapshot.Snapshot, **attrs)

    def delete_snapshot(self, snapshot, ignore_missing=True):
        """Delete a snapshot

        :param snapshot: The value can be either the ID of a snapshot or a
                         :class:`~openstack.volume.v2.snapshot.Snapshot`
                         instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the snapshot does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent snapshot.

        :returns: ``None``
        """
        self._delete(_snapshot.Snapshot, snapshot,
                     ignore_missing=ignore_missing)

    def get_type(self, type):
        """Get a single type

        :param type: The value can be the ID of a type or a
                     :class:`~openstack.volume.v2.type.Type` instance.

        :returns: One :class:`~openstack.volume.v2.type.Type`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_type.Type, type)

    def types(self):
        """Retrieve a generator of volume types

        :returns: A generator of volume type objects.
        """
        return self._list(_type.Type, paginated=False)

    def create_type(self, **attrs):
        """Create a new type from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.volume.v2.type.Type`,
                           comprised of the properties on the Type class.

        :returns: The results of type creation
        :rtype: :class:`~openstack.volume.v2.type.Type`
        """
        return self._create(_type.Type, **attrs)

    def delete_type(self, type, ignore_missing=True):
        """Delete a type

        :param type: The value can be either the ID of a type or a
                     :class:`~openstack.volume.v2.type.Type` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the type does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent type.

        :returns: ``None``
        """
        self._delete(_type.Type, type, ignore_missing=ignore_missing)

    def get_volume(self, volume):
        """Get a single volume

        :param volume: The value can be the ID of a volume or a
                       :class:`~openstack.volume.v2.volume.Volume` instance.

        :returns: One :class:`~openstack.volume.v2.volume.Volume`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_volume.Volume, volume)

    def volumes(self, details=True, **query):
        """Retrieve a generator of volumes

        :param bool details: When set to ``False``
                    :class:`~openstack.block_store.v2.volume.Volume` objects
                    will be returned. The default, ``True``, will cause
                    :class:`~openstack.block_store.v2.volume.VolumeDetail`
                    objects to be returned.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
            the volumes being returned.  Available parameters include:

            * name: Name of the volume as a string.
            * all_tenants: Whether return the volumes of all tenants
            * status: Value of the status of the volume so that you can filter
                    on "available" for example.
            * marker: The ID of the last record on the previous page.
                    The returned value is the value of the item after this one.
            * limit: The maximum number of query results that can be returned.
                    The value must be an integer greater than 0.
                    The default value is 1000.
            * sort_key: The keyword based on which the returned results are sorted.
                    The value can be id, status, size, or created_at,
                    and the default value is created_at.
            * sort_dir: The result sorting order.
                    The default value is desc (descending order).
            * offset: The offset. If the value is an integer greater than 0
                    but less than the number of disks,
                    all disks after this offset will be queried.
            * status: The disk status. For details, see Disk Status.
            * metadata_alias: The disk metadata.
            * availability_zone: The AZ.
            * changes_since: The time when the disk was updated,
                    for example, 2016-01-08T09:41:18.
                    This is an extended attribute.
                    Only administrators can set this parameter.

        :returns: A generator of volume objects.

                    * ``Response parameters:``
                        * If details is ``False``:
                            id, links, name
                        * If details is ``True``:
                            id, links, name, status, attachments,
                            availability_zone, host, source_volume_id, snapshot_id,
                            description, created_at, volume_type, tenant_id, size,
                            metadata, migstat, name_id, extended_status, encrypted,
                            replication_status, user_id, consistencygroup_id, is_bootable,
                            updated_at, shareable, multiattach, volume_image_metadata
        :rtype: If details is ``False``,
                type is :class:`~openstack.block_store.v2.volume.Volume`,
                if details is ``True``,
                type is :class:`~openstack.block_store.v2.volume.VolumeDetail`.
        """
        volume = _volume.VolumeDetail if details else _volume.Volume
        return self._list(volume, paginated=True, **query)

    def create_volume(self, **attrs):
        """Create a new volume from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.volume.v2.volume.Volume`,
                           comprised of the properties on the Volume class.

        :returns: The results of volume creation
        :rtype: :class:`~openstack.volume.v2.volume.Volume`
        """
        return self._create(_volume.Volume, **attrs)

    def delete_volume(self, volume, ignore_missing=True, cascade=False):
        """Delete a volume

        :param volume: The value can be either the ID of a volume or a
                       :class:`~openstack.volume.v2.volume.Volume` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the volume does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent volume.
        :param bool cascade: When set to ``Ture``
                    Delete all snapshots associated with the cloud drive.
                    The default value is false..

        :returns: ``None``
        """
        self._delete(_volume.Volume, volume, params={"cascade": cascade}, ignore_missing=ignore_missing)

    # def update_volume(self, volume_id, **data):
    #     """Updata a volume.
    #
    #     :param volume_id: The ID of a volume.
    #     :param data: Keyword arguments which will be used to update.
    #     :return: :class:`~openstack.volume.v2.volume.Volume`
    #     """
    #     return self._update(_volume.Volume, volume_id, **data)
    #
    # def get_quota_set(self, tenant_id):
    #     """Querying details of tenant quotas
    #
    #     :param tenant_id: tenant id
    #
    #     :returns: the details of tenant quotas
    #     :rtype: :class:`~openstack.block_store.v2.volume.QuotaSet`
    #     """
    #
    #     return self._get(_volume.QuotaSet, None, False, tenant_id=tenant_id)
    #
    # def create_volume_metadata(self, volume, **metadata):
    #     """Adding metadata of an block_store disk
    #
    #     :param volume: The value can be the ID of a volume
    #                    or a :class:`~openstack.block_store.v2.volume.Volume`
    #                    instance.
    #     :param dict metadata: Keyword arguments which will be used to create
    #                        a :class:`~openstack.block_store.v2.volume.VolumeMetadata`,
    #                        comprised of the properties on the VolumeMetadata
    #                        class.
    #
    #     :returns: the metadata of an block_store disk
    #     :rtype: :class:`~openstack.block_store.v2.volume.VolumeMetadata`
    #     """
    #     res = self._get_resource(_volume.Volume, volume)
    #     res_metadata = self._get_resource(_volume.VolumeMetadata, None)
    #     return res_metadata.create_metadata(self._session, res.id, metadata)
    #
    # def update_volume_metadata(self, volume, key=None, **metadata):
    #     """Updating metadata of an block_store disk
    #
    #     :param volume: The value can be the ID of a volume
    #                    or a :class:`~openstack.block_store.v2.volume.Volume`
    #                    instance.
    #     :param key: The key of metadata that requires the update.
    #     :param dict metadata: Keyword arguments which will be used to create
    #                        a :class:`~openstack.block_store.v2.volume.VolumeMetadata`,
    #                        comprised of the properties on the VolumeMetadata
    #                        class.
    #
    #     :returns: the metadata of an block_store disk
    #     :rtype: :class:`~openstack.blcok_store.v2.volume.VolumeMetadata`
    #     """
    #     res = self._get_resource(_volume.Volume, volume)
    #     res_metadata = self._get_resource(_volume.VolumeMetadata, None)
    #     return res_metadata.update_metadata(self._session, res.id, metadata, key)
    #
    # def delete_volume_metadata(self, volume, key, ignore_missing=True):
    #     """Deleting one piece of block_store disk metadata
    #
    #     :param volume: The value can be the ID of a volume
    #                    or a :class:`~openstack.block_store.v2.volume.Volume`
    #                    instance.
    #     :param key: The key of the metadata that requires the deletion.
    #     :param bool ignore_missing: When set to ``False``
    #                 :class:`~openstack.exceptions.ResourceNotFound` will be
    #                 raised when the metadata does not exist.
    #                 When set to ``True``, no exception will be set when
    #                 attempting to delete a nonexistent metadata.
    #
    #     :returns: ``None``
    #     """
    #     res = self._get_resource(_volume.Volume, volume)
    #     metadata = self._get_resource(_volume.VolumeMetadata, None)
    #     metadata.delete_metadata(self._session, res.id, key,
    #                              ignore_missing=ignore_missing)
    #
    # def get_volume_metadata(self, volume, key=None):
    #     """Querying block_store disk metadata
    #
    #     :param volume: The value can be the ID of a volume
    #                    or a :class:`~openstack.block_store.v2.volume.Volume`
    #                    instance.
    #     :param key: The key of the metadata to be queried.
    #
    #     :returns: The metadata of an block_store disk.
    #     :rtype: :class:`~openstack.block_store.v2.volume.VolumeMetadata`
    #     """
    #     res = self._get_resource(_volume.Volume, volume)
    #     metadata = self._get_resource(_volume.VolumeMetadata, None)
    #     return metadata.get_metadata(self._session, res.id, key)
    #
    # def expand_volume(self, volume_id, new_size):
    #     """Expanding the Capacity of a Disk.
    #
    #     :param volume_id: The ID of a volume.
    #     :param new_size: The disk capacity after expansion.
    #     """
    #     res = self._get_resource(_volume.VolumeAction, None)
    #     res.set_new_size(self._session, volume_id, new_size)
    #
    # def set_volume_bootable(self, volume, bootable):
    #     """Configuring bootable for an block_store disk
    #
    #     :param volume: The value can be the ID of a volume
    #                    or a :class:`~openstack.block_store.v2.volume.Volume`
    #                    instance.
    #     :param bootable: Whether to configure bootable for disk.
    #     """
    #     res = self._get_resource(_volume.Volume, volume)
    #     volume_action = self._get_resource(_volume.VolumeAction, None)
    #     volume_action.set_bootable(self._session, res.id, bootable)
    #
    # def set_volume_readonly(self, volume, readonly):
    #     """Configuring Read-Only attribute for an block_store disk
    #
    #     :param volume: The value can be the ID of a volume
    #                    or a :class:`~openstack.block_store.v2.volume.Volume`
    #                    instance.
    #     :param readonly: The readonly flag of disk.
    #     """
    #     res = self._get_resource(_volume.Volume, volume)
    #     volume_action = self._get_resource(_volume.VolumeAction, None)
    #     volume_action.set_readonly(self._session, res.id, readonly)
    #
    # def export_image_by_volume(self, volume_id, **data):
    #     """Exporting Disk Data as an Image.
    #
    #     :param volume_id: The ID of a volume.
    #     :param data: Keyword arguments which will be used to export image.
    #     :return: :class:`~openstack.block_store.v2.volume.ExportImageByVolume`
    #     """
    #     return self._create(_volume.ExportImageByVolume, volume_id=volume_id, **data)
    #
    # def update_snapshot(self, snapshot, **attrs):
    #     """Updating an block_store snapshot
    #
    #     :param snapshot: The value can be the ID of a snapshot
    #             or a :class: `~openstack.block_store.v2.snapshot.Snapshot`
    #             instance.
    #     :param dict attrs: Keyword arguments which will be used to create
    #             a :class:`~openstack.block_store.v2.snapshot.Snapshot`,
    #             comprised of the properties on the Snapshot class.
    #
    #     :returns: The updated snapshot
    #     :rtype: :class:`openstack.block_store.v2.snapshot.Snapshot`
    #     """
    #     return self._update(_snapshot.Snapshot, snapshot, **attrs)
    #
    # def create_snapshot_metadata(self, snapshot, **metadata):
    #     """Adding metadata of an block_store snapshot
    #
    #     :param snapshot: The value can be the ID of a snapshot
    #                    or a :class:`~openstack.block_store.v2.snapshot.Snapshot`
    #                    instance.
    #     :param dict metadata: Keyword arguments which will be used to create
    #                        a :class:`~openstack.block_store.v2.snapshot.SnapshotMetadata`,
    #                        comprised of the properties on the SnapshotMetadata
    #                        class.
    #
    #     :returns: the metadata of an block_store snapshot
    #     :rtype: :class:`~openstack.block_store.v2.snapshot.SnapshotMetadata`
    #     """
    #     res = self._get_resource(_snapshot.Snapshot, snapshot)
    #     res_metadata = self._get_resource(_snapshot.SnapshotMetadata, None)
    #     return res_metadata.create_metadata(self._session, res.id, metadata)
    #
    # def update_snapshot_metadata(self, snapshot, key=None, **metadata):
    #     """Updating metadata of an block_store snapshot
    #
    #     :param snapshot: The value can be the ID of a snapshot
    #                    or a :class:`~openstack.block_store.v2.snapshot.Snapshot`
    #                    instance.
    #     :param key: The key of metadata that requires the update.
    #     :param dict metadata: Keyword arguments which will be used to create
    #                        a :class:`~openstack.block_store.v2.snapshot.SnapshotMetadata`,
    #                        comprised of the properties on the SnapshotMetadata
    #                        class.
    #
    #     :returns: The metadata of an block_store snapshot
    #     :rtype: :class:`~openstack.blcok_store.v2.snapshot.SnapshotMetadata`
    #     """
    #     res = self._get_resource(_snapshot.Snapshot, snapshot)
    #     res_metadata = self._get_resource(_snapshot.SnapshotMetadata, None)
    #     return res_metadata.update_metadata(self._session, res.id, metadata, key)
    #
    # def delete_snapshot_metadata(self, snapshot, key, ignore_missing=True):
    #     """Deleting one piece of block_store disk snapshot metadata
    #
    #     :param snapshot: The value can be the ID of a snapshot
    #                    or a :class:`~openstack.block_store.v2.snapshot.Snapshot`
    #                    instance.
    #     :param key: The key of the metadata that requires the deletion.
    #     :param bool ignore_missing: When set to ``False``
    #                 :class:`~openstack.exceptions.ResourceNotFound` will be
    #                 raised when the metadata does not exist.
    #                 When set to ``True``, no exception will be set when
    #                 attempting to delete a nonexistent metadata.
    #
    #     :returns: ``None``
    #     """
    #     res = self._get_resource(_snapshot.Snapshot, snapshot)
    #     metadata = self._get_resource(_snapshot.SnapshotMetadata, None)
    #     metadata.delete_metadata(self._session, res.id, key,
    #                              ignore_missing=ignore_missing)
    #
    # def get_snapshot_metadata(self, snapshot, key=None):
    #     """Querying block_store snapshot metadata
    #
    #     :param snapshot: The value can be the ID of a snapshot
    #                    or a :class:`~openstack.block_store.v2.snapshot.Snapshot`
    #                    instance.
    #     :param key: The key of the metadata to be queried.
    #
    #     :returns: The metadata of an block_store snapshot
    #     :rtype: :class:`~openstack.block_store.v2.snapshot.SnapshotMetadata`
    #     """
    #     res = self._get_resource(_snapshot.Snapshot, snapshot)
    #     metadata = self._get_resource(_snapshot.SnapshotMetadata, None)
    #     return metadata.get_metadata(self._session, res.id, key)
    #
    # def extensions(self):
    #     """Retrieve a generator of extensions
    #
    #     :returns: A generator of extension objects.
    #     """
    #     return self._list(_extension.Extension)
    #
    # def availability_zones(self):
    #     """Retrieve a generator of availability zones.
    #
    #     :return: A generator of availability zones objects.
    #     """
    #     return self._list(_availability_zone.AvailabilityZone)
    #
    # def create_volume_transfer(self, **data):
    #     """Create a volume transfer.
    #
    #     :param data: Keyword arguments which will be used to create.
    #     :return: :class:`~openstack.block_store.v2.volume_transfer.VolumeTransfer`
    #     """
    #     return self._create(_volume_transfer.VolumeTransfer, **data)
    #
    # def delete_volume_transfer(self, volume_transfer_id, ignore_missing=True):
    #     """Delete a volume transfer.
    #
    #     :param volume_transfer_id: The id of volume transfer.
    #     :param ignore_missing: When set to ``False``
    #                 :class:`~openstack.exceptions.ResourceNotFound` will be
    #                 raised when the metadata does not exist.
    #                 When set to ``True``, no exception will be set when
    #                 attempting to delete a nonexistent metadata.
    #     """
    #     self._delete(_volume_transfer.VolumeTransfer, volume_transfer_id, ignore_missing=ignore_missing)
    #
    # def get_volume_transfer(self, volume_transfer_id):
    #     """Get a volume transfer.
    #
    #     :param volume_transfer_id: The id of volume transfer.
    #     :return: :class:`~openstack.block_store.v2.volume_transfer.VolumeTransfer`
    #     """
    #     return self._get(_volume_transfer.VolumeTransfer, volume_transfer_id)
    #
    # def volume_transfers(self, details=True, **query):
    #     """Retrieve a generator of volume transfers.
    #
    #     :param details: Need more details.
    #     :param query: Keyword arguments which will be used to query.
    #     :return: A generator of volume transfers.
    #     """
    #     resource_type = _volume_transfer.VolumeTransferDetail if details else _volume_transfer.VolumeTransfer
    #     return self._list(resource_type, paginated=True, **query)
    #
    # def accept_volume_transfer(self, volume_transfer_id, **data):
    #     """Accept the volume transfer.
    #
    #     :param volume_transfer_id: The id of volume transfer.
    #     :param data: Keyword arguments which will be used to accept transfer.
    #     :return: :class:`~openstack.block_store.v2.volume_transfer.VolumeTransferAccept`
    #     """
    #     return self._create(
    #         _volume_transfer.VolumeTransferAccept,
    #         prepend_key=False,
    #         transfer_id=volume_transfer_id,
    #         **data
    #     )
    #
    # def versions(self, v2=False):
    #     """Retrieve a generator of API versions
    #
    #     :param v2: Whether query v2.
    #     :returns: A generator of version objects.
    #     """
    #     res = _version.VersionV2 if v2 else _version.Version
    #     return self._list(res)
