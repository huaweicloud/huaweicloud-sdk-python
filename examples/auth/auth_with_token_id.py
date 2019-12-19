#!/usr/bin/env python
# coding=utf-8
from openstack import connection

auth_token = "replace-with-your-token-id"
auth_url = "https://iam.example.com/v3"

token_conn = connection.Connection(
    auth_url=auth_url,
    auth_token=auth_token,
)


def test_list_endpoints(conn):
    query = {
        "limit": 3,
    }
    objs = conn.identity.endpoints(**query)
    for i in objs:
        print i


if __name__ == "__main__":
    test_list_endpoints(token_conn)
