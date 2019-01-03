#!/usr/bin/python
#coding=utf-8


from openstack import connection


username = "xxxxx"
password = "xxxxx"
projectId = "xxxxx"
userDomainId = "xxxx"
auth_url = "xxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


def test_create_lb():
    _lb = {
        "name": "sdk-python-test",
        "vpc_id": "0062814e-fc74-4618-a351-fc32c178ece4",
        "bandwidth": 1,
        "type": "External",
        "is_admin_state_up": True
    }
    lb = conn.load_balancer.create_load_balancer(**_lb)
    return lb


def test_get_lb(lb_id):
    return conn.load_balancer.get_load_balancer(lb_id)


def test_get_all_lb():
    lbs = list(conn.load_balancer.load_balancers())
    print(lbs)


def test_update_lb(lb_id):
    update_lb = {
        "descriotion": "lb-update-test"
    }
    lb = conn.load_balancer.update_load_balancer(lb_id, **update_lb)
    return lb


def test_delete_lb(lb_id):
    return conn.load_balancer.delete_load_balancer(lb_id)


if __name__ == "__main__":
    lb = test_create_lb()
    test_get_lb(lb.id)
    test_get_all_lb()
    test_update_lb(lb.id)
    test_delete_lb(lb.id)