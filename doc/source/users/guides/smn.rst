Using SMN
==========

Before working with the SMN service, you'll need to create a
connection to your OpenStack cloud by following the :doc:`connect` user
guide. This will provide you with the ``conn`` variable used in the examples
below.

Set environment variable or add these in your application::

    os.environ.setdefault(
        'OS_SMN_ENDPOINT_OVERRIDE',
        'https://smn.eu-de.otc.t-systems.com/v2/%(project_id)s')
