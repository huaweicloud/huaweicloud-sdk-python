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


def images(_conn):
    query = {
        "status": "queued",
    }
    ims = _conn.image.images(**query)
    for im in ims:
        print(im)


def get_image(_conn):
    print(_conn.image.get_image('fd7c74ac-d32d-4267-896c-2e66a3ad61d5'))


def update_image(_conn):
    data = {
        "op": "replace",
        "path": "/name",
        "value": "image-test-update",
    }
    print(_conn.image.update_image('642f4242-37ef-4f78-b338-eaeec6811374', **data))


def upload_image(_conn):
    image_file = open('C:/Users/zWX547856/Desktop/test_upload_image.img', 'rb')
    data = {
        "name": "image-test-upload",
        "disk_format": "qcow2",
        "container_format": "bare",
        "min_disk": 40,
        "data": image_file.read()
    }
    print(_conn.image.upload_image(**data))


def delete_image(_conn):
    print(_conn.image.delete_image('4b2e277d-83c4-4152-89a7-08e8ca0cf194'))


if __name__ == '__main__':
    # images(conn)
    # get_image(conn)
    # update_image(conn)
    # upload_image(conn)
    # delete_image(conn)
    pass
