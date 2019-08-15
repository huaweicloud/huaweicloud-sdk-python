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


# get list of flavor
def list_flavors():
    flavors = conn.compute.flavors()
    for flavor in flavors:
        print(flavor)


# show flavor detail
def show_flavor(flavor_id):
    flavor = conn.compute.get_flavor(flavor_id)
    print(flavor)


# find flavor
def find_flavor(flavor_id):
    flavor = conn.compute.find_flavor(flavor_id)
    print(flavor)


if __name__ == "__main__":
    flavor_id = "s3.xlarge.2"
    list_flavors()
    show_flavor(flavor_id)
    find_flavor(flavor_id)
