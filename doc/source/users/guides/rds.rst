Using RDS
==========

Before working with the RDS service, you'll need to create a
connection to your OpenStack cloud by following the :doc:`connect` user
guide. This will provide you with the ``conn`` variable used in the examples
below.

Set environment variable or add these in your application::

    os.environ.setdefault(
        'OS_RDS_ENDPOINT_OVERRIDE',
        'https://rds.eu-de.otc.t-systems.com')

Please be note that RDS service support 2 modes, for OpenStack compatible mode
sdks, these sdks have `os_` prefix.
