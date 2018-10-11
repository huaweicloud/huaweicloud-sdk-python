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

import hashlib
import mock

from openstack.kms.v1 import _proxy
from openstack.tests.unit import test_proxy_base2


PLAIN_TEXT = "00000000000000000000000000000000000000000000000000000000000000" \
             "00000000000000000000000000000000000000000000000000000000000000" \
             "0000F5A5FD42D16A20302798EF6ED309979B43003D2320D9F0E8EA9831A927" \
             "59FB4B"


class TestKMSProxy(test_proxy_base2.TestProxyBase):
    def setUp(self):
        super(TestKMSProxy, self).setUp()
        self.proxy = _proxy.Proxy(self.session)

    def test_create_key(self):
        self._verify2('openstack.kms.v1.key.Key.create',
                      self.proxy.create_key,
                      method_args=[],
                      expected_args=[mock.ANY],
                      expected_kwargs={})

    def test_descrirbe_key(self):
        self._verify2('openstack.kms.v1.key.Key.describe',
                      self.proxy.describe_key,
                      method_args=['key'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'key_id': 'key'})

    def test_keys(self):
        self._verify2('openstack.kms.v1.key.Key.list',
                      self.proxy.keys,
                      method_args=[],
                      expected_args=[mock.ANY],
                      expected_kwargs={})

    def test_enable_key(self):
        self._verify2('openstack.kms.v1.key.Key.enable',
                      self.proxy.enable_key,
                      method_args=['key'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'key_id': 'key'})

    def test_disable_key(self):
        self._verify2('openstack.kms.v1.key.Key.disable',
                      self.proxy.disable_key,
                      method_args=['key'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'key_id': 'key'})

    def test_schedule_deletion_key(self):
        self._verify2('openstack.kms.v1.key.Key.schedule_deletion',
                      self.proxy.schedule_deletion_key,
                      method_args=['key', 7],
                      expected_args=[mock.ANY],
                      expected_kwargs={'key_id': 'key',
                                       'pending_days': 7})

    def test_cancel_deletion_key(self):
        self._verify2('openstack.kms.v1.key.Key.cancel_deletion',
                      self.proxy.cancel_deletion_key,
                      method_args=['key'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'key_id': 'key'})

    def test_create_datakey(self):
        self._verify2('openstack.kms.v1.key.DataKey.create_data_key',
                      self.proxy.create_datakey,
                      method_args=['key'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'key_id': 'key'})

    def test_create_datakey_wo_plain(self):
        self._verify2('openstack.kms.v1.key.DataKey.create_data_key_wo_plain',
                      self.proxy.create_datakey_wo_plain,
                      method_args=['key'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'key_id': 'key'})

    def test_encrypt_datakey(self):

        plain_text = PLAIN_TEXT
        hash = hashlib.sha256()
        hex_data = str(PLAIN_TEXT).decode("hex")
        hash.update(bytearray(hex_data))
        digest = hash.hexdigest()
        self._verify2('openstack.kms.v1.key.DataKey.encrypt',
                      self.proxy.encrypt_datakey,
                      method_args=['key'],
                      method_kwargs={'plain_text': PLAIN_TEXT},
                      expected_args=[mock.ANY],
                      expected_kwargs={'key_id': 'key',
                                       'plain_text': plain_text + digest})

    def test_decrypt_datakey(self):
        self._verify2('openstack.kms.v1.key.DataKey.decrypt',
                      self.proxy.decrypt_datakey,
                      method_args=['key'],
                      expected_args=[mock.ANY],
                      expected_kwargs={'key_id': 'key'})

    def test_gen_random(self):
        self._verify2('openstack.kms.v1.key.Random.get',
                      self.proxy.gen_random,
                      method_args=[],
                      expected_args=[mock.ANY],
                      expected_kwargs={})

    def test_get_instance_number(self):
        self._verify2('openstack.kms.v1.key.InstanceNumber.get',
                      self.proxy.get_instance_number,
                      method_args=[],
                      expected_args=[mock.ANY],
                      expected_kwargs={})

    def test_get_quota(self):
        self._verify2('openstack.kms.v1.key.Quota.list',
                      self.proxy.get_quota,
                      method_args=[],
                      expected_args=[mock.ANY],
                      expected_kwargs={})
