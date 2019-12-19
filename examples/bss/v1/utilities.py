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
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # endpoint url

if __name__ == '__main__':
    data = {
        "receiverType": "1",
        "scene": "29",
        "mobilePhone": "123456789",
        "countryCode": "0086"
    }
    conn = connection.Connection(auth_url=auth_url,
                                 user_domain_id=userDomainId,
                                 domain_id=userDomainId,
                                 username=username,
                                 password=password)
    '''
    If customers enter email addresses for registration, this API is used to send a registration verification code to the email addresses to verify the registration information.
    This API can be invoked only by the partner AK/SK or token.    
    '''
    ff = conn.bss.send_verification_code(userDomainId, **data)
    print(ff)
