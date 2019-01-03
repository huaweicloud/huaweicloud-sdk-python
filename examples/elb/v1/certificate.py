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


def test_create_cert():
    cert={
        "name": "sdk-test-cert",
        "certificate":"***",
        "private_key":"***"
    }
    certification = conn.load_balancer.create_certificate(**cert)
    return certification


def test_get_certs():
    certs = list(conn.load_balancer.certificates())
    print(len(certs))
    print(certs)


def test_update_cert(cert_id):
    update = {
        "description": "cert update test"
    }
    cert = conn.load_balancer.update_certificate(cert_id, **update)
    return cert


def test_delete_cert(cert_id):
    conn.load_balancer.delete_certificate(cert_id)


if __name__ == "__main__":
    cert = test_create_cert()
    test_get_certs()
    test_update_cert(cert.id)
    test_delete_cert(cert.id)