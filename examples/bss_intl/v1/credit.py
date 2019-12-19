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
        "customer_id": "0500e3466180d5b20fc3c0082dcf3e00"
    }
    '''
    This API can be used to query the budget of a customer for the partner to determine whether to adjust the budget.
    This API can be invoked only by the partner account AK/SK or token.
    '''
    ff = conn.bssintl.query_credit(userDomainId, **data)
    print(ff)

    data = {
        "customerId": "053ebf909680d53b0f7dc00693bdf3a0",
        "adjustmentAmount": 2019.19,
        "measureId": 1
    }
    '''
    This API is used to set or adjust a customer's budget.
    The api is only allowed to be called with the partner's AK/SK or Token.
    '''
    ff = conn.bssintl.set_credit(userDomainId, **data)
    print(ff)
