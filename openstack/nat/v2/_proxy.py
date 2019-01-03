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
from openstack.nat.v2 import nat_gateway
from openstack.nat.v2 import dnat_rule
from openstack.nat.v2 import snat_rule


class Proxy(proxy2.BaseProxy):
    def create_nat_gateway(self, **attr):
        """Create a new natgateway from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.nat.v2.natgateway.NatGateway`,
            comprised of the properties on the NatGateway class.

        :returns: The results of NatGateway creation
        :rtype: :class:`~openstack.nat.v2.natgateway.NatGateway`
        """
        return self._create(nat_gateway.NatGateway, **attr)

    def delete_nat_gateway(self, natgateway, ignore_missing=True):
        """Delete a natgateway

        :param natgateway: The value can be either the ID of a natgateway
                    or a :class:`~openstack.nat.v2.natgateway.NatGateway`
                    instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the floating ip does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent ip.

        :returns: ``None``
                """
        return self._delete(nat_gateway.NatGateway, natgateway,ignore_missing=ignore_missing)

    def get_nat_gateway(self, natgateway):
        """Get a single natgateway

        :param natgateway: The value can be the ID of a natgateway or a
                      :class:`~openstack.nat.v2.natgateway.NatGateway`
                      instance.

        :returns: One :class:`~openstack.nat.v2.natgateway.NatGateway`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(nat_gateway.NatGateway, natgateway)

    def nat_gateways(self, **attr):
        """List nat gateways.

        :param kwargs: Query conditions.

        :returns: A generator of nat gateways instances.
        """
        return self._list(nat_gateway.NatGateway, **attr)

    def update_nat_gateway(self, nat_gateway_id, **attr):
        """Update a nat gateways.

        :param nat_gateway_id: nat gateway id.
        :param kwargs: Used to update the nat gateway.

        :returns: :class:`~openstack.nat.v2.nat_gateway.NatGateway`
        """
        return self._update(nat_gateway.NatGateway, nat_gateway_id, **attr)


    def create_dnat_rule(self,**attr):
        """Create a new dnat rule from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.nat.v2.dnat_rule.DnatRule`,
            comprised of the properties on the DnatRule class.

        :returns: The results of DnatRule creation
        :rtype: :class:`~openstack.nat.v2.dnat_rule.DnatRule`
        """
        return self._create(dnat_rule.DnatRule, **attr)

    def dnat_rules(self, **query):
        """List  DnatRule.

        :param kwargs: Query conditions.

        :returns: A generator of DnatRule instances.
        """
        return self._list(dnat_rule.DnatRule, **query)

    def get_dnat_rule(self, dnat):
        """Get a DnatRule

        :param dnat: The value can be the ID of a DnatRule or a
                      :class:`~openstack.nat.v2.dnat_rule.DnatRule`
                      instance.

        :returns: One :class:`~openstack.nat.v2.dnat_rule.DnatRule`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(dnat_rule.DnatRule, dnat)

    def delete_dnat_rule(self, dnat, ignore_missing=True):
        """Delete a DnatRule

        :param dnat: The value can be the ID of a DnatRule or a
                      :class:`~openstack.nat.v2.dnat_rule.DnatRule`
                      instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the floating ip does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent ip.

        :returns: ``None``
                """
        return self._delete(dnat_rule.DnatRule, dnat, ignore_missing=ignore_missing)

    def snat_rules(self, **attr):
        """List snat rule.

        :param attr: Query conditions.
        :return: A generator of nat gateways instances.
        """
        return self._list(snat_rule.SnatRule, **attr)

    def get_snat_rule(self, snat_rule_id):
        """Get a snat rule.

        :param snat_rule_id: id of snat rule.
        :return: :class:`~openstack.nat.v2.snat_rule.SnatRule`
        """
        return self._get(snat_rule.SnatRule, snat_rule_id)

    def create_snat_rule(self, **attr):
        """Create a snat rule.

        :param attr: Used to create the snat rule.
        :return: :class:`~openstack.nat.v2.snat_rule.SnatRule`
        """
        return self._create(snat_rule.SnatRule, **attr)

    def delete_snat_rule(self, snat_rule_id):
        """Delete a snat rule.

        :param snat_rule_id: id of snat rule.
        :return: None
        """
        return self._delete(snat_rule.SnatRule, snat_rule_id)
