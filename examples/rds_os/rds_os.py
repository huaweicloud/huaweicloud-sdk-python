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


def list_rds_instances(conn):
    for i in conn.rds.os_instances():
        print(i)


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

    print(conn.rds.os_create_instance(**instance_dict))


def get_instance(conn, i):
    """i could be the instance id of an instance object"""
    return conn.rds.os_get_instance(i)


def get_flavor(conn, f):
    print(conn.rds.os_get_flavor(f))


def list_rds_flavors(conn):
    for f in conn.rds.os_flavors(dbId='87620726-6802-46c0-9028-a8785e1f1922',
                                 region="eu-de"):
        print(f)


def get_parameters(conn, version_id):
    """list parameters of a datastore"""
    for p in conn.rds.os_parameters(version_id):
        print(p)


def get_parameter(conn, version_id, name):
    """Get parameter of a datastore by name"""
    print(conn.rds.os_get_parameter(version_id, name))


def get_instance_default_configuration(conn, instance):
    print(conn.rds.os_get_instance_default_configuration(instance))


def list_configuration_group(conn):
    for g in conn.rds.os_list_configuration_group():
        print(g)


def create_configuration_group(conn):
    group_dict = {
        "configuration": {
            "name": "configuration_test",
            "description": "configuration_test",
            "values": {
                "max_connections": "10",
                "autocommit": "OFF"
            },
            "datastore": {
                "type": "mysql",
                "version": "5.6"
            }
        }
    }

    print(conn.rds.os_create_configuration_group(**group_dict))


def get_configuration_group(conn, cg):
    print(conn.rds.os_get_configuration_group(cg))


def delete_configuration_group(conn, group):
    conn.rds.os_delete_configuration_group(group)


def update_configuration_group(conn, cg):

    update_dict = {
        "configuration": {
            "name": "configuration_test",
            "description": "configuration_test",
            "values": {
                "max_connections": "10",
                "autocommit": "OFF"
            }
        }
    }

    print(conn.rds.os_update_configuration_group(cg, **update_dict))


def patch_configuration_group(conn, cg):
    patch_dict = {
        "configuration": {
            "values": {
                "max_connections": "10",
                "autocommit": "OFF"
            }
        }
    }

    print(conn.rds.os_patch_configuration_group(cg, **patch_dict))


def get_configuration_group_associated_instances(conn, cg):
    print(conn.rds.os_get_configuration_group_associated_instances(cg))
