# -*-coding:utf-8 -*-
import sys

from openstack import connection
from openstack import utils
import time

utils.enable_logging(debug=True, stream=sys.stdout)
# create connection
username = "xxxxx"
password = "xxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)

TIMES = 60
INTERVAL = 10


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


# get list of servers
def servers():
    query = {
        "name": "ecs",
        "status": "ACTIVE",
        "limit": 5,
        "offset": 1,
    }
    servers = conn.ecs.servers(**query)
    for server in servers:
        print("count: ", server.count)
        for each_server in server.servers:
            print (each_server["id"], each_server["name"])


# get list of servers with paginated parameter
def servers_with_paginated():
    query = {
        "name": "ecs",
        "status": "ACTIVE",
    }
    servers = conn.ecs.servers(paginated=False, **query)
    for server in servers:
        print("count: ", server.count)
        for each_server in server.servers:
            print (each_server["id"], each_server["name"])


# get detail of server
def get_server(server_id):
    server = conn.ecs.get_server(server_id)
    print(server)
    print(server.name)


# batch stop server
def stop_server():
    data = {
        "os-stop": {
            "type": "SOFT",
            "servers": [
                {
                    "id": "cd57e8fb-ce0c-45d8-b7c9-74910b29d734"
                },
                {
                    "id": "559a6009-ef40-48bb-a551-fe5385b13266"
                }
            ]
        }
    }
    action = conn.ecs.stop_server(**data)
    print (action)
    job = wait_for_job(TIMES, INTERVAL, action.job_id)
    success_servers, failed_servers = get_servers_after_job(job)
    print ("Stop success servers: ", success_servers)
    print ("Stop failed servers: ", failed_servers)


# batch change os server
def batch_change_os():
    data = {
        "servers": [
            {
                "id": "server_id1"
            },
            {
                "id": "server_id2"
            }
        ],
        "keyname": "keyname",
        "imageid": "image_id"
    }
    change_os_result = conn.ecs.batch_change_os(**data)
    job = wait_for_job(TIMES, INTERVAL, change_os_result.job_id)
    success_servers, failed_servers = get_servers_after_job(job)
    print ("change os success servers: ", success_servers)
    print ("change os failed servers: ", failed_servers)


# batch start server
def start_server():
    data = {
        "os-start": {
            "servers": [
                {
                    "id": "6e311c63-ae8a-4273-b04e-90aff7210213"
                },
                {
                    "id": "851f66fd-a1ee-4e54-8bb3-af1655d89d86"
                }
            ]
        }
    }
    action = conn.ecs.start_server(**data)
    print(action)
    job = wait_for_job(TIMES, INTERVAL, action.job_id)
    success_servers, failed_servers = get_servers_after_job(job)
    print ("Start success servers: ", success_servers)
    print ("Start failed servers: ", failed_servers)


# batch reboot server
def reboot_server():
    data = {
        "reboot": {
            "type": "SOFT",
            "servers": [
                {
                    "id": "cd57e8fb-ce0c-45d8-b7c9-74910b29d734"
                },
                {
                    "id": "559a6009-ef40-48bb-a551-fe5385b13266"
                }
            ]
        }
    }
    action = conn.ecs.reboot_server(**data)
    print(action)
    job = wait_for_job(TIMES, INTERVAL, action.job_id)
    success_servers, failed_servers = get_servers_after_job(job)
    print ("Reboot success servers: ", success_servers)
    print ("Reboot failed servers: ", failed_servers)


# resize server
def resize_server(server_id):
    data = {
        "flavorRef": "s3.2xlarge.4",
    }
    server = conn.ecs.resize_server(server_id, **data)
    job = wait_for_job(TIMES, INTERVAL, server.job_id)
    print(job)


# batch delete server
def delete_server():
    data = {
        "servers": [
            {
                "id": "cd57e8fb-ce0c-45d8-b7c9-74910b29d734"
            },
            {
                "id": "559a6009-ef40-48bb-a551-fe5385b13266"
            }
        ],
        "delete_publicip": True,
        "delete_volume": True
    }
    action = conn.ecs.delete_server(**data)
    print(action)
    job = wait_for_job(TIMES, INTERVAL, action.job_id)
    success_servers, failed_servers = get_servers_after_job(job)
    print ("Delete success servers: ", success_servers)
    print ("Delete failed servers: ", failed_servers)


# wait until job status becoming SUCCESS or FAIL
def wait_for_job(times, interval, job_id):
    job_result = None
    for index in range(times):
        time.sleep(interval)
        job = conn.ecs.get_job(job_id)
        if job.status == "SUCCESS":
            job_result = job
            print("Get job success after %s tries" % index)
            break
        elif job.status == "FAIL":
            job_result = job
            print("Get job failed after %s tries" % index)
            break
    return job_result


# get success and failed server list after waiting job status
def get_servers_after_job(job):
    sub_jobs = job.entities["sub_jobs"]
    success_servers = []
    failed_servers = []

    if len(sub_jobs) > 0:
        for sub_job in sub_jobs:
            if "server_id" in sub_job.get("entities"):
                if sub_job["status"] == "SUCCESS":
                    success_servers.append(sub_job.get("entities").get("server_id"))
                else:
                    failed_servers.append(sub_job.get("entities").get("server_id"))
    return success_servers, failed_servers


if __name__ == "__main__":
    server_id = "server_id"
    autorecovery = "true"
    get_autorecovery(server_id)
    config_autorecovery(server_id, autorecovery)
    create_server()
    servers()
    servers_with_paginated()
    get_server(server_id)
    stop_server()
    start_server()
    reboot_server()
    resize_server(server_id)
    delete_server()
    batch_change_os()
