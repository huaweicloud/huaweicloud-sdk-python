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


# Query user details
# GET /v3.0/OS-USER/users/{user_id}
def query_user_details():
    user_id = "**********"
    result = conn.iam.query_user_details(user_id)
    print(result)


# Create a user
# POST /v3.0/OS-USER/users
def create_user():
    user = {
        "user": {
            "domain_id": "**********",
            "name": "**********",
            "password": "**********",
            "email": "**********",
            "areacode": "**********",
            "phone": "**********",
            "enabled": True,
            "pwd_status": False,
            "default_project_id": "",
            "xuser_type": "",
            "xuser_id": "",
            "description": "**********"
        }
    }
    result = conn.iam.create_user(**user)
    print(result)


# Update user information
# PUT /v3.0/OS-USER/users/{user_id}/info
def update_user_information():
    user_id = "**********"
    user = {
        "user": {
            "email": "**********",
            "mobile": "**********"
        }
    }
    result = conn.iam.update_user_information(user_id, **user)
    if result is True:
        print("Update user information successfully")
    else:
        print("Update user information failure")


# Update user information by admin
# PUT /v3.0/OS-USER/users/{user_id}
def update_user_information_by_admin():
    user_id = "**********"
    user = {
        "user": {
            "email": "**********",
            "areacode": "**********",
            "phone": "**********",
            "enabled": True,
            "name": "**********",
            "password": "**********",
            "pwd_status": False,
            "xuser_type": "",
            "xuser_id": "",
            "description": "**********"
        }
    }
    result = conn.iam.update_user_information_by_admin(user_id, **user)
    print(result)


if __name__ == "__main__":
    query_user_details()
    create_user()
    update_user_information()
    update_user_information_by_admin()
