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

from openstack.kms import kms_service
from openstack import resource2 as resource
from openstack import utils


class KmsResource(resource.Resource):
    base_path = '/kms'
    service = kms_service.KMSService()

    def _post(self, session, action, **kwargs):
        url = utils.urljoin(self.base_path, action)

        body = kwargs
        if self.id is not None:
            body.update({
                'key_id': self.key_id})

        headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
            "Content-Length": str(len(str(body)))
        }

        endpoint_override = self.service.get_endpoint_override()
        resp = session.post(url, endpoint_filter=self.service,
                            endpoint_override=endpoint_override,
                            json=body,
                            headers=headers)

        resp = resp.json()
        for k in ['error', 'key_info']:
            if k in resp:
                resp = resp[k]
                self._body.attributes.update(resp)
                return self

        self._body.attributes.update(resp)
        # need this?
        self._body.clean()
        return self


class Key(KmsResource):

    # Properties
    #: Secret key ID
    key_id = resource.Body('key_id', alternate_id=True)
    #: User domain name
    domain_name = resource.Body('domain_name')
    #: User domain id
    domain_id = resource.Body('domain_id')
    #: Secret key alias
    key_alias = resource.Body('key_alias')
    #: Secret area
    realm = resource.Body('realm')
    #: Secret key description
    key_description = resource.Body('key_description')
    #: Secret key creation date
    creation_date = resource.Body('creation_date')
    #: Scheduled deletion time
    scheduled_deletion_date = resource.Body('scheduled_deletion_date')
    #: Key state. (2, enabled; 3, disabled; 4: sheduled deleted)
    key_state = resource.Body('key_state')
    #: Default key flag. (default 1 else 0)
    default_key_flag = resource.Body('default_key_flag')
    #: Secret key type.
    key_type = resource.Body('key_type')
    #: Error code when create a secret key
    error_code = resource.Body('error_code')
    #: Error message when create a secret key
    error_msg = resource.Body('error_msg')

    def create(self, session, **kwargs):
        return self._post(session, 'create-key', **kwargs)

    def describe(self, session, **kwargs):
        return self._post(session, 'describe-key', **kwargs)

    def enable(self, session, **kwargs):
        return self._post(session, 'enable-key', **kwargs)

    def disable(self, session, **kwargs):
        return self._post(session, 'disable-key', **kwargs)

    def schedule_deletion(self, session, **kwargs):
        return self._post(session, 'schedule-key-deletion', **kwargs)

    def cancel_deletion(self, session, **kwargs):
        return self._post(session, 'cancel-key-deletion', **kwargs)

    @classmethod
    def list(cls, session, paginated=False, **kwargs):
        url = utils.urljoin(cls.base_path, 'list-keys')
        body = kwargs

        more_data = True

        endpoint_override = cls.service.get_endpoint_override()

        while more_data:
            headers = {
                "Accept": "application/json",
                "Content-type": "application/json",
                "Content-Length": str(len(str(body)))
            }

            resp = session.post(url, endpoint_filter=cls.service,
                                endpoint_override=endpoint_override,
                                json=body,
                                headers=headers)

            resp = resp.json()

            if not resp:
                more_data = False
                return

            if 'error' in resp:
                more_data = False
                return

            if 'keys' in resp:
                for val in resp['keys']:
                    data = {'key_id': val}
                    value = cls.existing(**data)
                    yield value

            if 'truncated' in resp:
                if resp['truncated'] == 'false':
                    more_data = False

            if 'next_marker' in resp:
                if resp['next_marker'] != "":
                    body['marker'] = resp['next_marker']


class DataKey(KmsResource):

    # Properties
    #: Secret key ID
    key_id = resource.Body('key_id', alternate_id=True)
    #: Encryption context
    encryption_context = resource.URI('encryption_context')
    #: Datakey length
    datakey_length = resource.Body('datakey_length')
    #: Sequence
    sequence = resource.Body('sequence')
    #: Plain text of the data key
    plain_text = resource.Body('plain_text')
    #: Cipher text of the data key
    cipher_text = resource.Body('cipher_text')
    #: Error code when create a secret key
    error_code = resource.Body('error_code')
    #: Error message when create a secret key
    error_msg = resource.Body('error_msg')

    def create_data_key(self, session, **kwargs):
        return self._post(session,
                          'create-datakey',
                          **kwargs)

    def create_data_key_wo_plain(self, session, **kwargs):
        return self._post(session,
                          'create-datakey-without-plaintext',
                          **kwargs)

    def encrypt(self, session, **params):
        return self._post(session, 'encrypt-datakey', **params)

    def decrypt(self, session, **params):

        if self.cipher_text is not None:
            params.update({
                'cipher_text': self.cipher_text})
        return self._post(session, 'decrypt-datakey', **params)


class Random(KmsResource):

    # Properties
    #: Random data length
    random_data_length = resource.Body('random_data_length')
    #: Random data content
    random_data = resource.Body('random_data')
    #: Error code when create a secret key
    error_code = resource.Body('error_code')
    #: Error message when create a secret key
    error_msg = resource.Body('error_msg')

    def get(self, session, **params):
        return self._post(session, "gen-random", **params)


class InstanceNumber(KmsResource):

    base_path = 'kms/user-instances'
    allow_get = True
    # Properties
    #: Instance number
    #: *Type: int*
    instance_num = resource.Body('instance_num', type=int)
    #: Error code get instance number
    error_code = resource.Body('error_code')
    #: Error message when get instance number
    error_msg = resource.Body('error_msg')

    def get(self, session):
        return super(InstanceNumber, self).get(session, requires_id=False)


class Quota(KmsResource):

    # Properties

    # Resource type
    type = resource.Body('type')
    #: Used resource
    #: *Type: int*
    used = resource.Body('used', type=int)
    #: Quota number for this kind of resource
    #: *Type: int*
    quota = resource.Body('quota', type=int)
    #: Error code
    error_code = resource.Body('error_code')
    #: Error message
    error_msg = resource.Body('error_msg')

    @classmethod
    def list(cls, session):
        url = utils.urljoin(cls.base_path, 'user-quotas')
        endpoint_override = cls.service.get_endpoint_override()
        headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
        }
        resp = session.get(url, endpoint_filter=cls.service,
                           endpoint_override=endpoint_override,
                           headers=headers)
        resp = resp.json()
        if 'error' in resp:
            return
        resources = resp['quotas']['resources']
        for r in resources:
            value = cls.existing(**r)
            yield value
