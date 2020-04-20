#!/usr/bin/python
# coding=utf-8

from openstack import connection

username = "**********"
password = "**********"
userDomainId = "**********"
auth_url = "**********"

# create connection
conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    domain_id=userDomainId,
    username=username,
    password=password
)


# Create permanent accesskey
# POST /v3.0/OS-CREDENTIAL/credentials
def create_credential():
    credential = {
        "description": "**********",
        "user_id": "**********"
    }
    credential = conn.iam.create_credential(**credential)
    print(credential)


# Query all permanent accesskeys
# GET /v3.0/OS-CREDENTIAL/credentials
def get_credential_list():
    credentials = conn.iam.credentials()
    # credentials = conn.iam.credentials(user_id="**********")
    for credential in credentials:
        print(credential)


# Query permanent accesskey
# GET /v3.0/OS-CREDENTIAL/credentials/{access_key}
def get_credential():
    access_key = "**********"
    credential = conn.iam.get_credential(access_key)
    print(credential)


# update permanent accesskey
# PUT /v3.0/OS-CREDENTIAL/credentials/{access_key}
def update_credential():
    access_key = "**********"
    credential = {
        "credential": {
            "status": "**********",
            "description": "**********"
        }
    }
    credential = conn.iam.update_credential(access_key, **credential)
    print(credential)


# delete permanent accesskey
# DELETE /v3.0/OS-CREDENTIAL/credentials/{access_key}
def delete_credential():
    access_key = "**********"
    conn.iam.delete_credential(access_key)


if __name__ == "__main__":
    create_credential()
    get_credential_list()
    get_credential()
    update_credential()
    delete_credential()
