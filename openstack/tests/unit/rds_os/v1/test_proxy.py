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

from openstack.rds_os.v1 import _proxy
from openstack.rds_os.v1 import configuration as _configuration
from openstack.rds_os.v1 import flavor as _flavor
from openstack.rds_os.v1 import instance as _instance
from openstack.tests.unit import test_proxy_base2


class TestRDSOSProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestRDSOSProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

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
        self._verify2('openstack.rds_os.v1.instance.Instance.resize',
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
        self._verify2('openstack.rds_os.v1.instance.Instance.resize_volume',
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
        self._verify2('openstack.rds_os.v1.instance.Instance.restart',
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
        self._verify2('openstack.rds_os.v1.instance.Instance.restore',
                      self.proxy.restore_instance,
                      method_args=[inst_id, 'backupRef'],
                      expected_args=[mock.ANY, 'backupRef'],
                      expected_kwargs={})
        mock_find.assert_called_once_with(mock.ANY, inst_id,
                                          ignore_missing=False)

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

    def test_get_instance_default_configuration(self):
        self._verify2('openstack.proxy2.BaseProxy._get',
                      self.proxy.get_instance_default_configuration,
                      method_args=["inst"],
                      expected_args=[mock.ANY],
                      expected_kwargs={'instanceId': 'inst',
                                       'requires_id': False})

    def test_list_configuration_group(self):
        self.verify_list(self.proxy.list_configuration_group,
                         _configuration.Configurations)

    def test_get_configuration_group(self):
        self.verify_get(self.proxy.get_configuration_group,
                        _configuration.Configurations)

    def test_delete_configuration_group(self):
        self.verify_delete(self.proxy.delete_configuration_group,
                           _configuration.Configurations, True)

    def test_update_configuration_group(self):
        self.verify_update(self.proxy.update_configuration_group,
                           _configuration.Configurations)

    @mock.patch.object(_configuration.Configurations, 'find')
    def test_patch_configuration_group(self, mock_find):
        cg_id = '1234'
        cg = _configuration.Configurations(id=cg_id)
        mock_find.return_value = cg
        self._verify2('openstack.rds_os.v1.configuration.Configurations.patch',
                      self.proxy.patch_configuration_group,
                      method_args=[cg_id],
                      expected_args=[mock.ANY],
                      expected_kwargs={})
        mock_find.assert_called_once_with(mock.ANY, cg_id,
                                          ignore_missing=False)

    @mock.patch.object(_configuration.Configurations, 'find')
    def test_get_configuration_group_associated_instances(self, mock_find):
        cg_id = '1234'
        cg = _configuration.Configurations(id=cg_id)
        mock_find.return_value = cg
        self._verify2(
            'openstack.rds_os.v1.configuration.Configurations.'
            'get_associated_instances',
            self.proxy.get_configuration_group_associated_instances,
            method_args=[cg_id],
            expected_args=[mock.ANY],
            expected_kwargs={})
        mock_find.assert_called_once_with(mock.ANY, cg_id,
                                          ignore_missing=False)
