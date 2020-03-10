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


def backups(conn):
    query = {
        'instance_id': 'instance_id',
        'offset': 0,
        'limit': 10
    }
    print(conn.rdsv3.backups(**query))


def create_backup_policy(conn):
    policy = {
            "instance_id": "instance_id",
            "keep_days": 1,
            "start_time": "21:00-22:00",
            "period": "1,2,3"
    }

    close_policy = {
        "instance_id": "instance_id",
        "keep_days": 0,
    }
    print(conn.rdsv3.create_backup_policy(**close_policy))


def get_backup_policy(conn):
    query = {
        'instance_id': 'instance_id',
       }
    print(conn.rdsv3.get_backup_policy(**query))


def create_backup(conn):
    mysql_pg_backup = {
            "instance_id": "instance_id",
            "name": "dc_test02",
            "description": "mannual backup"
        }
    sqlserver = {
            "instance_id": "instance_id",
            "name": "backup",
            "description": "mannual backup",
            "databases": [{
                "name": "db1"
            }, {
                "name": "db2"
            }]
        }

    print(conn.rdsv3.create_backup(**mysql_pg_backup))


def delete_backup(conn):
    backup_id = "backup_id"
    print(conn.rdsv3.delete_backup(backup_id))





