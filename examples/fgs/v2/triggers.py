# -*-coding:utf-8 -*-
import os
from openstack import connection

# setup endpoint override for cloud services
# "example" in the endpoint stands for "Region.Cloud"
os.environ.setdefault(
    'OS_FUNCTIONGRAPH_ENDPOINT_OVERRIDE',
    'https://functiongraph.cn-north-1.myhuaweicloud.com/v2/%(project_id)s'
)

# create connection
username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"       # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"        # iam url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)

#create function
def create_function():
  function_req = {
      "func_name": "TestCreateFunctionInPythonSdk",
      "runtime": "Python3.6",
      "code_type": "inline",
      "timeout":30,
      "handler":"index.handler",
      "package": "default",
      "memory_size":128,
      "func_code": {
          "file": "aW1wb3J0IGpzb24KZGVmIGhhbmRsZXIgKGV2ZW50LCBjb250ZXh0KToKICAgIG91dHB1dCA9ICdIZWxsbyBtZXNzYWdlOiAnICsganNvbi5kdW1wcyhldmVudCkKICAgIHJldHVybiBvdXRwdXQ="
      }
  }
  function = conn.fgs.creat_function(**function_req)
  print(function)
  return function

#create trigger
def create_trigger(func_urn):
    function_req = {
        "trigger_type_code": "APIG",
        "event_type_code": "APICreated",
        "event_data": {
            "group_id": "6a50c9199d7f4857818188aeb3c3dc0b",
            "auth": "IAM",
            "backend_type": "FUNCTION",
            "env_id": "DEFAULT_ENVIRONMENT_RELEASE_ID",
            "env_name": "RELEASE",
            "func_info":{
                "timeout": 5000
            },
            "match_mode": "SWA",
            "name": "TestCreateTriggerSdk",
            "path": "/TestCreateFunctionInPythonSdk",
            "protocol": "HTTPS",
            "req_method": "ANY",
            "sl_domain": "6f53d3cf3b804cc3a1ea312c36bbc8b5.apigw.southchina.huaweicloud.com",
            "type": 1
        }
    }
    trigger = conn.fgs.create_trigger(func_urn,**function_req)
    print(trigger)
    return trigger

#Get list of  trigger
def get_trigger_list(func_urn):
    trigger = list(conn.fgs.trigges(func_urn))
    print(trigger)
    return  None

#Get a trigger
def get_trigger(func_urn,trigger_type_code,trigger_id):
    trigger = conn.fgs.get_trigger(func_urn,trigger_type_code,trigger_id)
    print(trigger)
    return trigger

#delete trigger by func_urn
def delete_all_trigger(func_urn):
    trigger = conn.fgs.delete_all_triggers(func_urn)
    return trigger

#delete trigger
def delete_trigger(function_urn,trigger_type_code,trigger_id):
    trigger = conn.fgs.delete_trigger(function_urn,trigger_type_code,trigger_id)
    return trigger


if __name__ == "__main__":
    #create function
    func = create_function()
    if func.func_urn:
        #create trigger
        trigger=create_trigger(func.func_urn)
        get_trigger(func.func_urn, trigger.trigger_type_code, trigger.trigger_id)
        delete_all_trigger(func.func_urn)
        conn.fgs.delete_function(func.func_urn[:-7])
