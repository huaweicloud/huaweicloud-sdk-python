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
from openstack.auto_scaling.v1 import group

DATA = {
        "lbaas_listeners": ['test'],
        "networks": [
            {
                "id": "2daf6ba6-fb24-424a-b5b8-c554fab95f15"
            }
        ],
        "detail": None,
        "scaling_group_name": "api_gateway_modify",
        "scaling_group_id": "d4e50321-3777-4135-97f8-9f5e9714a4b0",
        "scaling_group_status": "INSERVICE",
        "scaling_configuration_id": "53579851-3841-418d-a97b-9cecdb663a90",
        "scaling_configuration_name": "press",
        "current_instance_number": 7,
        "desire_instance_number": 8,
        "min_instance_number": 0,
        "max_instance_number": 100,
        "cool_down_time": 900,
        "lb_listener_id": None,
        "security_groups": [
            {
                "id": "23b7b999-0a30-4b48-ae8f-ee201a88a6ab"
            }
        ],
        "create_time": "2015-09-01T08:36:10Z",
        "vpc_id": "3e22f934-800d-4bb4-a588-0b9a76108190",
        "health_periodic_audit_method": "NOVA_AUDIT",
        "health_periodic_audit_time": 60,
        "health_periodic_audit_grace_period": 600,
        "instance_terminate_policy": "OLD_CONFIG_OLD_INSTANCE",
        "is_scaling": True,
        "delete_publicip": True,
        "notifications": [
            "EMAIL"
        ],
        "enterprise_project_id": "c92b1a5d-6f20-43f2-b1b7-7ce35e58e413",
        "available_zones": ["eu-de"],
        "cloud_location_id":"cloud_location_id"
    }

class TestGroup(testtools.TestCase):
    def test_basic(self):
        grp = group.Group()
        self.assertEqual('scaling_group', grp.resource_key)
        self.assertEqual('scaling_groups', grp.resources_key)
        self.assertEqual('/scaling_group', grp.base_path)
        self.assertEqual('auto-scaling', grp.service.service_type)
        self.assertTrue(grp.allow_create)
        self.assertTrue(grp.allow_get)
        self.assertTrue(grp.allow_update)
        self.assertTrue(grp.allow_delete)
        self.assertTrue(grp.allow_list)

    def test_make_it(self):
        grp = group.Group(**DATA)
        self.assertEqual(DATA["networks"], grp.networks)
        self.assertEqual(DATA["detail"], grp.detail)
        self.assertEqual(DATA["scaling_group_name"], grp.name)
        self.assertEqual(DATA["scaling_group_id"], grp.id)
        self.assertEqual(DATA["scaling_group_status"], grp.status)
        self.assertEqual(DATA["scaling_configuration_id"], grp.scaling_configuration_id)
        self.assertEqual(DATA["scaling_configuration_name"], grp.scaling_configuration_name)
        self.assertEqual(DATA["current_instance_number"],grp.current_instance_number)
        self.assertEqual(DATA["desire_instance_number"], grp.desire_instance_number)
        self.assertEqual(DATA["min_instance_number"], grp.min_instance_number)
        self.assertEqual(DATA["max_instance_number"], grp.max_instance_number)
        self.assertEqual(DATA["cool_down_time"], grp.cool_down_time)
        self.assertEqual(DATA["lb_listener_id"], grp.lb_listener_id)
        self.assertEqual(DATA["security_groups"], grp.security_groups)
        self.assertEqual(DATA["create_time"],grp.create_time)
        self.assertEqual(DATA["vpc_id"], grp.vpc_id)
        self.assertEqual(DATA["health_periodic_audit_method"], grp.health_periodic_audit_method)
        self.assertEqual(DATA["health_periodic_audit_time"], grp.health_periodic_audit_time)
        self.assertEqual(DATA["health_periodic_audit_grace_period"], grp.health_periodic_audit_grace_period)
        self.assertEqual(DATA["instance_terminate_policy"], grp.instance_terminate_policy)
        self.assertEqual(DATA["is_scaling"], grp.is_scaling)
        self.assertEqual(DATA["delete_publicip"], grp.delete_publicip)
        self.assertEqual(DATA["notifications"], grp.notifications)
        self.assertEqual(DATA["enterprise_project_id"], grp.enterprise_project_id)
        self.assertEqual(DATA["lbaas_listeners"], grp.lbaas_listeners)
        self.assertEqual(DATA["available_zones"], grp.availability_zones)
        self.assertEqual(DATA["cloud_location_id"],grp.cloud_location_id)





