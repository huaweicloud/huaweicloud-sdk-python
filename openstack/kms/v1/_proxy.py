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

import hashlib

from openstack.kms.v1 import key as _key
from openstack import proxy2


class Proxy(proxy2.BaseProxy):

    def create_key(self, **kwargs):
        """Create a encrypt key for encrypt a data key

        :param dict kwargs: Keyword arguments which will be used to overwrite a
                            :class:`~openstack.kms.v1.key.Key`
        :rtype: :class:`~openstack.kms.v1.key.Key`
        """
        key_obj = _key.Key.new(**kwargs)
        return key_obj.create(self._session, **kwargs)

    def describe_key(self, key, **kwargs):
        """Describe a encrypt key by given key id or key object

        :param key: key id or an instance of :class:`~openstack.kms.v1.key.Key`
        :param dict kwargs: Keyword arguments which will be used to describe
                            the key. e.g. sequence
        :rtype: :class:`~openstack.kms.v1.key.Key`
        """
        if isinstance(key, _key.Key):
            key_obj = key
        else:
            kwargs.update({"key_id": key})
            key_obj = _key.Key.new(**kwargs)

        return key_obj.describe(self._session, **kwargs)

    def keys(self, **query):
        """List all keys.

        :param dict kwargs: Keyword arguments which will be used to list keys.
                            limit, marker, sequence are allowed.

        """
        return _key.Key.list(self._session, **query)

    def enable_key(self, key, **params):
        """Enable a key

        :param key: key id or an instance of :class:`~openstack.kms.v1.key.Key`
        :param dict kwargs: Keyword arguments which will be used to enable key.
                            sequence is allowed.
        :rtype: :class:`~openstack.kms.v1.key.Key`
        """

        if isinstance(key, _key.Key):
            key_obj = key
        else:
            params.update({"key_id": key})
            key_obj = _key.Key.new(**params)

        return key_obj.enable(self._session, **params)

    def disable_key(self, key, **params):
        """Disable a key

        :param key: key id or an instance of :class:`~openstack.kms.v1.key.Key`
        :param dict kwargs: Keyword arguments which will be used to disable
                            key. sequence is allowed.
        :rtype: :class:`~openstack.kms.v1.key.Key`
        """

        if isinstance(key, _key.Key):
            key_obj = key
        else:
            params.update({"key_id": key})
            key_obj = _key.Key.new(**params)

        return key_obj.disable(self._session, **params)

    def schedule_deletion_key(self, key, pending_days, **params):
        """Schedule a key deletion

        :param key: key id or an instance of :class:`~openstack.kms.v1.key.Key`
        :param pending_days: Pending days before deletion, allow 7 to 1096
        :param dict kwargs: Keyword arguments which will be used to schedule a
                            key deletion. sequence is allowed.
        :rtype: :class:`~openstack.kms.v1.key.Key`
        """

        params.update({'pending_days': pending_days})
        if isinstance(key, _key.Key):
            key_obj = key
        else:
            params.update({"key_id": key})
            key_obj = _key.Key.new(**params)

        return key_obj.schedule_deletion(self._session, **params)

    def cancel_deletion_key(self, key, **params):
        """Cancel a key deletion

        :param key: key id or an instance of :class:`~openstack.kms.v1.key.Key`
        :param dict kwargs: Keyword arguments which will be used to schedule a
                            key deletion. sequence is allowed.
        :rtype: :class:`~openstack.kms.v1.key.Key`
        """

        if isinstance(key, _key.Key):
            key_obj = key
        else:
            params.update({"key_id": key})
            key_obj = _key.Key.new(**params)

        return key_obj.cancel_deletion(self._session, **params)

    def create_datakey(self, key, **params):
        """Create a data key

        :param key: key id or an instance of :class:`~openstack.kms.v1.key.Key`
        :param dict kwargs: Keyword arguments which will be used to create a
                            Data key, datakey_length is required,
                            encryption_context, sequence are optional.
        :rtype: :class:`~openstack.kms.v1.key.DataKey`
        """

        key_id = key
        if isinstance(key, _key.Key):
            key_id = key.key_id

        params.update({'key_id': key_id})
        data_key_obj = _key.DataKey.new()
        return data_key_obj.create_data_key(self._session, **params)

    def create_datakey_wo_plain(self, key, **params):
        """Create a data key without plain text

        :param key: key id or an instance of :class:`~openstack.kms.v1.key.Key`
        :param dict kwargs: Keyword arguments which will be used to create a
                            Data key, datakey_length is required,
                            encryption_context, sequence are optional.
        :rtype: :class:`~openstack.kms.v1.key.DataKey`
        """

        key_id = key
        if isinstance(key, _key.Key):
            key_id = key.key_id

        params.update({'key_id': key_id})
        data_key_obj = _key.DataKey.new()
        return data_key_obj.create_data_key_wo_plain(self._session, **params)

    def encrypt_datakey(self, datakey, **params):
        """Encrypt a data key

        :param datakey: key id or an instance of
                        :class:`~openstack.kms.v1.key.DataKey`
        :param dict kwargs: Keyword arguments which will be used to encrypt a
                            Data key, encryption_context, plain_text,
                            datakey_plain_length are required,
                            encryption_context, sequence are optional.
        :rtype: :class:`~openstack.kms.v1.key.DataKey`
        """

        data_key_obj = datakey

        if not isinstance(datakey, _key.DataKey):
            params.update({'key_id': datakey})
            data_key_obj = _key.DataKey.new(**params)

        plain_text = params.get("plain_text")
        if plain_text is None:
            raise ValueError("plain_text should be provided")
        # user provids plain text, do hash inside sdk
        hash = hashlib.sha256()
        hex_data = str(plain_text).decode("hex")
        hash.update(bytearray(hex_data))
        digest = hash.hexdigest()
        params.update({'plain_text': plain_text + digest})

        return data_key_obj.encrypt(self._session, **params)

    def decrypt_datakey(self, datakey, **params):
        """Decrypt a data key

        :param datakey: key id or an instance of
                        :class:`~openstack.kms.v1.key.DataKey`
        :param dict kwargs: Keyword arguments which will be used to decrypt a
                            Data key, cipher_text, datakey_cipher_length are
                            required, encryption_context, sequence are
                            optional.
        :rtype: :class:`~openstack.kms.v1.key.DataKey`
        """

        data_key_obj = datakey

        if not isinstance(datakey, _key.DataKey):
            params.update({'key_id': datakey})
            data_key_obj = _key.DataKey.new(**params)

        return data_key_obj.decrypt(self._session, **params)

    def gen_random(self, **params):
        """Generate random number

        :param dict kwargs: Keyword arguments which will be used to decrypt a
                            Data key, cipher_text, datakey_cipher_length are
                            required, encryption_context, sequence are
                            optional.
        :rtype: :class:`~openstack.kms.v1.key.Random`
        """
        random_obj = _key.Random.new(**params)
        return random_obj.get(self._session, **params)

    def get_instance_number(self):
        """Get encrpt key instance total number

        :rtype: :class:`~openstack.kms.v1.key.InstanceNumber`
        """
        instance_num_obj = _key.InstanceNumber()
        return instance_num_obj.get(self._session)

    def get_quota(self):
        """List quota resources for KMS service

        :returns: A generator of Quota object
        :rtype: :class:`~openstack.kms.v1.key.Quota`
        """
        return _key.Quota.list(self._session)
