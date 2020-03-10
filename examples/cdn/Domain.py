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

import os
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE',
                      'xxxxxxxxxxx')  # CDN API url,example:https://cdn.myhuaweicloud.com/v1.0/

# AKSK Auth
projectId = "xxxxxxxxxxx"  # Project ID of cn-north-1
cloud = "xxxxxxxxxxx"  # cdn use: cloud = "myhuaweicloud.com"
region = "xxxxxxxxxxx"  # example: region = "cn-north-1"
AK = "xxxxxxxxxxx"
SK = "xxxxxxxxxxx"

conn = connection.Connection(
    project_id=projectId,
    cloud=cloud,
    region=region,
    ak=AK,
    sk=SK)


# token Auth
# username = "xxxxxxxxxxx"  # IAM User Name
# password = "xxxxxxxxxxx"  # IAM User Password
# projectId = "xxxxxxxxxxx"  # Project ID of cn-north-1
# userDomainId = "xxxxxxxxxxx"  # Account ID
# auth_url = "xxxxxxxxxxx"  # IAM auth url,example: https://iam.myhuaweicloud.com/v3
#
# conn = connection.Connection(
#     auth_url=auth_url,
#     user_domain_id=userDomainId,
#     project_id=projectId,
#     username=username,
#     password=password
# )

# new version API
# part 1: Domain Name Operations
# Querying Acceleration Domain Names
def domains_query():
    print('List all domains:')
    for domain in conn.cdn.domains():
        print(domain)

    # Also support filtering by some attributes
    print('List all domains in "online" status: ')
    for domain in conn.cdn.domains(domain_status='online'):
        print(domain)

    print('List all domains of type "web": ')
    for domain in conn.cdn.domains(business_type='web'):
        print(domain)

    # You can list domains by page.
    print('List domains by page: ')
    for domain in conn.cdn.domains(page_size=2, page_number=1):
        print(domain)


def domains_query_by_enterprise_project_id(_enterprise_project_id):
    print('List all domains:')
    for domain in conn.cdn.domains(enterprise_project_id='ALL'):
        print(domain)

    # Also support filtering by some attributes
    print('List domains by enterprise_project_id in "online" status: ')
    for domain in conn.cdn.domains(enterprise_project_id=_enterprise_project_id, domain_status='online'):
        print(domain)

    print('List all domains of type "web": ')
    for domain in conn.cdn.domains(enterprise_project_id='ALL', business_type='web'):
        print(domain)

    # You can list domains by page.
    print('List domains by page: ')
    for domain in conn.cdn.domains(enterprise_project_id='ALL', page_size=10, page_number=1):
        print(domain)


# Creating an Acceleration Domain Name
def domain_create(_domain_name):
    print('Create a new acceleration domain name: ')
    attrs = {
        'domain_name': _domain_name,
        'business_type': 'web',
        'sources': [
            {
                'ip_or_domain': 'X.X.X.X',
                'origin_type': 'xxxxxxxxxxx',
                'active_standby': 1  # 1 means this source is active
            }
        ]
    }
    domain = conn.cdn.create_domain(**attrs)
    print(domain)


def domain_create_by_enterprise_project_id(_domain_name, _enterprise_project_id):
    print('Create a new acceleration domain name: ')
    attrs = {
        'domain_name': _domain_name,
        'business_type': 'web',
        'sources': [
            {
                'ip_or_domain': 'X.X.X.X',
                'origin_type': 'xxxxxxxxxxx',
                'active_standby': 1  # 1 means this source is active
            }
        ],
        'enterprise_project_id': _enterprise_project_id
    }
    domain = conn.cdn.create_domain(**attrs)
    print(domain)


# Querying Details About an Acceleration Domain Name
def domain_query_detail(_domain_id):
    print('Get the domain detail:')
    domain = conn.cdn.get_domain(_domain_id)
    print(domain)


def domain_query_detail_by_enterprise_project_id(_domain_id, _enterprise_project_id='ALL'):
    print('Get the domain detail:')
    domain = conn.cdn.get_domain_detail_by_enterprise_project_id(_domain_id, _enterprise_project_id)
    print(domain)
    print(domain.sources)


