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


# get list of flavors
def flavors():
    query = {
        "availability_zone": "kvmxen.dc1"
    }
    flavor_list = conn.ecs.flavors(**query)
    for flavor in flavor_list:
        print(flavor.name)
        print(flavor)


if __name__ == "__main__":
    flavors()
