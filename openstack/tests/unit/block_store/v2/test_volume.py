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
from openstack.block_store.v2 import volume

VOLUMEDETAIL = {
    "attachments": [],
    "availability_zone": "xxx",
    "bootable": False,
    "consistencygroup_id": None,
    "created_at": "2016-05-25T02:38:40.392463",
    "description": "create for api test",
    "encrypted": False,
    "id": "8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
    "links": [{
        "href": "https://volume.localdomain.com:8776/v2/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
        "rel": "self"
    }, {
        "href": "https://volume.localdomain.com:8776/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
        "rel": "bookmark"
    }
    ],
    "metadata": {
        "volume_owner": "openapi"
    },
    "name": "openapi_vol01",
    "replication_status": "disabled",
    "size": 40,
    "snapshot_id": None,
    "source_volid": None,
    "status": "creating",
    "updated_at": None,
    "user_id": "39f6696ae23740708d0f358a253c2637",
    "volume_type": "SATA",
    "shareable": True,
    "multiattach": True,
    "OS-SCH-HNT:scheduler_hints": {"test": "test"},
    "os-vol-host-attr:host": "host",
    "os-vol-tenant-attr:tenant_id": "os-vol-tenant-attr:tenant_id",
    "os-vol-mig-status-attr:migstat": "os-vol-mig-status-attr:migstat",
    "os-vol-mig-status-attr:name_id": "os-vol-mig-status-attr:name_id",
    "os-volume-replication:extended_status": "os-volume-replication:extended_status",
    "volume_image_metadata": {},
    "volumes_links": [{
        "href": "https://volume.localdomain.com:8776/v2/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
        "rel": "self"
    }, {
        "href": "https://volume.localdomain.com:8776/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
        "rel": "bookmark"
    }],
    "code": "evs",
    "message": "dddd"
}

VOLUME = {
    "imageRef": "test",
    "source_replica": "test",
    "OS-SCH-HNT:scheduler_hints": {},
    "attachments": [],
    "availability_zone": "xxx",
    "bootable": False,
    "consistencygroup_id": None,
    "created_at": "2016-05-25T02:38:40.392463",
    "description": "create for api test",
    "encrypted": False,
    "id": "8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
    "links": [{
        "href": "https://volume.localdomain.com:8776/v2/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
        "rel": "self"
    }, {
        "href": "https://volume.localdomain.com:8776/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66",
        "rel": "bookmark"
    }
    ],
    "metadata": {
        "volume_owner": "openapi"
    },
    "name": "openapi_vol01",
    "replication_status": "disabled",
    "size": 40,
    "snapshot_id": None,
    "source_volid": None,
    "status": "creating",
    "updated_at": None,
    "user_id": "39f6696ae23740708d0f358a253c2637",
    "volume_type": "SATA",
    "shareable": True,
    "multiattach": True,
    "os-vol-host-attr:host": "host",
    "os-vol-tenant-attr:tenant_id": "os-vol-tenant-attr:tenant_id",
    "os-vol-mig-status-attr:migstat": "os-vol-mig-status-attr:migstat",
    "os-vol-mig-status-attr:name_id": "os-vol-mig-status-attr:name_id",
    "os-volume-replication:extended_status": "os-volume-replication:extended_status",
    "volume_image_metadata": {},
    "code": "evs",
    "message": "dddd",
}


class TestVolume(testtools.TestCase):
    def test_basic(self):
        sot = volume.Volume()
        self.assertEqual("volume", sot.resource_key)
        self.assertEqual("volumes", sot.resources_key)
        self.assertEqual("/volumes", sot.base_path)
        self.assertEqual("volume", sot.service.service_type)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

        self.assertDictEqual({
            "limit": "limit",
            "marker": "marker",
            "all_tenants": "all_tenants",
            'name': "name",
            'status': "status",
            'project_id': "project_id",
            "sort_key": "sort_key",
            "offset": "offset",
            "availability_zone": "availability_zone",
            "change-since": "change-since",
            "metadata_alias": "metadata",
            "sort_dir": "desc",
            },
            sot._query_mapping._mapping)

    def test_create(self):
        sot = volume.Volume(**VOLUME)
        self.assertEqual(VOLUME["OS-SCH-HNT:scheduler_hints"], sot.scheduler_hints)
        self.assertEqual(VOLUME["source_replica"], sot.source_replica)
        self.assertEqual(VOLUME["imageRef"], sot.imageRef)
        self.assertEqual(VOLUME["created_at"], sot.created_at)
        self.assertEqual(VOLUME["consistencygroup_id"], sot.consistencygroup_id)
        self.assertEqual(VOLUME["bootable"], sot.is_bootable)
        self.assertEqual(VOLUME["availability_zone"], sot.availability_zone)
        self.assertEqual(VOLUME["attachments"], sot.attachments)
        self.assertEqual(VOLUME["updated_at"], sot.updated_at)
        self.assertEqual(VOLUME["description"], sot.description)
        self.assertEqual(VOLUME["encrypted"], sot.encrypted)
        self.assertEqual(VOLUME["id"], sot.id)
        self.assertEqual(VOLUME["links"], sot.links)
        self.assertEqual(VOLUME["metadata"], sot.metadata)
        self.assertEqual(VOLUME["name"], sot.name)
        self.assertEqual(VOLUME["replication_status"], sot.replication_status)
        self.assertEqual(VOLUME["size"], sot.size)
        self.assertEqual(VOLUME["snapshot_id"], sot.snapshot_id)
        self.assertEqual(VOLUME["source_volid"], sot.source_volume_id)
        self.assertEqual(VOLUME["status"], sot.status)
        self.assertEqual(VOLUME["updated_at"], sot.updated_at)
        self.assertEqual(VOLUME["user_id"], sot.user_id)
        self.assertEqual(VOLUME["volume_type"], sot.volume_type)
        self.assertEqual(VOLUME["shareable"], sot.shareable)
        self.assertEqual(VOLUME["multiattach"], sot.multiattach)
        self.assertEqual(VOLUME["os-vol-host-attr:host"], sot.host)
        self.assertEqual(VOLUME["os-vol-tenant-attr:tenant_id"], sot.tenant_id)
        self.assertEqual(VOLUME["os-vol-mig-status-attr:migstat"], sot.migstat)
        self.assertEqual(VOLUME["os-vol-mig-status-attr:name_id"], sot.name_id)
        self.assertEqual(VOLUME["os-volume-replication:extended_status"], sot.extended_status)
        self.assertEqual(VOLUME["volume_image_metadata"], sot.volume_image_metadata)
        self.assertEqual(VOLUME["code"], sot.code)
        self.assertEqual(VOLUME["message"], sot.message)


class TestVolumeDetail(testtools.TestCase):
    def test_basic(self):
        sot = volume.VolumeDetail()
        self.assertIsInstance(sot, volume.Volume)
        self.assertEqual("/volumes/detail", sot.base_path)

    def test_create(self):
        sot = volume.VolumeDetail(**VOLUMEDETAIL)
        self.assertEqual(VOLUMEDETAIL["volumes_links"], sot.volumes_links)
