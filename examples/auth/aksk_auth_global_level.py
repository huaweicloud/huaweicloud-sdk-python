#!/usr/bin/env python
# coding=utf-8
from openstack import connection

ak = "replace-with-your-ak"
sk = "replace-with-your-sk"
cloud = "myhuaweicloud.com"
domain_id = "replace-with-your-domain-id"

conn = connection.Connection(
    ak=ak,
    sk=sk,
    cloud=cloud,
    domain_id=domain_id,
)


def test_list_zones():
    query = {
        "limit": 3,
    }
    data = conn.dns.zones(**query)
    for i in data:
        print i


if __name__ == "__main__":
    test_list_zones()
