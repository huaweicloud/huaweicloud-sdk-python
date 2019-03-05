# Copyright 2018 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack import proxy2
from openstack.vpc.v1 import bandwidth as _bandwidth
from openstack.vpc.v1 import public_ip as _public_ip


class Proxy(proxy2.BaseProxy):

    def update_public_ip(self, public_ip, **attrs):
        """Update the elastic ip

        :param public_ip: The value can be the ID of a elastic ip or a
            :class:`~openstack.vpc.v1.public_ip.PublicIP`
            instance.
        :param dict attrs: The attributes to update on the ip represented
            by ``public_ip``. Available attributes include:

            * ``port_id``: The id of the port the public ip binds to.
            * ``ip_version``: The ip address version. The available values
                includes: 4, 6.

            These two attributes could not be update at the same time.

        :returns: The updated elastic ip
        :rtype: :class:`~openstack.vpc.v1.public_ip.PublicIP`
        """
        res = self._get_resource(_public_ip.PublicIP, public_ip)
        if ('ip_version' not in attrs) and ('port_id' not in attrs):
            attrs['port_id'] = None
        return self._update(_public_ip.PublicIP, res.id, **attrs)

    def bandwidths(self, **query):
        """Return a generator of bandwidths

        :param kwargs query: Optional query parameters to be sent to limit
            the resources being returned. Available parameters include:

            * ``limit``: The number of records returned on each page.
            * ``marker``: The resource ID of pagination query.

        :returns: A generator of bandwidth objects
        :rtype: :class:`~openstack.vpc.v1.bandwidth.Bandwidth`
        """
        return self._list(_bandwidth.Bandwidth, paginated=False, **query)

    def get_bandwidth(self, bandwidth):
        """Get a single bandwidth

        :param bandwidth: The value can be the ID of a bandwidth or a
            :class:`~openstack.vpc.v1.bandwidth.Bandwidth` instance.

        :returns: One :class:`~openstack.vpc.v1.bandwidth.Bandwidth`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
            when no resource can be found.
        """
        return self._get(_bandwidth.Bandwidth, bandwidth)
