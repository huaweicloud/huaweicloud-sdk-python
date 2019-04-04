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

import sys
import warnings
import os

from openstack import utils
from openstack import connection

utils.enable_logging(debug=False, stream=sys.stdout)
warnings.filterwarnings('ignore')

auth_url = '******'
userDomainId = '******'
projectId = '******'
username = '******'
password = '******'

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password,
    verify=False
)

os.environ.setdefault(
    'OS_IMS_ENDPOINT_OVERRIDE',
    'https://******/v2'
)
print('endpoint: ' + os.environ.get('OS_IMS_ENDPOINT_OVERRIDE'))


def cloudimages(_conn):
    query = {
        # "status": "active",
        # "limit": 5,
        # "name": "test_image_by_server",
    }
    images = _conn.ims.cloudimages(**query)
    for image in images:
        print(image._CloudImage__os_bit)
        print(image.os_bit)


def update_cloudimage(_conn):
    cloudimage_id = 'ac291469-0af6-49f3-acfc-3f93b0844bfe'
    data = {
        "op": "replace",
        "path": "/name",
        "value": "test_image_by_server"
    }
    up_image = _conn.ims.update_cloudimage(cloudimage_id, **data)
    print(up_image)


def create_cloudimage_by_ecs(_conn):
    data = {
        "name": "ims_by_ecs-zgf-20181010",
        "description": "create_cloudimage_by_ecs",
        "instance_id": "1cdd5621-93b7-4c49-be6a-500229c196f2",
        "tags": [
            "k1.v1",
            "k22.v22",
            "k333.v333"
        ]
    }
    image = _conn.ims.create_cloudimage(**data)
    print(image)


def create_cloudimage_by_data_disk(_conn):
    data = {
        "data_images": [
            {
                "name": "ims_by_data_disk-zgf-20181010",
                "description": "create_cloudimage_by_data_disk",
                "volume_id": "000f0c09-5ae5-4f3f-8ba3-86679719a31a",
                "image_tags": [
                    {
                        "key": "k1-by_new_tag",
                        "value": "v1-by_new_tag"
                    },
                    {
                        "key": "k22-by_new_tag",
                        "value": "v22-by_new_tag"
                    }
                ]
            }
        ]
    }
    image = _conn.ims.create_cloudimage(**data)
    print(image)


def create_cloudimage_by_outer_image_from_obs(_conn):
    data = {
        "name": "ims_by_outer_image_from_obs-zgf-20181010",
        "description": "create_cloudimage_by_outer_image_from_obs",
        "os_version": "Ubuntu 14.04 server 64bit",
        "image_url": "obs-xx2:Ubuntu14.04_Server_64bit_WebService_Picture.qcow2",
        "min_disk": 40,
        "is_config": True,
        "tags": [
            "k1.v1",
            "k22.v22",
            "k333.v333"
        ],
        "type": "ECS"
    }
    image = _conn.ims.create_cloudimage(**data)
    print(image)


if __name__ == '__main__':
    # cloudimages(conn)
    # update_cloudimage(conn)
    # create_cloudimage_by_ecs(conn)
    # create_cloudimage_by_data_disk(conn)
    # create_cloudimage_by_outer_image_from_obs(conn)
    pass
