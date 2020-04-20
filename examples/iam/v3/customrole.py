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


# Query a customrole list
# GET /v3.0/OS-ROLE/roles
def get_custom_role_list():
    roles = conn.iam.custom_roles()
    for role in roles:
        print(role)


# Query customrole details
# GET /v3.0/OS-ROLE/roles/{role_id}
def get_custom_role():
    role_id = "**********"
    role = conn.iam.get_custom_role(role_id)
    print(role)


# Create custom role
# POST /v3.0/OS-ROLE/roles
def create_custom_role():
    # Create cloud service custom role
    role = {
        "display_name": "**********",
        "type": "AX",
        "description": "**********",
        "description_cn": "**********",
        "policy": {
            "Version": "1.1",
            "Statement": [
                {
                    "Effect": "**********",
                    "Action": [
                        "**********"
                    ],
                    "Condition": {
                        "**********": {
                            "**********": [
                                "**********"
                            ]
                        }
                    },
                    "Resource": [
                        "**********"
                    ]
                }
            ]
        }
    }
    # Create agency custom role
    # role = {
    #         "display_name": "**********",
    #         "type": "**********",
    #         "description": "**********",
    #         "description_cn": "**********",
    #         "policy": {
    #             "Version": "1.1",
    #             "Statement": [
    #                 {
    #                     "Effect": "**********",
    #                     "Action": [
    #                         "**********"
    #                     ],
    #                     "Resource":{
    #                         "uri":[
    #                             "/iam/agencies/**********"
    #                         ]
    #                     }
    #                 }
    #             ]
    #         }
    #     }
    role = conn.iam.create_custom_role(**role)
    print(role)


# Update custom role
# PATCH /v3.0/OS-ROLE/roles/{role_id}
def update_custom_role():
    role_id = "**********"
    # Update cloud service custom role
    role = {
        "display_name": "**********",
        "type": "AX",
        "description": "**********",
        "description_cn": "**********",
        "policy": {
            "Version": "1.1",
            "Statement": [
                {
                    "Effect": "**********",
                    "Action": [
                        "**********"
                    ],
                    "Condition": {
                        "**********": {
                            "**********": [
                                "**********"
                            ]
                        }
                    },
                    "Resource": [
                        "**********"
                    ]
                }
            ]
        }
    }
    # Update agency custom role
    # role = {
    #         "display_name": "**********",
    #         "type": "**********",
    #         "description": "**********",
    #         "description_cn": "**********",
    #         "policy": {
    #             "Version": "1.1",
    #             "Statement": [
    #                 {
    #                     "Effect": "**********",
    #                     "Action": [
    #                         "**********"
    #                     ],
    #                     "Resource":{
    #                         "uri":[
    #                             "/iam/agencies/**********"
    #                         ]
    #                     }
    #                 }
    #             ]
    #         }
    #     }
    role = conn.iam.update_custom_role(role_id, **role)
    print(role)


# Delete custom role
# DELETE /v3.0/OS-ROLE/roles/{role_id}
def delete_custom_role():
    role_id = "**********"
    conn.iam.delete_custom_role(role_id)


if __name__ == "__main__":
    get_custom_role_list()
    get_custom_role()
    create_custom_role()
    update_custom_role()
    delete_custom_role()
