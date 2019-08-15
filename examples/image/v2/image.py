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
import os

from openstack import connection
from openstack import utils

# Set debug info.
utils.enable_logging(debug=False, stream=sys.stdout)

# Create connection.
auth_url = "https://iam.example.com/v3"
projectId = "replace-with-your-projectId"
userDomainId = "replace-with-your-domainId"
username = "replace-with-your-username"
password = os.getenv('get_secret_code')

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


# Create image metadata and upload file.
def upload_image(_conn):
    image = conn.image.upload_image(
        name='test_image',
        container_format='bare',
        disk_format='raw',
        data=open('/opt/cirros.img', 'rb').read()
    )
    print(image)


# List images.
def list_images(_conn):
    for image in conn.image.images(
        visibility='private',
        __platform='CentOS',
        __imagetype='private',
        name='suse_test_post'
    ):
        print(image)


# Get image.
def show_image(_conn):
    image_id = '******'
    image = conn.image.get_image(image_id)
    print(image)


# Delete image.
def delete_image(_conn):
    image_id = '******'
    conn.image.delete_image(image_id)


if __name__ == '__main__':
    # upload_image(conn)
    # list_images(conn)
    # show_image(conn)
    # delete_image(conn)
    pass
