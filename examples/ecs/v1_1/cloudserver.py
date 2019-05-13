# -*-coding:utf-8 -*-

from openstack import connection

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
        "availability_zone": "az1.dc1",
        "name": "test-name",
        "imageRef": "22ecd57e-aab4-4251-9d13-38058659d879",
        "root_volume": {
            "volumetype": "SATA"
        },
        "data_volumes": [
            {
                "volumetype": "SSD",
                "size": 50
            },
            {
                "volumetype": "SSD",
                "size": 50,
                "multiattach": "false",
                "hw:passthrough": "false"
            }
        ],
        "isAutoRename": "true",
        "flavorRef": "s1.medium",
        "personality": [
            {
                "path": "/etc/test.txt",
                "contents":"ICAgICAgDQoiQmFjaA=="
            }
        ],
        "security_groups": [
            {
                "id": "3cd0dc61-3a84-43de-9741-394fce012f38"
            }
        ],
        "vpcid": "515231d1-f0d9-4acf-a549-c79f90ef7c4e",
        "nics": [
            {
                "subnet_id": "0cf0ef67-9504-42f8-bf33-a0334792b2f6"
            }
        ],
        "publicip": {
            "eip": {
                "iptype": "5_bgp",
                "bandwidth": {
                    "size": 10,
                    "sharetype": "PER"
                }
            }
        },
        "key_name": "KeyPair-ccad",
        "count": 1,
        "metadata": {
            "ss": "ss"
        },
        "extendparam": {
            "chargingMode": "prePaid",
            "periodType": "month",
            "periodNum": 1,
            "isAutoRenew": "true",
            "isAutoPay": "true",
            "regionID": "southchina"
        },
        "os:scheduler_hints": {
            "group": "ae089094-087b-4c39-ba98-f1862d5e45b1"
        }
    }
    server = conn.ecs.create_server_ext(**data)
    print(server)


# resize server
def resize_server_extend():
    server_id = '136ae835-e453-4074-a17b-abcde482b3af'
    data = {
        "flavorRef": "c1.2xlarge",
        "extendparam": {
            "isAutoPay": "true"
        }
    }
    ff = conn.ecs.resize_server_ext(server_id=server_id, **data)
    print(ff)


if __name__ == "__main__":
    create_server()
    resize_server_extend()
