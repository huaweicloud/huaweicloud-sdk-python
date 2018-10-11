The MAAS API
============

For details on how to use maas, see :doc:`/users/guides/maas`

.. automodule:: openstack.maas.v1._proxy

The MAAS Class
--------------

The maas high-level interface is available through the ``maas``
member of a :class:`~openstack.connection.Connection` object.
The ``maas`` member will only be added if the service is detected.

Versions
^^^^^^^^
.. autoclass:: openstack.maas.v1._proxy.Proxy

   .. automethod:: openstack.maas.v1._proxy.Proxy.versions

Task Operations
^^^^^^^^^^^^^^^
.. autoclass:: openstack.maas.v1._proxy.Proxy

   .. automethod:: openstack.maas.v1._proxy.Proxy.tasks
   .. automethod:: openstack.maas.v1._proxy.Proxy.create_task
   .. automethod:: openstack.maas.v1._proxy.Proxy.delete_task
   .. automethod:: openstack.maas.v1._proxy.Proxy.get_task
   .. automethod:: openstack.maas.v1._proxy.Proxy.start_task
   .. automethod:: openstack.maas.v1._proxy.Proxy.stop_task
   .. automethod:: openstack.maas.v1._proxy.Proxy.task_count
