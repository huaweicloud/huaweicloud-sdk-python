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

import mock
import uuid

from openstack import exceptions
from openstack.tests.unit import test_proxy_base2
from openstack.vpc.v1 import _proxy
from openstack.vpc.v1 import bandwidth
from openstack.vpc.v1 import port
from openstack.vpc.v1 import private_ip
from openstack.vpc.v1 import public_ip
from openstack.vpc.v1 import quota
from openstack.vpc.v1 import security_group
from openstack.vpc.v1 import security_group_rule
from openstack.vpc.v1 import subnet
from openstack.vpc.v1 import vpc


VPC_ID = uuid.uuid4().hex
VPC_ATTRS = {'name': 'vpc-name', 'cidr': '192.168.0.0/16'}
VPC_RESULT = {
    'vpc': {
        'id': VPC_ID,
        'name': 'vpc-name',
        'cidr': '192.168.0.0/16',
        'status': 'CREATING',
    }
}
VPC = vpc.VPC(id=VPC_ID)
IDENTIFIER = 'IDENTIFIER'


class TestVPCProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestVPCProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_vpcs(self):
        self.verify_list(self.proxy.vpcs, vpc.VPC, paginated=True)

    def test_vpc_create(self):
        self.verify_create(self.proxy.create_vpc, vpc.VPC,
                           method_kwargs=VPC_ATTRS,
                           expected_kwargs=VPC_ATTRS,
                           expected_result=VPC_RESULT)

    def test_vpc_update(self):
        self.verify_update(self.proxy.update_vpc, vpc.VPC)

    def test_vpc_delete(self):
        self.verify_delete(self.proxy.delete_vpc, vpc.VPC, False)

    def test_vpc_delete_ignore(self):
        self.verify_delete(self.proxy.delete_vpc, vpc.VPC, True)

    def test_vpc_get_by_id(self):
        self.verify_get(self.proxy.get_vpc, vpc.VPC, value=[VPC_ID])

    def test_vpc_get_by_vpc(self):
        self.verify_get(self.proxy.get_vpc, vpc.VPC, value=[VPC])

    def test_vpc_find_by_id(self):
        self.verify_find(self.proxy.find_vpc, vpc.VPC)

    def test_subnet_create_attrs(self):
        self.verify_create(self.proxy.create_subnet, subnet.Subnet)

    def test_subnet_find(self):
        self.verify_find(self.proxy.find_subnet, subnet.Subnet)

    def test_subnet_get(self):
        self.verify_get(self.proxy.get_subnet, subnet.Subnet)

    def test_subnets(self):
        self.verify_list(self.proxy.subnets, subnet.Subnet, paginated=True)

    def test_subnet_update(self):
        mock_method = 'openstack.proxy2.BaseProxy._update'
        expected_args = [subnet.Subnet, 'name_or_id']
        expected_kwargs = {'x': 1, 'y': 2, 'vpc_id': 'vpc_id'}
        with mock.patch(mock_method) as mocked:
            self.proxy.update_subnet('name_or_id', **expected_kwargs)
            mocked.assert_called_once_with(*expected_args, **expected_kwargs)

    def test_public_ips(self):
        self.verify_list(self.proxy.public_ips,
                         public_ip.PublicIP,
                         paginated=True)

    def test_public_ip_get(self):
        self.verify_get(self.proxy.get_public_ip, public_ip.PublicIP)

    def test_public_ip_delete(self):
        self.verify_delete(self.proxy.delete_public_ip,
                           public_ip.PublicIP,
                           False)

    def test_public_ip_delete_ignore(self):
        self.verify_delete(self.proxy.delete_public_ip,
                           public_ip.PublicIP,
                           True)

    def test_public_ip_find(self):
        self.verify_find(self.proxy.find_public_ip, public_ip.PublicIP)

    def test_private_ip_create_attrs(self):
        self.verify_create(self.proxy.create_private_ip, private_ip.PrivateIP)

    def test_private_ip_batch_create(self):
        mock_method = 'openstack.vpc.v1.private_ip.PrivateIP.batch_create'
        with mock.patch(mock_method) as mocked:
            priv_ip = private_ip.PrivateIP()
            mocked.return_value = [priv_ip]
            req = {'subnet_id': 'id', 'ip_address': 'ip'}
            result = self.proxy.create_private_ips(req)
            mocked.assert_called_once_with(self.session, (req,))
            self.assertEqual(list, type(result))

    def test_private_ip_delete(self):
        self.verify_delete(self.proxy.delete_private_ip,
                           private_ip.PrivateIP, False)

    def test_private_ip_delete_ignore(self):
        self.verify_delete(self.proxy.delete_private_ip,
                           private_ip.PrivateIP, True)

    def test_private_ip_find(self):
        mock_method = 'openstack.proxy2.BaseProxy._find'
        test_method = self.proxy.find_private_ip
        method_args = ['name_or_id', 'subnet_id', True]
        expected_args = [private_ip.PrivateIP, 'name_or_id']
        expected_kwargs = {'ignore_missing': True, 'subnet_id': 'subnet_id'}
        self._verify2(mock_method, test_method,
                      method_args=method_args,
                      expected_args=expected_args,
                      expected_kwargs=expected_kwargs,
                      expected_result="result")

    def test_private_ip_get(self):
        self.verify_get(self.proxy.get_private_ip, private_ip.PrivateIP)

    def test_private_ips(self):
        self.verify_list(self.proxy.private_ips,
                         private_ip.PrivateIP, paginated=True,
                         method_args=['subnet_id'],
                         expected_kwargs={'subnet_id': 'subnet_id'})

    def test_ports(self):
        self.verify_list(self.proxy.ports, port.Port, paginated=True)

    def test_port_get(self):
        self.verify_get(self.proxy.get_port, port.Port)

    def test_port_create_attrs(self):
        self.verify_create(self.proxy.create_port, port.Port)

    def test_port_update(self):
        self.verify_update(self.proxy.update_port, port.Port)

    def test_port_delete(self):
        self.verify_delete(self.proxy.delete_port, port.Port, False)

    def test_port_delete_ignore(self):
        self.verify_delete(self.proxy.delete_port, port.Port, True)

    def test_port_find(self):
        self.verify_find(self.proxy.find_port, port.Port)

    def test_bandwidths(self):
        self.verify_list(self.proxy.bandwidths,
                         bandwidth.Bandwidth, paginated=False)

    def test_bandwidth_get(self):
        self.verify_get(self.proxy.get_bandwidth, bandwidth.Bandwidth)

    def test_bandwidth_update(self):
        self.verify_update(self.proxy.update_bandwidth, bandwidth.Bandwidth)

    def test_bandwidth_find(self):
        self.verify_find(self.proxy.find_bandwidth, bandwidth.Bandwidth)

    def test_security_group_create_attrs(self):
        self.verify_create(self.proxy.create_security_group,
                           security_group.SecurityGroup)

    def test_security_group_delete(self):
        self.verify_delete(self.proxy.delete_security_group,
                           security_group.SecurityGroup, False)

    def test_security_group_delete_ignore(self):
        self.verify_delete(self.proxy.delete_security_group,
                           security_group.SecurityGroup, True)

    def test_security_group_find(self):
        self.verify_find(self.proxy.find_security_group,
                         security_group.SecurityGroup)

    def test_security_group_get(self):
        self.verify_get(self.proxy.get_security_group,
                        security_group.SecurityGroup)

    def test_security_groups(self):
        self.verify_list(self.proxy.security_groups,
                         security_group.SecurityGroup,
                         paginated=True)

    def test_security_group_rule_create_attrs(self):
        self.verify_create(self.proxy.create_security_group_rule,
                           security_group_rule.SecurityGroupRule)

    def test_security_group_rule_delete(self):
        self.verify_delete(self.proxy.delete_security_group_rule,
                           security_group_rule.SecurityGroupRule, False)

    def test_security_group_rule_delete_ignore(self):
        self.verify_delete(self.proxy.delete_security_group_rule,
                           security_group_rule.SecurityGroupRule, True)

    def test_security_group_rule_find(self):
        self.verify_find(self.proxy.find_security_group_rule,
                         security_group_rule.SecurityGroupRule)

    def test_security_group_rule_get(self):
        self.verify_get(self.proxy.get_security_group_rule,
                        security_group_rule.SecurityGroupRule)

    def test_security_group_rules(self):
        self.verify_list(self.proxy.security_group_rules,
                         security_group_rule.SecurityGroupRule,
                         paginated=False)

    def test_quotas(self):
        self.verify_list(self.proxy.quotas, quota.Quota, paginated=False)
