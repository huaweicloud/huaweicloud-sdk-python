# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from openstack.anti_ddos.v1 import antiddos

CONFIG_EXAMPLE = {
    "traffic_limited_list": [
        {
            "traffic_pos_id": 1,
            "traffic_per_second": 10,
            "packet_per_second": 2000
        },
    ],
    "http_limited_list": [
        {
            "http_request_pos_id": 1,
            "http_packet_per_second": 100
        },
        {
            "http_request_pos_id": 2,
            "http_packet_per_second": 150
        },
    ],
    "connection_limited_list": [
        {
            "cleaning_access_pos_id": 1,
            "new_connection_limited": 10,
            "total_connection_limited": 30
        },
    ],
    "extend_ddos_config": [
        {
            "new_connection_limited": 80,
            "total_connection_limited": 700,
            "http_packet_per_second": 500000,
            "traffic_per_second": 1000,
            "packet_per_second": 200000,
            "setID": 33
        },
    ]
}

FLOATING_IP_EXAMPLE = {
    "enable_L7": True,
    "traffic_pos_id": 1,
    "http_request_pos_id": 1,
    "cleaning_access_pos_id": 1,
    "app_type_id": 1
}

TASK_STATUS_EXAMPLE = {
    "task_status": "running",
    "task_msg": ""
}


class TestQueryConfigList(testtools.TestCase):

    def test_basic(self):
        sot = antiddos.QueryConfigList()

        self.assertEqual('/antiddos/query_config_list', sot.base_path)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)

    def test_make_it(self):

        sot = antiddos.QueryConfigList(**CONFIG_EXAMPLE)
        self.assertEqual(CONFIG_EXAMPLE['traffic_limited_list'],
                         sot.traffic_limited_list)
        self.assertEqual(CONFIG_EXAMPLE['http_limited_list'],
                         sot.http_limited_list)
        self.assertEqual(CONFIG_EXAMPLE['connection_limited_list'],
                         sot.connection_limited_list)
        self.assertEqual(CONFIG_EXAMPLE['extend_ddos_config'],
                         sot.extend_ddos_config)


class TestFloatingIP(testtools.TestCase):

    def test_basic(self):
        sot = antiddos.FloatingIP()

        self.assertEqual('/antiddos', sot.base_path)
        self.assertFalse(sot.allow_create)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)

    def test_make_it(self):

        sot = antiddos.FloatingIP(**FLOATING_IP_EXAMPLE)
        self.assertEqual(FLOATING_IP_EXAMPLE['enable_L7'],
                         sot.enable_L7)
        self.assertEqual(FLOATING_IP_EXAMPLE['traffic_pos_id'],
                         sot.traffic_pos_id)
        self.assertEqual(FLOATING_IP_EXAMPLE['http_request_pos_id'],
                         sot.http_request_pos_id)
        self.assertEqual(FLOATING_IP_EXAMPLE['cleaning_access_pos_id'],
                         sot.cleaning_access_pos_id)
        self.assertEqual(FLOATING_IP_EXAMPLE['app_type_id'],
                         sot.app_type_id)


class TestTaskStatus(testtools.TestCase):

    def test_basic(self):

        sot = antiddos.TaskStatus()
        self.assertEqual('/antiddos/query_task_status', sot.base_path)

    def test_make_it(self):

        sot = antiddos.TaskStatus(**TASK_STATUS_EXAMPLE)
        self.assertEqual(TASK_STATUS_EXAMPLE['task_status'],
                         sot.task_status)
        self.assertEqual(TASK_STATUS_EXAMPLE['task_msg'],
                         sot.task_msg)
