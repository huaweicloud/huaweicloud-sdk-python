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
from openstack.ims import ims_service
from openstack import exceptions


class CloudImage(resource2.Resource):
    """Define a CloudImage class."""

    service = ims_service.ImsService()

    base_path = '/cloudimages'
    resources_key = 'images'

    # Allow operation for this resource.
    allow_list = True
    allow_update = True
    patch_update = True

    # Mapping of accepted query parameter names.
    _query_mapping = resource2.QueryParameters(
        '__isregistered',
        '__imagetype',
        'protected',
        'visibility',
        'owner',
        'id',
        'status',
        'name',
        'container_format',
        'disk_format',
        'min_ram',
        'min_disk',
        '__os_bit',
        '__platform',
        'marker',
        'limit',
        'sort_key',
        'sort_dir',
        '__os_type',
        'tag',
        'member_status',
        '__support_kvm',
        '__support_xen',
        '__support_diskintensive',
        '__support_highperformance',
        '__support_xen_gpu_type',
        'virtual_env_type',
        'enterprise_project_id'
    )

    # Image file download and upload link.
    file = resource2.Body('file')
    # Which tenant the image belongs to.
    owner = resource2.Body('owner')
    # Id of image.
    id = resource2.Body('id')
    size = resource2.Body('size', type=int)
    # Mirror link information.
    # warning: the self is a python keyword, maybe cause init error
    self = resource2.Body('self')
    # Mirror view.
    schema = resource2.Body('schema')
    # Mirror status.
    status = resource2.Body('status')
    # List of image's tags.
    tags = resource2.Body('tags', type=list)
    # Whether it is visible to other tenants.
    visibility = resource2.Body('visibility')
    # Name of image.
    name = resource2.Body('name')
    checksum = resource2.Body('checksum')
    # Whether it is a deleted image.
    deleted = resource2.Body('deleted', type=bool)
    # Whether it is a protected image.
    protected = resource2.Body('protected', type=bool)
    # Container type.
    container_format = resource2.Body('container_format')
    # The mirror runs the minimum memory.
    min_ram = resource2.Body('min_ram', type=int)
    # The maximum memory supported by the image.
    max_ram = resource2.Body('max_ram')
    # Update time.
    updated_at = resource2.Body('updated_at')
    # The number of operating system bits.
    __os_bit = resource2.Body('__os_bit')
    os_bit = resource2.Body('__os_bit')
    # The specific version of the operating system.
    __os_version = resource2.Body('__os_version')
    os_version = resource2.Body('__os_version')
    # Image description information.
    __description = resource2.Body('__description')
    description = resource2.Body('__description')
    # Mirrored format.
    disk_format = resource2.Body('disk_format')
    # Whether it is a registered image.
    __isregistered = resource2.Body('__isregistered')
    isregistered = resource2.Body('__isregistered')
    # Mirror platform classification.
    __platform = resource2.Body('__platform')
    platform = resource2.Body('__platform')
    # Operating system type.
    __os_type = resource2.Body('__os_type')
    os_type = resource2.Body('__os_type')
    # The smallest disk required for mirroring to run.
    min_disk = resource2.Body('min_disk', type=int)
    # The image uses the environment type.
    virtual_env_type = resource2.Body('virtual_env_type')
    # Mirror backend storage type.
    __image_source_type = resource2.Body('__image_source_type')
    image_source_type = resource2.Body('__image_source_type')
    # Mirror type.
    __imagetype = resource2.Body('__imagetype')
    imagetype = resource2.Body('__imagetype')
    # Create time.
    created_at = resource2.Body('created_at')
    virtual_size = resource2.Body('virtual_size', type=int)
    # Delete time.
    deleted_at = resource2.Body('deleted_at')
    # Parent image ID.
    __originalimagename = resource2.Body('__originalimagename')
    originalimagename = resource2.Body('__originalimagename')
    # Backup ID.
    __backup_id = resource2.Body('__backup_id')
    backup_id = resource2.Body('__backup_id')
    # The product ID of the market image.
    __productcode = resource2.Body('__productcode')
    productcode = resource2.Body('__productcode')
    # The size of the image file.
    __image_size = resource2.Body('__image_size')
    image_size = resource2.Body('__image_size')
    # Mirror source.
    __data_origin = resource2.Body('__data_origin')
    data_origin = resource2.Body('__data_origin')
    # Support kvm.
    __support_kvm = resource2.Body('__support_kvm')
    support_kvm = resource2.Body('__support_kvm')
    # Support xen.
    __support_xen = resource2.Body('__support_xen')
    support_xen = resource2.Body('__support_xen')
    # Support for dense storage.
    __support_diskintensive = resource2.Body('__support_diskintensive')
    support_diskintensive = resource2.Body('__support_diskintensive')
    # Support high computing performance.
    __support_highperformance = resource2.Body('__support_highperformance')
    support_highperformance = resource2.Body('__support_highperformance')
    # Support for GPU optimization types under the XEN virtualization platform.
    __support_xen_gpu_type = resource2.Body('__support_xen_gpu_type')
    support_xen_gpu_type = resource2.Body('__support_xen_gpu_type')
    # support for fpga types under kvm virtualization platform
    __support_kvm_fpga_type = resource2.Body('__support_kvm_fpga_type')
    support_kvm_fpga_type = resource2.Body('__support_kvm_fpga_type')
    # Indicates whether the current image supports publishing as a market image.
    __system_support_market = resource2.Body('__system_support_market', type=bool)
    system_support_market = resource2.Body('__system_support_market', type=bool)
    # Indicates the enterprise project to which the current image belongs.
    enterprise_project_id = resource2.Body('enterprise_project_id')
    # Indicates that the current image source is imported from the outside.
    __root_origin = resource2.Body('__root_origin')
    root_origin = resource2.Body('__root_origin')
    # Corresponds to the system disk slot location of the cloud server.
    __sequence_num = resource2.Body('__sequence_num')
    sequence_num = resource2.Body('__sequence_num')
    hw_vif_multiqueue_enabled = resource2.Body('hw_vif_multiqueue_enabled')
    # lazy loading
    __lazyloading = resource2.Body("__lazyloading", type=bool)
    lazyloading = resource2.Body("__lazyloading", type=bool)

    def update(self, session, prepend_key=True, has_body=True, **data):
        """Update the remote resource based on this instance.

        :param session: The session to use for making this request.
        :param prepend_key: A boolean indicating whether the resource_key
                            should be prepended in a resource update request.
                            Default to True.
        :param has_body: Whether to return the body.
        :param data: The property that needs to be updated.
        :return: This :class:`Resource` instance.
        """
        # The id cannot be dirty for an update
        self._body._dirty.discard("id")
        id_mapping_name = self._body_mapping()["id"]
        self._body._dirty.discard(id_mapping_name)

        if not self.allow_update:
            raise exceptions.MethodNotSupported(self, "update")

        request = self._prepare_request(prepend_key=prepend_key)

        endpoint_override = self.service.get_endpoint_override()
        patch_body = [data]
        if self.patch_update:
            response = session.patch(request.uri, endpoint_filter=self.service,
                                     endpoint_override=endpoint_override,
                                     json=patch_body,
                                     headers=request.headers)
        else:
            response = session.put(request.uri, endpoint_filter=self.service,
                                   endpoint_override=endpoint_override,
                                   json=patch_body, headers=request.headers)

        self._translate_response(response, has_body=has_body)
        return self


