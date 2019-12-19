#!/usr/bin/env python
# coding=utf-8
from openstack import connection

# create connection
username = "replace-with-your-username"
password = "replace-with-your-password"
domainId = "replace-with-your-domain-id"
userDomainId = "replace-with-your-user-domain-id"
auth_url = "https://iam.example.com/v3"
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             domain_id=domainId,
                             username=username,
                             password=password)


def test_list_zones():
    query = {
        "limit": 3,
    }
    data = conn.dns.zones(**query)
    for i in data:
        print i


if __name__ == "__main__":
    test_list_zones()
