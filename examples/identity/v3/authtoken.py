#!/usr/bin/python
# coding=utf-8

import sys

from openstack import connection, utils

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


# Creat token
# POST /v3/auth/tokens
def create_authtoken():
    # Create user token by password
    auth = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": "**********",
                        "password": "**********",
                        "domain": {
                            "name": "**********"
                        }
                    }
                }
            },
            "scope": {
                "domain": {
                    "name": "**********"
                }
            }
        }
    }
    # Create user token by password and MFA
    # auth = {
    #     "auth": {
    #         "identity": {
    #             "methods": [
    #                 "password",
    #                 "totp"
    #             ],
    #             "password": {
    #                 "user": {
    #                     "name": "**********",
    #                     "password": "**********",
    #                     "domain": {
    #                         "name": "**********"
    #                     }
    #                 }
    #             },
    #             "totp": {
    #                 "user": {
    #                     "id": "**********",
    #                     "passcode": "******"
    #                 }
    #             }
    #         },
    #         "scope": {
    #             "domain": {
    #                 "name": "**********"
    #             }
    #         }
    #     }
    # }

    # Create user token by agency
    # auth = {
    #     "auth": {
    #         "identity": {
    #             "methods": [
    #                 "assume_role"
    #             ],
    #             "assume_role": {
    #                 "domain_name": "**********",
    #                 "xrole_name": "**********"
    #             }
    #         },
    #         "scope": {
    #             "project": {
    #                 "name": "**********"
    #             }
    #         }
    #     }
    # }
    token = conn.identity.create_authtoken(auth)
    # token = conn.identity.create_authtoken(auth, nocatalog="true")
    print(token)

# validate token
# GET /v3/auth/tokens
def validate_authtoken():
    # token = conn.identity.validate_authtoken(x_subject_token="**********")
    token = conn.identity.validate_authtoken(x_subject_token="**********", nocatalog="true")
    print(token)


if __name__ == "__main__":
    create_authtoken()
    validate_authtoken()
