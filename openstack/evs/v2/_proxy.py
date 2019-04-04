# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
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

from openstack import proxy2
from openstack.evs.v2 import volume as _volume
from openstack.evs.v2 import volume_ext as _volume_ext
# from openstack.evs.v2 import snapshot as _snapshot
from openstack.evs.v2 import job as _job

class Proxy(proxy2.BaseProxy):

    def get_job(self, job_id):
        """
        get method to retrieve a task(job)
        :param job_id: id of job, that from a response
        :return: :class:`~openstack.evs.v2.job.Job`
        """
        _job.Job =  self._get(_job.Job, job_id)
        return _job.Job

    def create_volume(self, **attrs):
        """Create a new volume from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.evs.v2.volume.Volume`,
                           comprised of the properties on the Volume class.

        :returns: The results of volume creation
        :rtype: :class:`~openstack.evs.v2.volume.Volume`
        """
        resource_key = _volume.Volume.resource_key
        attrs = attrs.get(resource_key, attrs)
        return self._create(_volume.Volume, **attrs)

    def resize_volume(self, volume_id, **data):
        """
        post method to modify volume size
        :param volume_id: EVS volume_id
        :param data:
        :return: class:`~openstack.evs.v2.volume.ResizeVolume`
        """
        return self._create(_volume.ResizeVolume, volume_id=volume_id, **data)

    def create_volume_ext(self, **attrs):
        """Create a new volume from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.evs.v2.volume_ext.Volume`,
                           comprised of the properties on the Volume class.

        :returns: The results of volume creation
        :rtype: :class:`~openstack.evs.v2.volume_ext.Volume`
        """
        return self._create(_volume_ext.VolumeExt, **attrs)

    def resize_volume_ext(self, volume_id, **data):
        """
        post method to modify volume size
        :param volume_id: EVS volume_id
        :param data:
        :return: class:`~openstack.evs.v2.volume_ext.ResizeVolume`
        """
        return self._create(_volume_ext.ResizeVolume, volume_id=volume_id, **data)

    def update_volume(self, volume_id, **data):
        """
        Update a volume.
        :param volume_id: Id of volume.
        :param data: Keyword arguments which will be used to update.
        :return: class:`~openstack.evs.v2.volume.Volume`
        """
        return self._update(_volume.Volume, volume_id, **data)

    def get_volume(self, volume_id):
        """
        Get a volume.
        :param volume_id: Id of volume.
        :return: class:`~openstack.evs.v2.volume.Volume`
        """
        return self._get(_volume.Volume, volume_id)

    def volumes(self, **query):
        """Retrieve a generator of volumes

        :param kwargs query: Optional query parameters to be sent to limit
            the volumes being returned.  Available parameters include:

            * name: Name of the volume as a string.
            * status: Value of the status of the volume so that you can filter
                    on "available" for example.
            * marker: Specifies the last item on the previous page when the
            query results are displayed on multiple
                    pages.
            * limit: Specifies the maximum number of query results that can be
                    returned.
            * sort_key: Specifies the keyword based on which the returned
                    results are sorted.The value can be id, status, size,
                    created_at, or bootable.
            * sort_dir: Specifies the result sorting order. The value can be
                    desc (descending order) or asc (ascending order).
            * offset: Specifies the offset. If the value is an integer greater
                    than 0 but less than the number of disks,all disks after
                    this offset will be queried.
            * metadata: Specifies the EVS disk metadata.
            * availability_zone: Specifies the AZ.
            * multiattach: Specifies the shared disk information.
            * changes_since: Specifies the time when the disk was updated, for
                    example, 2016-01-08T09:41:18.
            * service_type: Specifies the service type. Currently, the supported
                    service types are EVS, DSS, and DESS.
            * dedicated_storage_id: Specifies the ID of the DSS storage pool.
                    All EVS disks in the DSS storage pool can
                    be filtered out. Only precise match is supported.
            * dedicated_storage_name:Specifies the name of the DSS storage pool.
                    All EVS disks in the DSS storage pool can be filtered
                    out. Fuzzy match is supported.
            * volume_type_id: Specifies the EVS disk type ID.
            * id: Specifies the EVS disk ID.
            * ids: Specifies the EVS disk IDs. The parameter value is in the
                    ids=['id1','id2',...,'idx'] format. In the response, the
                    ids value contains valid disk IDs only. Invalid disk IDs
                    will be ignored.Details about a maximum of 60 EVS disks
                    can be queried.If parameters id and ids are both specified
                    in the request, id will be ignored.
            * server_id: Specifies the server ID.This parameter supports exact
                    match only. That is, the id value must be in the UUID
                    format.
            * backup_id: Specifies the backup ID.This parameter supports exact
                    match only. That is, the id value must be in the UUID
                    format.
            * enterprise_project_id：Specifies the enterprise project ID for
                    filtering.If input parameter all_granted_eps exists, EVS
                    disks in all enterprise projects that are within the
                    permission scope will be queried.

        :returns: A generator of volume objects.
        """
        if query.__contains__("ids"):
            ids = query.get("ids")

            if ids in [None,""]:
                raise Exception(
                    "Invalid input received: Ids filter must be a list."
                )

            ids_str = "["
            for id in ids:
                ids_str = ids_str + "'" + id + "'" + ","
            ids_str = ids_str[:-1] + "]"
            query["ids"] = ids_str

        volume = _volume.VolumeDetail
        res = self._get_resource(volume, value=None, **query)
        return res.list_by_offset(self._session, paginated=True, **query)

    # def rollback_snapshot(self, snapshot_id, **data):
    #     """Rolling back a snapshot to a volume.
    #
    #     :param snapshot_id: The id of snapshot.
    #     :param data: Keyword arguments which will be used to rolling back.
    #     :return: class:`~openstack.evs.v2.snapshot.SnapshotRollback`
    #     """
    #     return self._create(_snapshot.SnapshotRollback, snapshot_id=snapshot_id, **data)
