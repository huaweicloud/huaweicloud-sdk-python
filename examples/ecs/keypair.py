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


# create keypair
def create_keypair(keypair_name):
    keypair = conn.compute.find_keypair(keypair_name)
    if not keypair:
        keypair = conn.compute.create_keypair(name=keypair_name)
    print(keypair)


# get list of keypair
def list_keypair():
    keypairs = conn.compute.keypairs()
    for keypair in keypairs:
        print(keypair)


# show keypair detail
def show_keypair(keypair_name):
    keypair = conn.compute.get_keypair(keypair_name)
    print(keypair)


# find keypair_id or name
def find_keypair(keypair_name):
    keypair = conn.compute.find_keypair(keypair_name)
    print(keypair)


# delete keypair
def delete_keypair(keypair_name):
    conn.compute.delete_keypair(keypair_name)


if __name__ == "__main__":
    keypairname = "test-python"
    create_keypair(keypairname)
    list_keypair()
    show_keypair(keypairname)
    find_keypair(keypairname)
    delete_keypair(keypairname)
