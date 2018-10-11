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

import mock

from openstack.smn.v2 import _proxy
from openstack.smn.v2 import message_template as _message_template
from openstack.smn.v2 import subscription as _subscription
from openstack.smn.v2 import topic as _topic
from openstack.tests.unit import test_proxy_base2


class TestSMNProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestSMNProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_create_topic(self):
        self.verify_create(self.proxy.create_topic, _topic.Topic)

    def test_topics(self):
        self.verify_list(self.proxy.topics, _topic.Topic)

    def test_delete_topic(self):
        self.verify_delete(self.proxy.delete_topic, _topic.Topic, True)

    def test_get_topic(self):
        self.verify_get(self.proxy.get_topic, _topic.Topic)

    def test_update_topic(self):
        self.verify_update(self.proxy.update_topic, _topic.Topic)

    def test_get_topic_attr(self):
        topic = '123'
        self.verify_list(self.proxy.get_topic_attr, _topic.TopicAttr,
                         paginated=False, method_args=[topic],
                         expected_kwargs={'topic_urn': topic})

    def test_update_topic_attr(self):
        topic_attr_dict = {'topic_urn': 'fakeurn'}
        topic_attr = _topic.TopicAttr(**topic_attr_dict)
        attrname = 'attr'
        value = 'val'
        self._verify2('openstack.proxy2.BaseProxy._update',
                      self.proxy.update_topic_attr,
                      method_args=[topic_attr, attrname, value],
                      expected_args=[mock.ANY, topic_attr],
                      expected_kwargs={'topic_urn': 'fakeurn',
                                       'attributes_name': attrname,
                                       'attr_value': value})

    def test_delete_topic_attr(self):
        topic_attr_dict = {'topic_urn': 'fakeurn'}
        topic_attr = _topic.TopicAttr(**topic_attr_dict)
        attrname = 'attr'
        self._verify2('openstack.proxy2.BaseProxy._delete',
                      self.proxy.delete_topic_attr,
                      method_args=[topic_attr, attrname],
                      expected_args=[mock.ANY, topic_attr],
                      expected_kwargs={'topic_urn': 'fakeurn',
                                       'attributes_name': attrname})

    def test_delete_topic_attrs(self):
        self._verify2('openstack.smn.v2.topic.TopicAttr.delete_all',
                      self.proxy.delete_topic_attrs,
                      method_args=['topic_urn'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'topic_urn': 'topic_urn'})

    def test_subscriptions(self):
        self.verify_list(self.proxy.subscriptions, _subscription.Subscription)

    def test_subscript_topic(self):
        self._verify2('openstack.proxy2.BaseProxy._create',
                      self.proxy.subscript_topic,
                      method_args=["topic_urn"],
                      expected_args=[mock.ANY],
                      expected_kwargs={'topic_urn': 'topic_urn'})

    def test_unsubscript_topic(self):
        self.verify_delete(self.proxy.unsubscript_topic,
                           _subscription.Subscription, True)

    def test_confirm_subcription(self):
        pass

    def test_create_message_template(self):
        self.verify_create(self.proxy.create_message_template,
                           _message_template.MessageTemplate)

    def test_message_templates(self):
        self.verify_list(self.proxy.message_templates,
                         _message_template.MessageTemplate, paginated=False)

    def test_get_message_template(self):
        self.verify_get(self.proxy.get_message_template,
                        _message_template.MessageTemplate)

    def test_update_message_template(self):
        self.verify_update(self.proxy.update_message_template,
                           _message_template.MessageTemplate)

    def test_delete_message_template(self):
        self.verify_delete(self.proxy.delete_message_template,
                           _message_template.MessageTemplate, True)

    def test_publish_topic(self):
        pass

    def test_direct_publish(self):
        pass
