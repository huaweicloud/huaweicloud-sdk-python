# -*-coding:utf-8 -*-

from openstack import connection

# create connection 
username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


# create server group
def create_server_group(name, policies):
    attrs = {"name": name, "policies": policies}
    server_group = conn.compute.create_server_group(**attrs)
    return server_group


# delete server group
def delete_server_group(server_group):
    conn.compute.delete_server_group(server_group)


# find server group_id or name
def find_server_group(server_group):
    server_group = conn.compute.find_server_group(server_group)
    print(server_group)


# get server group 
def get_server_group(server_group):
    server_group = conn.compute.get_server_group(server_group)
    print(server_group)


if __name__ == "__main__":
    name = "server_group_name"
    policies = ['anti-affinity']
    server_group = create_server_group(name, policies)
    find_server_group(server_group.name)
    get_server_group(server_group)
    delete_server_group(server_group)
