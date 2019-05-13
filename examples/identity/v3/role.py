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


# Querying a Role List
def get_role_list():
    roles = conn.identity.roles()
    for role in roles:
        print(role)


# Querying Role details
def get_role_detail(role_id):
    role = conn.identity.get_role(role_id)
    print(role)


# Querying Permissions of a User Group Under a Domain
def list_domain_user_group_role(domain_id, group_id):
    roles = conn.identity.list_domain_user_group_role(domain_id, group_id)
    for role in roles:
        print(role)


# Querying Permissions of a User Group Corresponding to a Project
def list_project_user_group_role(project_id, group_id):
    roles = conn.identity.list_project_user_group_role(project_id, group_id)
    for role in roles:
        print(role)


# Granting Permissions to a User Group of a Domain
def grant_domain_user_group_role(domain_id, group_id, role_id):
    result = conn.identity.grant_domain_group_role(domain_id, group_id, role_id)
    if result is True:
        print("Grant permission to a user group of domain successfully")
    else:
        print("Grant permission to a user group of domain failure")


# Granting Permissions to a User Group Corresponding to a Project
def grant_project_user_group_role(project_id, group_id, role_id):
    result = conn.identity.grant_project_group_role(project_id, group_id, role_id)
    if result is True:
        print("Grant permission to a user group of project successfully")
    else:
        print("Grant permission to a user group of project failure")


# Querying Whether a User Group Under a Domain Has Specific Permissions
def check_domain_user_group_role(domain_id, group_id, role_id):
    result = conn.identity.check_domain_group_role(domain_id, group_id, role_id)
    if result is True:
        print("The group of domain has this permission")
    else:
        print("The group of domain doesn't have this permission")


# Querying Whether a User Group Corresponding to a Project Has Specific Permissions
def check_project_user_group_role(project_id, group_id, role_id):
    result = conn.identity.check_project_group_role(project_id, group_id, role_id)
    if result is True:
        print("The group of project has this permission")
    else:
        print("The group of project doesn't have this permission")


# Deleting Permissions of a User Group of a Domain
def delete_domain_user_group_role(domain_id, group_id, role_id):
    result = conn.identity.delete_domain_group_role(domain_id, group_id, role_id)
    if result is True:
        print("Delete permission to a user group of domain successfully")
    else:
        print("Delete permission to a user group of domain failure")


# Deleting Permissions of a User Group Corresponding to a Project
def delete_project_user_group_role(project_id, group_id, role_id):
    result = conn.identity.delete_project_group_role(project_id, group_id, role_id)
    if result is True:
        print("Delete permission to a user group of project successfully")
    else:
        print("Delete permission to a user group of project failure")


if __name__ == "__main__":
    domain_id = "**********"
    group_id = "**********"
    project_id = "**********"
    role_id = "**********"
    get_role_list()
    get_role_detail(role_id)
    list_domain_user_group_role(domain_id, group_id)
    list_project_user_group_role(project_id, group_id)
    grant_domain_user_group_role(domain_id, group_id, role_id)
    grant_project_user_group_role(project_id, group_id, role_id)
    check_domain_user_group_role(domain_id, group_id, role_id)
    check_project_user_group_role(project_id, group_id, role_id)
    delete_domain_user_group_role(domain_id, group_id, role_id)
    delete_project_user_group_role(project_id, group_id, role_id)