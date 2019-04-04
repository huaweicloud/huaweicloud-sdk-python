# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack import connection

auth_url = '******'
userDomainId = '******'
projectId = '******'
username = '******'
password = '******'

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)

# create bms server
def create_server(_conn):
    data = {
    "imageRef" : "******",
    "flavorRef" : "******",
    "name" : "******",
    "metadata" : {
      "op_svc_userid" : "******"
    },
    "nics" : [ {
      "subnet_id" : "******",
      "ip_address" : "******"
    } ],
    "availability_zone" : "******",
    "vpcid" : "******",
    "count" : 1,
    "data_volumes" : [ {
      "volumetype" : "SATA",
      "size" : 10,
      "shareable" : False
    } ],
    "extendparam" : {
      "periodType" : "month",
      "periodNum" : 1,
      "isAutoPay" : True
    },
    "schedulerHints" : {
      "dec_baremetal" : "share"
    },
    "key_name": "******",
    "security_groups": [{
        "id": "******"
    }]
  }


    create_server = _conn.bms.create_server(**data)
    print create_server

# query bms server details
def get_server(conn):
    server_id = '******'
    server = conn.bms.get_server(server_id)
    print server

# rename bms server 
def rename_server(conn):
    server_id = '*******'
    data = {
        "name": "*******"
    }
    update_server = conn.bms.update_server_name(server_id, **data)
    print update_server


if __name__ == "__main__":
    create_server(conn)
    get_server(conn)
    rename_server(conn)
