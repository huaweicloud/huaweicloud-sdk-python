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


# Creating Securitytoken
def create_securitytoken(**auth):
    securitytoken = conn.iam.create_securitytoken(**auth)
    print(securitytoken)


if __name__ == "__main__":
    auth = {
        "auth": {
            "identity": {
                "methods": [
                    "token"
                ],
                "token": {
                    "id": "**********",
                }
            }
        }
    }
    create_securitytoken(**auth)