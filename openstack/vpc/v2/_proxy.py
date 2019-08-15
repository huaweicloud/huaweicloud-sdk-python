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
from openstack.vpc.v2 import bandwidth as _bandwidth
from openstack.vpc.v2 import eip as _eip
from openstack.vpc.v2 import sharebandwidth as _sharebandwidth
from openstack.vpc.v2 import peering as _peering
from openstack.vpc.v2 import route as _route
from openstack.vpc.v2 import network_ip_availability as _network_ip_availability


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

    def delete_sharebandwidth(self, bandwidth_id, ignore_missing=True):
        """Delete a share bandwidth.

        :param bandwidth_id: Id of share bandwidth.
        :param ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent resource.
        :return: None
        """
        self._delete(_sharebandwidth.ShareBandwidth, bandwidth_id, ignore_missing=ignore_missing)

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

    def create_peering(self, **data):
        """Create a peering connection.

        :param data: The attributes to create a peering connection.
        :return: :class:`~openstack.vpc.v2.peering.Peering`
        """
        return self._create(_peering.Peering, **data)

    def delete_peering(self, peering_id, ignore_missing=True):
        """Delete a peering connection.

        :param peering_id: The id of peering connection.
        :param ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent resource.
        :return: None
        """
        self._delete(_peering.Peering, peering_id, ignore_missing=ignore_missing)

    def update_peering(self, peering_id, **data):
        """Update a peering connection.

        :param peering_id: The id of peering connection.
        :param data: The attributes to update a peering connection.
        :return: :class:`~openstack.vpc.v2.peering.Peering`
        """
        return self._update(_peering.Peering, peering_id, **data)

    def get_peering(self, peering_id):
        """Get a peering connection.

        :param peering_id: The id of peering connection.
        :return: :class:`~openstack.vpc.v2.peering.Peering`
        """
        return self._get(_peering.Peering, peering_id)

    def peerings(self, **query):
        """Retrieve a generator of peering connection.

        :param query: The attributes to query peering connection.
        :return: A generator of peering connection.
        """
        return self._list(_peering.Peering, paginated=True, **query)

    def accept_peering(self, peering_id):
        """Accept a peering connection.

        :param peering_id: The id of peering connection.
        :return: :class:`~openstack.vpc.v2.peering.PeeringAccept`
        """
        return self._update(_peering.PeeringAccept, None, peering_id=peering_id)

    def reject_peering(self, peering_id):
        """Reject a peering connection.

        :param peering_id: The id of peering connection.
        :return: :class:`~openstack.vpc.v2.peering.PeeringReject`
        """
        return self._update(_peering.PeeringReject, None, peering_id=peering_id)

    def create_route(self, **data):
        """Create a route.

        :param data: The attributes to create a route.
        :return: :class:`~openstack.vpc.v2.route.Route`
        """
        return self._create(_route.Route, **data)

    def delete_route(self, route_id, ignore_missing=True):
        """Delete a route.

        :param route_id: The id of route.
        :param ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent resource.
        :return: None
        """
        self._delete(_route.Route, route_id, ignore_missing=ignore_missing)

    def get_route(self, route_id):
        """Get a route.

        :param route_id: The id of route.
        :return: :class:`~openstack.vpc.v2.route.Route`
        """
        return self._get(_route.Route, route_id)

    def routes(self, **query):
        """Retrieve a generator of route.

        :param query: The attributes to query route.
        :return: A generator of route.
        """
        return self._list(_route.Route, paginated=True, **query)

    def get_network_ip_availability(self, network_id):
        """Get IP availability of a network.

        :param network_id: The id of a network.
        :return: One :class:`~openstack.vpc.v2.network_ip_availability.
                NetworkIPAvailability`
        """
        return self._get(_network_ip_availability.NetworkIPAvailability, network_id)
