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
        "resource_ids": "53fe84f787754f309de56559ec03068b"
    }
    '''
    A customer can query one or all yearly/monthly resources on the customer platform.
    This API can be invoked only by the customer AK/SK or token.    
    '''
    ff = conn.bssintl.query_customer_period_resources_list(userDomainId, **data)
    print(ff)

    data = {
        "resource_ids": ["111338ec-8d86-48e5-ba3e-e437b18146bb"],
        "period_type": 2,
        "period_num": 1,
        "expire_mode": 0,
        "isAutoPay": 0
    }
    '''
    When subscription to yearly/monthly resources of a customer is about to expire, the customer can renew the subscription to the resources.
    This API can be invoked using the customer token only.
    '''
    ff = conn.bssintl.renew_subscription_by_resourceId(userDomainId, **data)
    print(ff)

    data = {
        "resourceIds": ["111338ec-8d86-48e5-ba3e-e437b18146bb"],
        "unSubType": 1,
        "unsubscribeReasonType": 5,
        "unsubscribeReason": "delete"
    }
    '''
    If a customer has subscribed to a yearly/monthly resource, the customer can use this API to unsubscribe from the resource, including the renewed part and currently used part.
     The customer cannot use the resources after unsubscription.
    This API can be invoked using the customer token only.    
    '''
    ff = conn.bssintl.unsubscribe_by_resourceId(userDomainId, **data)
    print(ff)

    '''
    A customer can use this API to enable automatic subscription renewal for its long-term yearly/monthly resources to prevent the resources from being deleted when they are expired.
    This API can be invoked using the customer token only.    
    '''
    ff = conn.bssintl.enable_auto_renew(userDomainId, resource_id="3e88931a-ddfe-4364-8604-84cd0882ad47", action_id="autorenew")
    print(ff)


    '''
    A customer can disable automatic subscription renewal when needed. After disabling this function, the customer needs to manually renew the subscription to the resources before they expire.
    This API can be invoked using the customer token only.    
    '''
    ff = conn.bssintl.disable_auto_renew(userDomainId, resource_id="3e88931a-ddfe-4364-8604-84cd0882ad47", action_id="autorenew")
    print(ff)

