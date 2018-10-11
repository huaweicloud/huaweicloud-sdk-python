Using Anti-DDOS
===============

Before working with the Anti-DDOS service, you'll need to create a
connection to your OpenStack cloud by following the :doc:`connect` user
guide. This will provide you with the ``conn`` variable used in the examples
below.

Set environment variable or add these in your application::

    os.environ.setdefault(
        'OS_ANTI_DDOS_ENDPOINT_OVERRIDE',
        'https://antiddos.eu-de.otc.t-systems.com/v1/%(project_id)s')
