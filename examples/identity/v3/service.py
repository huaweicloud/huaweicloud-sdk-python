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


# Querying a Service List
def get_service_list():
    services = conn.identity.services()
    for service in services:
        print(service)


# Querying Service Details
def get_service_detail(service_id):
    service = conn.identity.get_service(service_id)
    print(service)


if __name__ == "__main__":
    service_id = "**********"
    get_service_list()
    get_service_detail(service_id)