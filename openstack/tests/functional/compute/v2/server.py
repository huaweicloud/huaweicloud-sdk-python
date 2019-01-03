import sys
import warnings

from openstack import utils
from openstack import connection

utils.enable_logging(debug=False, stream=sys.stdout)
warnings.filterwarnings('ignore')

auth_url = '******'
userDomainId = '******'
projectId = '******'
username = '******'
password = '******'

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
    verify=False
)


def test_get_server(_conn):
    server_id = '6ad3faa9-89c7-4b45-9a8b-b362c2f5dedb'
    server = _conn.compute.get_server(server_id)
    print(server.status)


def test_start_server(_conn):
    server_id = '6ad3faa9-89c7-4b45-9a8b-b362c2f5dedb'
    _conn.compute.start_server(server_id)


def test_stop_server_default(_conn):
    server_id = '6ad3faa9-89c7-4b45-9a8b-b362c2f5dedb'
    _conn.compute.stop_server(server_id)


def test_stop_server_soft(_conn):
    server_id = '6ad3faa9-89c7-4b45-9a8b-b362c2f5dedb'
    stop_type = 'SOFT'
    _conn.compute.stop_server(server_id, stop_type)


def test_stop_server_hard(_conn):
    server_id = '6ad3faa9-89c7-4b45-9a8b-b362c2f5dedb'
    stop_type = 'HARD'
    _conn.compute.stop_server(server_id, stop_type)


if __name__ == '__main__':
    # test_get_server(conn)
    # test_start_server(conn)
    # test_stop_server_default(conn)
    # test_stop_server_soft(conn)
    # test_stop_server_hard(conn)
    pass
