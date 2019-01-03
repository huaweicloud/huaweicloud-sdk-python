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

# utils.enable_logging(debug=True, stream=sys.stdout)

username = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"
projectId = "xxxxxxxxxxx"
userDomainId = "xxxxxxxxxx"
auth_url = "xxxxxxxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


def test_show_all_rules(pl_id):
    rules = list(conn.network.rules(policy_id = pl_id))
    print('rule numbers: ', len(rules))
    for rule in rules:
        print(rule)


def test_show_rule(rule_id, pl_id):
    print(conn.network.get_rule(rule_id, pl_id))


def test_create_rule(pl_id):
    rule = conn.network.create_rule(policy_id = pl_id,
                                    type = 'HOST_NAME',
                                    compare_type = 'EQUAL_TO',
                                    value = 'www.test.com')
    return rule


def test_update_rule(rule_id, pl_id):
    data = {'policy_id':pl_id, 'cmpare_type':'EQUAL_TO', 'rule_value' : 'www.test-update.com'}
    rule = conn.network.update_rule(rule_id, **data)
    return rule


def test_delete_rule(rule_id, pl_id):
    conn.network.delete_rule(rule_id, pl_id)


if __name__ == "__main__":
    # policy without Domain Name
    policy_id = "9a6ea8f8-78ab-4ba3-8274-d1d05341565b"
    rule = test_create_rule(policy_id)
    rule_update = test_update_rule(rule.id, policy_id)
    test_show_rule(rule.id, policy_id)
    test_show_all_rules(policy_id)
    test_delete_rule(rule.id, policy_id)