# Deleting an Acceleration Domain Name
def domain_delete(_domain_id):
    print('Deleted the domain.')
    conn.cdn.delete_domain(_domain_id)


def domain_delete_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('Delete the domain: ')
    conn.cdn.delete_domain_by_enterprise_project_id(_domain_id, _enterprise_project_id)


# Enabling an Acceleration Domain Name
def domain_enable(_domain_id):
    print('enable the domain: ')
    # Enable the domain
    conn.cdn.enable_domain(_domain_id)


def domain_enable_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('enable the domain: ')
    # Enable the domain
    conn.cdn.enable_domain_by_enterprise_project_id(_domain_id, _enterprise_project_id)


# Disabling an Acceleration Domain Name
def domain_disable(_domain_id):
    print('Delete the domain: ')
    conn.cdn.disable_domain(_domain_id)


def domain_disable_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('Disable the domain: ')
    conn.cdn.disable_domain_by_enterprise_project_id(_domain_id, _enterprise_project_id)


# part 2: Domain Name Configuration
# Modifying Information About the Origin Server
def set_domain_sources(_domain_id):
    print('set domain sources: ')
    attrs = {
        'sources': [
            {
                'ip_or_domain': 'xxxxxxxxxxx',
                'origin_type': 'xxxxxxxxxxx',
                'active_standby': 1
            }
        ]
    }
    conn.cdn.set_domain_sources(_domain_id, **attrs)


def set_domain_sources_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('set domain sources: ')
    attrs = {
        'sources': [
            {
                'ip_or_domain': 'xxxxxxxxxxx',
                'origin_type': 'xxxxxxxxxxx',
                'active_standby': 1
            }
        ]
    }
    conn.cdn.set_domain_sources_by_enterprise_project_id(_domain_id, _enterprise_project_id, **attrs)


# Modifying the Configuration of the Retrieval Host
def set_domain_origin_host(_domain_id):
    print('set domain origin host: ')
    attrs = {
        'origin_host_type': 'accelerate',
        'customize_domain': 'xxxxxxxxxxx'
    }
    conn.cdn.set_domain_origin_host(_domain_id, **attrs)


def set_domain_origin_host_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('set domain origin host: ')
    attrs = {
        'origin_host_type': 'accelerate',
        'customize_domain': 'xxxxxxxxxxx'
    }
    conn.cdn.set_domain_origin_host_by_enterprise_project_id(_domain_id, _enterprise_project_id, **attrs)


# Querying a Retrieval Host
def get_domain_origin_host(_domain_id):
    print('get domain origin host: ')
    domain = conn.cdn.get_domain_origin_host(_domain_id)
    print(domain)


def get_domain_origin_host_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('get domain origin host: ')
    domain = conn.cdn.get_domain_origin_host_by_enterprise_project_id(_domain_id, _enterprise_project_id)
    print(domain)


# Enabling or Disabling Range-based Retrieval
def set_domain_range_status(_domain_id):
    print('set domain origin range: ')
    attrs = {
        'range_status': 'off',  # 'on' or 'off'
    }
    range_status = conn.cdn.set_domain_range_status(_domain_id, **attrs)
    print(range_status)


# Enabling/Disabling 302 Redirect Retrieval
def set_domain_follow302_switch(_domain_id):
    print('set domain follow302 switch: ')
    attrs = {
        'follow302_status': 'on',  # 'on' or 'off'
    }
    follow302_status = conn.cdn.set_domain_follow302_switch(_domain_id, **attrs)
    print(follow302_status)


# Configuring a Referrer List
def set_domain_referer(_domain_id):
    print('set domain referer:')
    attrs = {
        'referer_type': 1,
        'referer_list': 'xxxxxxxxxxx',
        'include_empty': False
    }
    conn.cdn.set_domain_referer(_domain_id, **attrs)


def set_domain_referer_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('set domain referer:')
    attrs = {
        'referer_type': 1,
        'referer_list': 'xxxxxxxxxxx',
        'include_empty': False
    }
    conn.cdn.set_domain_referer_by_enterprise_project_id(_domain_id, _enterprise_project_id, **attrs)


