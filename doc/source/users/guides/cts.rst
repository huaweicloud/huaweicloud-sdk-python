Using CTS
=========

Before working with the CTS service, you'll need to create a
connection to your OpenStack cloud by following the :doc:`connect` user
guide. This will provide you with the ``conn`` variable used in the examples
below.

Set environment variable or add these in your application::

    os.environ.setdefault(
        'OS_CTS_ENDPOINT_OVERRIDE',
       'https://cts.eu-de.otc.t-systems.com/v1.0/%(project_id)s')
