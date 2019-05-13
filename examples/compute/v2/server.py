# -*-coding:utf-8 -*-

from openstack import exceptions
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


# create server
def create_server():
    data = {
        "availability_zone": "az1.dc1",
        "name": "test-name",
        "image_id": "22ecd57e-aab4-4251-9d13-38058659d879",
        "flavor_id": "s1.medium",
        "security_groups":[
            {
                "name": "Sys-default"
            }
        ],
        "networks":[
            {
                "uuid": "0cf0ef67-9504-42f8-bf33-a0334792b2f6"
            }
        ],
        "user_data":"IyEvYmluL2Jhc2ggDQogZWNobyAncm9vdDpDbG91ZC4xMjM0JyB8IGNocGFzc3dkIDs="
    }
    server = conn.compute.create_server(**data)
    print(server)
    return server


# find server_id or name
def find_server(server_id):
    server = conn.compute.find_server(server_id)
    print(server)


# show server detail
def show_server(server_id):
    server = conn.compute.get_server(server_id)
    print(server)


# get list of server
def list_servers():
    servers = conn.compute.servers(limit=1)
    for server in servers:
        print(server)


# update server
def update_server(server_id, server_name):
    server = conn.compute.update_server(server_id, name=server_name)
    print(server)


# reboot server
def reboot_server(server_id, type="SOFT"):
    conn.compute.reboot_server(server_id, type)
    server = conn.compute.find_server(server_id)
    server = conn.compute.wait_for_server(server)
    print(server)


# rebuild server flavor
def rebuild_server(server_id, server_name, admin_password, image_id):
    server = conn.compute.rebuild_server(server_id, server_name,
                                         admin_password, image=image_id)
    server = conn.compute.wait_for_server(server)
    print(server)


# resize server flavor
def resize_server(server_id, flavor_id):
    conn.compute.resize_server(server_id, flavor_id)
    server = conn.compute.find_server(server_id)
    server = conn.compute.wait_for_server(server, status="VERIFY_RESIZE")
    print(server)


# comfirm server flavor
def confirm_server_resize(server_id, status):
    conn.compute.confirm_server_resize(server_id)
    server = conn.compute.find_server(server_id)
    server = conn.compute.wait_for_server(server, status=status)
    print(server)


# revert server flavor
def revert_server_resize(server_id, status):
    conn.compute.revert_server_resize(server_id)
    server = conn.compute.find_server(server_id)
    server = conn.compute.wait_for_server(server, status=status)
    print(server)


# create server image
def create_server_image(server_id, name):
    server_image = conn.compute.create_server_image(server_id, name)
    print(server_image)


# add EIP
def add_floating_ip_to_server(server_id, address):
    conn.compute.add_floating_ip_to_server(server_id, address)


# delete EIP
def remove_floating_ip_from_server(server_id, address):
    conn.compute.remove_floating_ip_from_server(server_id, address)


# lock server
def lock_server(server_id):
    conn.compute.lock_server(server_id)


# unlock server
def unlock_server(server_id):
    conn.compute.unlock_server(server_id)


# start server
def start_server(server_id):
    conn.compute.start_server(server_id)


# stop server
def stop_server(server_id):
    conn.compute.stop_server(server_id)


# set server metadata
def set_server_metadata(server_id):
    metadata = {"metadata_key": "metadata_value"}
    server = conn.compute.set_server_metadata(server_id, **metadata)
    print(server)


# get server metadata
def get_server_metadata(server_id):
    server_metadata = conn.compute.get_server_metadata(server_id)
    print(server_metadata)


# get server metadata with specified key
def get_server_metadata_with_key(server_id, key):
    server_metadata = conn.compute.get_server_metadata(server_id, key)
    print(server_metadata)


# delete server metadata
def delete_server_metadata(server_id):
    keys = ["metadata_key"]
    if type(keys) != list:
        message = "keys must be a list"
        raise exceptions.SDKException(message)
    server = conn.compute.delete_server_metadata(server_id, keys)
    print(server)


# wait for server
def wait_for_server(server, status):
    if type(server) == str:
        server = conn.compute.get_server(server.id)
    server = conn.compute.wait_for_server(server, status=status)
    return server


# delete server
def delete_server(server_id):
    server = conn.compute.delete_server(server_id)
    print(server)


if __name__ == "__main__":
    newflavor_id = "c2.medium"
    newimage_id = "228b642c-7538-4364-99b4-a88f271234a4"
    newserver_name = "name_test2"
    admin_password = None
    status = "VERIFY_RESIZE"
    address = "10.154.118.136"
    image_name = "image_name"
    key = "test_key"
    list_servers()
    server = create_server()
    find_server(server.id)
    show_server(server.id)
    update_server(server.id, newserver_name)
    reboot_server(server.id, type="SOFT")
    rebuild_server(server.id, newserver_name, admin_password, newimage_id)
    resize_server(server.id, newflavor_id)
    confirm_server_resize(server.id, status)
    revert_server_resize(server.id, status)
    create_server_image(server.id, image_name)
    add_floating_ip_to_server(server.id, address)
    remove_floating_ip_from_server(server.id, address)
    lock_server(server.id)
    unlock_server(server.id)
    start_server(server.id)
    stop_server(server.id)
    get_server_metadata(server.id)
    get_server_metadata_with_key(server.id, key)
    set_server_metadata(server.id)
    delete_server_metadata(server.id)
    wait_for_server(server, status)
    delete_server(server.id)
