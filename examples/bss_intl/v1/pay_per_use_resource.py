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
        "customerId": "3d2c6b3ab1fd4e26846b0f2c46e67bda",
        "regionCode": "cn-north-1",
        "cloudServiceTypeCode": "hws.service.type.ebs",
        "resourceTypeCode": "hws.resource.type.volume",
        "resourceIds": ["71e3eeb5-4b77-44ae-9c42-119ee7976cf7", "39d90d01-4774-4af6-8136-83ba5732bccf"],
        "startTimeBegin": "2019-06-01T11:00:00Z",
        "startTimeEnd": "2019-06-30T11:00:00Z"
    }
    '''
    A customer can query its pay-per-use resources on the partner sales platform.
    The on-demand resource data has a latency, and the latency for each cloud service data varies.
     The data obtained using this API is for reference only.
    This API can be invoked using the partner AK/SK or token only.    
    '''
    ff = conn.bssintl.query_customer_resource(userDomainId, **data)
    print(ff)
