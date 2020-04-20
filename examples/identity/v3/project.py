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


# Creat a project
# POST /v3/projects
def create_project():
    project = {
        "name": "**********",
        "parent_id": "**********",
        "domain_id": "**********",
        "description": "**********"
    }
    project = conn.identity.create_project(**project)
    print(project)


# Modify a project
# PATCH /v3/projects/{project_id}
def modify_project(project_id):
    project = {
        "name": "**********",
        "description": "**********"
    }
    project = conn.identity.update_project(project_id, **project)
    print(project)


# Query a project list
# GET /v3/projects
def get_project_list():
    projects = conn.identity.projects()
    # projects = conn.identity.projects(domain_id="**********", enabled="**********", is_domain="**********",
    #                                   name="**********", page="**********", parent_id="**********",
    #                                   per_page="**********")
    for project in projects:
        print(project)


# Query project details
# GET /v3/projects/{project_id}
def get_project_detail(project_id):
    project = conn.identity.get_project(project_id)
    print(project)


# Query a user project list
# GET /v3/users/{user_id}/projects
def list_user_projects(user_id):
    projects = conn.identity.list_user_projects(user_id)
    for project in projects:
        print(project)


# Query the list of projects accessible to users
# GET /v3/auth/projects
def get_project_scopes():
    projects = conn.identity.get_project_scopes()
    for project in projects:
        print(project)


if __name__ == "__main__":
    project_id = "**********"
    user_id = "**********"
    get_project_list()
    list_user_projects(user_id)
    create_project()
    get_project_detail(project_id)
    modify_project(project_id)
    get_project_scopes()
