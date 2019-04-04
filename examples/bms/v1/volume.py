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

# bms attach Volume
def mount_disk(conn):
    data = {
        "volumeId": "******",
        "device": "*****"
    }
    server_id = '*******'
    mount = conn.bms.create_volume_attachment(server_id,**data)
    print(mount)

# bms detach Volume
def umount_disk(conn):
    server_id = '*******'
    attachment_id = '*******'
    umount = conn.bms.delete_volume_attachment(server_id, attachment_id)
    print(umount)


if __name__ == "__main__":
     mount_disk(conn)
     umount_disk(conn)