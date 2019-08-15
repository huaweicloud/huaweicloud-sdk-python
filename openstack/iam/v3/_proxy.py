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

from openstack import proxy2
from openstack.iam.v3 import securitytoken as _securitytoken


class Proxy(proxy2.BaseProxy):

    # def create_securitytoken(self, **attrs):
    #     """Create a new securitytoken
    #
    #     :param dict attrs: Keyword arguments which will be used to create
    #                        a :class:`~openstack.iam.v3.securitytoken.Securitytoken`.
    #                        Please follow the API reference to get the request body.
    #
    #     :returns: The results of securitytoken creation
    #     :rtype: :class:`~openstack.iam.v3.iam.Securitytoken`
    #     """
    #     return self._create(_securitytoken.Securitytoken, **attrs)

    def create_securitytoken(self, **attrs):
        """
        Retrieve a generator of servers.
        :param attrs: An Auth entity
        :return: A generator of server instances.
        """
        res = self._get_resource(_securitytoken.Securitytoken, None)
        return res.create(self._session, **attrs)