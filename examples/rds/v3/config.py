#!/usr/bin/python
# -*- coding: UTF-8 -*-
from openstack import connection

projectId = "xxxxxxxxxxxxxx"
cloud = "xxxxxxxxxxxxxx"   # cdn use: cloud = "myhwclouds.com"
region = "xxxxxxxxxxxxxx"    # example: region = "cn-north-1"
AK = "xxxxxxxxxxxxxx"
SK = "xxxxxxxxxxxxxx"
conn = connection.Connection(
              project_id=projectId,
              cloud=cloud,
              region=region,
              ak=AK,
              sk=SK)


def configurations(conn):
    query = {}
    print(conn.rdsv3.configurations(**query))
