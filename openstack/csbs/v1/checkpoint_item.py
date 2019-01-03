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


class CheckpointItem(resource2.Resource):
    """Create a checkpoint_item resource."""

    service = csbs_service.CsbsService()

    base_path = '/checkpoint_items'
    resource_key = 'checkpoint_item'
    resources_key = 'checkpoint_items'

    # Allowed operations on this resource.
    allow_get = True
    allow_list = True

    # Query conditions in list operation.
    _query_mapping = resource2.QueryParameters(
        'status',
        'limit',
        'marker',
        'sort',
        'all_tenants',
        'name',
        'az',
        'resource_id',
        'resource_name',
        'start_time',
        'end_time',
        'image_type',
        'policy_id',
        'ip',
        'offset',
        'checkpoint_id',
        'resource_type',
        'dec'
    )

    # Id of checkpoint.
    checkpoint_id = resource2.Body('checkpoint_id')
    # Create time.
    created_at = resource2.Body('created_at')
    # Extend infomation.
    extend_info = resource2.Body('extend_info', type=dict)
    # Id of checkpoint item.
    id = resource2.Body('id')
    # Name of checkpoint item.
    name = resource2.Body('name')
    # Id of backup object.
    resource_id = resource2.Body('resource_id')
    # Status of checkpoint item.
    status = resource2.Body('status')
    # Update time.
    updated_at = resource2.Body('updated_at')
    # Metadata of VM.
    backup_data = resource2.Body('backup_data', type=dict)
    # Description of checkpoint item.
    description = resource2.Body('description')
    # Type of backup object.
    resource_type = resource2.Body('resource_type')
    # Copy the list of records.
    replication_records = resource2.Body('replication_records', type=list)
    # Backup data time point.
    protected_at = resource2.Body('protected_at')


class CheckpointItemCount(resource2.Resource):
    """Create a checkpoint_item_count resource."""

    service = csbs_service.CsbsService()

    base_path = '/checkpoint_items/count'

    # Allowed operations on this resource.
    allow_get = True

    # Query conditions in get operation.
    _query_mapping = resource2.QueryParameters(
        'status',
        'marker',
        'sort',
        'all_tenants',
        'name',
        'az',
        'resource_id',
        'resource_name',
        'start_time',
        'end_time',
        'image_type',
        'policy_id',
        'ip',
        'offset',
        'checkpoint_id',
        'resource_type',
        'dec'
    )
    # limit has removed from query filter
    _query_mapping._mapping.pop("limit", None)

    # Count of checkpoint item.
    count = resource2.Body('count', type=int)

    def get(self, session, requires_id=True, **data):
        """Get a remote resource based on this instance.

        :param session: The session to use for making this request.
        :param requires_id: A boolean indicating whether resource ID
                            should be part of the requested URI.
        :param data: Query conditions in get operation.
        :return: This :class:`Resource` instance.
        """
        if not self.allow_get:
            raise exceptions.MethodNotSupported(self, "get")

        request = self._prepare_request(requires_id=requires_id)
        endpoint_override = self.service.get_endpoint_override()
        query_params = self._query_mapping._transpose(data)
        response = session.get(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               params=query_params)

        self._translate_response(response)
        return self
