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


# Create a user
# POST /v3/users
def create_user():
    user = {
        "enabled": True,
        "name": "**********",
        "password": "**********",
        "description": "**********",
        "domain_id": "**********"
    }
    user = conn.identity.create_user(**user)
    print(user)


# Delete a user
# DELETE /v3/users/{user_id}
def delete_user(user_id):
    conn.identity.delete_user(user_id)


# Modify user information (including password)
# PATCH /v3/users/{user_id}
def modify_user(user_id):
    user = {
        "enabled": True,
        "name": "**********",
        "password": "**********",
        "pwd_status": False,
        "description": "**********"
    }
    user = conn.identity.update_user(user_id, **user)
    print(user)


# Query a user list
# GET /v3/users
def get_user_list():
    users = conn.identity.users()
    # users = conn.identity.users(domain_id="**********", enabled=True, name="**********",
    #                             password_expires_at="**********")
    for user in users:
        print(user)


# Query user details
# GET /v3/users/{user_id}
def get_user_detail(user_id):
    user = conn.identity.get_user(user_id)
    print(user)


# Change a password
# POST /v3/users/{user_id}/password
def change_password(user_id, **password_attr):
    result = conn.identity.change_password(user_id, **password_attr)
    if result is True:
        print("Change password successfully")
    else:
        print("Change password failure")


# Delete a user from a user group
# DELETE /v3/groups/{group_id}/users/{user_id}
def remove_user_from_group(group_id, user_id):
    result = conn.identity.remove_user_from_group(group_id, user_id)
    if result is True:
        print("Remove user from group successfully")
    else:
        print("Remove user from group failure")


# Query users in a user group
# GET /v3/groups/{group_id}/users
def list_group_users(group_id):
    groups = conn.identity.list_group_users(group_id)
    for group in groups:
        print(group)


# Query the user group to which a user belongs
# GET /v3/users/{user_id}/groups
def list_user_groups(user_id):
    groups = conn.identity.list_user_groups(user_id)
    for group in groups:
        print(group)


if __name__ == "__main__":
    group_id = "**********"
    user_id = "**********"
    password_attr = {
        "user": {
            "password": "**********",
            "original_password": "**********"
        }
    }
    get_user_list()
    get_user_detail(user_id)
    create_user()
    modify_user(user_id)
    change_password(user_id, **password_attr)
    remove_user_from_group(group_id, user_id)
    list_group_users(group_id)
    list_user_groups(user_id)
    delete_user(user_id)
