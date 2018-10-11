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
