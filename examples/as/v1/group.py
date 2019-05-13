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


#get list group
def list_group():
    query = {
        "name": "as-group-sff3",
        "atatus": "INSERVICE",
        "scaling_configuration_id": "c3689181-ad0a-46a5-b02c-d02446a29d90",
        "marker": 0,
        "limit": 10
    }
    groups = conn.auto_scaling.groups(**query)
    print(list(groups))

#get detail group
def detail_group(groupId):
    group = conn.auto_scaling.get_group(groupId),
    print(group)

#creat group
def create_group():
    _group = {
        "name": "as_NameTest1",
        "scaling_configuration_id": "e4d80962-426c-4590-8914-b362bc2b52a7",
        "desire_instance_number": 1,
        "min_instance_number" : 0,
        "max_instance_number" : 4,
        "cool_down_time" : 900,
        # "lb_listener_id" : "3aafa7259b3341869d714793bccfe368,3aafa7259b3341869d714793bccfe368",
        "available_zones" : ["cn-east-2a"],
        "health_periodic_audit_method" :"NOVA_AUDIT",
        "health_periodic_audit_time" : 5,
        "instance_terminate_policy" : "OLD_CONFIG_OLD_INSTANCE",
        "vpc_id" : "44107f7c-f978-4b59-ab23-5ea0933a013c",
        "networks" : [{
            "id": "b70522aa-0930-4f69-84c7-09cf26c977f6"
        }],
        "notifications" : ["EMAIL"],
        "detete_publicip" : "true",
        "security_groups":[{
            "id" : "b5024e19-fd6b-4464-86a0-005ea0c48934"
        }]
    }
    group = conn.auto_scaling.create_group(**_group)
    group = conn.auto_scaling.get_group(group)
    print(group)

#modify group
def modify_group(to_update_group_id):
    _group = {
        "name": "as_NameTest1",
        "scaling_configuration_id": "c3689181-ad0a-46a5-b02c-d02446a29d90",
        "desire_instance_number": 0,
        "min_instance_number": 0,
        "max_instance_number": 10,
        "cool_down_time": 800,
        "lb_listener_id": "d54bab4ca7044f1ab4c1d122f508383f",
        "available_zones": ["cn-north-1b"],
        "health_periodic_audit_method": "ELB_AUDIT",
        "health_periodic_audit_time": 15,
        "instance_terminate_policy": "OLD_CONFIG_NEW_INSTANCE",
        "networks": [{
        "id": "14e9645f-b282-4b60-965d-f9c822ca9c87"
         }],
        "notifications": ["EMAIL"],
        "detete_publicip": "true",
        "security_groups": [{
             "id": "87eed692-a9d7-46bd-a68b-645a0bf4ccf3"
         }]
    }
    group = conn.auto_scaling.update_group(to_update_group_id, **_group)
    group = conn.auto_scaling.get_group(group)
    print(group)

#resume group
def resume_group(groupId):
    conn.auto_scaling.resume_group(groupId)
    group = conn.auto_scaling.get_group(groupId)
    print(group)

#stop group
def pause_group(groupId):
    conn.auto_scaling.pause_group(groupId)
    group = conn.auto_scaling.get_group(groupId)
    print(group)

#delete group
def delete_group(groupId):
    conn.auto_scaling.delete_group(groupId)
    print("delete_ok")

if __name__ == "__main__":
    to_update_group_id = "56bcf54f-0100-4c17-b986-a6afacbdfc74"
    groupId = "485fe089-e9bf-4cfb-a7ac-d39e48d5ae07"
    list_group()
    detail_group(groupId)
    create_group()
    modify_group(to_update_group_id)
    resume_group(groupId)
    pause_group(groupId)
    delete_group(groupId)
