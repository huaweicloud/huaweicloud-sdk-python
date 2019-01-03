import sys

import base64
from openstack import connection
from openstack import utils

utils.enable_logging(debug=True, stream=sys.stdout)

# create connection
# username = "xxxxxx"
# password = "xxxxxx"
# projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
# userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
# auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url

conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


# use user_data to create linux server
def create_server_with_user_data():
    user_date_org = "#!/bin/bash \r\n echo 'root:P@ssWr0d123' | chpasswd ;"
    user_data = base64.b64encode(user_date_org)

    data = {
        "availability_zone": "kvmxen.dc1",
        "name": "test-sdk-for-userdata",
        "imageRef": "c71b64e7-4767-4406-afde-2c7c7ac2242c",
        "flavorRef": "s1.medium",
        "security_groups": [
            {
                "name": "3cd0dc61-3a84-43de-9741-394fce012f38"
            }
        ],
        "networks": [
            {
                "uuid": "939924e4-48c3-4091-bbb5-1bf097fcdbf5"
            }
        ],
        "user_data": user_data,
        "os:scheduler_hints": {
            "group": "ae089094-087b-4c39-ba98-f1862d5e45b1"
        }
    }
    ff = conn.compute.create_server(**data)
    print(ff)
    server_create = conn.compute.wait_for_server(ff, status="ACTIVE", wait=300)
    print(server_create)
    return server_create


# use adminpass to create windows server
def create_windows_server_with_adminpass():
    data = {
        "availability_zone": "kvmxen.dc1",
        "name": "Windows-test-sdk-for-adminpass",
        "imageRef": "0a205997-2c6e-4b5e-b73d-b435e8a06535",
        "flavorRef": "s1.xlarge",
        "security_groups": [
            {
                "name": "db06a582-b8f8-42d6-bfaa-67995528dddb"
            }
        ],
        "networks": [
            {
                "uuid": "d090d69f-2109-4228-a941-a6067723744a"
            }
        ],
        "os:scheduler_hints": {
            "group": "ae089094-087b-4c39-ba98-f1862d5e45b1"
        },
        "metadata": {
            "admin_pass": "cloud.1234"
        }
    }
    ff = conn.compute.create_server(**data)
    print(ff)
    server_wins = conn.compute.wait_for_server(ff, status="ACTIVE", wait=300)
    print(server_wins)
    return server_wins


# stop a server
def stop_server(server_id):
    ff = conn.compute.stop_server(server_id)
    print(ff)
    server_stop = conn.compute.wait_for_server(ff, status="SHUTOFF", wait=300)
    print(server_stop)


# start a server
def start_server(server_id):
    ff = conn.compute.start_server(server_id)
    print(ff)
    server_start = conn.compute.wait_for_server(ff, status="ACTIVE", wait=300)
    print(server_start)


# reboot a server
def reboot_server(server_id, type="SOFT"):
    ff = conn.compute.reboot_server(server_id, type)
    print(ff)
    server_reboot = conn.compute.wait_for_server(ff, status="ACTIVE", wait=300)
    print(server_reboot)


# delete a server
def delete_server(server_id):
    ff = conn.compute.delete_server(server_id)
    print(ff)


if __name__ == "__main__":

    server = create_server_with_user_data()
    server_windows = create_windows_server_with_adminpass()
    delete_server(server.id)
    reboot_server(server.id, type="SOFT")
    start_server(server.id)
    stop_server(server.id)