class CloudImageAction(resource2.Resource):
    """Define a CloudImage class."""

    service = ims_service.ImsService()

    base_path = '/cloudimages/action'

    # Allow operation for this resource.
    allow_create = True

    # Name of image.
    name = resource2.Body('name')
    # Description of image.
    description = resource2.Body('description')
    # The cloud server ID that needs to be converted.
    instance_id = resource2.Body('instance_id')
    # Data disk information to be converted.
    data_images = resource2.Body('data_images', type=list)
    # Mirror tag list.
    # Tags and image_tags can only use one.
    tags = resource2.Body('tags', type=list)
    # A list of mirrored labels for the new specification.
    # Tags and image_tags can only use one.
    image_tags = resource2.Body('image_tags', type=list)
    # The enterprise project id to which the current image belongs.
    enterprise_project_id = resource2.Body('enterprise_project_id')

    # Operating system version.
    os_version = resource2.Body('os_version')
    # External mirror file address in the OBS bucket.
    image_url = resource2.Body('image_url')
    # Minimum system disk size.
    min_disk = resource2.Body('min_disk', type=int)
    # Whether it is automatically configured.
    is_config = resource2.Body('is_config', type=bool)
    # Create a user master key for the encrypted image.
    cmk_id = resource2.Body('cmk_id')
    # Type of image.
    type = resource2.Body('type')

    # Id of job.
    job_id = resource2.Body('job_id')
    # Indicates the maximum memory supported by the image in MB.
    max_ram = resource2.Body("max_ram", type=int)
    # Indicates the minimum memory required for mirroring. The unit is MB. The default is 0, which means unlimited.
    min_ram = resource2.Body("min_ram", type=int)
    # is config init
    is_config_init = resource2.Body("is_config_init", type=bool)

