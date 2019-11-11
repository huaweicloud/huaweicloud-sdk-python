# -*- coding:utf-8 -*-

from openstack import connection

# Query Metric Information
def list_metrics(connection):
    query = {
        "namespace": "SYS.ECS",
        "metric_name": "disk_read_bytes_rate",
        "start": "SYS.ECS.cpu_util.instance_id:d9112af5-6913-4f3b-bd0a-3f96711e004d",
        "limit": 50,
        "order": "desc"
    }

    for metric in connection.cloud_eye.metrics(**query):
        print(metric)


if __name__ == "__main__":
    # create connection
    username = "xxxxxxxxxxxxxx"
    password = "xxxxxxxxxxxx"
    projectId = "xxxxxxxxxxxxxxxxxxxxxx"  # tenant ID
    userDomainId = "xxxxxxxxxxxxxxx"  # user account ID
    auth_url = "xxxxxxxxxxxxxxxxxxxxxx"  # endpoint url
    conn = connection.Connection(auth_url=auth_url,
                                 user_domain_id=userDomainId,
                                 project_id=projectId,
                                 username=username,
                                 password=password)
    list_metrics(conn)