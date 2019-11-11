# -*- coding:utf-8 -*-

import datetime
from openstack import connection
from openstack import utils

# Query Metric Data
def list_metric_aggregations(connection):
    query = {
        "namespace": "MINE.APP",
        "metric_name": "cpu_util",
        "from": utils.get_epoch_time(five_min_ago),
        "to": utils.get_epoch_time(now),
        "period": 300,
        "filter": "average",
        "dimensions": [{
            "name": "instance_id",
            "value": "33328f02-3814-422e-b688-bfdba93d4050"
        }]
    }
    for aggregation in connection.cloud_eye.metric_aggregations(**query):
        print(aggregation)

# Post Metric Data
def add_metric_data(connection):
    data = [
        {
            "metric": {
                "namespace": "MINE.APP",
                "dimensions": [
                    {
                        "name": "instance_id",
                        "value": "33328f02-3814-422e-b688-bfdba93d4050"
                    }
                ],
                "metric_name": "cpu_util"
            },
            "ttl": 172800,
            "collect_time": utils.get_epoch_time(five_min_ago),
            "value": 60,
            "unit": "%"
        },
        {
            "metric": {
                "namespace": "MINE.APP",
                "dimensions": [
                    {
                        "name": "instance_id",
                        "value": "33328f02-3814-422e-b688-bfdba93d4050"
                    }
                ],
                "metric_name": "cpu_util"
            },
            "ttl": 172800,
            "collect_time": utils.get_epoch_time(now),
            "value": 70,
            "unit": "%"
        }
    ]
    connection.cloud_eye.add_metric_data(data)


if __name__ == "__main__":
    now = datetime.datetime.now()
    five_min_ago = now - datetime.timedelta(minutes=5)

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

    add_metric_data(conn)
    list_metric_aggregations(conn)