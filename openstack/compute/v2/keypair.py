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

from openstack.compute import compute_service
from openstack import resource2


class Keypair(resource2.Resource):
    resource_key = 'keypair'
    resources_key = 'keypairs'
    base_path = '/os-keypairs'
    service = compute_service.ComputeService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_delete = True
    allow_list = True

    # Properties
    #: The short fingerprint associated with the ``public_key`` for
    #: this keypair.
    fingerprint = resource2.Body('fingerprint')
    # NOTE: There is in fact an 'id' field. However, it's not useful
    # because all operations use the 'name' as an identifier.
    # Additionally, the 'id' field only appears *after* creation,
    # so suddenly you have an 'id' field filled in after the fact,
    # and it just gets in the way. We need to cover this up by having
    # the name be both our id and name.
    #: The id identifying the keypair
    id = resource2.Body('name')
    #: A name identifying the keypair
    name = resource2.Body('name', alternate_id=True)
    #: The private key for the keypair
    private_key = resource2.Body('private_key')
    #: The SSH public key that is paired with the server.
    public_key = resource2.Body('public_key')
    #: The type of keypair.
    type = resource2.Body('type')
    #: Create time of the keypair.
    created_at = resource2.Body('created_at')
    #: Keypair deletion tag.*Type: bool*.
    deleted = resource2.Body('deleted', type=bool)
    #: Delete time of the keypair.
    deleted_at = resource2.Body('deleted_at')
    #: Update time of the keypair.
    updated_at = resource2.Body('updated_at')
    #: User information to which the keypair belongs.
    user_id = resource2.Body('user_id')

    @classmethod
    def list(cls, session, paginated=False):
        endpoint_override = cls.service.get_endpoint_override()
        resp = session.get(cls.base_path, endpoint_filter=cls.service,
                           headers={"Accept": "application/json"}, endpoint_override = endpoint_override)
        resp = resp.json()
        resp = resp[cls.resources_key]

        for data in resp:
            value = cls.existing(**data[cls.resource_key])
            yield value
