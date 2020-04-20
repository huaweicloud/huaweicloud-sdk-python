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


# Query a role list
# GET /v3/roles
def get_role_list():
    roles = conn.identity.roles()
    # roles = conn.identity.roles(domain_id="**********", name="**********")
    for role in roles:
        print(role)


# Query role details
# GET /v3/roles/{role_id}
def get_role_detail(role_id):
    role = conn.identity.get_role(role_id)
    print(role)


# Query permissions of a user group under a domain
# GET /v3/domains/{domain_id}/groups/{group_id}/roles
def list_domain_user_group_role(domain_id, group_id):
    roles = conn.identity.list_domain_user_group_role(domain_id, group_id)
    for role in roles:
        print(role)


# Query permissions of a user group corresponding to a project
# GET /v3/projects/{project_id}/groups/{group_id}/roles
def list_project_user_group_role(project_id, group_id):
    roles = conn.identity.list_project_user_group_role(project_id, group_id)
    for role in roles:
        print(role)


# Grant permissions to a user group of a domain
# PUT /v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}
def grant_domain_user_group_role(domain_id, group_id, role_id):
    result = conn.identity.grant_domain_group_role(domain_id, group_id, role_id)
    if result is True:
        print("Grant permission to a user group of domain successfully")
    else:
        print("Grant permission to a user group of domain failure")


# Grant permissions to a user group corresponding to a project
# PUT /v3/projects/{project_id}/groups/{group_id}/roles/{role_id}
def grant_project_user_group_role(project_id, group_id, role_id):
    result = conn.identity.grant_project_group_role(project_id, group_id, role_id)
    if result is True:
        print("Grant permission to a user group of project successfully")
    else:
        print("Grant permission to a user group of project failure")


# Query whether a user group under a domain has specific permissions
# HEAD /v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}
def check_domain_user_group_role(domain_id, group_id, role_id):
    result = conn.identity.check_domain_group_role(domain_id, group_id, role_id)
    if result is True:
        print("The group of domain has this permission")
    else:
        print("The group of domain doesn't have this permission")


# Query whether a user group corresponding to a project has specific permissions
# HEAD /v3/projects/{project_id}/groups/{group_id}/roles/{role_id}
def check_project_user_group_role(project_id, group_id, role_id):
    result = conn.identity.check_project_group_role(project_id, group_id, role_id)
    if result is True:
        print("The group of project has this permission")
    else:
        print("The group of project doesn't have this permission")


# Delete Permissions of a User Group of a Domain
# DELETE /v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}
def delete_domain_user_group_role(domain_id, group_id, role_id):
    result = conn.identity.delete_domain_group_role(domain_id, group_id, role_id)
    if result is True:
        print("Delete permission to a user group of domain successfully")
    else:
        print("Delete permission to a user group of domain failure")


# Delete Permissions of a User Group Corresponding to a Project
# DELETE /v3/projects/{project_id}/groups/{group_id}/roles/{role_id}
def delete_project_user_group_role(project_id, group_id, role_id):
    result = conn.identity.delete_project_group_role(project_id, group_id, role_id)
    if result is True:
        print("Delete permission to a user group of project successfully")
    else:
        print("Delete permission to a user group of project failure")


# Grant permissions to a user group corresponding to all projects
# PUT /v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects
def grant_all_projects_group_role(domain_id, group_id, role_id):
    result = conn.identity.grant_all_projects_group_role(domain_id, group_id, role_id)
    if result is True:
        print("Grant permissions to a user group corresponding to all projects successfully")
    else:
        print("Grant permissions to a user group corresponding to all projects failure")


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
    grant_all_projects_group_role(domain_id, group_id, role_id)
