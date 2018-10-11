The CTS API
==============

For details on how to use cts, see :doc:`/users/guides/cts`

.. automodule:: openstack.cts.v1._proxy

The cts Class
--------------------

The cts high-level interface is available through the ``cts``
member of a :class:`~openstack.connection.Connection` object.
The ``cts`` member will only be added if the service is detected.


Tracker Operations
^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.cts.v1._proxy.Proxy

   .. automethod:: openstack.cts.v1._proxy.Proxy.create_tracker
   .. automethod:: openstack.cts.v1._proxy.Proxy.update_tracker
   .. automethod:: openstack.cts.v1._proxy.Proxy.get_tracker
   .. automethod:: openstack.cts.v1._proxy.Proxy.delete_tracker

Trace Operations
^^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.cts.v1._proxy.Proxy

   .. automethod:: openstack.cts.v1._proxy.Proxy.traces
   .. automethod:: openstack.cts.v1._proxy.Proxy.traces_v2
