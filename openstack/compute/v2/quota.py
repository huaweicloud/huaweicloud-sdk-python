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

from openstack.compute import compute_service
from openstack import resource2
from openstack import exceptions
from openstack import utils
from openstack.resource2 import _Request

class QuotaDefault(resource2.Resource):
    resource_key = 'quota_set'
    base_path = '/os-quota-sets'
    service = compute_service.ComputeService()
    # capabilities
    allow_get = True

    # Vpcu quantity quota
    cores = resource2.Body("cores", type=int)
    # Fixed IP quantity quota, this parameter is currently not supported
    fixed_ips = resource2.Body("fixed_ips", type=int)
    # Floating IP quantity quota, this parameter is currently not supported
    floating_ips = resource2.Body("floating_ips", type=int)
    # project UUID
    id = resource2.Body("id")
    # File size quota for injecting files, in bytes
    injected_file_content_bytes = resource2.Body("injected_file_content_bytes", type=int)
    # Path size quota for injecting files, in bytes
    injected_file_path_bytes = resource2.Body("injected_file_path_bytes", type=int)
    # Inject file quota
    injected_files = resource2.Body("injected_files", type=int)
    # Cloud server quota
    instances = resource2.Body("instances", type=int)
    # Key pair quantity quota, this parameter is currently not supported
    key_pairs = resource2.Body("key_pairs", type=int)
    # Metadata quota
    metadata_items = resource2.Body("metadata_items", type=int)
    # Memory quota, in MB
    ram = resource2.Body("ram", type=int)
    # Quota for each security group rule, currently does not support this parameter
    security_group_rules = resource2.Body("security_group_rules", type=int)
    # Security group quantity quota, this parameter is currently not supported
    security_groups = resource2.Body("security_groups", type=int)
    # Cloud server group size quota
    server_group_members = resource2.Body("server_group_members", type=int)
    # Cloud server group quota
    server_groups = resource2.Body("server_groups", type=int)

    def _prepare_request(self, requires_id=True, prepend_key=False):
        body = self._body.dirty
        if prepend_key and self.resource_key is not None:
            body = {self.resource_key: body}

        headers = self._header.dirty

        if requires_id:
            if self.id is None:
                raise exceptions.InvalidRequest(
                    "Request requires an ID but none was found")
            uri = utils.urljoin(self.base_path, self.id, "defaults")
        return _Request(uri, body, headers)

class Quota(QuotaDefault):

    def _prepare_request(self, requires_id=False, prepend_key=False):
        body = self._body.dirty
        if prepend_key and self.resource_key is not None:
            body = {self.resource_key: body}
        headers = self._header.dirty
        if requires_id:
            if self.id is None:
                raise exceptions.InvalidRequest(
                    "Request requires an ID but none was found")
            uri = utils.urljoin(self.base_path, self.id)

        return _Request(uri, body, headers)