Anti-DDos API
=============

For details on how to use anti_ddos, see :doc:`/users/guides/anti_ddos`

.. automodule:: openstack.anti_ddos.v1._proxy

The Anti-DDos Class
-------------------

The anti_ddos high-level interface is available through the ``anti_ddos``
member of a :class:`~openstack.connection.Connection` object.
The ``anti_ddos`` member will only be added if the service is detected.

ConfigList
^^^^^^^^^^
.. autoclass:: openstack.anti_ddos.v1._proxy.Proxy

   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.query_config_list

FloatingIp Operations
^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.anti_ddos.v1._proxy.Proxy

   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.create_floating_ip
   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.get_floating_ip
   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.delete_floating_ip
   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.update_floating_ip
   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.floating_ips
   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.get_eip_status
   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.list_eip_daily
   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.list_eip_log
   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.get_eip_weekly

Task Operations
^^^^^^^^^^^^^^^
.. autoclass:: openstack.anti_ddos.v1._proxy.Proxy

   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.query_task_status

Warn alert config
^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.anti_ddos.v1._proxy.Proxy

   .. automethod:: openstack.anti_ddos.v1._proxy.Proxy.get_alert_config
