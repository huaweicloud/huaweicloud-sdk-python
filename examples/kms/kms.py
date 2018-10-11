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

"""
Managing key by KMS

"""


def keys(conn):
    print("List encript keys")
    for k in conn.kms.keys():
        print(conn.kms.describe_key(k))


def create_key(conn):
    key_dict = {
        "key_alias": "test-key-123-456789223",
        "realm": "cn-north-1eu-deaaa"
    }
    key = conn.kms.create_key(**key_dict)
    print(key)


def enable_key(conn, key):
    # a string of key id or an object of Key
    print(conn.kms.enable_key(key))


def disable_key(conn, key):
    # a string of key id or an object of Key
    print(conn.kms.disable_key(key))


def delete_key(conn, key):
    # a string of key id or an object of Key
    print(conn.kms.schedule_deletion_key(key, 7))


def cancel_delete_key(conn, key):
    # a string of key id or an object of Key
    print(conn.kms.cancel_deletion_key(key))


def create_random(conn):
    print(conn.kms.gen_random(random_data_length=512))


def create_data_key(conn, key):
    # a string of key id or an object of Key
    data_key_dict = {
        "datakey_length": "512"
    }
    print(conn.kms.create_datakey(key, **data_key_dict))

    print(conn.kms.create_datakey_wo_plain(key, **data_key_dict))


def encrypt_datakey(conn, key):
    params = {
        "plain_text": "fooofofoofofofofoofofoffofoofo",
        "datakey_plain_length": "64"
    }
    datakey = conn.kms.encrypt_datakey(key, **params)
    print(datakey)
    params = {
        "datakey_cipher_length": "64"
    }
    print(conn.kms.decrypt_datakey(datakey, **params))


def get_instance_number(conn):
    print(conn.kms.get_instance_number())


def list_quota(conn):
    for q in conn.kms.get_quota():
        print(q)
