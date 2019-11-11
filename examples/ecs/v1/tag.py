# -*-coding:utf-8 -*-
from openstack import connection

# create connection
username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


def create_server_tags(server_id):
    data = {
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    conn.ecs.create_server_tags(server_id, **data)


def delete_server_tags(server_id):
    data = {
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            }
        ]
    }
    conn.ecs.delete_server_tags(server_id, **data)


def get_server_tags(server_id):
    tags = conn.ecs.get_server_tags(server_id)
    for tag in tags:
        print(tag.key, tag.value)


def get_project_tags():
    tags = conn.ecs.get_project_tags()
    for tag in tags:
        print(tag.key, tag.values)


if __name__ == "__main__":
    server_id = "b0a9d2b4-2cae-4b66-a6ba-6af70f3bd7f8"
    create_server_tags(server_id)
    get_server_tags(server_id)
    delete_server_tags(server_id)
    get_project_tags()
