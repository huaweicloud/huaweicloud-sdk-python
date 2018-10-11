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

import sys

from openstack import connection
from openstack import exceptions as _exceptions
from openstack import utils

# logging.basicConfig()
utils.enable_logging(debug=True, stream=sys.stdout)


class __BaseVpnService(object):
    username = "zhoulei"
    password = "sssss"
    projectId = "054efa2069a64785a196efe56c05ee74"
    userDomainId = "cb06f3a9fa4e464ea62695b4dd26e5f0"
    auth_url = "https://iam.eu-de.otc.t-systems.com/v3"

    def __init__(self, debug=False):
        utils.enable_logging(debug=debug, stream=sys.stdout)
        try:
            self.conn = connection.Connection(auth_url=self.auth_url,
                                              user_domain_id=self.userDomainId,
                                              project_id=self.projectId,
                                              username=self.username,
                                              password=self.password,
                                              verify=False)
        except _exceptions.InvalidRequest as e:
            raise _exceptions.InvalidRequest(message='init connect error')


class VPNService(__BaseVpnService):
    def create_vpn_service(self):
        data = {
            "subnet_id": None,
            "router_id": "12a5ead9-9b93-4ac9-b28e-ba0992ac8a85",
            "name": "myservice",
            "admin_state_up": True,
        }

        ff = self.conn.network.create_vpn_service(**data)
        print ff

    def for_test(self):
        ff = self.conn.network.networks()

        network = [i for i in ff]
        data = {
            "subnet_id": None,
            "router_id": "12a5ead9-9b93-4ac9-b28e-ba0992ac8a85",
            "name": "myservice",
            "admin_state_up": True,
        }
        # data.update({'router_id': network[0].name})
        ff = self.conn.network.create_vpn_service(**data)
        return ff

    def get_vpn_services(self):
        ff = self.conn.network.vpn_services()
        return ff

    def get_vpn_service(self, vpn_id):
        ff = self.conn.network.get_vpn_service(vpn_id)
        print ff

    def find_vpn_service(self, vpn_id):
        ff = self.conn.network.find_vpn_service(vpn_id)
        print ff

    def detele_vpn_service(self, vpn_id):
        ff = self.conn.network.delete_vpn_service(vpn_id)
        print ff

    def update_vpn_service(self, vpn_id):
        ff = self.conn.network.update_vpn_service(vpn_id)
        print ff


class IPSecPolicy(__BaseVpnService):
    def create_ipsec_service(self):
        data = {
            "name": "ipsecpolicy1sdfasdfasdfasdf",
            "transform_protocol": "esp",
            "auth_algorithm": "sha1",
            "encapsulation_mode": "tunnel",
            "encryption_algorithm": "aes-128",
            "pfs": "group14",
            "lifetime": {
                "units": "seconds",
                "value": 1212
            },
            "description": "ZLZLZLZ"
        }

        ff = self.conn.network.create_ipsec_policy(**data)
        return ff

    def get_ipsecs(self):
        ff = self.conn.network.get_ipsec_policy()
        return ff

    def get_ipsec_from_id(self, ipsecpolicy_id):
        ff = self.conn.network.find_ipsec_policy(ipsecpolicy_id)
        print ff

    def delete_ipsec(self, policy_id):
        ff = self.conn.network.delete_ipsec_policy(policy_id)
        print ff

    def modify_ipsec(self, policy_id):
        data = {
            "pfs": "group2",
            "name": 'thisisnew'
        }
        ff = self.conn.network.update_ipsec_policy(policy_id, **data)
        print ff


class IkePolcy(__BaseVpnService):
    def create_ike_service(self):
        data = {
            "phase1_negotiation_mode": "main",
            "auth_algorithm": "sha1",
            "encryption_algorithm": "aes-128",
            "pfs": "group5",
            "lifetime": {
                "units": "seconds",
                "value": 7200
            },
            "ike_version": "v1",
            "name": "ikepolicy1tetetetette"
        }

        ff = self.conn.network.create_ike_policy(**data)
        return ff

    def get_ikes(self):
        ff = self.conn.network.get_ike_policy()
        return ff

    def get_ike_from_id(self, ikepolicy_id):
        ff = self.conn.network.find_ike_policy(ikepolicy_id)
        print ff

    def delete_ike(self, policy_id):
        ff = self.conn.network.delete_ike_policy(policy_id)
        print ff

    def modify_ike(self, policy_id):
        data = {
            "description": 'thisisnew'
        }
        ff = self.conn.network.update_ike_policy(policy_id, **data)
        print ff


