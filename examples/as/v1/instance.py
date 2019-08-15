#!/usr/bin/env python
#coding=utf-8


import logging
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

#list_instance
def list_instance(groupId):
    query = {
        "lifecycle": "INSERVICE",
        "health_status": "NORMAL",
        "marker": 0,
        "limit": 10
    }
    instances = conn.auto_scaling.instances(groupId, **query)
    print(list(instances))


#delete instances
def delete_instance(instance_to_be_removed):
    conn.auto_scaling.remove_instance(instance_to_be_removed, delete_instance= False)

#batchdelete instances
def batchdelete_instance(group_of_instance):
    instance_to_be_removed = ["505f7cd1-62d6-457b-8acf-9d02097e83f3","af633ab6-7855-4115-b5fd-9009f727d1c0"]
    conn.auto_scaling.batch_remove_instances(group_of_instance,instance_to_be_removed, delete_instance= False)


#batchadd instances
def batchdadd_instance(group_of_instance):
    instance_to_be_added = ["505f7cd1-62d6-457b-8acf-9d02097e83f3","af633ab6-7855-4115-b5fd-9009f727d1c0"]
    conn.auto_scaling.batch_add_instances(group_of_instance,instance_to_be_added)

if __name__ == "__main__":
    groupId = "4d14467d-d40c-4caf-9fd4-575e01237550"
    list_instance(groupId)
    delete_instance(groupId)
    batchdelete_instance(groupId)
    batchdadd_instance(groupId)
