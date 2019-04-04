# -*-coding:utf-8 -*-

from openstack import connection
from openstack import exceptions


# create connection
username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # project ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


# create a host.
def create_host():
    data = {
        "name": "deh-tesk-sdk",
        "auto_placement": "off",
        "availability_zone": "az1.dc1",
        "host_type": "general",
        "quantity": 1
    }
    try:
        host = conn.deh.create_dedicated_host(**data)
        print(host)
        return host
    except exceptions.HttpException as e:
        print e.code
        print e.message
        print e.details


# list hosts.
def list_dedicated_hosts():
    query = {
        # "dedicated_host_id": "5ec9fb89-8c6d-4603-ac3b-a6fa2373c4e2",
        # "name": "deh-sdk",
        # "host_type": "general",
        # "host_type_name": "",
        # "flavor": "",
        # "state": "",
        # "tenant": "",
        # "availability_zone": "kvmxen.dc1",
        # "limit": "10",
        # "marker": "",
        # "changes-since": ""
        # "instance_uuid": ""
        # "sys_enterprise_project_id": "0"
    }
    dehs = conn.deh.dedicated_hosts(**query)
    for deh in dehs:
        print deh


# show a host.
def get_dedicated_host(host_id):
    deh = conn.deh.get_dedicated_host(host_id)
    print deh


# update a host.
def update_host(host_id):
    data = {
        "auto_placement": "off",
        "name": "deh-sdk"
    }
    host = conn.deh.update_dedicated_host(host_id, **data)
    print(host)


# delete a host.
def delete_host(host_id):
    try:
        host = conn.deh.delete_dedicated_host(host_id)
        print(host)
    except exceptions.HttpException as e:
        print e.code
        print e.message
        print e.details


# list servers from host.
def list_host_servers(host_id):
    query = {
        "limit": "3",
        "marker": ""
    }
    servers = conn.deh.host_servers(host_id, **query)
    for server in servers:
        print(server)


# list type of host.
def list_host_types(az):
    types = conn.deh.host_types(az)
    for index in types:
        print(index)


# list quota of host.
def list_host_quotas(tenant_id):
    query = {
        "resource": "h1"
    }
    quotas = conn.deh.host_quotas(tenant_id, **query)
    for quota in quotas:
        print(quota)


if __name__ == "__main__":
    deh = create_host()
    id = deh.dedicated_host_ids[0]
    list_dedicated_hosts()
    get_dedicated_host(id)
    update_host(id)
    list_host_servers(id)
    delete_host(id)
    az = "az1.dc1"
    list_host_types(az)
    tenant_id = "128a7bf965154373a7b73c89eb6b65aa"
    list_host_quotas(tenant_id)

