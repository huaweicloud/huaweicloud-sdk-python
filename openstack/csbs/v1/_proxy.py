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

from openstack import proxy2
from openstack.csbs.v1 import checkpoint_item as _checkpoint_item
from openstack.csbs.v1 import checkpoint as _checkpoint


class Proxy(proxy2.BaseProxy):
    """Proxy of csbs service."""

    def get_checkpoint_item(self, checkpoint_item_id):
        """Get a checkpoint item.

        :param checkpoint_item_id: Id of checkpoint item.
        :return: :class:`~openstack.csbs.v1.checkpoint_item.CheckpointItem`
        """
        return self._get(_checkpoint_item.CheckpointItem, checkpoint_item_id)

    def checkpoint_items(self, **data):
        """List checkpoint item.

        :param data: Query conditions.
        :return: A generator of checkpoint item instances.
        """
        return self._list(_checkpoint_item.CheckpointItem, **data)

    def get_checkpoint_item_count(self, **data):
        """Get count of checkpoint item.

        :param data: Query conditions.
        :return: :class:`~openstack.csbs.v1.checkpoint_item.CheckpointItemCount`
        """
        res = self._get_resource(_checkpoint_item.CheckpointItemCount, None)
        return res.get(self._session, requires_id=False, **data)

    def create_checkpoint(self, provider_id, **data):
        """Create a checkpoint record by policy.

        :param provider_id: Id of backup provider.
        :param data: Keyword arguments which will be used to create.
        :return: :class:`~openstack.csbs.v1.checkpoint.Checkpoint`
        """
        return self._create(_checkpoint.Checkpoint, provider_id=provider_id, **data)

    def delete_checkpoint(self, checkpoint_id, provider_id, ignore_missing=True, **data):
        """Delete checkpoint item.

        :param checkpoint_id: Id of checkpoint record.
        :param provider_id: Id of backup provider.
        :param ignore_missing: Ignore missing or error.
        :param data: Delete conditions.
        :return: None
        """
        res = self._get_resource(_checkpoint.Checkpoint, checkpoint_id, provider_id=provider_id)
        return res.delete(self._session, ignore_missing=ignore_missing, **data)
