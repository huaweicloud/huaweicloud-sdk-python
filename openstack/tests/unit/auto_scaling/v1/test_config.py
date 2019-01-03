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

import testtools
from openstack.auto_scaling.v1 import config

DATA = {
"tenant": "ce061903a53545dcaddb300093b477d2",
"scaling_configuration_id": "6afe46f9-7d3d-4046-8748-3b2a1085ad86",
"scaling_configuration_name": " config_name_1",
"instance_config": {
    "disk": [
        {
            "size": 40,
            "volume_type": "SATA",
            "disk_type": "SYS"
        },
        {
            "size": 100,
            "volume_type": "SATA",
            "disk_type": "DATA"
        }
    ],
    "personality": None,
    "instance_name": None,
    "instance_id": None,
    "flavorRef": "103",
    "imageRef": "37ca2b35-6fc7-47ab-93c7-900324809c5c",
    "key_name": "keypair01",
    "public_ip": None,
    "user_data": None,
    "metadate": {},
    "security_groups": [{
         "id": "6c22a6c0-b5d2-4a84-ac56-51090dcc33be"
    }],
},
"create_time": "2015-07-23T01:04:07Z"
}

class TestConfig(testtools.TestCase):

    def test_basic(self):
        cfg = config.Config()
        self.assertEqual('scaling_configuration', cfg.resource_key)
        self.assertEqual('scaling_configurations', cfg.resources_key)
        self.assertEqual('/scaling_configuration', cfg.base_path)
        self.assertEqual('auto-scaling', cfg.service.service_type)
        self.assertTrue(cfg.allow_create)
        self.assertTrue(cfg.allow_get)
        self.assertTrue(cfg.allow_delete)
        self.assertTrue(cfg.allow_list)

    def test_make_it(self):
        cfg = config.Config(**DATA)
        self.assertEqual(DATA['tenant'], cfg.tenant)
        self.assertEqual(DATA['scaling_configuration_id'], cfg.id)
        self.assertEqual(DATA['scaling_configuration_name'], cfg.name)
        self.assertIsInstance(cfg.instance_config, config.InstanceConfig)
        self.assertEqual(DATA['create_time'], cfg.create_time)


