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


# Query a endpoint list
# GET /v3/endpoints
def get_endpoint_list():
    endpoints = conn.identity.endpoints()
    # endpoints = conn.identity.endpoints(interface="**********", service_id="**********")
    for endpoint in endpoints:
        print(endpoint)


# Query endpoint details
# GET /v3/endpoints/{endpoint_id}
def get_endpoint_detail(endpoint_id):
    endpoint = conn.identity.get_endpoint(endpoint_id)
    print(endpoint)


if __name__ == "__main__":
    endpoint_id = "**********"
    get_endpoint_list()
    get_endpoint_detail(endpoint_id)
