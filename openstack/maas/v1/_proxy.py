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

from openstack.maas.v1 import task as _task
from openstack.maas.v1 import version as _version
from openstack import proxy2


class Proxy(proxy2.BaseProxy):

    def versions(self):
        """Get support versions list

        :returns: A generator of Version object
        :rtype: :class:`~openstack.maas.v1.version.Version`
        """
        return self._list(_version.Version, paginated=False)

    def tasks(self, **query):
        """Query all tasks of a tenant

        :param dict query: Dict of query parameters, possible keys are `start`,
                           `limit`, `state` of the migration task.
        :returns: A generator of migration task object
        :rtype: :class:`~openstack.maas.v1.task.Task`
        """
        return self._list(_task.Task, paginated=False, **query)

    def create_task(self, **kwargs):
        """Create a migrate task

        :param dict kwargs: Keyword arguments which will be used to overwrite a
                            :class:`~openstack.maas.v1.task.Task`
        :rtype: :class:`~openstack.maas.v1.task.Task`
        """
        return self._create(_task.Task, **kwargs)

    def delete_task(self, task, ignore_missing=True):
        """Delete a migrate task, can not delete a running task.

        :param task: The task id or an instance of
                     :class:`~openstack.maas.v1.task.Task`

        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the task does not exist.
        :returns: ``None``
        """
        self._delete(_task.Task, task, ignore_missing=ignore_missing)

    def get_task(self, task_id):
        """Get detail about a given migration task id

        :param task_id: The task id or an instance of
                        :class:`~openstack.maas.v1.task.Task`

        :rtype: :class:`~openstack.maas.v1.task.Task`
        """
        return self._get(_task.Task, task_id)

    def start_task(self, task, source_ak, source_sk, target_ak, target_sk):
        """Start a migration task

        :param task_id: The task id or an instance of
                        :class:`~openstack.maas.v1.task.Task`
        :param source_ak: Source node ak
        :param source_sk: Source node sk
        :param target_ak: Target node ak
        :param target_sk: Target node sk

        :returns: Action successful or not
        :rtype: bool
        """
        if isinstance(task, _task.Task):
            task_obj = task
        else:
            task_obj = _task.Task.existing(id=task)

        return task_obj.start(self._session,
                              source_ak, source_sk,
                              target_ak, target_sk)

    def stop_task(self, task):
        """Stop a migration task

        :param task_id: The task id or an instance of
                        :class:`~openstack.maas.v1.task.Task`

        :returns: Action successful or not
        :rtype: bool
        """
        if isinstance(task, _task.Task):
            task_obj = task
        else:
            task_obj = _task.Task.existing(id=task)

        return task_obj.stop(self._session)

    def task_count(self, state=None):
        """Return total migrate task with state

        :param state: The state of task, can be 0-5, or None
        :returns: count number
        :rtype: int
        """
        return _task.Task.task_count(self._session, state)
