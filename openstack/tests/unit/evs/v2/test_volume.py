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
from openstack.evs.v2 import volume

DATA = {
        "attachments": [ ],
        "links": [
            {
                "href": "https://volume.az0.dc1.domainname.com/v2/40acc331ac784f34842ba4f08ff2be48/volumes/591ac654-26d8-41be-bb77-4f90699d2d41",
                "rel": "self"
            },
            {
                "href": "https://volume.az0.dc1.domainname.com/40acc331ac784f34842ba4f08ff2be48/volumes/591ac654-26d8-41be-bb77-4f90699d2d41",
                "rel": "bookmark"
            }
        ],
        "availability_zone": "az1.dc1",
        "os-vol-host-attr:host": "az1.dc1#SSD",
        "encrypted": False,
        "multiattach": True,
        "updated_at": "2016-02-03T02:19:29.895237",
        "replication_status": "disabled",
        "snapshot_id": None,
        "id": "591ac654-26d8-41be-bb77-4f90699d2d41",
        "size": 40,
        "user_id": "fd03ee73295e45478d88e15263d2ee4e",
        "os-vol-tenant-attr:tenant_id": "40acc331ac784f34842ba4f08ff2be48",
        "volume_image_metadata": {},
        "os-vol-mig-status-attr:migstat": None,
        "metadata": {
            "__openstack_region_name": "az1.dc1",
            "quantityGB": "40"
        },
        "tags": {
            "key1": "value1",
            "key2": "value2"
        },
        "status": "error_restoring",
        "description": "auto-created_from_restore_from_backup",
        "source_volid": None,
        "consistencygroup_id": None,
        "os-vol-mig-status-attr:name_id": None,
        "name": "restore_backup_0115efb3-678c-4a9e-bff6-d3cd278238b9",
        "bootable": "false",
        "created_at": "2016-02-03T02:19:11.723797",
        "volume_type": None,
        "service_type": "EVS",
        "dedicated_storage_id": None,
        "dedicated_storage_name": None,
        "wwn": " 688860300000d136fa16f48f05992360",
        "job_id": "123",
        "shareable": True,
        "message": "test",
        "code":100,
        "backup_id": "test",
        "imageRef":"test",
        "count": 1,
        "enterprise_project_id": "test",
        "volumes_links": [],
}


class TestVolume(testtools.TestCase):
    def test_basic(self):
        obj = volume.Volume()
        self.assertEqual("/cloudvolumes",obj.base_path)
        self.assertEqual("volume", obj.resource_key)
        self.assertTrue(obj.allow_create)
        self.assertTrue(obj.allow_update)
        self.assertTrue(obj.allow_get)

    def test_make_it(self):
        obj=volume.Volume(**DATA)
        self.assertEqual(DATA["id"], obj.id)
        self.assertEqual(DATA["attachments"], obj.attachments)
        self.assertEqual(DATA["links"], obj.links)
        self.assertEqual(DATA["availability_zone"], obj.availability_zone)
        self.assertEqual(DATA["os-vol-host-attr:host"], obj.host)
        self.assertEqual(DATA["encrypted"], obj.encrypted)
        self.assertEqual(DATA["multiattach"], obj.multiattach)
        self.assertEqual(DATA["updated_at"], obj.updated_at)
        self.assertEqual(DATA["replication_status"], obj.replica_status)
        self.assertEqual(DATA["snapshot_id"], obj.snapshot_id)
        self.assertEqual(DATA["size"], obj.size)
        self.assertEqual(DATA["user_id"], obj.user_id)
        self.assertEqual(DATA["os-vol-tenant-attr:tenant_id"], obj.attr_tenant_id)
        self.assertEqual(DATA["volume_image_metadata"], obj.volume_image_metadata)
        self.assertEqual(DATA["os-vol-mig-status-attr:migstat"], obj.migstat)
        self.assertEqual(DATA["metadata"], obj.metadata)
        self.assertEqual(DATA["tags"], obj.tags)
        self.assertEqual(DATA["status"], obj.status)
        self.assertEqual(DATA["description"], obj.description)
        self.assertEqual(DATA["source_volid"], obj.source_volid)
        self.assertEqual(DATA["name"], obj.name)
        self.assertEqual(DATA["bootable"], obj.bootable)
        self.assertEqual(DATA["created_at"], obj.created_at)
        self.assertEqual(DATA["volume_type"], obj.volume_type)
        self.assertEqual(DATA["service_type"], obj.service_type)
        self.assertEqual(DATA["dedicated_storage_id"], obj.dedicated_storage_id)
        self.assertEqual(DATA["dedicated_storage_name"], obj.dedicated_storage_name)
        self.assertEqual(DATA["wwn"], obj.wwn)
        self.assertEqual(DATA["job_id"], obj.job_id)
        self.assertEqual(DATA["shareable"], obj.shareable)
        self.assertEqual(DATA["message"], obj.message)
        self.assertEqual(DATA["code"], obj.code)
        self.assertEqual(DATA["enterprise_project_id"], obj.enterprise_project_id)
        self.assertEqual(DATA["count"], obj.count)
        self.assertEqual(DATA["backup_id"], obj.backup_id)
        self.assertEqual(DATA["volumes_links"], obj.volumes_links)


