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

from openstack.block_store import block_store_service
from openstack import format
from openstack import resource2
from openstack import utils
from openstack import exceptions


class Snapshot(resource2.Resource):
    resource_key = "snapshot"
    resources_key = "snapshots"
    base_path = "/snapshots"
    service = block_store_service.BlockStoreService()

    _query_mapping = resource2.QueryParameters('all_tenants', 'name', 'status',
                                               'volume_id', "offset")

    # capabilities
    allow_get = True
    allow_create = True
    allow_delete = True
    allow_update = True
    allow_list = True

    # Properties
    #: A ID representing this snapshot.
    id = resource2.Body("id")
    #: Name of the snapshot. Default is None.
    name = resource2.Body("name")

    #: The current status of this snapshot. Potential values are creating,
    #: available, deleting, error, and error_deleting.
    status = resource2.Body("status")
    #: Description of snapshot. Default is None.
    description = resource2.Body("description")
    #: The timestamp of this snapshot creation.
    created_at = resource2.Body("created_at")
    #: Metadata associated with this snapshot.
    metadata = resource2.Body("metadata", type=dict)
    #: The ID of the volume this snapshot was taken of.
    volume_id = resource2.Body("volume_id")
    #: The size of the volume, in GBs.
    size = resource2.Body("size", type=int)
    #: Indicate whether to create snapshot, even if the volume is attached.
    #: Default is ``False``. *Type: bool*
    is_forced = resource2.Body("force", type=format.BoolStr)
    #: Update time.
    updated_at = resource2.Body("updated_at")
    #: Same as name.
    display_name = resource2.Body("display_name")
    #: Same as description.
    display_description = resource2.Body("display_description")
    #: The percentage of completeness the snapshot is currently at.
    progress = resource2.Body("os-extended-snapshot-attributes:progress")
    #: The project ID this snapshot is associated with.
    project_id = resource2.Body("os-extended-snapshot-attributes:project_id")



class SnapshotDetail(Snapshot):

    base_path = "/snapshots/detail"




class SnapshotMetadata(resource2.Resource):
    base_path = '/snapshots'
    service = block_store_service.BlockStoreService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True

    # Properties
    #: The disk snapshot information
    meta = resource2.Body('meta')
    metadata = resource2.Body('metadata')

    def _operate_metadata(self, method, url, has_body=True, **kwargs):
        request = self._prepare_request(requires_id=False)
        request.uri = url
        endpoint_override = self.service.get_endpoint_override()
        response = method(request.uri,
                          endpoint_filter=self.service,
                          endpoint_override=endpoint_override,
                          **kwargs)
        self._translate_response(response, has_body)
        return self

    def create_metadata(self, session, snapshot_id, metadata):
        url = utils.urljoin(self.base_path, snapshot_id, 'metadata')
        d = {
            'json': metadata,
            'headers': {},
        }
        return self._operate_metadata(session.post, url, **d)

    def get_metadata(self, session, snapshot_id, key=None):
        if key:
            url = utils.urljoin(self.base_path, snapshot_id, 'metadata', key)
        else:
            url = utils.urljoin(self.base_path, snapshot_id, 'metadata')
        return self._operate_metadata(session.get, url)

    def update_metadata(self, session, snapshot_id, metadata, key=None):
        if key:
            url = utils.urljoin(self.base_path, snapshot_id, 'metadata', key)
        else:
            url = utils.urljoin(self.base_path, snapshot_id, 'metadata')
        if key and metadata.get('meta'):
            for k in list(metadata['meta'].keys()):
                if not k == key:
                    del metadata[k]
        d = {
            'json': metadata,
            'headers': {},
        }
        return self._operate_metadata(session.put, url, **d)

    def delete_metadata(self, session, snapshot_id, key, ignore_missing):
        url = utils.urljoin(self.base_path, snapshot_id, 'metadata', key)
        d = {
            'headers': {'Accept': ''},
            'params': None
        }
        try:
            self._operate_metadata(session.delete, url, has_body=False, **d)
        except exceptions.NotFoundException as e:
            if ignore_missing:
                return None
            else:
                # Reraise with a more specific type and message
                raise exceptions.ResourceNotFound(
                    message="No %s found for %s" %
                            (self.__name__, key),
                    details=e.details, response=e.response,
                    request_id=e.request_id, url=e.url, method=e.method,
                    http_status=e.http_status, cause=e.cause, code=e.code)
