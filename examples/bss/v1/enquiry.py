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
        "tenantId": "96e3db86e207438fbd351b91ba35da59",
        "regionId": "4135",
        "chargingMode": "0",
        "periodType": "0",
        "periodNum": "1",
        "subscriptionNum": 1,
        "productInfos": [{
            "id": "1546",
            "cloudServiceType": "4651446",
            "resourceType": "15613210",
            "resourceSpecCode": "15641621"
        }]
    }
    '''
    The partner sales platform obtains the product prices on the HUAWEI CLOUD official website based on the product catalog.
    This API can be invoked using the customer token, or the partner's AK/SK or token.    
    '''
    ff = conn.bss.query_rating(userDomainId, **data)
    print(ff)
