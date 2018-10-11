The DMS API
===========

For details on how to use dms, see :doc:`/users/guides/dms`

.. automodule:: openstack.dms.v1._proxy

The dms Class
--------------------

The dms high-level interface is available through the ``dms``
member of a :class:`~openstack.connection.Connection` object.
The ``dms`` member will only be added if the service is detected.

Queue Operations
^^^^^^^^^^^^^^^^
.. autoclass:: openstack.dms.v1._proxy.Proxy

   .. automethod:: openstack.dms.v1._proxy.Proxy.create_queue
   .. automethod:: openstack.dms.v1._proxy.Proxy.get_queue
   .. automethod:: openstack.dms.v1._proxy.Proxy.delete_queue
   .. automethod:: openstack.dms.v1._proxy.Proxy.queues

Group Operations
^^^^^^^^^^^^^^^^
.. autoclass:: openstack.dms.v1._proxy.Proxy

   .. automethod:: openstack.dms.v1._proxy.Proxy.groups
   .. automethod:: openstack.dms.v1._proxy.Proxy.create_groups
   .. automethod:: openstack.dms.v1._proxy.Proxy.delete_group

Message Operations
^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.dms.v1._proxy.Proxy

   .. automethod:: openstack.dms.v1._proxy.Proxy.send_messages
   .. automethod:: openstack.dms.v1._proxy.Proxy.consume_message
   .. automethod:: openstack.dms.v1._proxy.Proxy.ack_consumed_message
   .. automethod:: openstack.dms.v1._proxy.Proxy.quotas

Quota Operations
^^^^^^^^^^^^^^^^
.. autoclass:: openstack.dms.v1._proxy.Proxy

   .. automethod:: openstack.dms.v1._proxy.Proxy.quotas
