#!/usr/bin/env python
# coding=utf-8
from openstack import connection

# create connection
username = "replace-with-your-username"
password = "replace-with-your-password"
projectId = "replace-with-your-project-id"
userDomainId = "replace-with-your-user-domain-id"
auth_url = "https://iam.example.com/v3"
conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


def list_metrics():
    query = {
        "namespace": "SYS.ECS",
        "metric_name": "cpu_util",
        "limit": 1
    }
    metrics = conn.cloud_eye.metrics(**query)
    for metric in metrics:
        print(metric)


if __name__ == "__main__":
    list_metrics()
