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

#query activity list
def list_activity(group):
    query = {
        "start_time": "2017-06-22T01:21:02Z",
        "end_time": "2017-06-22T15:00:02Z",
        "limit": 10
    }
    activities = conn.auto_scaling.activities(group, **query)
    print(activities)

if __name__ == "__main__":
    group = "588b4592-0998-4722-b51d-e6dbc574ec32"
    list_activity(group)
