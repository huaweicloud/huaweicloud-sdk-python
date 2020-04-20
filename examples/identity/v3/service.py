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
    # get_service_catalog():"project_id" instead of "domain_id"
    domain_id=userDomainId,
    username=username,
    password=password,
    # get_service_catalog():"project_id" instead of "domain_id"
    # project_id="**********"
)


# Query a service list
# GET /v3/services
def get_service_list():
    services = conn.identity.services()
    # services = conn.identity.services(type="**********")
    for service in services:
        print(service)


# Query service details
# GET /v3/services/{service_id}
def get_service_detail(service_id):
    service = conn.identity.get_service(service_id)
    print(service)


# Query service catalog
# GET /v3/auth/catalog
def get_service_catalog():
    result = conn.identity.get_service_catalog()
    for item in result.catalog:
        print(item)


if __name__ == "__main__":
    service_id = "**********"
    get_service_list()
    get_service_detail(service_id)
    get_service_catalog()
