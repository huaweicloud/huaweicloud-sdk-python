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
from openstack.cloud_eye.v1 import alarm
from openstack.cloud_eye.v1.metric import Metric

metric = Metric(
    namespace="SYS.ELB",
    dimensions=[
        {
            "name": "lb_instance_id",
            "value": "44d06d10-bce0-4237-86b9-7b4d1e7d5621"
        }
    ],
    metric_name="m8_out_Bps"
)

DATA = {
    "alarm_name": "alarm-ipwx",
    "alarm_description": "",
    "metric": metric,
    "condition":
        {
            "period": 300,
            "filter": "sum",
            "comparison_operator": ">=",
            "value": 0,
            "unit": "",
            "count": 1
        },
    "alarm_enabled": True,
    "alarm_level": 2,
    "alarm_type": "test",
    "alarm_action_enabled": True,
    "alarm_actions":
        [
            {
                "type": "notification",
                "notificationList": ["urn:smn:southchina:68438a86d98e427e907e0097b7e35d48:sd"]
            }
        ],
    "ok_actions":
        [
            {
                "type": "notification",
                "notificationList": ["urn:smn:southchina:68438a86d98e427e907e0097b7e35d48:sd"]
            }
        ],
    "alarm_id": "al1498096535573r8DNy7Gyk",
    "update_time": 1498100100000,
    "alarm_state": "alarm",
    "insufficientdata_actions": [
            {
                "type": "notification",
                "notificationList": ["urn:smn:southchina:68438a86d98e427e907e0097b7e35d48:sd"]
            }
        ]
}


class TestAlarm(testtools.TestCase):
    def test_basic(self):
        obj = alarm.Alarm()
        self.assertEqual("/alarms", obj.base_path)
        self.assertEqual("metric_alarms", obj.resource_key)
        self.assertEqual("metric_alarms", obj.resources_key)
        self.assertTrue(obj.allow_get)
        self.assertTrue(obj.allow_list)
        self.assertTrue(obj.allow_delete)
        self.assertEqual("cloud-eye", obj.service.service_type)

    def test_make_it(self):
        obj = alarm.Alarm(**DATA)
        self.assertEqual(DATA["alarm_name"], obj.name)
        self.assertEqual(DATA["alarm_id"], obj.id)
        self.assertEqual(DATA["alarm_description"], obj.description)
        self.assertEqual(DATA["metric"], obj.metric)
        self.assertEqual(DATA["condition"], obj.condition)
        self.assertEqual(DATA["alarm_enabled"], obj.alarm_enabled)
        self.assertEqual(DATA["alarm_level"], obj.alarm_level)
        self.assertEqual(DATA["alarm_action_enabled"], obj.alarm_action_enabled)
        self.assertEqual(DATA["alarm_actions"], obj.alarm_actions)
        self.assertEqual(DATA["ok_actions"], obj.ok_actions)
        self.assertEqual(DATA["alarm_id"], obj.id)
        self.assertEqual(DATA["update_time"], obj.update_time)
        self.assertEqual(DATA["alarm_state"], obj.state)
        self.assertEqual(DATA["insufficientdata_actions"], obj.insufficientdata_actions)
