# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

"""
Managing rds

"""


def datastore_versions(conn):
    for v in conn.rds.datastore_versions('MySQL'):
        print(v)


def list_rds_instances(conn):
    for i in conn.rds.instances():
        print(i)


def list_rds_flavors(conn):
    for f in conn.rds.flavors(dbId='87620726-6802-46c0-9028-a8785e1f1922',
                              region="eu-de"):
        print(f)


def create_instance(conn):
    instance_dict = {
        "name": "trove-instance-rep2",
        "datastore": {
            "type": "MySQL",
            "version": "5.6.30"},
        "flavorRef": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4",
        "volume": {
            "type": "COMMON",
            "size": 100
        },
        "region": "eu-de",
        "availabilityZone": "eu-de-01",
        "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
        "nics": {
            "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
        },
        "securityGroup": {
            "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
        },
        "backupStrategy": {
            "startTime": "01:00:00",
            "keepDays": 3
        },
        "dbRtPd": "Test@123"
    }

    print(conn.rds.create_instance(**instance_dict))


def get_instance(conn, i):
    """i could be the instance id of an instance object"""
    return conn.rds.get_instance(i)


def set_instance_params(conn, i):
    """i could be the instance id of an instance object"""
    params = {
        "connect_timeout": 17,
        "sync_binlog": 1
    }
    print(conn.rds.set_instance_params(i, **params))


def reset_instance_params(conn, i):
    """i could be the instance id of an instance object"""
    print(conn.rds.reset_instance_params(i))


def list_instance_errorlog(conn, i):
    """i could be the instance id of an instance object"""
    for l in conn.rds.list_instance_errorlog(i,
                                             startDate="2017-07-11+06:35",
                                             endDate="2017-07-20+06:35"):
        print(l)


def list_instance_slowlog(conn, i):
    """i could be the instance id of an instance object"""
    for l in conn.rds.list_instance_slowlog(i, sftype='UPDATE'):
        print(l)


def get_flavor(conn, f):
    print(conn.rds.get_flavor(f))


def backups(conn):
    for b in conn.rds.backups():
        print(b)


def create_backup_policy(conn, i):
    print(conn.rds.create_backup_policy(i, 7, "22:00:00"))


def get_backup_policy(conn, i):
    print(conn.rds.get_backup_policy(i))


def create_backup(conn, i):
    print(conn.rds.create_backup(i, "myname", "my desc"))


def get_version(conn, version):
    print(conn.rds.get_rds_version(version))


def list_version(conn):
    for v in conn.rds.list_rds_version():
        print(v)
