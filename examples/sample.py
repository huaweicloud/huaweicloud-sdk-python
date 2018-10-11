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

import datetime
import os
import time

from openstack import connection

# those services's endpoint will be auto detected from V3 auth token
#
#       Nova         ->   ECS
#       Cinder       ->   EVS
#       Neutron      ->   VPC
#       Keystone     ->   IAM
#       Glance       ->   IMS
#       Heat         ->   RTS
#
# so, we do not need to setup the endpoint override for them.


# setup endpoint override for cloud services
# "example" in the endpoint stands for "Region.Cloud"
os.environ.setdefault(
    'OS_CLOUD_EYE_ENDPOINT_OVERRIDE',
    'https://ces.example.com/V1.0/%(project_id)s'
)


# endpoint override for the other service
# "example" in the endpoint stands for "Region.Cloud"
"""
os.environ.setdefault(
    'OS_AUTO_SCALING_ENDPOINT_OVERRIDE',
    ('https://as.example.com'
     '/autoscaling-api/v1/%(project_id)s')
)
os.environ.setdefault(
    'OS_DNS_ENDPOINT_OVERRIDE',
    'https://dns.example.com/v2'
)
os.environ.setdefault(
    'OS_VOLUME_BACKUP_ENDPOINT_OVERRIDE',
    'https://vbs.example.com/v2/%(project_id)s'
)
os.environ.setdefault(
    'OS_LOAD_BALANCER_ENDPOINT_OVERRIDE',
    'https://elb.example.com/v1.0/%(project_id)s'
)
os.environ.setdefault(
    'OS_MAP_REDUCE_ENDPOINT_OVERRIDE',
    'https://mrs.example.com/v1.1/%(project_id)s'
)
os.environ.setdefault(
    'OS_CTS_ENDPOINT_OVERRIDE',
    'https://cts.example.com/v1.0/%(project_id)s')
os.environ.setdefault(
    'OS_SMN_ENDPOINT_OVERRIDE',
    'https://smn.example.com/v2/%(project_id)s')
os.environ.setdefault(
    'OS_MAAS_ENDPOINT_OVERRIDE',
    'https://maas.example.com/v1/%(project_id)s')
os.environ.setdefault(
    'OS_KMS_ENDPOINT_OVERRIDE',
    'https://kms.example.com/v1.0/%(project_id)s')
os.environ.setdefault(
    'OS_ANTI_DDOS_ENDPOINT_OVERRIDE',
    'https://antiddos.example.com/v1/%(project_id)s')
os.environ.setdefault(
    'OS_DMS_ENDPOINT_OVERRIDE',
    'https://dms.example.com/v1.0/%(project_id)s')
"""


# create connection
username = "replace-with-your-username"
password = "replace-with-your-password"
projectId = "replace-with-your-project-id"
userDomainId = "replace-with-your-user-domain-id"
auth_url = "https://iam.example.com/v3"
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)

# some common constant required by tutorial
now = datetime.datetime.now()
dimensions = [{
    "name": "instance_id",
    "value": "33328f02-3814-422e-b688-bfdba93d4050"
}]


def get_epoch_time(datetime_):
    if datetime_:
        seconds = time.mktime(datetime_.timetuple())
        return int(seconds) * 1000
    else:
        return None


def list_metrics():
    query = {
        "namespace": "SYS.ECS",
        "metric_name": "cpu_util",
        "limit": 1
    }
    metrics = conn.cloud_eye.metrics(**query)
    for metric in metrics:
        print(metric)


def add_metric_data():
    # prepare metric data list
    data = [
        {
            "metric": {
                "namespace": "SDK.unittests",
                "dimensions": dimensions,
                "metric_name": "cpu_util"
            },
            "ttl": 604800,
            "collect_time": get_epoch_time(now
                                           - datetime.timedelta(minutes=5)),
            "value": 60,
            "unit": "%"
        },
        {
            "metric": {
                "namespace": "SDK.unittests",
                "dimensions": dimensions,
                "metric_name": "cpu_util"
            },
            "ttl": 604800,
            "collect_time": get_epoch_time(now),
            "value": 60,
            "unit": "%"
        }
    ]
    conn.cloud_eye.add_metric_data(data)


def list_metric_aggr_data():
    query = {
        "namespace": "SDK.unittests",
        "metric_name": "cpu_util",
        "from": get_epoch_time(now - datetime.timedelta(minutes=5)),
        "to": get_epoch_time(now),
        "period": 300,
        "filter": "average",
        "dimensions": dimensions
    }
    # we query for the data add by add_metric_data()
    aggregations = list(conn.cloud_eye.metric_aggregations(**query))
    for aggr in aggregations:
        print(aggr)

# visit API
list_metrics()
add_metric_data()
list_metric_aggr_data()
