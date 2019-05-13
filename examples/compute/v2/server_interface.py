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


# create server interface
def create_server_interface(server_id, net_id=None, port_id=None,
                            fixed_ip=None):
    attrs = {"net_id": net_id, "port_id": port_id, "fixed_ip": fixed_ip}
    kwargs = {}
    for key in attrs:
        if attrs[key]:
            kwargs[key] = attrs[key]
    print(kwargs)
    if kwargs == {}:
        message = "Parameter error"
        raise exceptions.SDKException(message)
    server = conn.compute.create_server_interface(server_id, **kwargs)
    print(server)
    return server


# delete interface
def delete_server_interface(server_interface, servr_id):
    conn.compute.delete_server_interface(server_interface, server=servr_id)


# show interface detail
def get_server_interface(server_interface, servr_id):
    server_ifa = conn.compute.get_server_interface(server_interface,
                                                   server=servr_id)
    print(server_ifa)


# get list of interface
def server_interfaces(server_id):
    server_ifas = conn.compute.server_interfaces(server_id)
    for ifa in server_ifas:
        print(ifa)


if __name__ == "__main__":
    server_id = "8700184b-79ff-414b-ab8e-11ed01bd3d3d"
    net_id = "e2103034-dcf3-4ac3-b551-6d5dd8fadb6e"
    server = create_server_interface(server_id, net_id)
    get_server_interface(server.id, server_id)
    server_interfaces(server_id)
    delete_server_interface(server.id, server_id)
