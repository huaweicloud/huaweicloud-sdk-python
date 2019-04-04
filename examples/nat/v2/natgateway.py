#!/usr/bin/python
# coding=utf-8


from openstack import connection

username = "xxxxx"
password = "xxxxx"
projectId = "xxxxx"
userDomainId = "xxxx"
auth_url = "xxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


# create natGateWay
def create_nat_gateway():
    nat_gateway = conn.nat.create_nat_gateway(router_id='7c7d9bf6-9431-4366-9be2-e0caea8eb382',
                                              name='nat_gateway_create_test',
                                              description='nat_gateway_create_description',
                                              internal_network_id='8719d692-a4e9-4dbc-bba1-15afd13c4ce5',
                                              spec='1')
    print(nat_gateway)
    return nat_gateway


# get natGateWay detail
def get_nat_gateway(id):
    nat_gateway = conn.nat.get_nat_gateway(id)
    print(nat_gateway)
    return nat_gateway


# get natGateWayList
def get_nat_gateway_list():
    nat_gateways = conn.nat.nat_gateways()
    print(nat_gateways)
    return nat_gateways


# update natGateWay
def update_nat_gateway(id, **data):
    nat_gateway = conn.nat.update_nat_gateway(id, **data)
    print(nat_gateway)
    return nat_gateway


# delete natGateWay
def delete_nat_gateway(id):
    return conn.nat.delete_nat_gateway(id)


if __name__ == '__main__':
    data = {'name': 'nat_gateway_update_test',
            'description': 'nat_gateway_update_description',
            'spec': '3'}
    nat_gateway = create_nat_gateway()
    get_nat_gateway(nat_gateway.id)
    get_nat_gateway_list()
    update_nat_gateway(nat_gateway.id, **data)
    delete_nat_gateway(nat_gateway.id)

