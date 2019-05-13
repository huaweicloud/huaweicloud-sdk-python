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
from openstack.vpc.v1 import port as _port
from openstack.vpc.v1 import private_ip as _private_ip
from openstack.vpc.v1 import public_ip as _public_ip
from openstack.vpc.v1 import quota as _quota
from openstack.vpc.v1 import security_group as _security_group
from openstack.vpc.v1 import security_group_rule as _security_group_rule
from openstack.vpc.v1 import subnet as _subnet
from openstack.vpc.v1 import vpc as _vpc


class Proxy(proxy2.BaseProxy):

    def vpcs(self, **query):
        """Return a generator of VPCs

        :param kwargs query: Optional query parameters to be sent to limit
            the resources being returned. Available parameters include:

            * ``marker``: The resource ID of pagination query.
            * ``limit``: The number of records returned on each page.
            * ``enterprise_project_id``: The ID of the enterprise project.

        :returns: A generator of network objects
        :rtype: :class:`~openstack.vpc.v1.vpc.VPC`
        """
        return self._list(_vpc.VPC, paginated=True, **query)

    def get_vpc(self, vpc):
        """Get a single VPC

        :param vpc: The value can be the ID of a VPC or a VPC instance.
        :type vpc: :class:`~openstack.vpc.v1.vpc.VPC`

        :returns: The VPC resource.
        :rtype: :class:`~openstack.vpc.v1.vpc.VPC`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_vpc.VPC, vpc)

    def create_vpc(self, **attrs):
        """Create a new VPC from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.vpc.v1.vpc.VPC`,
            comprised of the properties on the VPC class.
            Available attributes include:

            * ``name``: The name of the VPC. The value is a string of
                no more than 64 characters and can contain digits, letters,
                underscores (_), and hyphens (-).
                The name must be unique for a tenant.
            * ``cidr``: The range of available subnets in the VPC.
                The value must be in CIDR format, for example, 192.168.0.0/16.
                The value ranges from 10.0.0.0/8 to 10.255.255.0/24,
                172.16.0.0/12 to 172.31.255.0/24,
                or 192.168.0.0/16 to 192.168.255.0/24.
            * ``enterprise_project_id``: The id of the enterprise project
                for the VPC.
                The value is a string of UUID of ``0``. ``0`` means the default
                enterprise project. Otherwise the value is the id of the
                enterprise project. Max length is 36 bytes.

        :returns: The results of VPC creation
        :rtype: :class:`~openstack.vpc.v1.vpc.VPC`
        """
        return self._create(_vpc.VPC, **attrs)

    def update_vpc(self, vpc, **attrs):
        """Update information about a VPC

        :param vpc: Either the id of a VPC or a VPC instance.
        :type vpc: :class:`~openstack.vpc.v1.vpc.VPC`
        :param dict attrs: The attributes to update on the VPC represented
            by ``vpc``. Available attributes include:

            * ``name``: The name of the VPC. The value is a string of
                no more than 64 characters and can contain digits, letters,
                underscores (_), and hyphens (-).
                If ``name`` is not specified, ``cidr`` must be specified.
            * ``cidr``: The range of available subnets in the VPC.
                The value must be in CIDR format, for example, 192.168.0.0/16.
                The value ranges from 10.0.0.0/8 to 10.255.255.0/24,
                172.16.0.0/12 to 172.31.255.0/24,
                or 192.168.0.0/16 to 192.168.255.0/24.
                If ``cidr`` is not specified, ``name`` must be specified.
            * ``enterprise_project_id``: The id of the enterprise project
                for the VPC.
                The value is a string of UUID of ``0``. ``0`` means the default
                enterprise project. Otherwise the value is the id of the
                enterprise project. Max length is 36 bytes.

        :returns: The updated VPC
        :rtype: :class:`~openstack.vpc.v1.vpc.VPC`
        """
        return self._update(_vpc.VPC, vpc, **attrs)

    def delete_vpc(self, vpc, ignore_missing=True):
        """Delete a VPC

        :param vpc: The value can be either the ID of a VPC or a VPC instance.
        :type vpc: :class:`~openstack.vpc.v1.vpc.VPC`
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the vpc does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent vpc.

        :returns: ``None``
        """
        self._delete(_vpc.VPC, vpc, ignore_missing=ignore_missing)

    def find_vpc(self, name_or_id, ignore_missing=True):
        """Find a single VPC

        :param name_or_id: The name or ID of a VPC.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.vpc.v1.vpc.VPC` or None
        """
        return self._find(_vpc.VPC, name_or_id,
                          ignore_missing=ignore_missing)

    def subnets(self, **query):
        """Return a generator of subnets

        :param dict query: Optional query parameters to be sent to limit
            the resources being returned. Available parameters include:

            * ``limit``: The number of records returned on each page.
            * ``marker``: The resource ID of pagination query.
            * ``vpc_id``: The VPC ID of which the subnets belong to

        :returns: A generator of subnet objects
        :rtype: :class:`~openstack.vpc.v1.subnet.Subnet`
        """
        return self._list(_subnet.Subnet, paginated=True, **query)

    def get_subnet(self, subnet):
        """Query details about a subnet.

        :param subnet: The value can be the ID of a subnet or a
            :class:`~openstack.vpc.v1.subnet.Subnet` instance.

        :returns: One :class:`~openstack.vpc.v1.subnet.Subnet`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_subnet.Subnet, subnet)

    def create_subnet(self, **attrs):
        """Create a new subnet from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.vpc.v1.subnet.Subnet`,
            comprised of the properties on the Subnet class.
            Available attributes include:

            * ``name``: The subnet name. Mandatory.
            * ``cidr``: The network segment on which the subnet resides.
                Mandatory.
            * ``gateway_ip``: The gateway of the subnet. Mandatory.
            * ``dhcp_enable``: Whether the DHCP is enabled for the subnet.
                Optional.
            * ``primary_dns``: The IP address of primary DNS server. Optional.
            * ``secondary_dns``: The IP address of secondary DNS server.
                Optional.
            * ``dnsList``: The DNS server address list of a subnet. Optional.
            * ``availability_zone``: The availability zone (AZ) to which
                the subnet belongs. Optional.
            * ``vpc_id``: The ID of the VPC to which the subnet belongs.
                Mandatory.

        :returns: The results of subnet creation
        :rtype: :class:`~openstack.vpc.v1.subnet.Subnet`
        """
        return self._create(_subnet.Subnet, **attrs)

    def update_subnet(self, subnet, vpc_id, **attrs):
        """Update a subnet

        :param subnet: Either the id of a subnet or a
            :class:`~openstack.vpc.v1.subnet.Subnet` instance.
        :param vpc_id: The id of VPC the subnet belongs to.
        :param dict attrs: The attributes to update on the subnet represented
            by ``subnet``. Available attributes include:

            * ``name``: The subnet name. Mandatory.
            * ``dhcp_enable``: Whether the DHCP is enabled for the subnet.
                Optional.
            * ``primary_dns``: The IP address of primary DNS server. Optional.
            * ``secondary_dns``: The IP address of secondary DNS server.
                Optional.
            * ``dnsList``: The DNS server address list of a subnet. Optional.

        :returns: The updated subnet
        :rtype: :class:`~openstack.vpc.v1.subnet.Subnet`
        """
        res = self._get_resource(_subnet.Subnet, subnet)
        return self._update(_subnet.Subnet, res.id, vpc_id=vpc_id, **attrs)

    def delete_subnet(self, subnet, vpc_id, ignore_missing=True):
        """Delete a subnet

        :param subnet: The value can be either the ID of a subnet or a
            :class:`~openstack.vpc.v1.subnet.Subnet` instance.
        :param vpc_id: The id of VPC the subnet belongs to.
            Mandatory when the subnet is the ID of a subnet.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the subnet does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent subnet.

        :returns: ``None``
        """
        res = self._get_resource(_subnet.Subnet, subnet)
        self._delete(_subnet.Subnet, res.id, vpc_id=vpc_id, ignore_missing=ignore_missing)

    def find_subnet(self, name_or_id, ignore_missing=True):
        """Find a single subnet

        :param name_or_id: The name or ID of a subnet.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.vpc.v1.subnet.Subnet` or None
        """
        return self._find(_subnet.Subnet, name_or_id,
                          ignore_missing=ignore_missing)

    def public_ips(self, **query):
        """Return a generator of elastic ips

        :param dict query: Optional query parameters to be sent to limit
            the resources being returned. Valid parameters are:

            * ``limit``: The number of records returned on each page.
            * ``marker``: The resource ID of pagination query.
            * ``ip_version``: The IP address version. 4: IPv4, 6: IPv6.

        :returns: A generator of elastic IP objects
        :rtype: :class:`~openstack.vpc.v1.public_ip.PublicIP`
        """
        return self._list(_public_ip.PublicIP, paginated=True, **query)

    def get_public_ip(self, public_ip):
        """Get a single elastic ip

        :param public_ip: The value can be the ID of a elastic ip or a
            :class:`~openstack.vpc.v1.public_ip.PublicIP`
            instance.

        :returns: One :class:`~openstack.vpc.v1.public_ip.PublicIP`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_public_ip.PublicIP, public_ip)

    def create_public_ip(self, **attrs):
        """Create a new elastic ip from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.vpc.v1.public_ip.PublicIP`.
        :returns: The results of elastic IP creation
        :rtype: :class:`~openstack.vpc.v1.public_ip.PublicIP`
        """
        return self._create(_public_ip.PublicIP, prepend_key=False, **attrs)

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

    def delete_public_ip(self, public_ip, ignore_missing=True):
        """Delete a elastic ip

        :param public_ip: The value can be either the ID of a elastic ip
            or a :class:`~openstack.vpc.v1.public_ip.PublicIP`
            instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the elastic ip does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent ip.

        :returns: ``None``
        """
        self._delete(_public_ip.PublicIP, public_ip,
                     ignore_missing=ignore_missing)

    def find_public_ip(self, name_or_id, ignore_missing=True):
        """Find a single elastic IP

        :param name_or_id: The name or ID of an IP.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.vpc.v1.public_ip.PublicIP`
            or None
        """
        return self._find(_public_ip.PublicIP, name_or_id,
                          ignore_missing=ignore_missing)

    def private_ips(self, subnet, **query):
        """Return a generator of private ips

        :param subnet: The value can be either the ID of a subnet or a
            :class:`~openstack.vpc.v1.subnet.Subnet` instance.
        :param dict query: Optional query parameters to be sent to limit
            the resources being returned. Valid parameters are:

            * ``limit``: The number of records returned on each page.
            * ``marker``: The resource ID of pagination query.

        :returns: A generator of public IP objects
        :rtype: :class:`~openstack.vpc.v1.private_ip.PrivateIP`
        """
        subnet_id = subnet.id if isinstance(subnet, _subnet.Subnet) else subnet
        query = query or {}
        query.update(subnet_id=subnet_id)
        return self._list(_private_ip.PrivateIP, paginated=True, **query)

    def get_private_ip(self, private_ip):
        """Get a single private ip

        :param private_ip: The value can be the ID of a private ip or a
            :class:`~openstack.vpc.v1.private_ip.PrivateIP`
            instance.

        :returns: One :class:`~openstack.vpc.v1.private_ip.PrivateIP`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_private_ip.PrivateIP, private_ip)

    def create_private_ip(self, **attrs):
        """Create a new private ip from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.vpc.v1.private_ip.PrivateIP`,
            comprised of the properties on the PrivateIP class.
            Available attribute keys are:

            * ``subnet_id``: The ID of the subnet from which the IP address
                is allocated. Mandatory.
            * ``ip_address``: The target IP address. The value can be
                an available IP address in the subnet. If it is not specified,
                the system automatically assigns an IP address.

        :returns: The results of private IP creation
        :rtype: :class:`~openstack.vpc.v1.private_ip.PrivateIP`
        """
        return self._create(_private_ip.PrivateIP, **attrs)

    def create_private_ips(self, *private_ips):
        """Create private ips in batch

        :param \*private_ips: A list of dict defined private ip.
            Available attribute keys are:

            * ``subnet_id``: The ID of the subnet from which the IP address
                is allocated. Mandatory.
            * ``ip_address``: The target IP address. The value can be
                an available IP address in the subnet. If it is not specified,
                the system automatically assigns an IP address.

        :returns: A list of private IPs
        :rtype: `list` of :class:`openstack.vpc.v1.private_ip.PrivateIP`
        """
        return _private_ip.PrivateIP.batch_create(self._session, private_ips)

    def delete_private_ip(self, private_ip, ignore_missing=True):
        """Delete a private ip

        :param private_ip: The value can be either the ID of a private ip
            or a :class:`~openstack.vpc.v1.private_ip.PrivateIP`
            instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the private ip does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent ip.

        :returns: ``None``
        """
        self._delete(_private_ip.PrivateIP, private_ip,
                     ignore_missing=ignore_missing)

    def find_private_ip(self, name_or_id, subnet_id, ignore_missing=True):
        """Find a single private IP

        :param name_or_id: The name or ID of an IP.
        :param subnet_id: The id of the subnet in which to find private ip
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.vpc.v1.private_ip.PrivateIP`
            or None
        """
        return self._find(_private_ip.PrivateIP, name_or_id,
                          ignore_missing=ignore_missing,
                          subnet_id=subnet_id)

    def ports(self, **query):
        """Return a generator of ports

        :param kwargs query: Optional query parameters to be sent to limit
            the resources being returned. Available parameters include:

            * ``id``: The port ID.
            * ``name``: The port name.
            * ``network_id``: ID of network that owns the ports.
            * ``mac_address``: Port MAC address.
            * ``device_id``: Port device ID.
            * ``device_owner``: Port device owner (e.g. ``network:dhcp``).
            * ``status``: The port status. Value is ``ACTIVE``, ``BUILD``
                or ``DOWN``.
            * ``is_admin_state_up``: The administrative state of the port.

        :returns: A generator of port objects
        :rtype: :class:`~openstack.vpc.v1.port.Port`
        """
        return self._list(_port.Port, paginated=True, **query)

    def get_port(self, port):
        """Get a single port

        :param port: The value can be the ID of a port or a
            :class:`~openstack.vpc.v1.port.Port` instance.

        :returns: One :class:`~openstack.vpc.v1.port.Port`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
            when no resource can be found.
        """
        return self._get(_port.Port, port)

    def create_port(self, **attrs):
        """Create a new port from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.vpc.v1.port.Port`,
            comprised of the properties on the Port class.
            Available attributes include:

            * ``network_id``: The ID of the network to which the port belongs.
                Mandatory.
            * ``name``: The port name. Optional.
            * ``admin_state_up``: The administrative state of the port.
                The value can only be true, and the default value is true.
                Optional.
            * ``fixed_ips``: A list of IP addresses for the port. Each element
                is a dict contains ``ip_address`` and ``subnet_id`` keys.
                Optional.
            * ``project_id``: The ID of the project(tenant). Optional.
            * ``security_group_ids``: A list of UUID of the security groups.
                Optional.
            * ``allowed_address_pairs``: A list of address pairs allowed for
                the port. Each element is a dict contains ``ip_address`` and
                ``mac_address`` keys. Optional.
            * ``extra_dhcp_opts``: A list of extra DHCP option key/value pairs
                for the port. Each element is a dict contains ``opt_name`` and
                ``opt_value`` keys. Optional.

        :returns: The results of port creation
        :rtype: :class:`~openstack.vpc.v1.port.Port`
        """
        return self._create(_port.Port, **attrs)

    def update_port(self, port, **attrs):
        """Update a port

        :param port: Either the id of a port or a
            :class:`~openstack.vpc.v1.port.Port` instance.
        :param dict attrs: The attributes to update on the port represented
            by ``port``. Available attributes include:

            * ``name``: The port name. Optional.
            * ``security_group_ids``: A list of UUID of the security groups.
                Optional.
            * ``allowed_address_pairs``: A list of address pairs allowed for
                the port. Each element is a dict contains ``ip_address`` and
                ``mac_address`` keys. Optional.
            * ``extra_dhcp_opts``: A list of extra DHCP option key/value pairs
                for the port. Each element is a dict contains ``opt_name`` and
                ``opt_value`` keys. Optional.

        :returns: The updated port
        :rtype: :class:`~openstack.vpc.v1.port.Port`
        """
        return self._update(_port.Port, port, **attrs)

    def delete_port(self, port, ignore_missing=True):
        """Delete a port

        :param port: The value can be either the ID of a port or a
            :class:`~openstack.vpc.v1.port.Port` instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the port does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent port.

        :returns: ``None``
        """
        self._delete(_port.Port, port, ignore_missing=ignore_missing)

    def find_port(self, name_or_id, ignore_missing=True):
        """Find a single port

        :param name_or_id: The name or ID of a port.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.vpc.v1.port.Port` or None
        """
        return self._find(_port.Port, name_or_id,
                          ignore_missing=ignore_missing)

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

    def update_bandwidth(self, bandwidth, **attrs):
        """Update a bandwidth

        :param bandwidth: Either the id of a bandwidth or a
            :class:`~openstack.vpc.v1.bandwidth.Bandwidth` instance.
        :param dict attrs: The attributes to update on the bandwidth
            represented by ``bandwidth``. Available attributes include:

            * ``name``: The port name. Optional. The value is a string
                of 1 to 64 characters that can contain letters, digits,
                underscores (_), and hyphens (-).
            * ``size``: The bandwidth size. The value ranges from 1 Mbit/s
                to 2000 Mbit/s. Optional.

            Either parameter `size` or `name` must be set.

        :returns: The updated bandwidth
        :rtype: :class:`~openstack.vpc.v1.bandwidth.Bandwidth`
        """
        return self._update(_bandwidth.Bandwidth, bandwidth, **attrs)

    def find_bandwidth(self, name_or_id, ignore_missing=True):
        """Find a single bandwidth

        :param name_or_id: The name or ID of a bandwidth.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.vpc.v1.bandwidth.Bandwidth` or None
        """
        return self._find(_bandwidth.Bandwidth, name_or_id,
                          ignore_missing=ignore_missing)

    def security_groups(self, **query):
        """Return a generator of security groups

        :param dict query: Optional query parameters to be sent to limit
                           the resources being returned. Valid parameters are:

            * ``limit``: The number of records returned on each page.
            * ``marker``: The resource ID of pagination query.
            * ``vpc_id``: The ID of the VPC this security group is
                          associated with.
            * ``enterprise_project_id``: The ID of the enterprise project.

        :returns: A generator of security group objects
        :rtype: :class:`~openstack.vpc.v1.security_group.SecurityGroup`
        """
        return self._list(_security_group.SecurityGroup, paginated=True,
                          **query)

    def create_security_group(self, **attrs):
        """Create a new security group from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.vpc.v1.security_group.SecurityGroup`,
            comprised of the properties on the SecurityGroup class.
            Available attributes include:

            * ``name``: The security group name. The value is a string
                of 1 to 64 characters that can contain letters, digits,
                underscores (_), and hyphens (-).
            * ``description``: The supplementary information about
                the security group. The value is a string of 0 to 128
                characters, which consists of letters and digits.
            * ``vpc_id``: The resource ID of the VPC to which
                the security group belongs.

        :returns: The results of security group creation
        :rtype: :class:`~openstack.vpc.v1.security_group.SecurityGroup`
        """
        return self._create(_security_group.SecurityGroup, **attrs)

    def delete_security_group(self, security_group, ignore_missing=True):
        """Delete a security group

        :param security_group:
            The value can be either the ID of a security group or a
            :class:`~openstack.vpc.v1.security_group.SecurityGroup`
            instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the security group does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent security group.

        :returns: ``None``
        """
        self._delete(_security_group.SecurityGroup, security_group,
                     ignore_missing=ignore_missing)

    def find_security_group(self, name_or_id, ignore_missing=True):
        """Find a single security group

        :param name_or_id: The name or ID of a security group.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.vpc.v1.security_group.
            SecurityGroup` or None
        """
        return self._find(_security_group.SecurityGroup, name_or_id,
                          ignore_missing=ignore_missing)

    def get_security_group(self, security_group):
        """Get a single security group

        :param security_group: The value can be the ID of a security group or a
            :class:`~openstack.vpc.v1.security_group.SecurityGroup` instance.

        :returns: One
            :class:`~openstack.vpc.v1.security_group.SecurityGroup`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
            when no resource can be found.
        """
        return self._get(_security_group.SecurityGroup, security_group)

    def create_security_group_rule(self, **attrs):
        """Create a new security group rule from attributes

        :param dict attrs: Keyword arguments which will be used to create a
            :class:`~openstack.vpc.v1.security_group_rule.
            SecurityGroupRule`, comprised of the properties on the
            SecurityGroupRule class. Available attributes include:

            * ``security_group_id``: The security group ID. Mandatory.
            * ``description``: The extra readable information about the rule.
                Optional.
            * ``direction``: The direction of access control. The value can be
                'egress' or 'ingress'. Mandatory.
            * ``ethertype``: The version of the Internet Protocol. The value
                can be 'IPv4' or 'IPv6'. Default to 'IPv4'. Optional.
            * ``protocol``: The protocol type. The value can be 'icmp', 'tcp',
                or 'udp'. Default to all types of protocol. Optional.
            * ``port_range_min``: The start port. The value ranges from
                1 to 65,535. Optional.
            * ``port_range_max``: The end port. The value ranges from
                1 to 65,535. Optional.
            * ``remote_ip_prefix``: The remote IP address. The value can be
                in the CIDR format or IP addresses. For 'egress' direction, it
                specifies the VM's IP address. For 'ingress' direction, it
                specifies the remote IP address. Optional.
                The parameter is exclusive with parameter ``remote_group_id``.
            * ``remote_group_id``: The ID of the peer security group.
                The value is exclusive with parameter ``remote_ip_prefix``.
                Optional.

        :returns: The results of security group rule creation
        :rtype: :class:`~openstack.vpc.v1.security_group_rule.\
            SecurityGroupRule`
        """
        return self._create(_security_group_rule.SecurityGroupRule, **attrs)

    def delete_security_group_rule(self, security_group_rule,
                                   ignore_missing=True):
        """Delete a security group rule

        :param security_group_rule:
            The value can be either the ID of a security group rule
            or a :class:`~openstack.vpc.v1.security_group_rule.
            SecurityGroupRule` instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the security group rule does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent security group rule.

        :returns: ``None``
        """
        self._delete(_security_group_rule.SecurityGroupRule,
                     security_group_rule, ignore_missing=ignore_missing)

    def find_security_group_rule(self, name_or_id, ignore_missing=True):
        """Find a single security group rule

        :param str name_or_id: The ID of a security group rule.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.vpc.v1.security_group_rule.
                  SecurityGroupRule` or None
        """
        return self._find(_security_group_rule.SecurityGroupRule,
                          name_or_id, ignore_missing=ignore_missing)

    def get_security_group_rule(self, security_group_rule):
        """Get a single security group rule

        :param security_group_rule:
            The value can be the ID of a security group rule or a
            :class:`~openstack.vpc.v1.security_group_rule.\
            SecurityGroupRule` instance.

        :returns: :class:`~openstack.vpc.v1.security_group_rule.\
            SecurityGroupRule`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
            when no resource can be found.
        """
        return self._get(_security_group_rule.SecurityGroupRule,
                         security_group_rule)

    def security_group_rules(self, **query):
        """Return a generator of security group rules

        :param kwargs query: Optional query parameters to be sent to limit
            the resources being returned. Available parameters include:

            * ``security_group_id``: ID of security group that owns the rules

        :returns: A generator of security group rule objects
        :rtype: :class:`~openstack.vpc.v1.security_group_rule.
            SecurityGroupRule`
        """
        return self._list(_security_group_rule.SecurityGroupRule,
                          paginated=False, **query)

    def quotas(self, **query):
        """Return a generator of quotas

        :param dict query: Optional query parameters to be sent to limit
            the resources being returned. Currently no query
            parameter is supported. Available parameters include:

            * ``type``: he resource type. The value can be 'vpc', 'subnet',
                'securityGroup', 'securityGroupRule', 'publicIp', 'vpn',
                'vpngw', 'vpcPeer', 'firewall', 'shareBandwidth',
                'shareBandwidthIP'.

        :returns: A generator of quota objects
        :rtype: :class:`~openstack.vpc.v1.quota.Quota`
        """
        return self._list(_quota.Quota, paginated=False, **query)
