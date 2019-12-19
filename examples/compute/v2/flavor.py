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


# get list of flavor with paginated parameter
def list_flavors_with_paginated():
    flavors = conn.compute.flavors(paginated=True, limit=10)
    for flavor in flavors:
        print(flavor)
        print(flavor.id)


# show flavor detail
def show_flavor(flavor_id):
    flavor = conn.compute.get_flavor(flavor_id)
    print(flavor)


# find flavor
def find_flavor(flavor_id):
    flavor = conn.compute.find_flavor(flavor_id)
    print(flavor)


# find flavor extra specs
def query_flavor_extra_specs(flavor_id):
    extra_specs = conn.compute.query_flavor_extra_specs(flavor_id)
    if extra_specs is not None:
        extra_specs_dict = extra_specs.extra_specs;
        if extra_specs_dict is not None:
            print("extra_specs:%s" % extra_specs_dict)
            status = extra_specs_dict.get("cond:operation:status")
            generation = extra_specs_dict.get("ecs:generation")
            if status is not None:
                print(status)
            if generation is not None:
                print(generation)
        else:
            print("extra_specs body is None")
    else:
        print("get extra_specs result is None")


if __name__ == "__main__":
    flavor_id = "s3.xlarge.2"
    list_flavors()
    list_flavors_with_paginated()
    show_flavor(flavor_id)
    find_flavor(flavor_id)
    query_flavor_extra_specs(flavor_id)
