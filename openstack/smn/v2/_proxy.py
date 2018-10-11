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
from openstack.smn.v2 import message_template as _mt
from openstack.smn.v2 import subscription as _subscription
from openstack.smn.v2 import topic as _topic


class Proxy(proxy2.BaseProxy):

    def create_topic(self, **kwargs):
        """Create a topic

        :param dict kwargs: Keyword arguments which will be used to overwrite a
                            :class:`~openstack.smn.v2.topic.Topic`
        :rtype: :class:`~openstack.smn.v2.topic.Topic
        """
        return self._create(_topic.Topic, **kwargs)

    def update_topic(self, topic, **kwargs):
        """Update topic, only support update display_name for now.

        :param topic: An instance of  :class:`~openstack.smn.v2.topic.Topic`
        :param dict kwargs: Keyword arguments which will be used to overwrite a
                            :class:`~openstack.smn.v2.topic.Topic`
        :rtype: :class:`~openstack.smn.v2.topic.Topic
        """
        return self._update(_topic.Topic, topic, **kwargs)

    def delete_topic(self, topic, ignore_missing=True):
        """Delete topic

        :param task: The topic urn or an instance of
                     :class:`~openstack.smn.v2.topic.Topic`
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the topic does not exist.

        :returns: ``None``
        """
        self._delete(_topic.Topic, topic, ignore_missing=ignore_missing)

    def topics(self, **query):
        """Get all topics

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.
        :returns: A generator of Topic object
        :rtype: :class:`~openstack.smn.v2.topic.Topic
        """
        return self._list(_topic.Topic, paginated=False, **query)

    def get_topic(self, topic):
        """Get detail about a given topic

        :param topic: The topic urn or an instance of
                      :class:`~openstack.smn.v2.topic.Topic`

        :returns: A Topic object
        :rtype: :class:`~openstack.smn.v2.topic.Topic`
        """
        return self._get(_topic.Topic, topic)

    def get_topic_attr(self, topic, attrname=None):
        """Get topic attr

        :param topic: The topic urn or an instance of
                      :class:`~openstack.smn.v2.topic.Topic`
        :param attrname: attrname
        :rtype: :class:`~openstack.smn.v2.topic.TopicAttr`
        """

        if isinstance(topic, _topic.Topic):
            topic_urn = topic.id
        else:
            topic_urn = topic

        if attrname is not None:
            return self._list(_topic.TopicAttr,
                              topic_urn=topic_urn,
                              paginated=False,
                              name=attrname)
        else:
            return self._list(_topic.TopicAttr,
                              paginated=False,
                              topic_urn=topic_urn)

    def update_topic_attr(self, topic_attr, attrname, value):
        """Update a topic attr by attrname

        :param topic_attr: The topicattr object
                           :class:`~openstack.smn.v2.topic.TopicAttr`
        :param attrname: attribute name. String value.
        :param value: Topic attribute to be updated. String value
        :rtype: :class:`~openstack.smn.v2.topic.TopicAttr`
        """

        return self._update(_topic.TopicAttr,
                            topic_attr,
                            topic_urn=topic_attr.topic_urn,
                            attributes_name=attrname,
                            attr_value=value)

    def delete_topic_attr(self, topic_attr, attrname):
        """Delete a topic attr by attrname

        :param topic_attr: The topicattr object
                           :class:`~openstack.smn.v2.topic.TopicAttr`
        :param attrname: attrname
        :returns: None
        """

        self._delete(_topic.TopicAttr,
                     topic_attr,
                     topic_urn=topic_attr.topic_urn,
                     attributes_name=attrname)

    def delete_topic_attrs(self, topic):
        """Delete all topics attrs on a topic

        :param topic: The topic urn or an instance of
                      :class:`~openstack.smn.v2.topic.Topic`
        :param attrname: attrname
        :returns: None
        """

        if isinstance(topic, _topic.Topic):
            topic_urn = topic.id
        else:
            topic_urn = topic
        return _topic.TopicAttr.delete_all(self._session,
                                           topic_urn=topic_urn)

    def subscriptions(self, **query):
        """List all Subscriptions

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.
        :returns: A generator of Subscription object
        :rtype: :class:`~openstack.smn.subscription.Subscription
        """

        return self._list(_subscription.Subscription, paginated=False, **query)

    def topic_subscriptions(self, topic, **query):
        """List all Subscriptions of a specific topic

        :param topic: The topic urn or an instance of
                      :class:`~openstack.smn.v2.topic.Topic`
        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.
        :returns: A generator of TopicSubscription object, TopicSubscription
                  and Subscription object can be treat as some object.
        :rtype: :class:`~openstack.smn.subscription.TopicSubscription
        """

        if isinstance(topic, _topic.Topic):
            topic_urn = topic.id
        else:
            topic_urn = topic

        return self._list(_subscription.TopicSubscription, paginated=False,
                          topic_urn=topic_urn, **query)

    def subscript_topic(self, topic, **kwargs):
        """Add a subscription for the topic

        :param topic: The topic urn or an instance of
                      :class:`~openstack.smn.v2.topic.Topic`
        :param kwargs: Optional query parameters to be sent to limit
                       the resources being returned.
        :returns: TopicSubscription object.
        :rtype: :class:`~openstack.smn.subscription.TopicSubscription

        """

        if isinstance(topic, _topic.Topic):
            topic_urn = topic.id
        else:
            topic_urn = topic

        return self._create(_subscription.TopicSubscription,
                            topic_urn=topic_urn, **kwargs)

    def unsubscript_topic(self, sub, ignore_missing=True):
        """Delete subscription

        :param sub: A string of subscription_urn or object of an instance of
                :class:`~openstack.smn.subscription.TopicSubscription or
                :class:`~openstack.smn.subscription.Subscription
        :param bool ignore_missing: When set to ``False``
                       :class:`~openstack.exceptions.ResourceNotFound` will be
                       raised when the TopicSubscription does not exist

        :returns: None
        """

        sub_obj = sub
        if isinstance(sub, _subscription.TopicSubscription):
            sub_obj = sub.subscription_urn

        return self._delete(_subscription.Subscription,
                            sub_obj,
                            ignore_missing=ignore_missing)

    def confirm_subcription(self, sub, token):
        """Delete subscription

        :param : An instance of object
                :class:`~openstack.smn.subscription.TopicSubscription or
                :class:`~openstack.smn.subscription.Subscription
        :returns: a dict object
        :rtype: dict
        """

        sub_obj = sub
        if isinstance(sub, _subscription.TopicSubscription):
            sub_obj = _subscription.Subscription(topic_urn=sub.topic_urn,
                                                 endpoint=sub.endpoint)

        return sub_obj.confirm(self._session, token)

    def create_message_template(self, **kwargs):
        """Create a message template

        :param dict kwargs: Keyword arguments which will be used to overwrite a
               :class:`~openstack.smn.v2.message_template.MessageTemplate`
        :rtype: :class:`~openstack.smn.v2.message_template.MessageTemplate`
        """
        return self._create(_mt.MessageTemplate, **kwargs)

    def update_message_template(self, mt, **kwargs):
        """Update a message template

        :param dict kwargs: Keyword arguments which will be used to overwrite a
               :class:`~openstack.smn.v2.message_template.MessageTemplate`
        :returns: A updated object of message template
        :rtype: :class:`~openstack.smn.v2.message_template.MessageTemplate`
        """
        return self._update(_mt.MessageTemplate, mt, **kwargs)

    def delete_message_template(self, mt, ignore_missing=True):
        """Delete a message template

        :param mt: message template id of an instance of object
               :class:`~openstack.smn.v2.message_template.MessageTemplate`

        :param bool ignore_missing: When set to ``False``
                       :class:`~openstack.exceptions.ResourceNotFound` will be
                       raised when the message template  does not exist.
                       When set to ``True``, no exception will be set when
                       attempting to delete a nonexistent message template.
        :returns: None
        """

        self._delete(_mt.MessageTemplate, mt, ignore_missing=ignore_missing)

    def message_templates(self, **query):
        """List all message templates

        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.
        :returns: A generator of TemplateMessage object
        :rtype: :class:`~openstack.smn.v2.message_template.MessageTemplate`
        """

        return self._list(_mt.MessageTemplate, paginated=False, **query)

    def get_message_template(self, mt):
        """Get detail of a message template

        :param mt: The message template id or an instance of
            :rtype: :class:`~openstack.smn.v2.message_template.MessageTemplate`

        :returns: A MessageTemplate object
        :rtype: :class:`~openstack.smn.v2.message_template.MessageTemplate`
        """

        return self._get(_mt.MessageTemplate, mt)

    def publish_topic(self, topic, **kwargs):
        """Publish message on topic

        :param topic: topic urn or an object of Topic of
                      :class:`~openstack.smn.v2.topic.Topic`

        :param kwargs \*\*query: dict of message to be send allow parameters
                                 are `subject` and `message`
        :returns: A dict contains message id and request id
        :rtype: dict
        """

        if isinstance(topic, _topic.Topic):
            obj = topic
        else:
            obj = self._find(_topic.Topic, topic, ignore_missing=False)
        return obj.publish(self._session, **kwargs)

    def direct_publish(self, **kwargs):
        """Direct publish message

        :param kwargs \*\*query: dict of message to be send.
                                 `endpoint` and `message` are required.
                                 sign_id is optional.
        :returns: A dict contains message id and request id
        :rtype: dict
        """
        return _topic.Topic.direct_publish(self._session, **kwargs)
