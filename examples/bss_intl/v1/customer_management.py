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
        "searchType": "email",
        "searchKey": "huawei@huawei.com"
    }
    '''
    This API is used to check whether the account name, and mobile number or email address entered by the customer can be used for registration.
    This API can be invoked only by the partner AK/SK or token.
    '''
    ff = conn.bssintl.check_customer_register_info(userDomainId, **data)
    print(ff)

    data = {
        "xAccountId": "xxxxxxxxxxx",
        "xAccountType": "xxxxxxxxxxxxxxx",
        "domainName": "xxxxxxxxx",
        "password": "xxxxxxxxxxx",
        "domainArea":"HK"
    }
    '''
    This API is used to create a HUAWEI CLOUD account for a customer when the customer creates an account on your sales platform,
     and bind the customer account on the partner sales platform to the HUAWEI CLOUD account.
     In addition, the HUAWEI CLOUD account is bound to the partner account.
    This API can be invoked only by the partner AK/SK or token.
    '''
    ff = conn.bssintl.create_customer(userDomainId, **data)
    print(ff)

    data = {
        "cooperationTimeStart": "2019-05-01T00:01:00Z",
        "cooperationTimeEnd": "2019-12-01T00:01:00Z"
    }
    '''
    This API is used to query your customers.
    This API can be invoked only by the partner account AK/SK or token.
    '''
    ff = conn.bssintl.query_customer_list(userDomainId, **data)
    print(ff)

    data = {
        "customerIds": [
            "06fa387d9c0026640f05c00f73289540"
        ],
        "reason": "Arrears"
    }
    '''
     A partner can freeze an account of a customer associated with the partner by reseller model.
    This API can be invoked only by the partner account AK/SK or token.
    '''
    ff = conn.bssintl.freeze_customer(userDomainId, **data)
    print(ff)

    data = {
        "customerIds": [
            "06fa387d9c0026640f05c00f73289540"
        ],
        "reason": "The customer has topped up its account."
    }
    '''
    A partner can unfreeze an account of a customer associated with the partner by reseller model.
    This API can be invoked only by the partner account AK/SK or token.
    '''
    ff = conn.bssintl.unfreeze_customer(userDomainId, **data)
    print(ff)

