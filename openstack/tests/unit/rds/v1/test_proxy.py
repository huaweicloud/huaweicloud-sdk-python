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

import mock

from openstack.rds.v1 import _proxy
from openstack.rds.v1 import backup as _backup
from openstack.rds.v1 import flavor as _flavor
from openstack.rds.v1 import instance as _instance
from openstack.tests.unit import test_proxy_base2


class TestRDSProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestRDSProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_datastore_versions(self):
        self._verify2('openstack.proxy2.BaseProxy._list',
                      self.proxy.datastore_versions,
                      method_args=["dbname"],
                      expected_args=[mock.ANY],
                      expected_kwargs={'paginated': False,
                                       'datastore_name': 'dbname'})

    def test_instances(self):
        self.verify_list(self.proxy.instances, _instance.Instance)

    def test_get_instance(self):
        self.verify_get(self.proxy.get_instance, _instance.Instance)

    def test_delete_instance(self):
        self.verify_delete(self.proxy.delete_instance,
                           _instance.Instance, True)

    def test_create_instance(self):
        self.verify_create(self.proxy.create_instance, _instance.Instance)

    @mock.patch.object(_instance.Instance, 'find')
    def test_resize_instance(self, mock_find):
        inst_id = '1234'
        inst = _instance.Instance(id=inst_id)
        mock_find.return_value = inst
        self._verify2('openstack.rds.v1.instance.Instance.resize',
                      self.proxy.resize_instance,
                      method_args=[inst_id, 'flavorRef'],
                      expected_args=[mock.ANY, 'flavorRef'],
                      expected_kwargs={})
        mock_find.assert_called_once_with(mock.ANY, inst_id,
                                          ignore_missing=False)

    @mock.patch.object(_instance.Instance, 'find')
    def test_resize_instance_volume(self, mock_find):
        inst_id = '1234'
        inst = _instance.Instance(id=inst_id)
        mock_find.return_value = inst
        self._verify2('openstack.rds.v1.instance.Instance.resize_volume',
                      self.proxy.resize_instance_volume,
                      method_args=[inst_id, 10],
                      expected_args=[mock.ANY, 10],
                      expected_kwargs={})
        mock_find.assert_called_once_with(mock.ANY, inst_id,
                                          ignore_missing=False)

    @mock.patch.object(_instance.Instance, 'find')
    def test_restart_instance(self, mock_find):
        inst_id = '1234'
        inst = _instance.Instance(id=inst_id)
        mock_find.return_value = inst
        self._verify2('openstack.rds.v1.instance.Instance.restart',
                      self.proxy.restart_instance,
                      method_args=[inst_id],
                      expected_args=[mock.ANY],
                      expected_kwargs={})
        mock_find.assert_called_once_with(mock.ANY, inst_id,
                                          ignore_missing=False)

    @mock.patch.object(_instance.Instance, 'find')
    def test_restore_instance(self, mock_find):
        inst_id = '1234'
        inst = _instance.Instance(id=inst_id)
        mock_find.return_value = inst
        self._verify2('openstack.rds.v1.instance.Instance.restore',
                      self.proxy.restore_instance,
                      method_args=[inst_id, 'backupRef'],
                      expected_args=[mock.ANY, 'backupRef'],
                      expected_kwargs={})
        mock_find.assert_called_once_with(mock.ANY, inst_id,
                                          ignore_missing=False)

    def test_set_instance_params(self):
        self._verify2(
            'openstack.rds.v1.instance.InstanceParameter.set_params',
            self.proxy.set_instance_params,
            method_args=['inst'],
            expected_args=[mock.ANY],
            expected_kwargs={'instanceId': 'inst'})

    def test_reset_instance_params(self):
        self._verify2(
            'openstack.rds.v1.instance.InstanceParameter.reset_params',
            self.proxy.reset_instance_params,
            method_args=['inst'],
            expected_args=[mock.ANY],
            expected_kwargs={'instanceId': 'inst'})

    def test_list_instance_errorlog(self):
        self._verify2('openstack.proxy2.BaseProxy._list',
                      self.proxy.list_instance_errorlog,
                      method_args=['inst'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'instanceId': 'inst'})

    def test_list_instance_slowlog(self):
        self._verify2('openstack.proxy2.BaseProxy._list',
                      self.proxy.list_instance_slowlog,
                      method_args=['inst'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'instanceId': 'inst'})

    def test_flavors(self):
        self._verify2('openstack.proxy2.BaseProxy._list',
                      self.proxy.flavors,
                      method_args=["dbId", 'region'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'dbId': 'dbId',
                                       'region': 'region',
                                       'paginated': False})

    def test_get_flavor(self):
        self.verify_get(self.proxy.get_flavor, _flavor.Flavor)

    def test_backups(self):
        self.verify_list(self.proxy.backups, _backup.Backup)

    def test_create_backup(self):
        self._verify2('openstack.proxy2.BaseProxy._create',
                      self.proxy.create_backup,
                      method_args=["inst", 'name', 'desc'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'instance': 'inst',
                                       'name': 'name',
                                       'description': 'desc'})

    def test_delete_backup(self):
        self.verify_delete(self.proxy.delete_backup, _backup.Backup, True)

    def test_create_backup_policy(self):
        self._verify2('openstack.proxy2.BaseProxy._create',
                      self.proxy.create_backup_policy,
                      method_args=["inst", 9, '11:00:00'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'instanceId': 'inst',
                                       'keepday': 9,
                                       'starttime': '11:00:00'})

    def test_get_backup_policy(self):
        self._verify2('openstack.proxy2.BaseProxy._get',
                      self.proxy.get_backup_policy,
                      method_args=["inst"],
                      expected_args=[mock.ANY],
                      expected_kwargs={'instanceId': 'inst',
                                       'requires_id': False})

    def test_parameters(self):
        self._verify2('openstack.proxy2.BaseProxy._list',
                      self.proxy.parameters,
                      method_args=["datastore"],
                      expected_args=[mock.ANY],
                      expected_kwargs={'datastore_version_id': 'datastore'})

    def test_get_parameter(self):
        self._verify2('openstack.proxy2.BaseProxy._get',
                      self.proxy.get_parameter,
                      method_args=["datastore", 'name'],
                      expected_args=[mock.ANY, 'name'],
                      expected_kwargs={'datastore_version_id': 'datastore'})
