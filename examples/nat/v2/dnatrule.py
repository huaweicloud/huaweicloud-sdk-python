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


# create dnatRule
def create_dnat_rule():
    dnat_rule = conn.nat.create_dnat_rule(nat_gateway_id="8d45f435-61f7-4a30-b955-ae40f3e3989b",
                                          floating_ip_id="dd05c596-fde4-491f-bc1b-24f2d7e3e623",
                                          protocol="TCP",
                                          external_service_port=6000,
                                          internal_service_port=5000,
                                          port_id="66db34af-2eba-4356-b7b8-9e5f71b3a5dd")
    print(dnat_rule)
    return dnat_rule


# get dnatRule detail
def get_dnat_rule(id):
    dnat_rule = conn.nat.get_dnat_rule(id)
    print(dnat_rule)
    return dnat_rule


# get dnatRuleList
def get_dnat_rule_list():
    dnat_rules = conn.nat.get_dnat_rule_list()
    print(dnat_rules)
    return dnat_rules


# delete dnatRule
def delete_dnat_rule(id):
    return conn.nat.delete_dnat_rule(id)


if __name__ == '__main__':
    dnat_rule = create_dnat_rule()
    get_dnat_rule(dnat_rule.id)
    get_dnat_rule_list()
    delete_dnat_rule(dnat_rule.id)