# Querying a Referrer List
def get_domain_referer(_domain_id):
    print('get domain referer:')
    domain = conn.cdn.get_domain_referer(_domain_id)
    print(domain)


def get_domain_referer_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('get domain referer:')
    domain = conn.cdn.get_domain_referer_by_enterprise_project_id(_domain_id, _enterprise_project_id)
    print(domain)


# Querying the IP Address Blacklist or Whitelist
def get_domain_ip_acl(_domain_id):
    print('get domain ip acl:')
    ip_acl = conn.cdn.get_domain_ip_acl(_domain_id)
    print(ip_acl)


# Setting an IP Address Blacklist or Whitelist
def set_domain_ip_acl(_domain_id):
    print('set domain ip acl:')
    attrs = {
        'type': 1,
        'ip_list': [
            "1.2.3.5",
            "2.3.4.5"
        ]
    }
    ip_acl = conn.cdn.set_domain_ip_acl(_domain_id, **attrs)
    print(ip_acl)


# Configuring a Cache Rule
def set_domain_cache_rules(_domain_id):
    print('set domain cache rules:')
    attrs = {
        'ignore_url_parameter': False,
        'rules': [
            {
                'rule_type': 1,
                'content': '.jpg;.png',
                'ttl': 21,
                'ttl_type': 3,
                'priority': 1
            }
        ]
    }
    conn.cdn.set_domain_cache_rules(_domain_id, **attrs)


def set_domain_cache_rules_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('set domain cache rules:')
    attrs = {
        'ignore_url_parameter': False,
        'rules': [
            {
                'rule_type': 1,
                'content': '.jpg;.png;.zip',
                'ttl': 22,
                'ttl_type': 3,
                'priority': 1
            }
        ]
    }
    conn.cdn.set_domain_cache_rules_by_enterprise_project_id(_domain_id, _enterprise_project_id, **attrs)


# Querying a Cache Rule
def get_domain_cache_rules(_domain_id):
    print('get domain cache rules:')
    domain = conn.cdn.get_domain_cache_rules(_domain_id)
    print(domain)


def get_domain_cache_rules_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('get domain cache rules:')
    domain = conn.cdn.get_domain_cache_rules_by_enterprise_project_id(_domain_id, _enterprise_project_id)
    print(domain)


# Configuring HTTPS
def set_domain_https(_domain_id):
    print('set domain https:')
    attrs = {
        'force_redirect_https': 0,
        'https_status': 2,
        'cert_name': 'xxxxxxxxxxx',
        'certificate': 'xxxxxxxxxxx',
        'private_key': 'xxxxxxxxxxx'
    }
    conn.cdn.set_domain_https(_domain_id, **attrs)


def set_domain_https_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('set domain https:')
    attrs = {
        'force_redirect_https': 0,
        'https_status': 2,
        'cert_name': 'xxxxxxxxxxx',
        'certificate': 'xxxxxxxxxxx',
        'private_key': 'xxxxxxxxxxx'
    }
    conn.cdn.set_domain_https_by_enterprise_project_id(_domain_id, _enterprise_project_id, **attrs)


# Querying HTTPS Configurations
def get_domain_https(_domain_id):
    print('get domain https:')
    domain = conn.cdn.get_domain_https(_domain_id)
    print(domain)


def get_domain_https_by_enterprise_project_id(_domain_id, _enterprise_project_id):
    print('get domain https:')
    domain = conn.cdn.get_domain_https_by_enterprise_project_id(_domain_id, _enterprise_project_id)
    print(domain)


# Checking IP Address Information
def get_cdn_ips(_ips):
    print('get cdn ips:')
    iplist = conn.cdn.get_cdn_ips(_ips)
    print(iplist)


def get_cdn_ips_enterprise(_ips, _enterprise_project_id):
    print('get cdn ips:')
    iplist = conn.cdn.get_cdn_ips(_ips, _enterprise_project_id)
    print(iplist)


