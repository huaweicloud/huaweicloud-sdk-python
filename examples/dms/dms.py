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
Managing dms

"""


def create_queue(conn):
    queue_dict = {
        'name': "queue001",
        'description': 'test1'
    }

    q = conn.dms.create_queue(**queue_dict)
    print(q)

    print("list queues")
    for qs in conn.dms.queues():
        print(qs)

    print("get queue")
    getq = conn.dms.get_queue(q)
    print(getq)


def create_delete_groups(conn, queue):
    print("create groups on queue %s", queue)
    groups = {
        "groups": [
            {
                "name": "aaaxjjjacccc"
            },
            {
                "name": "dddeeessfff"
            }

        ]
    }
    print(conn.dms.create_groups(queue, **groups))

    for g in conn.dms.groups(queue):
        print(g)
        conn.dms.delete_group(queue, g)


def create_message(conn, queue):
    print("send message on a queue %s", queue)
    msg_dict = {
        "messages": [
            {
                "body": "TEST11",
                "attributes":
                {
                    "attribute1": "value1",
                    "attribute2": "value2"
                }
            },
            {
                "body":
                {
                    "foo": "test02"
                },
                "attributes":
                {
                    "attribute1": "value1",
                    "attribute2": "value2"
                }
            }
        ]
    }
    print(conn.dms.send_messages(queue, **msg_dict))


def consume_message(conn, queue):

    print("delete groups for queue %s", queue)
    for g in conn.dms.groups(queue):
        print(g)
        conn.dms.delete_group(queue, g)

    groups = {
        "groups": [
            {
                "name": "aaaxjjjacccc"
            },
            {
                "name": "dddeeessfff"
            }

        ]
    }

    grp = conn.dms.create_groups(queue, **groups)

    for cm in conn.dms.consume_message(queue, grp[0].id):
        print("ack consumed message")
        print(conn.dms.ack_consumed_message(cm))


# Consume message by tag list in queue and group
def consume_message_with_tags(conn, qui, gid):
    qid = '673f8fca-9aa1-4974-8fc5-b0eb1c5f9724'
    # gid = 'g-a826e437-2e67-46c7-b220-63836b5bb463'
    params = {
        'max_msgs': 10,
        'time_wait': 30,
        'tags': ['tag1', 'tag2'],
        'tag_type': 'or'
    }

    for c in conn.dms.consume_message(qid, gid, **params):
        print(c)


def get_quotas(conn):

    for q in conn.dms.quotas():
        print(q)
        print(q.type)
        print(q.quota)
        print(q.used)
