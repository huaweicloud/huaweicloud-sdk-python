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
#      Huawei has modified this source file.
#            Copyright 2018 Huawei Technologies Co., Ltd.
#            Licensed under the Apache License, Version 2.0 (the "License"); you may not
#            use this file except in compliance with the License. You may obtain a copy of
#            the License at
#
#                http://www.apache.org/licenses/LICENSE-2.0
#
#            Unless required by applicable law or agreed to in writing, software
#            distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#            WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#            License for the specific language governing permissions and limitations under
#            the License.

from openstack.compute import compute_service
from openstack import resource2


class VolumeAttachment(resource2.Resource):
    resource_key = 'volumeAttachment'
    resources_key = 'volumeAttachments'
    base_path = '/servers/%(serverId)s/os-volume_attachments'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = False
    allow_delete = True
    allow_list = True

    #: Name of the device such as, /dev/vdb.
    device = resource2.Body('device')
    #: The ID of the attachment.
    id = resource2.Body('id')
    #: The ID for the server.
    server_id = resource2.URI('serverId')
    #: The ID of the attached volume.
    volume_id = resource2.Body('volumeId')
    # attachment id
    attachment_id = resource2.Body('attachment_id', alternate_id=True)
