#!/usr/bin/env python
#coding=utf-8

from openstack import connection

# create connection
username = "xxxxxxxxxx"
password = "xxxxxxxxxx"
projectId = "xxxxxxxxxx"
userDomainId = "xxxxxxxxxx"
auth_url = "xxxxxxxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
)

#quota list
def list_quota():
    quotas = list(self.conn.auto_scaling.quotas())
    print(quotas)

#group quota list
def list_group_quota(groupId):
    quotas = list(conn.auto_scaling.quotas(groupId))
    print(quotas)

if __name__ == "__main__":
    groupId = "ce2f1071-acc9-418e-b5f7-1a7bc82e4aa3"
    list_quota()
    list_group_quota(groupId)