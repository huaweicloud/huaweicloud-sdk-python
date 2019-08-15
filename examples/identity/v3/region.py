#!/usr/bin/python
# coding=utf-8

from openstack import connection

username = "**********"
password = "**********"
userDomainId = "**********"
auth_url = "**********"

# create connection
conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    domain_id=userDomainId,
    username=username,
    password=password
)


# Querying a Region List
def get_region_list():
    regions = conn.identity.regions()
    for region in regions:
        print(region)


# Querying Region Details
def get_region_detail(region_id):
    region = conn.identity.get_region(region_id)
    print(region)


if __name__ == "__main__":
    region_id = "**********"
    get_region_list()
    get_region_detail(region_id)