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
from openstack.ecs.v1 import server

DATA = {
    "id": "4f4b3dfa-eb70-47cf-a60a-998a53bd598a",
    "name": "ecs-2ecf",
    "addresses": {
        "0431c5e5-bc94-4a44-8263-15da2a642435": [{
            "version": "4",
            "addr": "192.168.1.99",
            "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:df:18:6d",
            "OS-EXT-IPS:port_id": "23037c18-027a-44e5-b6b9-f8d8f113fe02",
            "OS-EXT-IPS:type": "fixed"
        }]
    },
    "flavor": {
        "disk": "0",
        "vcpus": "1",
        "ram": "1024",
        "id": "s3.small.1",
        "name": "s3.small.1"
    },
    "accessIPv4": "",
    "accessIPv6": "",
    "status": "ACTIVE",
    "progress": 0,
    "hostId": "c7145889b2e3202cd295ceddb1742ff8941b827b586861fd0acedf64",
    "updated": "2018-09-13T07:06:51Z",
    "created": "2018-09-13T07:03:44Z",
    "metadata": {
        "metering.order_id": "CS1809131459IGC24",
        "metering.image_id": "c71b64e7-4767-4406-afde-2c7c7ac2242c",
        "metering.imagetype": "gold",
        "metering.resourcespeccode": "s3.small.1.linux",
        "image_name": "HEC_Public_Cloudinit_Oracle_Linux_7.4_64bit_40G",
        "metering.resourcetype": "1",
        "metering.product_id": "00301-117024-0--0",
        "cascaded.instance_extrainfo": "pcibridge:2",
        "os_bit": "64",
        "vpc_id": "0431c5e5-bc94-4a44-8263-15da2a642435",
        "os_type": "Linux",
        "charging_mode": "1"
    },
    "tags": [],
    "description": "",
    "locked": False,
    "config_drive": "",
    "tenant_id": "ff2eb406effc455aba53174463eb9322",
    "user_id": "0bc5e11f91dd48849bb03b7c8a263b2c",
    "key_name": "KeyPair-d750",
    "os-extended-volumes:volumes_attached": [{
        "device": "/dev/vda",
        "bootIndex": "0",
        "id": "80c15cff-2473-4982-a816-d760cad6c42c",
        "delete_on_termination": "false"
    }],
    "OS-EXT-STS:power_state": 1,
    "OS-EXT-STS:vm_state": "active",
    "OS-EXT-SRV-ATTR:host": "az21.dc1",
    "OS-EXT-SRV-ATTR:instance_name": "instance-0015147f",
    "OS-EXT-SRV-ATTR:hypervisor_hostname": "nova003@74",
    "OS-DCF:diskConfig": "MANUAL",
    "OS-EXT-AZ:availability_zone": "kvmxen.dc1",
    "os:scheduler_hints": {

    },
    "OS-EXT-SRV-ATTR:root_device_name": "/dev/vda",
    "OS-EXT-SRV-ATTR:ramdisk_id": "",
    "enterprise_project_id": "441d5677-b76a-4dd4-a97a-ef7fd633c095",
    "OS-EXT-SRV-ATTR:user_data": "IyEvYmluL2Jhc2gKZWNobyAncm9vdDokNiRKQ2FzUWQkbm5wVmhJUFZlNVMwc3pXbnJGLnZVZ1FCWk4xTEo5Vy8wd09WTmFZaWpBRXdtRnhuQmZaTllVZXhBWktVWFVTeVhEeERuSUMzV2JjZEJyQUVBZkZvLy8nIHwgY2hwYXNzd2QgLWU7",
    "OS-SRV-USG:launched_at": "2018-08-13T13:46:46.000000",
    "OS-EXT-SRV-ATTR:kernel_id": "",
    "OS-EXT-SRV-ATTR:launch_index": 0,
    "host_status": "UP",
    "OS-EXT-SRV-ATTR:reservation_id": "r-nrd8b5c4",
    "OS-EXT-SRV-ATTR:hostname": "ecs-2ecf",
    "sys_tags": [{
        "key": "_sys_enterprise_project_id",
        "value": "0"
    }],
    "security_groups": [{
        "name": "sg-95ec"
    }],
    "imageRef": "testimageref",
    "flavorRef": "test",
    "user_data": "test",
    "adminPass": "test",
    "vpcid": "test",
    "nics": ["test"],
    "publicip": {},
    "count": 1,
    "isAutoRename": True,
    "root_volume": {},
    "data_volumes": [],
    "availability_zone": "TEST",
    "extendparam": {},
    "server_tags": [],
    "OS-EXT-STS:task_state": 'test',
    "OS-SRV-USG:terminated_at": "test",
}


