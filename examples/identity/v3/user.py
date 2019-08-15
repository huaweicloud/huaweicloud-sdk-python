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


# Creating a User
def create_user():
    user = {
        "enabled": True,
        "name": "**********",
        "password": "**********"
    }
    conn.identity.create_user(**user);


# Deleteing a User
def delete_user(user_id):
    conn.identity.delete_user(user_id)


# Modifying User Information (including password)
def modify_user(user_id):
    user = {
        "enabled": True,
        "name": "**********",
        "password": "**********"
    }
    conn.identity.update_user(user_id, **user)


# Querying a User List
def get_user_list():
    users = conn.identity.users()
    for user in users:
        print(user)


# Querying User Details
def get_user_detail(user_id):
    user = conn.identity.get_user(user_id)
    print(user)


# Changing a Password
def change_password(user_id, **password_attr):
    result = conn.identity.change_password(user_id, **password_attr)
    if result is True:
        print("Change password successfully")
    else:
        print("Change password failure")


# Deleting a User from a User Group
def remove_user_from_group(group_id, user_id):
    result = conn.identity.remove_user_from_group(group_id, user_id)
    if result is True:
        print("Remove user from group successfully")
    else:
        print("Remove user from group failure")


# Querying Users in a User Group
def list_group_users(group_id):
    groups = conn.identity.list_group_users(group_id)
    for group in groups:
        print(group)


# Querying the User Group to Which a User Belongs
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
