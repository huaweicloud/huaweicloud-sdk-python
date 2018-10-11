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

from openstack.dms.v1 import queue as _queue
from openstack import proxy2


class Proxy(proxy2.BaseProxy):

    def create_queue(self, **kwargs):
        """Create a queue

        :param dict kwargs: Keyword arguments which will be used to overwrite a
                            :class:`~openstack.dms.v1.queue.Queue`
        ::rtype: :class:`~openstack.dms.v1.queue.Queue`
        """
        return self._create(_queue.Queue, **kwargs)

    def queues(self):
        """List all queues

        :returns: A generator of Queue object
        ::rtype: :class:`~openstack.dms.v1.queue.Queue`
        """
        return self._list(_queue.Queue, paginated=False)

    def get_queue(self, queue):
        """Get detail about a given queue id

        :param queue: The queue id or an instance of
                      :class:`~openstack.dms.v1.queue.Queue`
        :returns: one object of class :class:`~openstack.dms.v1.queue.Queue`
        ::rtype: :class:`~openstack.dms.v1.queue.Queue`
        """
        return self._get(_queue.Queue, queue)

    def delete_queue(self, queue, ignore_missing=True):
        """Delete queue

        :param queue: The queue id or an instance of
                      :class:`~openstack.dms.v1.queue.Queue`
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the queue does not exist.
        :returns: ``None``
        """

        self._delete(_queue.Queue, queue, ignore_missing=ignore_missing)

    def create_groups(self, queue, **kwargs):
        """Create a list consume groups for a queue

        :param queue: The queue id or an instance of
                      :class:`~openstack.dms.v1.queue.Queue`
        :param dict kwargs: Keyword arguments which will be used to overwrite a
                            :class:`~openstack.dms.v1.queue.Group`
        :returns: A list of object :class:`~openstack.dms.v1.queue.Group`
        """
        queue_id = queue
        if isinstance(queue, _queue.Queue):
            queue_id = queue.id

        return _queue.Group.create_groups(self._session,
                                          queue_id=queue_id,
                                          **kwargs)

    def groups(self, queue):
        """List all groups for a given queue

        :param queue: The queue id or an instance of
                      :class:`~openstack.dms.v1.queue.Queue`
        :returns: A generator of Group object
        ::rtype: :class:`~openstack.dms.v1.queue.Group`
        """
        queue_id = queue
        if isinstance(queue, _queue.Queue):
            queue_id = queue.id
        return self._list(_queue.Group, queue_id=queue_id, paginated=False)

    def delete_group(self, queue, group):
        """Delete a consume on the queue

        :param queue: The queue id or an instance of
                      :class:`~openstack.dms.v1.queue.Queue`
        :param group: The consume group id or an instance of
                      :class:`~openstack.dms.v1.queue.Group`
        :returns: ``None``
        """
        queue_id = queue
        if isinstance(queue, _queue.Queue):
            queue_id = queue.id

        self._delete(_queue.Group, group, queue_id=queue_id)

    def send_messages(self, queue, **kwargs):
        """Send messages for a given queue

        :param queue: The queue id or an instance of
                      :class:`~openstack.dms.v1.queue.Queue`
        :param dict kwargs: Keyword to create messages
        :returns: dict
        """
        queue_id = queue
        if isinstance(queue, _queue.Queue):
            queue_id = queue.id
        _queue.Message.create_messages(self._session,
                                       queue_id=queue_id, **kwargs)

    def consume_message(self, queue, consume_group, **query):
        """Consume queue's message

        :param queue: The queue id or an instance of
                      :class:`~openstack.dms.v1.queue.Queue`
        :param consume_group: The consume group id or an instance of
                      :class:`~openstack.dms.v1.queue.Group`
        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.
        :returns: A list of object
                  :class:`~openstack.dms.v1.queue.MessageConsume`
        """
        queue_id = queue
        if isinstance(queue, _queue.Queue):
            queue_id = queue.id
        consumer_group_id = consume_group
        if isinstance(queue, _queue.Group):
            consumer_group_id = consume_group.id

        return self._list(_queue.MessageConsume, queue_id=queue_id,
                          consumer_group_id=consumer_group_id, **query)

    def ack_consumed_message(self, consumed_message, status='success'):

        """Confirm consumed message
        :param consumed_message: An object of  instance of

                               :class:`~openstack.dms.v1.queue.MessageConsume`
        :param status: The expeced status of the consumed message
        :returns: An object of an instance of
                  :class:`~openstack.dms.v1.queue.MessageConsume`

        """

        if isinstance(consumed_message, list) and len(consumed_message) > 0:
            msg = consumed_message[0]
        if isinstance(consumed_message, _queue.MessageConsume):
            msg = consumed_message
            consumed_message = [msg]
        return msg.ack(self._session, consumed_message, status=status)

    def quotas(self):
        return self._list(_queue.Quota)
