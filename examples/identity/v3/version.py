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


# Query version of keystone APIs
# GET /
def get_version_of_keystone():
    versions = conn.identity.get_version_of_keystone()
    print(versions)


# Query version3.0 of keystone APIs
# GET /v3
def get_version3_of_keystone():
    version = conn.identity.get_version3_of_keystone()
    print(version)


if __name__ == "__main__":
    get_version_of_keystone()
    get_version3_of_keystone()
