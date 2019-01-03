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


def test_create_health_check():
    ls_id = "5c3e9a7ed7a54347a443a1cc76e4fd02"
    health_check = {
        "listener_id": ls_id,
        "healthcheck_protocol": "HTTP",
        "healthcheck_connect_port": 80,
        "healthcheck_interval": 5,
        "healthcheck_timeout": 10,
        "healthcheck_uri": "/",
        "healthy_threshold": 3,
        "unhealthy_threshold": 3
    }
    healthcheck = conn.load_balancer.create_health_check(**health_check)
    return healthcheck


def test_get_health_check(health_check_id):
    print(conn.load_balancer.get_health_check(health_check_id))


def test_update_health_check(health_check_id):
    update = {
        "healthcheck_connect_port": 88,
        "healthcheck_interval": 10
    }
    health_check = conn.load_balancer.update_health_check(health_check_id,
                                                          **update)
    return health_check


def test_delete_health_check(health_check_id):
    return conn.load_balancer.delete_health_check(health_check_id)


if __name__ == "__main__":
    health_check = test_create_health_check()
    test_get_health_check(health_check.id)
    test_update_health_check(health_check.id)
    test_delete_health_check(health_check.id)