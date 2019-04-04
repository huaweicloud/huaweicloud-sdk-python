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


# Create image by instance.
def create_cloudimage_by_instance(_conn):
    cloudimage = conn.ims.create_cloudimage(
        instance_id='9862d90e-42cc-4419-ad1e-be1b0e64f923',
        name='sdk_test_image',
        description='test'
    )
    print(cloudimage)


# Create image by file which in obs.
# Image_url format: bucketName:objectFileName.
def create_cloudimage_by_file(_conn):
    cloudimage = conn.ims.create_cloudimage(
        image_url='ims-huanan-image:Fedora.zvhd',
        name='sdk_test_image_2',
        min_disk=40,
        os_version='CentOS 7.2 64bit',
        description='test'
    )
    print(cloudimage)


# Update image.
def update_cloudimage(_conn):
    image_id = '******'
    image = conn.ims.update_cloudimage(
        image_id,
        op="add",
        path="/name",
        value="sdr_plugin_test"
    )
    print(image)


if __name__ == '__main__':
    # create_cloudimage_by_instance(conn)
    # create_cloudimage_by_file(conn)
    # update_cloudimage(conn)
    pass
