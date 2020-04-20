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


# Query an agency list
# GET /v3.0/OS-AGENCY/agencies
def get_agency_list():
    agencies = conn.iam.agencies(domain_id=userDomainId)
    # agencies = conn.iam.agencies(domain_id=userDomainId, name="**********", trust_domain_id="**********")
    for agency in agencies:
        print(agency)


# Query agency details
# GET /v3.0/OS-AGENCY/agencies/{agency_id}
def get_agency():
    agency_id = "**********"
    agency = conn.iam.get_agency(agency_id)
    print(agency)


# Create agency
# POST /v3.0/OS-AGENCY/agencies
def create_agency():
    agency = {
        "name": "**********",
        "domain_id": "**********",
        "trust_domain_id": "**********",
        "trust_domain_name": "**********",
        "duration": "**********",
        "description": "**********"
    }
    agency = conn.iam.create_agency(**agency)
    print(agency)


# Update agency
# POST /v3.0/OS-AGENCY/agencies
def update_agency():
    agency_id = "**********"
    agency = {
        "agency": {
            "trust_domain_id": "**********",
            "trust_domain_name": "**********",
            "description": "**********",
            "duration": "**********"
        }
    }
    agency = conn.iam.update_agency(agency_id, **agency)
    print(agency)


# Delete agency
# DELETE /v3.0/OS-CREDENTIAL/credentials/{access_key}
def delete_agency():
    agency_id = "**********"
    conn.iam.delete_agency(agency_id)


# Query domain permissions of an agency
# GET /v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles
def list_domain_agency_role():
    domain_id = "**********"
    agency_id = "**********"
    roles = conn.iam.list_domain_agency_role(domain_id, agency_id)
    for role in roles:
        print(role)


# Query project permissions of an agency
# GET /v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles
def list_project_agency_role():
    project_id = "**********"
    agency_id = "**********"
    roles = conn.iam.list_project_agency_role(project_id, agency_id)
    for role in roles:
        print(role)


# Grant domain permission to an agency
# PUT /v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}
def grant_domain_agency_role():
    domain_id = "**********"
    agency_id = "**********"
    role_id = "**********"
    result = conn.iam.grant_domain_agency_role(domain_id, agency_id, role_id)
    if result is True:
        print("Grant domain permission to an agency successfully")
    else:
        print("Grant domain permission to an agency failure")


# Grant project permission to an agency
# PUT /v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}
def grant_project_agency_role():
    project_id = "**********"
    agency_id = "**********"
    role_id = "**********"
    result = conn.iam.grant_project_agency_role(project_id, agency_id, role_id)
    if result is True:
        print("Grant project permission to an agency successfully")
    else:
        print("Grant project permission to an agency failure")


# Query whether an agency has specific domain permission
# HEAD /v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}
def check_domain_agency_role():
    domain_id = "**********"
    agency_id = "**********"
    role_id = "**********"
    result = conn.iam.check_domain_agency_role(domain_id, agency_id, role_id)
    if result is True:
        print("The agency has this domain permission")
    else:
        print("The agency doesn't have this domain permission")


# Query whether an agency has specific project permission
# HEAD /v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}
def check_project_agency_role():
    project_id = "**********"
    agency_id = "**********"
    role_id = "**********"
    result = conn.iam.check_project_agency_role(project_id, agency_id, role_id)
    if result is True:
        print("The agency has this project permission")
    else:
        print("The agency doesn't have this project permission")


# Delete domain permission of an agency
# DELETE /v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}
def delete_domain_agency_role():
    domain_id = "**********"
    agency_id = "**********"
    role_id = "**********"
    result = conn.iam.delete_domain_agency_role(domain_id, agency_id, role_id)
    if result is True:
        print("Delete domain permission of an agency successfully")
    else:
        print("Delete domain permission of an agency failure")


# Delete project permission of an agency
# DELETE /v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}
def delete_project_agency_role():
    project_id = "**********"
    agency_id = "**********"
    role_id = "**********"
    result = conn.iam.delete_project_agency_role(project_id, agency_id, role_id)
    if result is True:
        print("Delete project permission of an agency successfully")
    else:
        print("Delete project permission of an agency failure")


if __name__ == "__main__":
    get_agency_list()
    get_agency()
    create_agency()
    update_agency()
    delete_agency()
    list_domain_agency_role()
    list_project_agency_role()
    grant_domain_agency_role()
    grant_project_agency_role()
    check_domain_agency_role()
    check_project_agency_role()
    delete_domain_agency_role()
    delete_project_agency_role()
