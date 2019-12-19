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

import sys

from openstack import connection


# create connection
username = "xxxxxx"
password = "xxxxxx"
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # endpoint url

if __name__ == '__main__':
    conn = connection.Connection(auth_url=auth_url,
                                 user_domain_id=userDomainId,
                                 domain_id=userDomainId,
                                 username=username,
                                 password=password)

    data = {
        "customerId": "xxxxxxxxxxxxxxxxxxxxx",
        "identifyType": 0,
        "verifiedType": 0,
        "verifiedFileURL": [
            "zhengmian.jpg",
            "fanmian.jpg",
            "chizheng2.jpg"
        ],
        "name": "NAME",
        "verifiedNumber": "xxxxxxxxxxx",
        "changeType": -1,
        "xaccountType": "xxxx_IDP"
    }
    '''
    This API can be used to submit an individual real-name authentication application.
    This API can be invoked only by the partner account AK/SK or token.    
    '''
    ff = conn.bssintl.individual_realname_auth(userDomainId, **data)
    print(ff)


    data = {
        "customerId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "identifyType": 1,
        "certificateType": 0,
        "verifiedFileURL": [
            "zhengmian.jpg",
            "fanmian.jpg",
            "chizheng2.jpg"
        ],
        "corpName": "xxxxxxxxxxxxxx",
        "verifiedNumber": "220002",
        "regCountry": "CN",
        "regAddress": "nanjing",
        "changeType": -1,
        "xaccountType": "xxxxxxxxxxxxxxxxx",
        "enterprisePerson": {
            "legelName": "xxxxxxxxxxxxxxxxx",
            "legelIdNumber": "xxxxxxxxxxxxxxx",
            "certifierRole": "legalPerson"}
    }
    '''
    This API can be used to submit an enterprise real-name authentication application.
    This API can be invoked only by the partner account AK/SK or token.
    '''
    ff = conn.bssintl.enterprise_realname_auth(userDomainId, **data)
    print(ff)

    data = {"customerId": "xxxxxxxxxxxxxxxxxxxxxxx",
            "identifyType": 1,
            "certificateType": 0,
            "verifiedFileURL": [
                "zhengmian.jpg",
                "fanmian.jpg",
                "chizheng2.jpg"
            ],
            "corpName": "xxxxxxxxxxxxxxxxxxxxxx",
            "verifiedNumber": "220002",
            "regCountry": "CN",
            "regAddress": "nanjing",
            "changeType": '1',
            "xaccountType": "xxxxxxxxxxxxxxxxx",
            "enterprisePerson": {
                "legelName": "xxxxxxxxxxxxxxxx",
                "legelIdNumber": "xxxxxxxxxxxxxxxxxxxxxx",
                "certifierRole": "legalPerson"
            }}
    '''
    This API can be used to submit a real-name authentication change application.
    This API can be invoked only by the partner account AK/SK or token.
    '''
    ff = conn.bssintl.change_enterprise_realname_auth(userDomainId, **data)
    print(ff)


    data = {
        "customerId": "06184258078025be0f84c0031df9e360"
    }
    '''
    If the response to a real-name authentication application or real-name authentication change application indicates that manual review is required,
    this API can be used to query the review result.
    This API can be invoked only by the partner account AK/SK or token.
    '''
    ff = conn.bssintl.query_realname_auth(userDomainId, **data)
    print(ff)
