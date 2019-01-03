# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
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

import sys
from openstack import connection
from openstack import utils

# utils.enable_logging(debug=True, stream=sys.stdout)

username = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"
projectId = "xxxxxxxxxxx"
userDomainId = "xxxxxxxxxx"
auth_url = "xxxxxxxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


def test_show_all_whitelist():
    wls = list(conn.network.whitelists())
    print('whitelist numbers: ', len(wls))
    for wl in wls:
        print(wl)


def test_show_whitelist(wl_id):
    print(conn.network.get_whitelist(wl_id))


def test_create_whitelist(ls_id, wlist):
    wl = conn.network.create_whitelist(listener_id = ls_id,
                                       enable_whitelist = True,
                                       whitelist = wlist)
    return wl


def test_update_whitelist(wl_id, wlist):
    wlist = { 'enable_whitelist' : False, 'whitelist' : wlist}
    wl_update = conn.network.update_whitelist(wl_id, **wlist)
    return wl_update


def test_delete_whitelist(wl_id):
    conn.network.delete_whitelist(wl_id)


if __name__ == "__main__":
    # listener without whitelist
    ls_id = "805062ed-dfbd-4904-828c-8fe11121c0e9"
    wlist = "192.168.0.3,192.168.0.6,192.168.0.9"
    wlist2 = "192.168.1.3,192.168.1.6,192.168.1.9"
    whiteList = test_create_whitelist( ls_id, wlist )
    whiteList_update = test_update_whitelist( whiteList.id, wlist2 )
    test_show_whitelist(whiteList_update.id)
    test_show_all_whitelist()
    test_delete_whitelist(whiteList_update.id)