#!/usr/bin/python
# coding=utf-8
import sys

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


# Create securitytoken
# POST /v3.0/OS-CREDENTIAL/securitytokens
def create_securitytoken(**auth):
    securitytoken = conn.iam.create_securitytoken(**auth)
    print(securitytoken)


if __name__ == "__main__":
    # Create securitytoken by token
    auth = {
        "auth": {
            "identity": {
                "methods": [
                    "token"
                ],
                "token": {
                    "id": "**********",
                    "duration-seconds": 900
                }
            }
        }
    }

    # Create securitytoken by agency
    # auth = {
    #     "auth": {
    #         "identity": {
    #             "methods": [
    #                 "assume_role"
    #             ],
    #             "assume_role": {
    #                 "domain_name": "**********",
    #                 "agency_name": "**********",
    #                 "duration-seconds": 3600,
    #                 "session_user": {
    #                     "name": "**********"
    #                 }
    #             }
    #         }
    #     }
    # }
    create_securitytoken(**auth)
