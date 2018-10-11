The KMS API
===========

For details on how to use kms, see :doc:`/users/guides/kms`

.. automodule:: openstack.kms.v1._proxy

The kms Class
-------------

The kms high-level interface is available through the ``kms``
member of a :class:`~openstack.connection.Connection` object.
The ``kms`` member will only be added if the service is detected.

Key Operations
^^^^^^^^^^^^^^
.. autoclass:: openstack.kms.v1._proxy.Proxy

   .. automethod:: openstack.kms.v1._proxy.Proxy.create_key
   .. automethod:: openstack.kms.v1._proxy.Proxy.describe_key
   .. automethod:: openstack.kms.v1._proxy.Proxy.keys
   .. automethod:: openstack.kms.v1._proxy.Proxy.enable_key
   .. automethod:: openstack.kms.v1._proxy.Proxy.disable_key
   .. automethod:: openstack.kms.v1._proxy.Proxy.schedule_deletion_key
   .. automethod:: openstack.kms.v1._proxy.Proxy.cancel_deletion_key

DataKey Operations
^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.kms.v1._proxy.Proxy

   .. automethod:: openstack.kms.v1._proxy.Proxy.create_datakey
   .. automethod:: openstack.kms.v1._proxy.Proxy.create_datakey_wo_plain
   .. automethod:: openstack.kms.v1._proxy.Proxy.encrypt_datakey
   .. automethod:: openstack.kms.v1._proxy.Proxy.decrypt_datakey

Random Operations
^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.kms.v1._proxy.Proxy

   .. automethod:: openstack.kms.v1._proxy.Proxy.gen_random

InstanceNumber Operations
^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: openstack.kms.v1._proxy.Proxy

   .. automethod:: openstack.kms.v1._proxy.Proxy.get_instance_number

Quota Operations
^^^^^^^^^^^^^^^^
.. autoclass:: openstack.kms.v1._proxy.Proxy

   .. automethod:: openstack.kms.v1._proxy.Proxy.get_quota