class EndPointGroup(__BaseVpnService):
    def create_endpoint_group(self):
        data = {
            "endpoints": ["100.2.0.0/24", "100.3.0.0/24"],
            "type": "cidr",
            "name": "peers"
        }

        ff = self.conn.network.create_endpoint_group(**data)
        print ff

    def for_test(self):
        data1 = {
            "endpoints": ["100.2.0.0/24", "100.3.0.0/24"],
            "type": "cidr",
            "name": "peers"
        }

        data2 = {
            "endpoints": ["10.2.0.0/24", "10.3.0.0/24"],
            "type": "cidr",
            "name": "peers"
        }

        ff = []
        ff1 = self.conn.network.create_endpoint_group(**data1)
        ff2 = self.conn.network.create_endpoint_group(**data2)
        ff.append(ff1)
        ff.append(ff2)
        return ff

    def get_endpoint_group(self):
        ff = self.conn.network.get_endpoint_group()
        return ff

    def get_endpoint_group_from_id(self, endpoint_group):
        ff = self.conn.network.find_endpoint_group(endpoint_group)
        print ff

    def delete_endpoint_group(self, endpoint_group):
        ff = self.conn.network.delete_endpoint_group(endpoint_group)
        print ff

    def modify_endpoint_group(self, endpoint_group):
        data = {
            "description": 'thisisnew'
        }
        ff = self.conn.network.update_endpoint_group(endpoint_group, **data)
        print ff


class VPNConnetion(__BaseVpnService):
    def create_vpn_connection(self):
        data = {
            "psk": "secret",
            "initiator": "bi-directional",
            "ipsecpolicy_id": "e6e23d0c-9519-4d52-8ea4-5b1f96d857b1",
            "admin_state_up": True,
            "mtu": "1500",
            "peer_ep_group_id": "9ad5a7e0-6dac-41b4-b20d-a7b8645fddf1",
            "ikepolicy_id": "9b00d6b0-6c93-4ca5-9747-b8ade7bb514f",
            "vpnservice_id": "5c561d9d-eaea-45f6-ae3e-08d1a7080828",
            "local_ep_group_id": "3e1815dd-e212-43d0-8f13-b494fa553e68",
            "peer_address": "172.24.4.233",
            "peer_id": "172.24.4.233",
            "name": "vpnconnection1"
        }

        ff = self.conn.network.create_vpn_connection(**data)
        print ff

    def for_test(self, ipsecpolicy_id, ikepolicy_id, local_ep_group_id, peer_ep_group_id, vpnservice_id):
        data = {
            "psk": "secret",
            "initiator": "bi-directional",
            "ipsecpolicy_id": "e6e23d0c-9519-4d52-8ea4-5b1f96d857b1",
            "admin_state_up": True,
            "mtu": "1500",
            "peer_ep_group_id": "9ad5a7e0-6dac-41b4-b20d-a7b8645fddf1",
            "ikepolicy_id": "9b00d6b0-6c93-4ca5-9747-b8ade7bb514f",
            "vpnservice_id": "5c561d9d-eaea-45f6-ae3e-08d1a7080828",
            "local_ep_group_id": "3e1815dd-e212-43d0-8f13-b494fa553e68",
            "peer_address": "172.24.4.233",
            "peer_id": "172.24.4.233",
            "name": "vpnconnection1"
        }

        data['ipsecpolicy_id'] = ipsecpolicy_id
        data['ikepolicy_id'] = ikepolicy_id
        data['local_ep_group_id'] = local_ep_group_id
        data['peer_ep_group_id'] = peer_ep_group_id
        data['vpnservice_id'] = vpnservice_id

        ff = self.conn.network.create_vpn_connection(**data)
        return ff

    def get_vpn_connection(self):
        ff = self.conn.network.get_vpn_connection()
        return ff

    def get_vpn_connection_from_id(self, vpn_connection):
        ff = self.conn.network.find_vpn_connection(vpn_connection)
        print ff

    def delete_vpn_connection(self, vpn_connection):
        ff = self.conn.network.delete_vpn_connection(vpn_connection)
        print ff

    def modify_vpn_connection(self, vpn_connection):
        data = {
            "description": 'thisisnew'
        }
        ff = self.conn.network.update_vpn_connection(vpn_connection, **data)
        print ff


