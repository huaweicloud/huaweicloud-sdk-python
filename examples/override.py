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
    'https://as.example.com/v1/%(project_id)s')
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
    'OS_ELBV1_ENDPOINT_OVERRIDE',
    'https://elb.example.com/v1.0/%(project_id)s'
)
os.environ.setdefault(
    'OS_MAP_REDUCE_ENDPOINT_OVERRIDE',
    'https://mrs.example.com/v1.1/%(project_id)s'
)
os.environ.setdefault(
    'OS_CTS_ENDPOINT_OVERRIDE',
    'https://cts.example.com/v1.0/%(project_id)s'
)
os.environ.setdefault(
    'OS_SMN_ENDPOINT_OVERRIDE',
    'https://smn.example.com/v2/%(project_id)s'
)
os.environ.setdefault(
    'OS_MAAS_ENDPOINT_OVERRIDE',
    'https://maas.example.com/v1/%(project_id)s'
)
os.environ.setdefault(
    'OS_KMS_ENDPOINT_OVERRIDE',
    'https://kms.example.com/v1.0/%(project_id)s'
)
os.environ.setdefault(
    'OS_ANTI_DDOS_ENDPOINT_OVERRIDE',
    'https://antiddos.example.com/v1/%(project_id)s'
)
os.environ.setdefault(
    'OS_DMS_ENDPOINT_OVERRIDE',
    'https://dms.example.com/v1.0/%(project_id)s'
)
"""

# create connection
username = "replace-with-your-username"
password = os.getenv("secret","")
projectId = "replace-with-your-project-id"
userDomainId = "replace-with-your-user-domain-id"
auth_url = "https://iam.example.com/v3"
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


def list_metrics():
    query = {
        "namespace": "SYS.ECS",
        "metric_name": "cpu_util",
        "limit": 1
    }
    metrics = conn.cloud_eye.metrics(**query)
    for metric in metrics:
        print(metric)


# visit API
list_metrics()
