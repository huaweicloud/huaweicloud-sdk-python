The RDS_OS API
==============

For details on how to use rds_os, see :doc:`/users/guides/rds_os`

.. automodule:: openstack.rds_os.v1._proxy

The rds_os Class
----------------

The rds_os high-level interface is available through the ``rds_os``
member of a :class:`~openstack.connection.Connection` object.
The ``rds_os`` member will only be added if the service is detected.

Instance Operations
^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.rds_os.v1._proxy.Proxy

   .. automethod:: openstack.rds_os.v1._proxy.Proxy.instances
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.get_instance
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.delete_instance
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.create_instance
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.resize_instance
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.resize_instance_volume
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.restart_instance
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.restore_instance

Flavor Operations
^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.rds_os.v1._proxy.Proxy

   .. automethod:: openstack.rds_os.v1._proxy.Proxy.flavors
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.get_flavor

Parameters Operations
^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.rds_os.v1._proxy.Proxy

   .. automethod:: openstack.rds_os.v1._proxy.Proxy.parameters
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.get_parameter
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.get_instance_default_configuration

Parameter Group Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.rds_os.v1._proxy.Proxy

   .. automethod:: openstack.rds_os.v1._proxy.Proxy.list_configuration_group
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.create_configuration_group
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.get_configuration_group
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.delete_configuration_group
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.update_configuration_group
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.patch_configuration_group
   .. automethod:: openstack.rds_os.v1._proxy.Proxy.get_configuration_group_associated_instances
