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
from openstack import utils
import time

utils.enable_logging(debug = True, stream = sys.stdout)

username = "***"
password = "***"
projectId = "128a7bf965154373a7b73c89eb6b65aa"
userDomainId = "3b011b89b2f64fb68782a43380e2a78f"
auth_url = "https://iam.cn-north-1.myhwclouds.com/v3"

conn = connection.Connection(
                             auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password,
                             verify=False
                             )

def test_ulb():
    lbs = conn.network.loadbalancers()
    for lb in lbs:
        print lb.id
    lb  = conn.network.get_loadbalancer("fd18b88e-e75f-46d6-984e-753eb56d7b17")
    print lb

    st = conn.network.get_loadbalancer_status_stree("fd18b88e-e75f-46d6-984e-753eb56d7b17")
    print st

    st = conn.network.update_loadbalancer('fd18b88e-e75f-46d6-984e-753eb56d7b17',description = 'this is test')

    lb = conn.network.create_loadbalancer(name = 'ulb-test',
                                      tenant_id  = '128a7bf965154373a7b73c89eb6b65aa',
                                      vip_subnet_id ='20b8a44b-e724-4103-8233-f70c7aa1bbc2',
                                      provider = "vlb",
                                      admin_state_up = True,
                                      description = 'this is a test'
                                      )
    time.sleep(10)
    conn.network.delete_loadbalancer(lb)

    lss = conn.network.listeners()
    for ls in lss:
        print ls

    ls = conn.network.create_listener(
                                    protocol_port = '80',
                                    protocol = 'HTTP',
                                    loadbalancer_id = 'fd18b88e-e75f-46d6-984e-753eb56d7b17'
                                )
    lsn =  conn.network.get_listener('c188ba92-8a1b-416e-9ec6-75b9826be486')

    conn.network.update_listener(lsn, name = 'test-listener')

    conn.network.get_listener('c188ba92-8a1b-416e-9ec6-75b9826be486')

    conn.network.delete_listener('c188ba92-8a1b-416e-9ec6-75b9826be486')
    pos = conn.network.pools()
    for p in pos:
        print p.listener_id
    p = conn.network.update_pool('ad1044de-fcd7-405c-9542-650f857b0c25', description = "this is test pool")
    p = conn.network.create_pool(
                             lb_algorithm = "LEAST_CONNECTIONS",
                             protocol = "HTTP",
                             loadbalancer_id = 'fd18b88e-e75f-46d6-984e-753eb56d7b17',
                             admin_state_up = True,
                             name = "pool-test-lb",
                             description="this is test pool,create with lb-id"
                             )
    print p
    print conn.network.get_pool('ad1044de-fcd7-405c-9542-650f857b0c25')
    conn.network.delete_pool('5c0517a6-9157-4ce1-b078-def2550fb4f4')
    ms = conn.network.members(pool_id = 'ad1044de-fcd7-405c-9542-650f857b0c25')
    for m in ms:
        print m
    m = conn.network.create_member(
        name = "test-member",
        address = '192.168.1.165',
        protocol_port= 6000,
        subnet_id = '20b8a44b-e724-4103-8233-f70c7aa1bbc2',
        admin_state_up = True,
        pool_id = 'ad1044de-fcd7-405c-9542-650f857b0c25'
    )
    print conn.network.get_member('8366279f-54af-4b0e-b9eb-d96405b2e726', pool = 'ad1044de-fcd7-405c-9542-650f857b0c25')
    print conn.network.update_member('8366279f-54af-4b0e-b9eb-d96405b2e726', name = 'updated-name',pool_id = 'ad1044de-fcd7-405c-9542-650f857b0c25')
    conn.network.delete_member('8366279f-54af-4b0e-b9eb-d96405b2e726',pool = 'ad1044de-fcd7-405c-9542-650f857b0c25')
    hms = conn.network.healthmonitors()
    for hm in hms:
        print hm
    print conn.network.get_healthmonitor('08eac2e1-7d78-43b1-b210-afd801045897')

    healthmonitor = conn.network.create_healthmonitor(
        # must parameter
        # 'HTTP', 'HTTPS', 'PING', 'TCP', 'UDP_CONNECT'
        type = 'HTTP',
        delay = 10,
        timeout = 5,
        max_retries = 3,
        pool_id = 'ad1044de-fcd7-405c-9542-650f857b0c25',
        # optional parameter
        tenant_id = '128a7bf965154373a7b73c89eb6b65aa',
        name = 'hm_name_by_create',
        admin_state_up = True,
        monitor_port = 8000,
        expected_codes = '200',
        url_path = '/',
        http_method = 'GET'
    )
    print 'print start >'
    print healthmonitor
    print '< print end'

    print conn.network.update_healthmonitor('08eac2e1-7d78-43b1-b210-afd801045897',delay = 10,
                                        max_retries= 3,
                                        name = 'updated-name',
                                        timeout = 3,
                                        http_method='GET',
                                        expected_codes = '200',
                                        url_path = '/',
                                        monitor_port = 8000
                                        )
    conn.network.delete_healthmonitor("08eac2e1-7d78-43b1-b210-afd801045897")
    data = {
    "action": "REDIRECT_TO_POOL",
    "listener_id": "11d633e3-ea9f-4e14-bd87-2d2866d347fd",
    "redirect_pool_id": "3a412129-863e-430e-a03a-aa6c66a7827e",
    "name": "test-policy",
    "admin_state_up": True
    }

    print conn.network.create_policy(**data)
    pls = conn.network.poliycies()
    for pl in pls:
        print pl
    print conn.network.get_policy("a1154af3-9bdf-4fd8-9c96-f63b93319c7e")
    print conn.network.update_policy("a1154af3-9bdf-4fd8-9c96-f63b93319c7e", name = "update-policy", description = "this is a test")
    conn.network.delete_policy("a1154af3-9bdf-4fd8-9c96-f63b93319c7e")
    print conn.network.get_policy("a1154af3-9bdf-4fd8-9c96-f63b93319c7e")

    print conn.network.create_rule(
        policy_id = '561fdc6c-c4e1-40c7-8eff-9926c34c30c2',
        type = 'HOST_NAME',
        compare_type = 'EQUAL_TO',
        value = '100'

    )

    rs = conn.network.rules(policy_id = '561fdc6c-c4e1-40c7-8eff-9926c34c30c2')
    for r in rs:
        print r
    print conn.network.get_rule( "fcd3fe4f-7651-4279-a000-d5dcee182fed",'561fdc6c-c4e1-40c7-8eff-9926c34c30c2')
    print conn.network.update_rule("fcd3fe4f-7651-4279-a000-d5dcee182fed",
                                   policy_id = '561fdc6c-c4e1-40c7-8eff-9926c34c30c2',
                                   rule_value = "test"
    )
    conn.network.delete_rule("fcd3fe4f-7651-4279-a000-d5dcee182fed",'561fdc6c-c4e1-40c7-8eff-9926c34c30c2')

    #whitelist get
    whitelist = conn.network.get_whitelist(
        '7d70c81c-ebb9-4740-87b9-521eb3524915'
    )
    print 'print start >'
    print whitelist
    print '< print end'

    #whitelist list
    whitelists = conn.network.whitelists(
        # listener_id='76323057-293c-4154-936d-ae5a245492c9',
        # id = '***',
        # enable_whitelist = True,
        # whitelist = '***'
    )
    print 'print start >'
    for whitelist in whitelists:
        print whitelist
    print '< print end'

    #whitelist create
    whitelist = conn.network.create_whitelist(
        # must parameter
        listener_id = '76323057-293c-4154-936d-ae5a245492c9',
        # optional parameter
        tenant_id = '128a7bf965154373a7b73c89eb6b65aa',
        enable_whitelist = True,
        whitelist = '192.168.0.3,192.168.0.6,192.168.0.9'
    )
    # print 'print start >'
    print whitelist
    print '< print end'

    #whitelist delete
    conn.network.delete_whitelist(
        '7d70c81c-ebb9-4740-87b9-521eb3524915'
    )

    #whitelist update
    whitelist = {
        'enable_whitelist': True,
        'whitelist': '192.168.0.62,192.168.0.82,192.168.0.92'
    }
    update_whitelist = conn.network.update_whitelist(
        '7d70c81c-ebb9-4740-87b9-521eb3524915',
        **whitelist
    )
    cers = conn.network.certificates()
    for cer in cers:
        print cer
    print conn.network.get_certificate('a173f078ff644a4a96e4a84ed854c4b0')

    data = {
        'name' : 'yyxtest',
        'type': 'server',
        'private_key':"-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEA53b//XxsH/oKhMitHnJDRfNU+VeBLbnJeh2j3Jp5tXdkwIENqKjgC17lMtboKvupwBTlqSCFIeVfdu1rLsKsV7p4uWTDM8+lqbrN4qQ26OtEF5Nc9/4jVRCqe6hHR8l4g+B5aOPz0Nz4gn4XRI83c/iSninGy1ewc2C8nmAcNRxsP69AfOBtkp9tr83QmmNQEdj7sXjAsPvlRz3SV5rpE687vIBlJUGUTX+hdhJc/vMfLqmHpDFJI9IqfLPH1bPQ1ZKZmqAucxENCZM7LV24iew061uy8XmLhYHWXMvozQX5MjmM8RhIZIUua0GxS5sk0KQul3a/WgmuydMITijIaQIDAQABAoIBABkq8U7ItqELeRVTFK/Y0MPMX5L1FtC4ANZMXsLf8RfwMX5VCf0qz6Gs4dMTVw9FagG+w/IN3SwAWs79pcfh1wd6+SF/eVIq4+J+s2BPZsEQw8ikd1lnwsO/Gipz87w0hewg/lKPZrVxMXxO5YzI3ci4YIjeFgWKNV92R0wZOzfy+EhpkRGv4KcowoOXhMqAvXdPklSTMk66cOFOXTtzSPOBAsTjWquScW3QTP19HtGZgaCnSmIjqAocmN6ZpHOFEC9sxf1cZ9DMgPwKLz0+qL+liAA+yx6J92kITRYzw1/7Px+O2g1ZGrHKN79Y02TOJD3ohbq3wqeLTET8nprFltkCgYEA958bXxqnJL2pjVHMABUIKl+eTff/bks909Z+B4uDRUXCR0l5u6zP6eFsDnCQxjMm3mI0ekh0yQRfBWzwUxUyLDXxJs2a4ZiYt+SC0dQtoTMSqB1svZm7sq422iBRHFCZ9g8f4RWYkARdEbz4gF8YFN2M2tIaNXluLKNdwW6JjZMCgYEA70vxvAx5JYQ4/uQBXqN6VMF+8tapbesj5J2J4rrUcjMputRgtJLqn9nfT4/00x+026D0jEPhfyAS1MM5rsPB0Li+Wl3/ubvsKXDSyl2la/eRNc15Sqbz4TYlC2DgeylXbHCOFOTxBoQMd3FD2P5GhwCkqxhwGq3iJKnpL1Qnr5MCgYA2w2tsRxq8F24OIQ763avmoysBl11YaS+NUByjUol/ooPq/Cb+CKQa143sS5zZGKr598IfYTLi2iKhsowb884a1Ps2V7ZvOi5cTR9ZhJFq2z6/C3LnI77NL5ZV+1u05WaHcqTcRMhu4Wgr6h0TVvSeeLkUE+9T8D0bhi3P/8BQHQKBgDZ7OvFOgbKJ9RQLQ0iRvcNYPpf5SZ/t/kEJoSAO21mYznJr8gyKuoJkb1RE+T+sI1gxwBvDRK7V1ZO9Uv+4MANeXHBkoFlgMLeKqWNLiOMY/WWbf3cApdvroOmDR/iig/X7dk3Jhhquq8vx7LmVwubvvY36xWM9nZQtXxrYdSSjAoGAX1PvpF2zIn47mI+rcyEJKlY3aEaQAc0xL6h11C2074ASBx8t3/FO0hyJqD9sp3iaoL7OdP9XG1zRi6E7B17ibaMXCzHFTek05xhZj1SxylxF1/Qu4ZZZXZsHRQ4QGwp93CjLqL5RJ3RyrvZGmxh0jEuYdJnq+i7U44e+yvIVFd8=\n-----END RSA PRIVATE KEY-----",
        'certificate':"-----BEGIN CERTIFICATE-----\nMIIELTCCAxWgAwIBAgIJAJU5p3WMgr37MA0GCSqGSIb3DQEBBQUAMGwxCzAJBgNVBAYTAnh4MQswCQYDVQQIEwJ4eDELMAkGA1UEBxMCeHgxCzAJBgNVBAoTAnh4MQswCQYDVQQLEwJ4eDELMAkGA1UEAxMCeHgxHDAaBgkqhkiG9w0BCQEWDXh4QGh1YXdlaS5jb20wHhcNMTcxMDMxMDczMTQxWhcNMjAxMDMwMDczMTQxWjBsMQswCQYDVQQGEwJ4eDELMAkGA1UECBMCeHgxCzAJBgNVBAcTAnh4MQswCQYDVQQKEwJ4eDELMAkGA1UECxMCeHgxCzAJBgNVBAMTAnh4MRwwGgYJKoZIhvcNAQkBFg14eEBodWF3ZWkuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA53b//XxsH/oKhMitHnJDRfNU+VeBLbnJeh2j3Jp5tXdkwIENqKjgC17lMtboKvupwBTlqSCFIeVfdu1rLsKsV7p4uWTDM8+lqbrN4qQ26OtEF5Nc9/4jVRCqe6hHR8l4g+B5aOPz0Nz4gn4XRI83c/iSninGy1ewc2C8nmAcNRxsP69AfOBtkp9tr83QmmNQEdj7sXjAsPvlRz3SV5rpE687vIBlJUGUTX+hdhJc/vMfLqmHpDFJI9IqfLPH1bPQ1ZKZmqAucxENCZM7LV24iew061uy8XmLhYHWXMvozQX5MjmM8RhIZIUua0GxS5sk0KQul3a/WgmuydMITijIaQIDAQABo4HRMIHOMB0GA1UdDgQWBBRl/kItQ4EVKVSo+8Ic+LMYgrekmzCBngYDVR0jBIGWMIGTgBRl/kItQ4EVKVSo+8Ic+LMYgrekm6FwpG4wbDELMAkGA1UEBhMCeHgxCzAJBgNVBAgTAnh4MQswCQYDVQQHEwJ4eDELMAkGA1UEChMCeHgxCzAJBgNVBAsTAnh4MQswCQYDVQQDEwJ4eDEcMBoGCSqGSIb3DQEJARYNeHhAaHVhd2VpLmNvbYIJAJU5p3WMgr37MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEBAN+eExoMQ717UK8dWmLSWblcoN0w74AQ6tCS8wcFsS3c5TK8UkiGd5lMms8pp6V61jwzuJEDxm8Fwa2107pF06gMTPVg4qeRmAzCJZGhNtul0Ba5KDXWPI6PZx1ipP2jdlqme5hjexw0pBDYzGOomxNToXv2DBBNXtT5VH4F3pvLJo+Ai2yxd5PAHRHBrvLyic2tCBO1GRQx7Jrpooc82fm84s5MZjdy0I7lzTnm1krT8dRg2uKVUkhDZhB96MAj6Mx0hIqlrfMQbLoSvpAyMDyX58xkE2j5N899ZNj211zhzrX/Ikb4+KBX+Wat+5LJeAo42c5gVohkzAUe3Kc0xRc=\n-----END CERTIFICATE-----"
    }
    print conn.network.create_certificate(**data)
    print conn.network.update_certificate('b17e4b9086944f4aa8b6b9c348a26008', name = 'updated-certificate')
    print conn.network.delete_certificate('b17e4b9086944f4aa8b6b9c348a26008')
    print conn.network.get_certificate('b17e4b9086944f4aa8b6b9c348a26008')



if __name__ == "__main__":
    test_ulb()