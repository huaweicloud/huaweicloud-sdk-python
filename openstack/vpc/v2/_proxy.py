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
from openstack.vpc.v2 import bandwidth as _bandwidth
from openstack.vpc.v2 import eip as _eip
from openstack.vpc.v2 import sharebandwidth as _sharebandwidth


class Proxy(proxy2.BaseProxy):
    def create_publicip_ext(self, **attrs):
        """Create a new eip from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.vpc.v2.eip.EIP`,
                           comprised of the properties on the EIP class.

        :returns: The results of eip creation
        :rtype: :class:`~openstack.vpc.v2.eip.EIP`
        """
        return self._create(_eip.EIP, **attrs)

    def update_bandwidth_ext(self, bandwidth_id, **attrs):
        """Create a new bandwidth from attributes

        :param string bandwidth_id: id of bandwidth
        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.vpc.v2.bandwidth.Bandwidths`,
                           comprised of the properties on the Bandwidths class.

        :returns: The results of bandwidth creation
        :rtype: :class:`~openstack.vpc.v2.bandwidth.Bandwidths`
        """
        return self._create(_bandwidth.Bandwidths, bandwidth_id=bandwidth_id, **attrs)

    def create_sharebandwidth(self, **data):
        """Create a share bandwidth.

        :param data: The attributes to create a share bandwidth.
        :return: :class:`~openstack.vpc.v2.sharebandwidth.ShareBandwidth`
        """
        return self._create(_sharebandwidth.ShareBandwidth, **data)

    def delete_sharebandwidth(self, bandwidth_id):
        """Delete a share bandwidth.

        :param bandwidth_id: Id of share bandwidth.
        :return: None
        """
        return self._delete(_sharebandwidth.ShareBandwidth, bandwidth_id)

    def create_batch_sharebandwidth(self, **data):
        """Create share bandwidth in batches.

        :param data: The attributes to create share bandwidth in batches.
        :return: :class:`~openstack.vpc.v2.sharebandwidth.BatchShareBandwidth`
        """
        return self._create(_sharebandwidth.BatchShareBandwidth, **data)

    def insert_ip_to_bandwidth(self, bandwidth_id, **data):
        """Shared bandwidth is inserted into the elastic public IP address.

        :param bandwidth_id: Id of a bandwidth.
        :param data: The attributes to insert ip to bandwidth.
        :return: :class:`~openstack.vpc.v2.sharebandwidth.InsertIpToBandwidth`
        """
        return self._create(_sharebandwidth.InsertIpToBandwidth, bandwidth_id=bandwidth_id, **data)

    def remove_ip_from_bandwidth(self, bandwidth_id, **data):
        """Shared bandwidth removal elastic public IP.

        :param bandwidth_id: Id of a bandwidth.
        :param data: The attributes to remove ip from bandwidth.
        :return: None.
        """
        return self._create(_sharebandwidth.RemoveIpFromBandwidth, bandwidth_id=bandwidth_id, **data)
