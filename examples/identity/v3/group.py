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


# Create a group
# POST /v3/groups
def create_group():
    group = {
        "description": "**********",
        "domain_id": "**********",
        "name": "**********"
    }
    group = conn.identity.create_group(**group)
    print(group)


# Delete a group
# DELETE /v3/groups/{group_id}
def delete_group(group_id):
    conn.identity.delete_group(group_id)


# Modify a group
# PATCH /v3/groups/{group_id}
def modify_group(group_id):
    group = {
        "description": "**********",
        "domain_id": "**********",
        "name": "**********"
    }
    group = conn.identity.update_group(group_id, **group)
    print(group)


# Query a group list
# GET /v3/groups
def get_group_list():
    groups = conn.identity.groups()
    # groups = conn.identity.groups(domain_id="**********", name="**********")
    for group in groups:
        print(group)


# Query group details
# GET /v3/groups/{group_id}
def get_group_detail(group_id):
    group = conn.identity.get_group(group_id)
    print(group)


# Add a User to a User Group
# PUT /v3/groups/{group_id}/users/{user_id}
def add_user_to_group(group_id, user_id):
    result = conn.identity.add_user_to_group(group_id, user_id)
    if result is True:
        print("Add user to group successfully")
    else:
        print("Add user to group failure")


# Query whether a user belongs to a user group
# HEAD /v3/groups/{group_id}/users/{user_id}
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
