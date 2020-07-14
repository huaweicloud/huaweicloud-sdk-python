from openstack import connection


projectId = "xxxxxxxxxxxxxx"
cloud = "xxxxxxxxxxxxxx"   # cdn use: cloud = "myhwclouds.com"
region = "xxxxxxxxxxxxxx"    # example: region = "cn-north-1"
AK = "xxxxxxxxxxxxxx"
SK = "xxxxxxxxxxxxxx"
connect = connection.Connection(
    project_id=projectId,
    cloud=cloud,
    region=region,
    ak=AK,
    sk=SK)


def databases(conn):
    instance_id = 'xxxxxxxxxxxxxxxxxxxxxxx'
    query = {
        'page': 1,
        'limit': 10
    }
    for database in conn.rdsv3.databases(instance_id, details=True, **query):
        print(database)


def create_database(conn):
    database = {
        "name": 'test_db1',
        "character_set": 'utf8'
    }
    instance_id = 'xxxxxxxxxxxxxxxxxxxxxxx'
    print(conn.rdsv3.create_database(instance_id=instance_id, **database))


def delete_database(conn):
    database_name = 'test_db1'
    instance_id = 'xxxxxxxxxxxxxxxxxxxxxxx'
    print(conn.rdsv3.delete_database(database_name, instance_id))
