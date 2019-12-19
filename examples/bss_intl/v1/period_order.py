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
        "orderId": "CS1909211253I0LZZ",
        "payAccountType": 2,
        "bpId": "198bd648de5b4437aa569061c6ba0fc4",
        "couponIds": [
            "CP190921034223R7H1"
        ]
    }
    '''
    A customer can invoke this API to pay yearly-monthly product orders in the pending payment status.
    This API can be invoked using the customer token only.    
    '''
    ff = conn.bssintl.pay_period_order(userDomainId, **data)
    print(ff)

    data = {
        "order_id": "CS1909211347TNTZY",
        "unsub_type": 3,
        "unsubscribe_reason_type": 2,
        "unsubscribe_reason": "reason"
    }
    '''
    A customer can invoke this API to unsubscribe from early-monthly product orders in the subscribed, changing, or failed to be provisioned status.
    This API can be invoked using the customer token only.
    '''
    ff = conn.bssintl.unsubscribe_period_order(userDomainId, **data)
    print(ff)

    '''
    A customer can invoke this API to cancel orders in the pending payment status.
    This API can be invoked using the customer token only.
    '''
    ff = conn.bssintl.cancel_order(userDomainId, orderId="CS1910091053TNVOZ", action_id="cancel")
    print(ff)

    data = {
        "order_id": "CS1906131030ERCSE",
        "offset": 1,
        "limit": 10
    }
    '''
    A customer can invoke this API to cancel orders in the pending payment status.
    This API can be invoked using the customer token only.
    '''
    ff = conn.bssintl.query_order_detail(userDomainId, **data)
    print(ff)

    data = {
        "page_size": "1",
        "page_index": "10"
    }
    '''
    After a customer purchases yearly/monthly resources, it can query the orders in different statuses,
     such as in the pending approval, processing, canceled, completed, and pending payment statuses.
    This API can be invoked using the customer AK/SK or token.
    '''
    ff = conn.bssintl.query_order_list(userDomainId, **data)
    print(ff)

    '''
     A customer can query the resources and original orders of the unsubscription amount for an unsubscription order or degrade order.
     This API can be invoked using the AK/SK or token of the partner or the token of the partner's customer.
    '''
    ff = conn.bssintl.query_refund_order_amount(domain_id=userDomainId, order_id='CS1911122241QKILM')
    print(ff)

    ''' 
    A customer can query resource details and provisioning status of an order on the partner sales platform.
    This API can be invoked using the customer token only.
    '''
    ff = conn.bssintl.query_resource_status_by_orderId(userDomainId, order_id="CS1909211350H67DB")
    print(ff)
