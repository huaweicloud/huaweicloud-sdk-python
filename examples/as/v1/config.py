#!/usr/bin/env python
#coding=utf-8

import logging
from openstack import connection

# create connection
username = "xxxxxxxxxx"
password = "xxxxxxxxxx"
projectId = "xxxxxxxxxx"
userDomainId = "xxxxxxxxxx"
auth_url = "xxxxxxxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
)

#get config list
def list_config():
    query = {
        "name": "as-config-lsqn",
        "image_id": "a3934478-bfeb-4a02-b257-9089779f0380",
        "marker": 0,
        "limit": 10
    }
    configs = conn.auto_scaling.configs(**query)
    print(list(configs))

#get config detail
def detail_config(configId):
    config = conn.auto_scaling.get_config(configId)
    print(config)

#creat config
def create_config():
    instance_config = {
        "flavor_id": "c2.medium",
        "image_id":"f2003c7b-99c4-4616-be19-334beaca81b1",
        "disk":[{
            "size": 40,
            "volume_type": "SATA",
            "disk_type": "SYS"
        },
        {
            "size": 100,
            "volume_type": "SATA",
            "disk_type": "DATA"
        }],
        "personality":[{
            "path": "/etc/foo.txt",
            "content": "ZmRncmdyZmdyZ2g="
        }],
        "metadata": {
            "key1": "value1",
            "tag": "app"
        },
        "key_name": "KeyPair-d571",
        "user_data": "MT12",
        "public_ip": {
            "eip": {
                "ip_type":"5_sbgp",
                "bandwidth": {
                    "size":5,
                    "share_type": "PER",
                    "charging_mode": "bandwidth"
                }
            }
        }
    }
    config_name = "auto-scaling-config-name"
    config = conn.auto_scaling.create_config(config_name, **instance_config)
    config = conn.auto_scaling.get_config(config)
    print(config)

#delete config
def delete_config(configId):
    conn.auto_scaling.delete_config(configId)

#batch delete config
def batch_delete_config(configIds):
    conn.auto_scaling.batch_delete_configs(configIds)

if __name__ == "__main__":
    configId = "485fe089-e9bf-4cfb-a7ac-d39e48d5ae07"
    configIds = [
        "485fe089-e9bf-4cfb-a7ac-d39e48d5ae07",
        "485fe089-e9bf-4cfb-a7ac-d39e48d5ae07"
    ]
    list_config()
    detail_config(configId)
    create_config()
    delete_config(configId)
    batch_delete_config(configIds)




