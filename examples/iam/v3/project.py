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


# Update project status
# PUT /v3-ext/projects/{project_id}
def update_project_status():
    project_id = "**********"
    project = {
        "project": {
            "status": "**********"
        }
    }
    result = conn.iam.update_project_status(project_id, project)
    if result is True:
        print("Update project status successfully")
    else:
        print("Update project status failure")

# Query project details and status
# GET /v3-ext/projects/{project_id}
def get_project_details_and_status():
    project_id = "**********"
    result = conn.iam.get_project_details_and_status(project_id)
    print(result)


if __name__ == "__main__":
    update_project_status()
    get_project_details_and_status()
