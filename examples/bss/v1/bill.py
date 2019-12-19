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
        "cycle": "2019-09",
        "cloud_service_type_code": "hws.service.type.ebs",
        "type": "1",
    }
    '''
    This API can be used to query the expenditure summary bills of a customer on the customer platform. The bills summarize the summary data by month. The data of the previous day is updated once a day.
    This API can be invoked using the customer AK/SK or token only.
    '''
    ff = conn.bss.query_monthly_expenditure_summary(userDomainId, **data)
    print(ff)

    data = {
        'cycle': "2019-09",
        'cloudServiceTypeCode': 'hws.service.type.ec2',
        'resourceTypeCode': 'hws.resource.type.vm',
        'regionCode': 'cn-north-1',
        'resInstanceId': "xxxxxxxxxxxxxxx",
        'payMethod': '0',
        'offset': '1',
        'limit': '10'
    }
    '''
    This API can be used to query usage details of each resource for a customer on the customer platform. The resource details have a latency (a maximum of 24 hours).
    This API can be invoked using the customer AK/SK or token only.
    '''
    ff = conn.bss.query_resource_usage_details(userDomainId, **data)
    print(ff)

    data = {
        'startTime': '2019-09-01',
        'endTime': '2019-09-30',
        'payMethod': '1'
    }
    '''
    This API can be used to query the usage details of each resource for a customer on the customer platform.
    This API can be invoked using the customer AK/SK or token only.
    '''
    ff = conn.bss.query_resource_usage_record(userDomainId, **data)
    print(ff)
