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


def test_create_listener():
    listener = {
        "name": "test_listener",
        "loadbalancer_id": "49ab5b7be5d745d39e22a28fd58e3426",
        "protocol": "HTTP",
        "port": "80",
        "backend_protocol": "HTTP",
        "backend_port": "8080",
        "lb_algorithm": "roundrobin",
        "is_session_sticky": True,
        "sticky_session_type": "insert",
        "cookie_timeout": 60
    }
    ls = conn.load_balancer.create_listener(**listener)
    return ls


def test_get_listener(ls_id):
    return conn.load_balancer.get_listener(ls_id)


def test_get_listeners():
    listeners = list(conn.load_balancer.listeners())
    print(len(listeners))
    print(listeners)


def test_update_listener(ls_id):
    update = {
        "description": "listener update test",
        "port": 800
    }
    ls = conn.load_balancer.update_listener(ls_id, **update)
    return ls


def test_delete_listener(ls_id):
    return conn.load_balancer.delete_listener(ls_id)


if __name__ == "__main__":
    ls = test_create_listener()
    test_get_listener(ls.id)
    test_get_listeners()
    ls_update = test_update_listener(ls.id)
    test_delete_listener(ls.id)