#!/usr/bin/env python
#coding=utf-8

import sys
from openstack import connection
from openstack import utils

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


#create lifecycle_hook
def create_life_cycle_hook(groupId):
   attrs = {
       "lifecycle_hook_name": "test-hook_c",
       "lifecycle_hook_type": "INSTANCE_LAUNCHING",
       "default_result": "CONTINUE",
       "default_timeout": "86400",
       "notification_topic_urn": "urn:smn:cn-suzhou2-1:ebac0c927c104c4587687ce375d0b656:ces_tset",
       "notification_metadata": "xxxxxxx"
   }
   new_hook = conn.auto_scaling.create_lifecycle_hook(groupId,**attrs)
   print(list(new_hook))


#list life cycle hook
def list_life_cycle_hook(groupId):
    hooks = conn.auto_scaling.lifecycle_hooks(groupId)
    print(list(hooks))

#query life cycle hook_dtai
def query_life_cycle_hook_detail(groupId):
    hook_name = "test-hook_6"
    hook_detail = conn.auto_scaling.get_lifecycle_hook(groupId,hook_name)
    print(hook_detail)

#update life cycle hook
def update_life_cycle_hook(groupId):
   hook_name = "test-hook_a"
   attrs = {
       "lifecycle_hook_type": "INSTANCE_LAUNCHING",
       "default_result": "CONTINUE",
       "default_timeout": "86400",
       "notification_topic_urn": "urn:smn:cn-suzhou2-1:ebac0c927c104c4587687ce375d0b656:1025",
       "notification_metadata": "<>&'( )"
   }
   update_hook = conn.auto_scaling.update_lifecycle_hook(groupId,hook_name,**attrs)
   update_hook = conn.auto_scaling.lifecycle_hooks(groupId)
   print(list(update_hook))

#delete life cycle hook
def delete_life_cycle_hook(groupId):
   hook_name = "test-hook_1"
   conn.auto_scaling.delete_lifecycle_hook(groupId,hook_name)
   hooks = conn.auto_scaling.lifecycle_hooks(groupId)
   print(list(hooks))

#life cycle hook instance
def get_group_hanging_instance(groupId):
   query = {
        "instance_id": "6638cce3-e76d-4bee-a56b-c6a7066fa86c"
   }
   temp = conn.auto_scaling.get_group_hanging_instance(groupId,**query)
   for i in temp:
       print i
   print(temp)

#life cycle hook callback
def callback_group_hanging_instance(groupId):
   attrs = {
       "lifecycle_action_result": "ABANDON",
      # "lifecycle_action_key":"449ffb6d-14c8-4d07-bc38-104269c15f86",
       "instance_id": "7565235f-c1a3-464a-b558-cd7c6df5a888",
       "lifecycle_hook_name": "test-hook_a"
   }
   conn.auto_scaling.call_back_instance(groupId,**attrs)

if __name__ == "__main__":
    groupId = "c031932b-b4d1-47d8-a403-7a394d34d930"
    create_life_cycle_hook(groupId)
    list_life_cycle_hook(groupId)
    query_life_cycle_hook_detail(groupId)
    update_life_cycle_hook(groupId)
    delete_life_cycle_hook(groupId)
    get_group_hanging_instance(groupId)
    callback_group_hanging_instance(groupId)