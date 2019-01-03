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

import sys
import warnings

from openstack import utils
from openstack import connection

utils.enable_logging(debug=False, stream=sys.stdout)
warnings.filterwarnings('ignore')

auth_url = '******'
userDomainId = '******'
projectId = '******'
username = '******'
password = '******'

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
    verify=False
)


def create_server_ext(conn):
    data = {
        "availability_zone": "az1.dc1",
        "name": "newserverkak",
        "imageRef": "ad134bba-dfca-4aa1-a307-26b51e4c608b",
        "root_volume": {
            "volumetype": "SATA"
        },
        "data_volumes": [
            {
                "volumetype": "SATA",
                "size": 50
            },
            {
                "volumetype": "SSD",
                "size": 10,
                "multiattach": "true",
                "hw:passthrough": "false"
            }
        ],
        "isAutoRename": "true",
        "flavorRef": "c1.xlarge",
        "personality": [
            {
                "path": "/etc/banner.txt",
                "contents": "ICAgICAgDQoiQmFjaA=="
            }
        ],
        "security_groups": [
            {
                "id": "53234334-9c3d-4344-b577-2cdd6c244707"
            }
        ],
        "vpcid": "5b2a6c9a-093d-4d56-8889-a7917e44229c",
        "nics": [
            {
                "subnet_id": "a8f622a7-0d10-470e-ae80-c8e0e8bc7d12"
            }
        ],
        "publicip": {
            "eip": {
                "iptype": "5_bgp",
                "bandwidth": {
                    "size": 1,
                    "sharetype": "PER"
                }
            }
        },
        "key_name": "KeyPair-1565",
        "count": 1,
        "metadata": {
            "ss": "ss"
        },
        "extendparam": {
            "chargingMode": "postPaid",
            "periodType": "month",
            "periodNum": 1,
            "isAutoRenew": "true",
            "isAutoPay": "true",
            "regionID": "southchina"
        },
        "os:scheduler_hints": {
            "group": "cc10d0d1-d371-4f33-9452-fd5fbf14dc06"
        }
    }

    ff = conn.ecs.create_server_ext(**data)
    print(ff)


def resize_server_ext(conn):
    server_id = '8b0e2ecb-b73b-4be8-9cc5-0134ecbc4887'
    data = {
        "flavorRef": "c1.2xlarge",
        "extendparam": {
            "isAutoPay": "true"
        }
    }
    ff = conn.ecs.resize_server_ext(server_id=server_id, **data)
    print(ff)


def create_server(conn):
    data = {
        "availability_zone": "az1.dc1",
        "name": "kk",
        "imageRef": "ad134bba-dfca-4aa1-a307-26b51e4c608b",
        "root_volume": {
            "volumetype": "SATA"
        },
        "data_volumes": [
            {
                "volumetype": "SATA",
                "size": 50
            },
            {
                "volumetype": "SSD",
                "size": 10,
                "multiattach": "true",
                "hw:passthrough": "false"
            }
        ],
        "isAutoRename": "true",
        "flavorRef": "c1.xlarge",
        "personality": [
            {
                "path": "/etc/banner.txt",
                "contents": "ICAgICAgDQoiQmFjaA=="
            }
        ],
        "security_groups": [
            {
                "id": "53234334-9c3d-4344-b577-2cdd6c244707"
            }
        ],
        "vpcid": "5b2a6c9a-093d-4d56-8889-a7917e44229c",
        "nics": [
            {
                "subnet_id": "a8f622a7-0d10-470e-ae80-c8e0e8bc7d12"
            }
        ],
        "publicip": {
            "eip": {
                "iptype": "5_bgp",
                "bandwidth": {
                    "size": 1,
                    "sharetype": "PER"
                }
            }
        },
        "key_name": "KeyPair-1565",
        "count": 1,
        "metadata": {
            "ss": "ss"
        },
        "extendparam": {
            "chargingMode": "postPaid",
            "periodType": "month",
            "periodNum": 1,
            "isAutoRenew": "true",
            "isAutoPay": "true",
            "regionID": "southchina"
        },
        "os:scheduler_hints": {
            "group": "cc10d0d1-d371-4f33-9452-fd5fbf14dc06"
        }
    }

    ff = conn.ecs.create_server(**data)
    print(ff)


def resize_server(conn):
    server_id = 'b38ce153-5e7f-4560-8617-54d6066bc926'
    data = {
        "flavorRef": "c1.2xlarge",
        "extendparam": {
            "isAutoPay": "true"
        }
    }
    ff = conn.ecs.resize_server(server_id=server_id, **data)
    print(ff)


# New dedicated host ID (only for Elastic Cloud Server on a dedicated host)
def resize_server_deh(conn):
    server_id = "b38ce153-5e7f-4560-8617-54d6066bc926"
    data = {
        "flavorRef": "c1.2xlarge",
        "dedicated_host_id": "b38ce153-5e7f-4560-8617-54d6066bc926" # only for Elastic Cloud Server on a dedicated host

    }
    ff = conn.ecs.resize_server(server_id=server_id, **data)
    print(ff)


def delete_server(conn):
    data = {
        "servers": [
            {
                "id": "b2796d4e-6b91-4099-9693-3b43345b1a01"
            },
            {
                "id": "ee474f41-b150-4bde-a7aa-04a49c8dbae3"
            }
        ],
        "delete_publicip": "false",
        "delete_volume": "false"
    }
    ff = conn.ecs.delete_server(**data)
    print(ff)


def server_action_start(conn):
    data = {
        "os-start": {
            "servers": [
                {
                    "id": "cc1745d3-64c6-488e-b712-a25025795005"
                },
                {
                    "id": "ee474f41-b150-4bde-a7aa-04a49c8dbae3"
                }
            ]
        }
    }
    ff = conn.ecs.start_server(**data)
    print(ff)


def server_action_stop(conn):
    data = {
        "os-stop": {
            "type": "HARD",
            "servers": [
                {
                    "id": "cc1745d3-64c6-488e-b712-a25025795005"
                },
                {
                    "id": "ee474f41-b150-4bde-a7aa-04a49c8dbae3"
                }

            ]
        }
    }
    ff = conn.ecs.stop_server(**data)
    print(ff)


def server_action_restart(conn):
    data = {
        "reboot": {
            "type": "SOFT",
            "servers": [
                {
                    "id": "cc1745d3-64c6-488e-b712-a25025795005"
                },
                {
                    "id": "ee474f41-b150-4bde-a7aa-04a49c8dbae3"
                }

            ]
        }
    }
    ff = conn.ecs.reboot_server(**data)
    print(ff)


def get_server(_conn):
    ff = conn.ecs.get_server('600ea016-47c2-4aed-a8c1-c1a2106e3ad0')
    print(ff)


def servers(_conn):
    query = {
        "offset": 1,
        # Cloud server flavor ID, flavor_id is an alias for flavor.
        "flavor_id": "c1.medium",
        "name": "ecs-5280",
        "status": "SHUTOFF",
        "limit": 1
    }
    generator = conn.ecs.servers(**query)
    for servers_list in generator:
        print(servers_list)
        for server in servers_list.servers:
            print((server.get('id')))


if __name__ == '__main__':
    # get_server(conn)
    # servers(conn)
    pass
