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


# create snatRule
def create_snat_rule():
    snat_rule = conn.nat.create_snat_rule(nat_gateway_id='8d45f435-61f7-4a30-b955-ae40f3e3989b',
                                          network_id='247e2ef9-4625-4cfd-870a-f128f6f38acf',
                                          floating_ip_id='dd05c596-fde4-491f-bc1b-24f2d7e3e623')
    print(snat_rule)
    return snat_rule


# get snatRule detail
def get_snat_rule(id):
    snat_rule = conn.nat.get_snat_rule(id)
    print(snat_rule)
    return snat_rule


# get snatRuleList
def get_snat_rule_list():
    snat_rules = conn.nat.get_snat_rule_list()
    print(snat_rules)
    return snat_rules


# delete snatRule
def delete_snat_rule(id):
    return conn.nat.delete_snat_rule(id)


if __name__ == '__main__':
    snat_rule = create_snat_rule()
    get_snat_rule(snat_rule.id)
    get_snat_rule_list()
    delete_snat_rule(snat_rule.id)

