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
def create_group():
    group = {
        "name": "**********",
        "description": "**********"
    }
    conn.identity.create_group(**group)


# Deleting a Group
def delete_group(group_id):
    conn.identity.delete_group(group_id)


# Modifying a Group
def modify_group(group_id):
    group = {
        "name": "**********",
        "description": "**********"
    }
    conn.identity.update_group(group_id, **group)


# Querying a Group List
def get_group_list():
    groups = conn.identity.groups()
    for group in groups:
        print(group)


# Querying Group Details
def get_group_detail(group_id):
    group = conn.identity.get_group(group_id)
    print(group)


# Adding a User to a User Group
def add_user_to_group(group_id, user_id):
    result = conn.identity.add_user_to_group(group_id, user_id)
    if result is True:
        print("Add user to group successfully")
    else:
        print("Add user to group failure")


# Querying Whether a User Belongs to a User Group
def check_group_user(group_id, user_id):
    result = conn.identity.check_group_user(group_id, user_id)
    if result is True:
        print("The user is in the group")
    else:
        print("The user is not in the group")


if __name__ == "__main__":
    group_id = "**********"
    user_id = "**********"
    get_group_list()
    get_group_detail(group_id)
    create_group()
    modify_group(group_id)
    add_user_to_group(group_id, user_id)
    check_group_user(group_id, user_id)
    delete_group(group_id)