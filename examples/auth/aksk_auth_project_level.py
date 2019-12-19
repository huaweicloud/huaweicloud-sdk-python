#!/usr/bin/env python
# coding=utf-8
from openstack import connection

ak = "replace-with-your-ak"
sk = "replace-with-your-sk"
cloud = "myhuaweicloud.com"
project_id = "replace-with-your-project-id"
region = "replace-with-your-region-name"
conn = connection.Connection(
    ak=ak,
    sk=sk,
    cloud=cloud,
    project_id=project_id,
    region=region
)


def test_list_servers():
    query = {
        "limit": 3,
    }
    objs = conn.compute.servers(**query)
    for i in objs:
        print i


if __name__ == "__main__":
    test_list_servers()
