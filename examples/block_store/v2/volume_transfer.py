# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
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

import os
from openstack import connection

# create connection
username = "xxxxxx"
password = os.getenv('get_secret_code')
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)

# create volume transfer
def create_volume_transfer():
    data = {
        "volume_id": "xxx",
        "name": "volume_transfer_test"
    }
    print(conn.block_store.create_volume_transfer(**data))

# accept volume transfer
def accept_volume_transfer():
    transfer_id = 'xxx'
    data = {
        "accept": {
            "auth_key": "xxx"
        }
    }
    print(conn.block_store.accept_volume_transfer(transfer_id, **data))

# delete volume transfer
def delete_volume_transfer():
    transfer_id = 'xxx'
    print(conn.block_store.delete_volume_transfer(transfer_id))

# get volume transfer
def get_volume_transfer():
    transfer_id = 'xxx'
    print(conn.block_store.get_volume_transfer(transfer_id))

# volume transfers
def volume_transfers():
    for index in conn.block_store.volume_transfers(details=False):
        print(index)


if __name__ == '__main__':
    create_volume_transfer()
    accept_volume_transfer()
    delete_volume_transfer()
    get_volume_transfer()
    volume_transfers()
