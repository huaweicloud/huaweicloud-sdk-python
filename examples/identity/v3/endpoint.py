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


# Querying a Endpoint List
def get_endpoint_list():
    endpoints = conn.identity.endpoints()
    for endpoint in endpoints:
        print(endpoint)


# Querying Endpoint Details
def get_endpoint_detail(endpoint_id):
    endpoint = conn.identity.get_endpoint(endpoint_id)
    print(endpoint)


if __name__ == "__main__":
    endpoint_id = "**********"
    get_endpoint_list()
    get_endpoint_detail(endpoint_id)