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


# get list of server ip
def server_ips(server_id):
    server_ips = conn.compute.server_ips(server_id)
    for ip in server_ips:
        print(ip)


if __name__ == "__main__":
    server_id = "ef9cab69-c4d0-4e40-b9e9-80a96bc45415"
    server_ips(server_id)
