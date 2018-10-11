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

from openstack.cts.v1 import trace as _trace
from openstack.cts.v1 import tracker as _tracker
from openstack import proxy2


class Proxy(proxy2.BaseProxy):

    def create_tracker(self, **kwargs):
        """Create tracker

        :param dict kwargs: Keyword arguments which will be used to overwrite a
                            :class:`~openstack.cts.v1.tracker.Tracker`
        :returns: A instance of Tracker object
        :rtype: :class:`~openstack.cts.v1.tracker.Tracker`
        """
        return self._create(_tracker.Tracker, **kwargs)

    def update_tracker(self, tracker, **kwargs):
        """Update tracker

        :param tracker: tracker name or a object of
                        :class:`~openstack.cts.v1.tracker.Tracker`
        :param dict kwargs: Keyword arguments which will be used to overwrite a
                            :class:`~openstack.cts.v1.tracker.Tracker`
        :returns: A instance of Tracker object
        :rtype: :class:`~openstack.cts.v1.tracker.Tracker`
        """
        return self._update(_tracker.Tracker, tracker, **kwargs)

    def get_tracker(self, name='system'):
        """Query a tracker by name

        :param name: tracker name, default is system
        :returns: A instance of Tracker object
        :rtype: :class:`~openstack.cts.v1.tracker.Tracker`
        """
        _tracker.Tracker.list(self._session, tracker_name=name)

    def delete_tracker(self, tracker='system', ignore_missing=True):
        """Delete a tracker

        :param tracker: tracker name or
               :class:`~openstack.smn.v2.message_template.MessageTemplate`

        :param bool ignore_missing: When set to ``False``
                       :class:`~openstack.exceptions.ResourceNotFound` will be
                       raised when the stack does not exist.
                       When set to ``True``, no exception will be set when
                       attempting to delete a nonexistent message template.
        :returns: None
        """
        self._delete(_tracker.Tracker, tracker, ignore_missing=ignore_missing)

    def traces(self, tracker='system', **query):
        """List of the trace of a give tracker

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        """
        if isinstance(tracker, _tracker.Tracker):
            tracker_name = tracker.tracker_name
        else:
            tracker_name = tracker

        return self._list(_trace.Trace, tracker_name=tracker_name, **query)

    def traces_v2(self, tracker='system', **query):
        """List of the trace of a give tracker

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        """
        if isinstance(tracker, _tracker.Tracker):
            tracker_name = tracker.tracker_name
        else:
            tracker_name = tracker

        return self._list(_trace.TraceV2, tracker_name=tracker_name, **query)
