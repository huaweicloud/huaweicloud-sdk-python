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

from openstack import proxy2
from openstack.ims.v2 import cloudimage as _cloudimage


class Proxy(proxy2.BaseProxy):

    def cloudimages(self, **query):
        """List cloud images.

        :param query: Query conditions.
        :return: A generator of cloud image instances.
        """
        return self._list(_cloudimage.CloudImage, **query)

    def update_cloudimage(self, cloudimage_id, **data):
        """Update a cloud image.

        :param cloudimage_id: Id of cloud image.
        :param data: Update a cloud image from attributes.
        :return: :class:`~openstack.ims.v2.cloudimage.CloudImage`
        """
        res = self._get_resource(_cloudimage.CloudImage, cloudimage_id)
        return res.update(self._session, **data)

    def create_cloudimage(self, **data):
        """Create a cloud image: Make a private image using
                    a cloud server or an external image file
                    uploaded to the OBS bucket.

        :param data: Create a cloud image from attributes.
        :return: :class:`~openstack.ims.v2.cloudimage.CloudImageAction`
        """
        return self._create(_cloudimage.CloudImageAction, **data)
