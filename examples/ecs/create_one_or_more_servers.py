import sys

import base64
import time
from openstack import connection
from openstack import utils

utils.enable_logging(debug=True, stream=sys.stdout)

# create connection
username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url

conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)

TIMES = 60
INTERVAL = 10


# use user_data to create linux server
def create_two_servers_one_time():
    user_date_org = "#!/bin/bash \r\n echo 'root:P@ssWr0d123' | chpasswd ;"
    user_data = base64.b64encode(user_date_org)

    data = {
        "availability_zone": "az1.dc1",
        "name": "test-sdk-for-Linux-userdata",
        "imageRef": "af60e0d5-6952-4f3d-b0ed-31bb19d4a692",
        "flavorRef": "c2.large",
        "vpcid": "0f22416a-53aa-4f45-b351-7807118c680b",
        "user_data": user_data,
        "nics": [
            {
                "subnet_id": "d090d69f-2109-4228-a941-a6067723744a"
            }
        ],
        "root_volume": {
            "volumetype": "SATA"
        },
        "count": 2
    }

    ff = conn.ecs.create_server(**data)
    print(ff)
    wait_time(TIMES, INTERVAL, ff.job_id)


# batch reboot servers
def reboot_server():
    data = {
        "reboot": {
            "type": "SOFT",
            "servers": [
                {
                    "id": "3ba7bd88-9c49-44ee-b4d4-a776d6dffad5"
                },
                {
                    "id": "3e0fe563-6dbe-43f9-8b38-dbca1fc1c9dd"
                }
                        ]
                }
            }
    ff = conn.ecs.reboot_server(**data)
    print(ff)
    wait_time(TIMES, INTERVAL, ff.job_id)


# batch stop server
def stop_server():
    data = {
        "os-stop": {
            "type": "SOFT",
            "servers": [
                {
                    "id": "3ba7bd88-9c49-44ee-b4d4-a776d6dffad5"
                },
                {
                    "id": "3e0fe563-6dbe-43f9-8b38-dbca1fc1c9dd"
                }
            ]
        }
    }
    ff = conn.ecs.stop_server(**data)
    print(ff)
    wait_time(TIMES, INTERVAL, ff.job_id)


# batch start server
def start_server():
    data = {
        "os-start": {
            "servers": [
                {
                    "id": "3ba7bd88-9c49-44ee-b4d4-a776d6dffad5"
                },
                {
                    "id": "3e0fe563-6dbe-43f9-8b38-dbca1fc1c9dd"
                }
            ]
        }
    }
    ff = conn.ecs.start_server(**data)
    print(ff)
    wait_time(TIMES, INTERVAL, ff.job_id)


# batch delete server
def delete_server(publicip_type="false", volume_type="false"):
    data = {
        "servers": [
            {
                "id": "105bf369-4f9a-485c-ae65-18408ff16182"
            },
            {
                "id": "8bb9fd7a-8a76-400b-bd51-43a76815ae83"
            }
            ],
            "delete_publicip": publicip_type,
            "delete_volume": volume_type
            }
    ff = conn.ecs.delete_server(**data)
    print(ff)
    wait_time(TIMES, INTERVAL, ff.job_id)


# wait until job status become SUCCESS or FAIL
def wait_time(times, interval, job_id):
    for index in range(times):
        time.sleep(interval)
        job = conn.ecs.get_job(job_id)
        if job.status == "SUCCESS":
            print("Get job success after %s tries" % index)
            break
        elif job.status == "FAIL":
            print("Get job failed after %s tries" % index)
            break


if __name__ == "__main__":
    create_two_servers_one_time()
    reboot_server()
    stop_server()
    start_server()
    delete_server(publicip_type="false", volume_type="false")
