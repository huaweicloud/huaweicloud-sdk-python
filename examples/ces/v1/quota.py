# -*- coding:utf-8 -*-

from openstack import connection

# Query Resource Quota
def list_quotas(connection):
    quotas = connection.cloud_eye.quotas()
    for quota in quotas:
        print(quota)


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
    list_quotas(conn)