def ops_vpn_service():
    vpn_gateway = VPNService()
    vpn_gateway.for_test()

    # ff = vpn_gateway.get_vpn_services()
    # for i in ff:
    #     print i
    #     vpn_gateway.detele_vpn_service(vpn_id=i.id)


def ops_ip_sec_policy():
    ip_sec_policy = IPSecPolicy(debug=False)
    # create_ipsec_service()
    ff = ip_sec_policy.get_ipsecs()
    for i in ff:
        print i
        # ip_sec_policy.get_ipsec_from_id(ipsecpolicy_id=i.id)
        # ip_sec_policy.get_ipsec_from_id(ipsecpolicy_id='6aae8319-2f6c-46af-9f3a-3f1d8b8a38d2')
        # # modify_ipsec(policy_id='6aae8319-2f6c-46af-9f3a-3f1d8b8a38d2')
        ip_sec_policy.delete_ipsec(policy_id=i.id)
        # ip_sec_policy.get_ipsec_from_id(ipsecpolicy_id='6aae8319-2f6c-46af-9f3a-3f1d8b8a38d2')


def ops_ike_policy():
    ike_policy = IkePolcy(debug=False)
    # ike_policy.create_ike_service()
    ff = ike_policy.get_ikes()
    for i in ff:
        print i
        # ike_policy.get_ike_from_id(ikepolicy_id='809bc07e-04d6-4c8f-b516-410c900b2845')
        # ike_policy.modify_ike(policy_id='809bc07e-04d6-4c8f-b516-410c900b2845')
        # ike_policy.get_ike_from_id(ikepolicy_id='809bc07e-04d6-4c8f-b516-410c900b2845')
        ike_policy.delete_ike(policy_id=i.id)
        #     ike_policy.get_ike_from_id(ikepolicy_id='809bc07e-04d6-4c8f-b516-410c900b2845')


def ops_endpoint_group():
    endpoint_group = EndPointGroup(debug=False)
    # endpoint_group.create_endpoint_group()
    ff = endpoint_group.get_endpoint_group()
    # endpoint_group.get_endpoint_group_from_id(endpoint_group='32ce9d07-7640-40a7-9ed5-9e7c1d13eede')
    # endpoint_group.modify_endpoint_group(endpoint_group='32ce9d07-7640-40a7-9ed5-9e7c1d13eede')
    # endpoint_group.get_endpoint_group_from_id(endpoint_group='32ce9d07-7640-40a7-9ed5-9e7c1d13eede')
    for i in ff:
        print i
        endpoint_group.delete_endpoint_group(endpoint_group=i.id)
    endpoint_group.get_endpoint_group()


def ops_vpn_connection():
    vpn_connection = VPNConnetion()
    ff = vpn_connection.get_vpn_connection()
    for i in ff:
        print i
        vpn_connection.delete_vpn_connection(vpn_connection=i.id)
        # vpn_connection.create_vpn_connection()
        # vpn_connection.get_vpn_connection_from_id(vpn_connection='e191b292-9867-48e8-9e12-ae9ffc47cc2a')
        # vpn_connection.modify_vpn_connection(vpn_connection='e191b292-9867-48e8-9e12-ae9ffc47cc2a')
        # vpn_connection.delete_vpn_connection(vpn_connection='e191b292-9867-48e8-9e12-ae9ffc47cc2a')


def ops_all():


    vpn_gateway = VPNService()
    vpnservice_id = vpn_gateway.for_test()
    vpn_gateway.for_test()
    endpoint_group = EndPointGroup()
    tem = endpoint_group.for_test()
    local_ep_group_id = tem[0]
    peer_ep_group_id = tem[1]

    ip_sec_policy = IPSecPolicy()
    ipsecpolicy_id = ip_sec_policy.create_ipsec_service()

    ike_policy = IkePolcy()
    ikepolicy_id = ike_policy.create_ike_service()
    vpn_connection = VPNConnetion()
    result = vpn_connection.for_test(ikepolicy_id=ikepolicy_id.id, ipsecpolicy_id=ipsecpolicy_id.id,
                                     local_ep_group_id=local_ep_group_id.id, peer_ep_group_id=peer_ep_group_id.id,
                                     vpnservice_id=vpnservice_id.id)

    print result


if __name__ == '__main__':
    # ops_vpn_service()
    # ops_endpoint_group()
    # ops_ike_policy()
    # ops_ip_sec_policy()
    # ops_vpn_connection()
    ops_all()