# Adding/Modifying Response Header Configurations
def set_domain_response_header(_domain_id):
    print('set domain response headers:')
    attrs = {
        'Content-Disposition': "test.xml",
        'Content-Language': "zh-CN",
        'Access-Control-Allow-Origin': "http://www.test.com",
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Max-Age': '86400',
        'Access-Control-Expose-Headers': 'content-type'
    }
    response_header = conn.cdn.set_domain_response_header(_domain_id, **attrs)
    print(response_header)


def set_domain_response_header_enterprise(_domain_id, _enterprise_project_id):
    print('set domain response headers:')
    attrs = {
        'Content-Disposition': "test.xml",
        'Content-Language': "zh-CN",
        'Access-Control-Allow-Origin': "http://www.test.com",
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Max-Age': '86400',
        'Access-Control-Expose-Headers': 'content-type'
    }
    response_header = conn.cdn.set_domain_response_header(_domain_id, _enterprise_project_id, **attrs)
    print(response_header)


# Querying Response Header Configurations
def get_domain_response_header(_domain_id):
    print('get domain response headers:')
    response_header = conn.cdn.get_domain_response_header(_domain_id)
    print(response_header)


def get_domain_response_header_enterprise(_domain_id, _enterprise_project_id):
    print('get domain response headers:')
    response_header = conn.cdn.get_domain_response_header(_domain_id, _enterprise_project_id)
    print(response_header)


if __name__ == "__main__":
    domain_name = 'xxxxxxxxxxx'
    domain_id = 'xxxxxxxxxxx'
    enterprise_project_id = 'ALL'

    # new version API
    # part 1: Domain Name Operations
    # Querying Acceleration Domain Names
    domains_query()
    domains_query_by_enterprise_project_id(enterprise_project_id)

    # Creating an Acceleration Domain Name
    domain_create(domain_name)
    domain_create_by_enterprise_project_id(domain_name, enterprise_project_id)

    # Querying Details About an Acceleration Domain Name
    domain_query_detail(domain_id)
    domain_query_detail_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Deleting an Acceleration Domain Name
    domain_delete(domain_id)
    domain_delete_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Enabling an Acceleration Domain Name
    domain_enable(domain_id)
    domain_enable_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Disabling an Acceleration Domain Name
    domain_disable(domain_id)
    domain_disable_by_enterprise_project_id(domain_id, enterprise_project_id)

    # part 2: Domain Name Configuration
    # Modifying Information About the Origin Server
    set_domain_sources(domain_id)
    set_domain_sources_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Modifying the Configuration of the Retrieval Host
    set_domain_origin_host(domain_id)
    set_domain_origin_host_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Querying a Retrieval Host
    get_domain_origin_host(domain_id)
    get_domain_origin_host_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Enabling or Disabling Range-based Retrieval
    set_domain_range_status(domain_id)

    # Enabling/Disabling 302 Redirect Retrieval
    set_domain_follow302_switch(domain_id)

    # Configuring a Referrer List
    set_domain_referer(domain_id)
    set_domain_referer_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Querying a Referrer List
    get_domain_referer(domain_id)
    get_domain_referer_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Querying the IP Address Blacklist or Whitelist
    get_domain_ip_acl(domain_id)

    # Setting an IP Address Blacklist or Whitelist
    set_domain_ip_acl(domain_id)

    # Configuring a Cache Rule
    set_domain_cache_rules(domain_id)
    set_domain_cache_rules_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Querying a Cache Rule
    get_domain_cache_rules(domain_id)
    get_domain_cache_rules_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Configuring HTTPS
    set_domain_https(domain_id)
    set_domain_https_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Querying HTTPS Configurations
    get_domain_https(domain_id)
    get_domain_https_by_enterprise_project_id(domain_id, enterprise_project_id)

    # Checking IP Address Information
    ips = "1.2.3.4,2.3.4.5,3.4.5.6"
    get_cdn_ips(ips)
    get_cdn_ips_enterprise(ips, enterprise_project_id)

    # Adding/Modifying Response Header Configurations
    set_domain_response_header(domain_id)
    set_domain_response_header_enterprise(domain_id, enterprise_project_id)

    # Querying Response Header Configurations
    get_domain_response_header(domain_id)
    get_domain_response_header_enterprise(domain_id, enterprise_project_id)