class TestServer(testtools.TestCase):
    def test_basic(self):
        obj = server.Servers()
        self.assertEqual("/cloudservers", obj.base_path)
        self.assertEqual("server", obj.resource_key)
        self.assertEqual("servers", obj.resources_key)
        self.assertEqual("ecs", obj.service.service_type)
        self.assertTrue(obj.allow_get)
        self.assertTrue(obj.allow_create)

    def test_make_it(self):
        obj = server.Servers(**DATA)
        self.assertEqual(DATA["id"], obj.id)
        self.assertEqual(DATA["name"], obj.name)
        self.assertEqual(DATA["addresses"], obj.addresses)
        self.assertEqual(DATA["flavor"], obj.flavor)
        self.assertEqual(DATA["accessIPv4"], obj.accessIPv4)
        self.assertEqual(DATA["accessIPv6"], obj.accessIPv6)
        self.assertEqual(DATA["status"], obj.status)
        self.assertEqual(DATA["progress"], obj.progress)
        self.assertEqual(DATA["hostId"], obj.hostId)
        self.assertEqual(DATA["updated"], obj.updated)
        self.assertEqual(DATA["created"], obj.created)
        self.assertEqual(DATA["metadata"], obj.metadata)
        self.assertEqual(DATA["tags"], obj.tags)
        self.assertEqual(DATA["description"], obj.description)
        self.assertEqual(DATA["locked"], obj.locked)
        self.assertEqual(DATA["config_drive"], obj.config_drive)
        self.assertEqual(DATA["tenant_id"], obj.project_id)
        self.assertEqual(DATA["user_id"], obj.user_id)
        self.assertEqual(DATA["key_name"], obj.key_name)
        self.assertEqual(DATA["os-extended-volumes:volumes_attached"], obj.os_extended_volumes_volumes_attached)
        self.assertEqual(DATA["OS-EXT-STS:power_state"], obj.OS_EXT_STS_power_state)
        self.assertEqual(DATA["OS-EXT-STS:vm_state"], obj.OS_EXT_STS_vm_state)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:host"], obj.OS_EXT_SRV_ATTR_host)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:instance_name"], obj.OS_EXT_SRV_ATTR_instance_name)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:hypervisor_hostname"], obj.OS_EXT_SRV_ATTR_hypervisor_hostname)
        self.assertEqual(DATA["OS-DCF:diskConfig"], obj.OS_DCF_diskConfig)
        self.assertEqual(DATA["OS-EXT-AZ:availability_zone"], obj.OS_EXT_AZ_availability_zone)
        self.assertEqual(DATA["os:scheduler_hints"], obj.scheduler_hints)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:root_device_name"], obj.OS_EXT_SRV_ATTR_root_device_name)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:ramdisk_id"], obj.OS_EXT_SRV_ATTR_ramdisk_id)
        self.assertEqual(DATA["enterprise_project_id"], obj.enterprise_project_id)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:user_data"], obj.OS_EXT_SRV_ATTR_user_data)
        self.assertEqual(DATA["OS-SRV-USG:launched_at"], obj.OS_SRV_USG_launched_at)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:kernel_id"], obj.OS_EXT_SRV_ATTR_kernel_id)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:launch_index"], obj.OS_EXT_SRV_ATTR_launch_index)
        self.assertEqual(DATA["host_status"], obj.host_status)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:reservation_id"], obj.OS_EXT_SRV_ATTR_reservation_id)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:hostname"], obj.OS_EXT_SRV_ATTR_hostname)
        self.assertEqual(DATA["sys_tags"], obj.sys_tags)
        self.assertEqual(DATA["security_groups"], obj.security_groups)
        self.assertEqual(DATA["imageRef"], obj.imageRef)
        self.assertEqual(DATA["flavorRef"], obj.flavorRef)
        self.assertEqual(DATA["user_data"], obj.user_data)
        self.assertEqual(DATA["adminPass"], obj.adminPass)
        self.assertEqual(DATA["server_tags"], obj.server_tags)
        self.assertEqual(DATA["vpcid"], obj.vpcid)
        self.assertEqual(DATA["nics"], obj.nics)
        self.assertEqual(DATA["publicip"], obj.publicip)
        self.assertEqual(DATA["count"], obj.count)
        self.assertEqual(DATA["isAutoRename"], obj.isAutoRename)
        self.assertEqual(DATA["root_volume"], obj.root_volume)
        self.assertEqual(DATA["data_volumes"], obj.data_volumes)
        self.assertEqual(DATA["availability_zone"], obj.availability_zone)
        self.assertEqual(DATA["extendparam"], obj.extendparam)
        self.assertEqual(DATA["OS-EXT-STS:task_state"], obj.OS_EXT_STS_task_state)
        self.assertEqual(DATA["OS-SRV-USG:terminated_at"], obj.OS_SRV_USG_terminated_at)
        self.assertEqual(DATA["OS-EXT-SRV-ATTR:reservation_id"], obj.OS_EXT_SRV_ATTR_reservation_id)

