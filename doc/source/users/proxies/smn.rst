The SMN API
==============

For details on how to use smn, see :doc:`/users/guides/smn`

.. automodule:: openstack.smn.v2._proxy

The SMN Class
--------------------

The smn high-level interface is available through the ``smn``
member of a :class:`~openstack.connection.Connection` object.
The ``smn`` member will only be added if the service is detected.

Topic Operations
^^^^^^^^^^^^^^^^
.. autoclass:: openstack.smn.v2._proxy.Proxy

   .. automethod:: openstack.smn.v2._proxy.Proxy.create_topic
   .. automethod:: openstack.smn.v2._proxy.Proxy.update_topic
   .. automethod:: openstack.smn.v2._proxy.Proxy.delete_topic
   .. automethod:: openstack.smn.v2._proxy.Proxy.topics
   .. automethod:: openstack.smn.v2._proxy.Proxy.get_topic

TopicAttr Operations
^^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.smn.v2._proxy.Proxy

   .. automethod:: openstack.smn.v2._proxy.Proxy.get_topic_attr
   .. automethod:: openstack.smn.v2._proxy.Proxy.delete_topic_attr
   .. automethod:: openstack.smn.v2._proxy.Proxy.delete_topic_attrs
   .. automethod:: openstack.smn.v2._proxy.Proxy.update_topic_attr

Subscriptions Operations
^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.smn.v2._proxy.Proxy

   .. automethod:: openstack.smn.v2._proxy.Proxy.subscriptions
   .. automethod:: openstack.smn.v2._proxy.Proxy.topic_subscriptions
   .. automethod:: openstack.smn.v2._proxy.Proxy.subscript_topic
   .. automethod:: openstack.smn.v2._proxy.Proxy.unsubscript_topic
   .. automethod:: openstack.smn.v2._proxy.Proxy.subscript_topic
   .. automethod:: openstack.smn.v2._proxy.Proxy.confirm_subcription

Message Template Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.smn.v2._proxy.Proxy

   .. automethod:: openstack.smn.v2._proxy.Proxy.create_message_template
   .. automethod:: openstack.smn.v2._proxy.Proxy.update_message_template
   .. automethod:: openstack.smn.v2._proxy.Proxy.delete_message_template
   .. automethod:: openstack.smn.v2._proxy.Proxy.message_templates
   .. automethod:: openstack.smn.v2._proxy.Proxy.get_message_template

Message Topic Operations
^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.smn.v2._proxy.Proxy

   .. automethod:: openstack.smn.v2._proxy.Proxy.publish_topic
   .. automethod:: openstack.smn.v2._proxy.Proxy.direct_publish
