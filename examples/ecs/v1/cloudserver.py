# -*-coding:utf-8 -*-
import sys

from openstack import connection
from openstack import utils
import os
import base64


utils.enable_logging(debug=True, stream=sys.stdout)
# create connection
username = "xxxxx"
password = "xxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


# create server
def create_server():
    data = {
        "availability_zone": "AZ1",
        "name": "test-name",
        "description": "",
        "isAutoRename": False,
        "imageRef": "4c4f6f5d-b198-44bf-96a5-f5e8a44bda37",
        "flavorRef": "c1.medium",
        "root_volume": {
            "volumetype": "SAS",
            "size": 40,
            "extendparam": {
                "resourceSpecCode": "SAS",
                "resourceType": "3"
            }
        },
        "data_volumes": [

        ],
        "vpcid": "00a2e4fe-5295-4c0e-8bfd-ad3b8426cb93",
        "nics": [
            {
                "subnet_id": "47822b98-c5bd-45b3-9454-d9773380f249",
                "ip_address": "",
                "nictype": "",
                "extra_dhcp_opts": [

                ],
                "binding:profile": {
                    "disable_security_groups": False
                }
            }
        ],
        "security_groups": [
            {
                "id": "831902ed-5ad1-453f-b54a-702d85c1d657"
            }
        ],
        "personality": [

        ],
        "count": 1,
        "extendparam": {
            "chargingMode": "0",
            "regionID": "southchina"
        },
        "metadata": {
            "op_svc_userid": "19c27257bf014edc9d318fa3872c2896"
        },
        "server_tags": [

        ],
        "key_name": "KeyPair-7631"
    }
    server = conn.ecs.create_server(**data)
    print(server)


# get autorecovery configuration of a server.
def get_autorecovery(server_id):
    auto_recovery = conn.ecs.get_autorecovery(server_id)
    print ("support_auto_recovery:", auto_recovery)


# manage automatic recovery of a server.
def config_autorecovery(server_id, autorecovery):
    conn.ecs.config_autorecovery(server_id, autorecovery)


if __name__ == "__main__":
    server_id = "server_id"
    autorecovery = "true"
    get_autorecovery(server_id)
    config_autorecovery(server_id, autorecovery)
    create_server()
