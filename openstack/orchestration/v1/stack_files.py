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

from openstack.orchestration import orchestration_service
from openstack import resource2 as resource


class StackFiles(resource.Resource):

    service = orchestration_service.OrchestrationService()
    base_path = "/stacks/%(stack_name)s/%(stack_id)s/files"

    # capabilities
    allow_create = False
    allow_list = False
    allow_get = True
    allow_delete = False
    allow_update = False

    # Properties
    #: Name of the stack where the template is referenced.
    stack_name = resource.URI('stack_name')
    #: ID of the stack where the template is referenced.
    stack_id = resource.URI('stack_id')

    def get(self, session):
        # The stack files response contains a map of filenames and file
        # contents.
        request = self._prepare_request(requires_id=False)
        endpoint_override = self.service.get_endpoint_override()
        return session.get(request.uri, endpoint_filter=self.service, endpoint_override = endpoint_override)
