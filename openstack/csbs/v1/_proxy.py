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
from openstack.csbs.v1 import resource as _resource
from openstack.csbs.v1 import policy as _policy


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

    # def create_resource_backup(self, provider_id, resource_id, **data):
    #     """Create a resource backup.
    #
    #     :param provider_id: Id of provider.
    #     :param resource_id: Id of the backup object.
    #     :param data: Keyword arguments which will be used to create.
    #     :return: :class:`~openstack.csbs.v1.resource.ResourceBackup`
    #     """
    #     return self._create(_resource.ResourceBackup, provider_id=provider_id, resource_id=resource_id, prepend_key=False, **data)
    #
    # def query_resource_backup_capability(self, provider_id, **data):
    #     """Query resource backup capability.
    #
    #     :param provider_id: Id of provider.
    #     :param data: Keyword arguments which will be used to query.
    #     :return: :class:`~openstack.csbs.v1.resource.ResourceBackupCapability`
    #     """
    #     return self._create(_resource.ResourceBackupCapability, provider_id=provider_id, **data)
    #
    # def query_resource_recovery_capability(self, provider_id, **data):
    #     """Query resource recovery capability.
    #
    #     :param provider_id: Id of provider.
    #     :param data: Keyword arguments which will be used to query.
    #     :return: :class:`~openstack.csbs.v1.resource.ResourceRecoveryCapability`
    #     """
    #     return self._create(_resource.ResourceRecoveryCapability, provider_id=provider_id, **data)
    #
    # def create_backup_policy(self, **data):
    #     """Create a backup policy.
    #
    #     :param data: Keyword arguments which will be used to create.
    #     :return: :class:`~openstack.csbs.v1.policy.Policy`
    #     """
    #     return self._create(_policy.Policy, **data)
    #
    # def delete_backup_policy(self, policy_id):
    #     """Delete a backup policy.
    #
    #     :param policy_id: Id of backup policy.
    #     :return: None
    #     """
    #     return self._delete(_policy.Policy, policy_id)
    #
    # def update_backup_policy(self, policy_id, **data):
    #     """Update a backup policy.
    #
    #     :param policy_id: Id of backup policy.
    #     :param data: Keyword arguments which will be used to update.
    #     :return: :class:`~openstack.csbs.v1.policy.Policy`
    #     """
    #     return self._update(_policy.Policy, policy_id, **data)
    #
    # def get_backup_policy(self, policy_id):
    #     """Get a backup policy.
    #
    #     :param policy_id: Id of backup policy.
    #     :return: :class:`~openstack.csbs.v1.policy.Policy`
    #     """
    #     return self._get(_policy.Policy, policy_id)
    #
    # def backup_policys(self, **query):
    #     """List backup policy.
    #
    #     :param query: Keyword arguments which will be used to query.
    #     :return: A generator of backup policy instances.
    #     """
    #     return self._list(_policy.Policy, paginated=True, **query)
