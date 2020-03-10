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


def list_error_log(conn):

    query = {
        'instance_id': "instance_id",
        'start_date': '2019-07-29T10:41:14+0800',
        'end_date': '2019-08-14T10:41:14+0800',
        'offset': 0,
        'limit': 10,
    }
    error_log_list = conn.rdsv3.list_instance_errorlog(**query)
    for error_log in error_log_list:
        print(error_log)


def list_slow_log(conn):
    query = {
        'instance_id': "instance_id",
        'start_date': '2019-07-29T10:41:14+0800',
        'end_date': '2019-08-14T10:41:14+0800',
    }
    slow_log_list = conn.rdsv3.list_instance_slowlog(**query)
    for slow_log in slow_log_list:
        print(slow_log)
