#!/usr/bin/python
# -*- coding: utf-8 -*-

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


# Querying a Function List
def get_function_list():
    function_list = conn.fgs.functions(marker=0,maxitems=400)
    for data in function_list:
        print(data)
    return None

#Creating a Function
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
  function = conn.fgs.create_function(**function_req)
  print(function)
  return function

# Querying the Metadata Information of a Function
def get_function_metadata(function_urn):
    function = conn.fgs.get_function_metadata(function_urn)
    print(function)
    return function

# Querying the Code of a Function
def get_function_code(function_urn):
    function = conn.fgs.get_function_code(function_urn)
    return function

# Deleting a Function
def del_function(function_urn):
    function = conn.fgs.delete_function(function_urn)
    return function

# Modifying the Code of a Function
def update_function_code(function_urn):
    function_req={
        "code_filename": "index.zip",
        "code_type": "inline",
        "code_url": "",
        "depend_list": [],
        "dependency_pkg": "",
        "func_code": {
            "file": "UEsDBAoAAAAAAO5Qak5BtFZEugAAALoAAAAIAAAAaW5kZXgucHlpbXBvcnQganNvbgpkZWYgaGFuZGxlciAoZXZlbnQsIGNvbnRleHQpOgogICAgb3V0cHV0ID0gJ0hlbGxvIG1lc3NhZ2U6ICcgKyBqc29uLmR1bXBzKGV2ZW50KQogICAgcHJpbnQoIjIzMjM0MjQzNDM0MzQzNDM0MzQzNTQ1MzQzPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgIHJldHVybiBvdXRwdXRQSwECHgMKAAAAAADuUGpOQbRWRLoAAAC6AAAACAAAAAAAAAAAAAAAtIEAAAAAaW5kZXgucHlQSwUGAAAAAAEAAQA2AAAA4AAAAAAA",
            "link": ""
        }
    }
    function = conn.fgs.update_function_code(function_urn,**function_req)
    return  function

# Modifying the Metadata Information of a Function
def update_function_conf(function_urn):
    function_req={
        "app_xrole": "",
        "description": "",
        "func_name": "TestCreateFunctionInPythonSdk",
        "depend_list": [],
        "dependency_pkg": "",
        "func_vpc": {
            "subnet_id": "",
            "vpc_id": ""
        },
        "handler":"index.handler",
        "initializer_handler": "",
        "initializer_timeout": 0,
        "memory_size": 256,
        "runtime":"Python3.6",
        "strategy_config":{
            "concurrency": -1
        },
        "timeout":300,
        "user_data":"",
        "xrole":""
    }
    function = conn.fgs.update_function_metadata(function_urn,**function_req)
    return  function

# Publishing a Function Version
def public_function_verion(function_urn):
    function_req = {
        "description": "test1.0.1↵函数服务发布版本1.0.1",
        "version": "1.0.1"
    }
    function = conn.fgs.publish_function_version(function_urn,**function_req)
    return  function

# Creating an Alias for a Function Version
def create_function_aliase(function_urn):
    function_req = {
        "additional_version_weights": {
            "1.0.1":50
        },
        "description":"函数服务灰度版本别名",
        "name":"latest-1_1",
        "version": "latest"
    }
    function = conn.fgs.create_function_aliase(function_urn,**function_req)
    return  function

# Modifying the Alias Information of a Function Version
def update_function_aliase(function_urn,alias_name):
    function_req = {
        "additional_version_weights": {
            "1.0.1":80
        },
        "description":"函数服务灰度版本别名",
        "version": "latest"
    }
    function = conn.fgs.update_function_aliase(function_urn,alias_name,**function_req)
    return  function

# Querying the Alias Information of a Function Version
def get_function_aliase(function_urn,alias_name):
    function = conn.fgs.get_function_aliase(function_urn,alias_name)
    return  function

# Querying the Aliases of a Function's All Versions
def get_function_aliase_list(function_urn):
    function_list = list(conn.fgs.function_aliases(function_urn))
    print(function_list)
    return  None

# Deleting an Alias of a Function Version
def delete_function_aliase(function_urn,alias_name):
    function = conn.fgs.delete_function_aliase(function_urn,alias_name)
    return  function

# Executing a Function Synchronously
def execut_function_synchronously(function_urn):
    function_req = {
        "test1":"value1"
    }
    function = conn.fgs.execute_function_synchronously(function_urn,**function_req)
    return  function

# Executing a Function Asynchronously
def execut_function_asynchronously(function_urn):
    function_req = {
        "test2":"value2"
    }
    function = conn.fgs.execute_function_asynchronously(function_urn,**function_req)
    return  function

# Querying the Aliases of a Function's All Versions
def get_function_version(function_urn):
    function_list = conn.fgs.get_function_version(function_urn=function_urn,marker=0,maxitems=400)
    for data in function_list:
        print(data)
    return None

if __name__ == "__main__":
    #Querying a Function List
    get_function_list()

    #Creating a Function
    func = create_function()
    if func.func_urn:
        #Querying the Metadata Information of a Function
        func_get_conf = get_function_metadata(func.func_urn)
        print("func_get_conf:")
        print(func_get_conf)
        #Executing a Function Synchronously
        execut_function_syn = execut_function_synchronously(func.func_urn)
        print("execut_function_synchronously:")
        print(execut_function_syn)
        #Modifying the Code of a Function
        func_update_conf = update_function_conf(func.func_urn)
        print("func_update_conf:")
        print(func_update_conf)
        #Publishing a Function Version
        func_public_version = public_function_verion(func.func_urn)
        print("public_function_verion:")
        print(func_public_version)
        #Querying the Aliases of a Function's All Versions
        get_function_version=get_function_version(func.func_urn)
        print("get_function_version:")
        print(get_function_version)
        #Querying the Code of a Function
        func_get_code = get_function_code(func.func_urn)
        print("func_get_code:")
        print(func_get_code)
        #Modifying the Code of a Function
        func_update_code = update_function_code(func.func_urn)
        print("func_update_code:")
        print(func_update_code)
        #Creating an Alias for a Function Version
        func_create_aliase = create_function_aliase(func.func_urn)
        print("create_function_aliase:")
        print(func_create_aliase)
        #Modifying the Alias Information of a Function Version
        func_update_aliase = update_function_aliase(func.func_urn,func_create_aliase.name)
        print("update_function_aliase:")
        print(func_update_aliase)
        #Querying the Alias Information of a Function Version
        get_function_aliase(func.func_urn,func_create_aliase.name)
        #Querying the Aliases of a Function's All Versions
        get_function_aliase_list(func.func_urn)
        #Executing a Function Asynchronously
        execut_func_asynchronously = execut_function_asynchronously(func.func_urn)
        print("execut_function_asynchronously:")
        print(execut_func_asynchronously)
        #Deleting an Alias of a Function Version
        delete_function_aliase(func.func_urn, func_create_aliase.name)
        #Deleting a Function or Function Version
        del_function(func.func_urn[:-7])
