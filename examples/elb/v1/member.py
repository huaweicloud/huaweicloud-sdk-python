#!/usr/bin/python
#coding=utf-8


from openstack import connection


username = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"
projectId = "xxxxxxxxxxx"
userDomainId = "xxxxxxxxxx"
auth_url = "xxxxxxxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


def test_create_member():
    _member = {
        "listener_id": "5c3e9a7ed7a54347a443a1cc76e4fd02",
        "server_id": "89de9d1e-37f9-423e-8f90-21c73156a769",
        "address": "192.168.0.143"
    }
    member = conn.load_balancer.create_member(**_member)
    return member


def test_get_members():
    members = list(conn.load_balancer.get_member())
    print(len(members))
    print(members)


def test_delete_member(member_id):
    return conn.load_balancer.delete_member(member_id)


if __name__ == "__main__":
    member=test_create_member()
    test_get_members()
    test_delete_member(member.id)