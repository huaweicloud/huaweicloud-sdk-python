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


# Creating a Project
def create_project():
    project = {
        "name": "**********",
        "description": "**********"
    }
    conn.identity.create_project(**project)


# Modifying a Project
def modify_project(project_id):
    project = {
        "name": "**********",
        "description": "**********"
    }
    conn.identity.update_project(project_id, **project)


# Querying a Project List
def get_project_list():
    projects = conn.identity.projects()
    for project in projects:
        print(project)


# Querying Project Details
def get_project_detail(project_id):
    project = conn.identity.get_project(project_id)
    print(project)


# Querying a User Project List
def list_user_projects(user_id):
    projects = conn.identity.list_user_projects(user_id)
    for project in projects:
        print(project)


# Querying the List of Projects Accessible to Users
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