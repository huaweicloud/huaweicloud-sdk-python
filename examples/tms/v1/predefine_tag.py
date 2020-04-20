import sys
import warnings
import os

from openstack import utils
from openstack import connection

username = "*************"
password = '*************'
userDomainId = "*************"
auth_url = "https://iam.xxx.com/v3"  # endpoint url

conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             domain_id=userDomainId,
                             username=username,
                             password=password)

def list_predefine_tags(_conn):
    res = _conn.tms.list_predefine_tags()
    print res

def  update_predefine_tag (_conn):
    data = {
        "new_tag": {
            "key": "test",
            "value": "123122132TTTTTTT"
        },
        "old_tag": {
            "key": 'test1',
            "value": 'value1'
        }
    }
    res = _conn.tms.update_predefine_tag( **data)
    print res

def create_predefine_tag(_conn):
    data = {
        "action": "create",
        "tags": [{
            "key": "test",
            "value": "value2"
        }]
    }
    res = _conn.tms.create_predefine_tag(**data)
    print res

if __name__ == '__main__':
    list_predefine_tags(conn)
    update_predefine_tag(conn)
    create_predefine_tag(conn)