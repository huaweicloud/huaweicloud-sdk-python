# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

import sys
import warnings
import os

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

host_id = '5ec9fb89-8c6d-4603-ac3b-a6fa2373c4e2'

os.environ.setdefault(
    'OS_DEH_ENDPOINT_OVERRIDE',
    'https://******/v1.0/%(project_id)s'
)
print('endpoint: ' + os.environ.get('OS_DEH_ENDPOINT_OVERRIDE'))


# Test create a host.
def create_host(_conn):
    data = {
        "name": "deh-zgf-python-20181012",
        "auto_placement": "off",
        "availability_zone": "kvmxen.dc1",
        "host_type": "general",
        "quantity": 1
    }
    host = _conn.deh.create_dedicated_host(**data)
    print(host)


# Test list hosts.
def list_hosts(_conn):
    query = {
        # "dedicated_host_id": "e4858b2a-f2ef-408d-9842-8e1a5c03e514",
        # "name": "deh-zgf-python",
        # "host_type": "general",
        # "host_type_name": "",
        # "flavor": "",
        # "state": "",
        # "tenant": "",
        # "availability_zone": "kvmxen.dc1",
        # "limit": "10",
        # "marker": "",
        # "changes-since": ""
    }
    hosts = _conn.deh.dedicated_hosts(**query)
    for host in hosts:
        print(host)


# Test get a host.
def get_host(_conn, _host_id):
    host = _conn.deh.get_dedicated_host(_host_id)
    print(host)


# Test update a host.
def update_host(_conn, _host_id):
    data = {
        "auto_placement": "off",
        "name": "deh-zgf-python-update-x2"
    }
    host = _conn.deh.update_dedicated_host(_host_id, **data)
    print(host)


# Test delete a host.
def delete_host(_conn, _host_id):
    host = _conn.deh.delete_dedicated_host(_host_id)
    print(host)


# Test list servers from host.
def list_host_servers(_conn, _host_id):
    query = {
        # "limit": "3",
        # "marker": ""
    }
    servers = _conn.deh.host_servers(_host_id, **query)
    for server in servers:
        print(server)


# Test list type of host.
def list_host_types(_conn):
    types = _conn.deh.host_types('kvmxen.dc1')
    for index in types:
        print(index)


# Test list quota of host.
def list_host_quotas(_conn):
    query = {
        # "resource": "h1"
    }
    quotas = _conn.deh.host_quotas('128a7bf965154373a7b73c89eb6b65aa', **query)
    for quota in quotas:
        print(quota)


if __name__ == "__main__":
    # create_host(conn)
    # list_hosts(conn)
    # get_host(conn, host_id)
    # update_host(conn, host_id)
    # delete_host(conn, host_id)
    # list_host_servers(conn, host_id)
    # list_host_types(conn)
    # list_host_quotas(conn)
    pass
