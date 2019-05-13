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



#list_policy
def list_policy(groupId):
    query = {
        "name": "as-policy-s5dg",
        "type": "ALARM",
        "marker": 0,
        "limit": 20
    }
    policies = self.conn.auto_scaling.policies (groupId, **query)
    print(list(policies))

#get detail policy
def detail_policy(groupId):
    policy = conn.auto_scaling.get_policy(groupId)
    print(policy)

# creat policy daily
def creat_policy_Daily(groupId):
    as_policy_name = "as-policy-name"
    _policy = {
        "name":"as-policy-name",
        "scaling_policy_action":{
            "operation":"ADD",
            "instance_number":1
        },
        "cool_down_time": 900,
        "scheduled_policy" :{
            "launch_time": "16:00",
            "recurrence_type":"Daily",
            "recurrence_value":None,
            "start_time":"2017-11-12T04:34Z",
            "end_time": "2017-12-27T03:34Z"
        },
        "type": "RECURRENCE",
        "scaling_group_id": groupId
    }
    policy = conn.auto_scaling.create_policy(**_policy)
    policy = conn.auto_scaling.get_policy(policy)
    print(policy)

#creat policy weekly
def creat_policy_Weekly(groupId):
    as_policy_name = "as-policy-name"
    _policy = {
        "name":"as-policy-name",
        "scaling_policy_action":{
            "operation":"ADD",
            "instance_number":1
        },
        "cool_down_time": 900,
        "scheduled_policy" :{
            "launch_time": "16:00",
            "recurrence_type":"Weekly",
            "recurrence_value":"1,2,3",
            "start_time":"2017-11-12T04:34Z",
            "end_time": "2017-12-27T03:34Z"
        },
        "type": "RECURRENCE",
        "scaling_group_id": groupId
    }
    policy = conn.auto_scaling.create_policy(**_policy)
    policy = conn.auto_scaling.get_policy(policy)
    print(policy)

#creat policy Monthly
def creat_policy_Monthly(groupId):
    as_policy_name = "as-policy-name"
    _policy = {
        "name":"as-policy-name",
        "scaling_policy_action":{
            "operation":"ADD",
            "instance_number":1
        },
        "cool_down_time": 900,
        "scheduled_policy" :{
            "launch_time": "16:00",
            "recurrence_type":"Monthly",
            "recurrence_value":"1,2,3,24",
            "start_time":"2017-11-12T04:34Z",
            "end_time": "2018-12-27T03:34Z"
        },
        "type": "RECURRENCE",
        "scaling_group_id": groupId
    }
    policy = conn.auto_scaling.create_policy(**_policy)
    policy = conn.auto_scaling.get_policy(policy)
    print(policy)

#creat policy scheduled
def creat_policy_scheduled(groupId):
    as_policy_name = "as-policy-name"
    _policy = {
        "name":"as-policy-name",
        "scaling_policy_action":{
            "operation":"ADD",
            "instance_number":1
        },
        "cool_down_time": 900,
        "scheduled_policy" :{
            "launch_time": "2017-11-20T16:00Z",
            "recurrence_type":None,
            "recurrence_value":None,
            "start_time":None,
            "end_time": None
        },
        "type": "SCHEDULED",
        "scaling_group_id": groupId
    }
    policy = conn.auto_scaling.create_policy(**_policy)
    policy = conn.auto_scaling.get_policy(policy)
    print(policy)

#creat policy Alarm
def creat_policy_Alarm(groupId):
    # as_policy_name = "as-policy-name"
    _policy = {
        "name":"as-policy-name",
        "scaling_policy_action":{
            "operation":"ADD",
            "instance_number":1
        },
        "cool_down_time": 900,
        "scheduled_policy" :{
            "launch_time": None,
            "recurrence_type":None,
            "recurrence_value":None,
            "start_time":None,
            "end_time": None
        },
        "type": "ALARM",
        "alarm_id": "al1510663515403vr5RRKWrd",
        "scaling_group_id": as_group_id
    }
    policy = conn.auto_scaling.create_policy(**_policy)
    policy = conn.auto_scaling.get_policy(policy)
    print(policy)

#modify policy Alarm
def modify_policy_Alarm(to_update_policy_id):
    _policy = {
        "name":"as-policy-name",
        "scaling_policy_action":{
            "operation":"ADD",
            "instance_number":1
        },
        "cool_down_time": 900,
        "scheduled_policy" :{
            "launch_time": None,
            "recurrence_type":None,
            "recurrence_value":None,
            "start_time":None,
            "end_time": None
        },
        "type": "ALARM",
        "alarm_id": "al1510663515403vr5RRKWrd",
    }
    policy = conn.auto_scaling.update_policy(to_update_policy_id,**_policy)
    policy = conn.auto_scaling.get_policy(policy)
    print(policy)

#excute policy
def excute_policy():
    conn.auto_scaling.execute_policy("ce2f1071-acc9-418e-b5f7-1a7bc82e4aa3")

#pause policy
def pause_policy():
    conn.auto_scaling.pause_policy("ce2f1071-acc9-418e-b5f7-1a7bc82e4aa3")

#resume policy
def resume_policy():
    conn.auto_scaling.resume_policy("ce2f1071-acc9-418e-b5f7-1a7bc82e4aa3")

#delete policy
def delete_policy():
    conn.auto_scaling.delete_policy("ce2f1071-acc9-418e-b5f7-1a7bc82e4aa3")

if __name__ == "__main__":
    groupId = "ce2f1071-acc9-418e-b5f7-1a7bc82e4aa3"
    to_update_policy_id = "ce2f1071-acc9-418e-b5f7-1a7bc82e4aa3"
    list_policy(groupId)
    detail_policy(groupId)
    creat_policy_Daily(groupId)
    creat_policy_Weekly(groupId)
    creat_policy_Monthly(groupId)
    creat_policy_scheduled(groupId)
    creat_policy_Alarm(groupId)
    modify_policy_Alarm(to_update_policy_id)
    excute_policy()
    pause_policy()
    resume_policy()
    delete_policy()
