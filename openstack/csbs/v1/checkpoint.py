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
from openstack.csbs import csbs_service
from openstack import exceptions


class Checkpoint(resource2.Resource):
    """Create a checkpoint resource."""

    service = csbs_service.CsbsService()

    base_path = '/providers/%(provider_id)s/checkpoints'
    resource_key = 'checkpoint'

    # Allowed operations on this resource.
    allow_create = True
    allow_delete = True

    # Query conditions in delete operation.
    _query_mapping = resource2.QueryParameters(
        'checkpoint_items'
    )

    # Id of backup provider.
    provider_id = resource2.URI('provider_id')

    # Backup parameters.
    parameters = resource2.Body('parameters', type=dict)
    # Backup policy id.
    plan_id = resource2.Body('plan_id')
    # Auto trigger.
    auto_trigger = resource2.Body('auto_trigger', type=bool)
    # List of backup object.
    resources = resource2.Body('resources', type=list)

    # Status of checkpoint record.
    status = resource2.Body('status')
    # Create time.
    created_at = resource2.Body('created_at')
    # Id of checkpoint record.
    id = resource2.Body('id')
    # Resource graph.
    resource_graph = resource2.Body('resource_graph')
    # Id of project.
    project_id = resource2.Body('project_id')
    # Backup policy infomation.
    protection_plan = resource2.Body('protection_plan', type=dict)

    def delete(self, session, has_body=False, ignore_missing=True, **data):
        """Delete the remote resource based on this instance.

        :param session: The session to use for making this request.
        :param has_body: Should mapping response body to resource.
        :param ignore_missing: Ignore missing or error.
        :param data: Query conditions in delete operation.
        :return: This :class:`Resource` instance.
        """
        if not self.allow_delete:
            raise exceptions.MethodNotSupported(self, "delete")

        request = self._prepare_request()
        endpoint_override = self.service.get_endpoint_override()
        query_params = self._query_mapping._transpose(data)
        try:
            response = session.delete(request.uri, endpoint_filter=self.service,
                                      endpoint_override=endpoint_override,
                                      headers={"Accept": ""},
                                      params=query_params)
        except exceptions.NotFoundException:
            if ignore_missing:
                return None
            else:
                raise exceptions.ResourceNotFound(
                    message="Not found the resource."
                )

        self._translate_response(response, has_body=has_body)
        return self
