#!/usr/bin/python
# coding=utf-8

from openstack import connection

username = "**********"
password = "**********"
userDomainId = "**********"
auth_url = "**********"

# create connection
conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    domain_id=userDomainId,
    username=username,
    password=password
)


# Querying the List of Domains Accessible to Users
def get_domain_scopes():
    domains = conn.identity.get_domain_scopes()
    for domain in domains:
        print(domain)


# Query domain password strength config
def get_password_config(domain_id):
    password_config = conn.identity.get_password_config(domain_id)
    print(password_config)


# Query domain password strength config with option
def get_password_config_by_option(domain_id, option):
    password_config = conn.identity.get_password_config_by_option(domain_id, option)
    print(password_config)


if __name__ == "__main__":
    domain_id = "**********"
    option = "**********"   # the value of option can be 'password_regex' or 'password_regex_description'
    get_domain_scopes()
    get_password_config(domain_id)
    get_password_config_by_option(domain_id, option)
