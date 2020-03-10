from openstack import connection
from openstack.rds.v3 import instance as _instance
from openstack.rds.v3.rdsresource import ErrorResponse


projectId = "xxxxxxxxxxxxxx"
cloud = "xxxxxxxxxxxxxx"   # cdn use: cloud = "myhwclouds.com"
region = "xxxxxxxxxxxxxx"    # example: region = "cn-north-1"
AK = "xxxxxxxxxxxxxx"
SK = "xxxxxxxxxxxxxx"
conn = connection.Connection(
              project_id=projectId,
              cloud=cloud,
              region=region,
              ak=AK,
              sk=SK)


def datastore_versions(conn):
    for version in conn.rdsv3.datastore_versions('mysql'):
        print(version)


def flavors(conn):
    query = {
         'database_name': 'mysql',
         'version_name': '5.6'
    }
    for flavor in conn.rdsv3.flavors(**query):
        print(flavor)


def instances(conn):
    query = {
        'offset': 0,
        'limit': 100
    }
    for instance in conn.rdsv3.instances(**query):
        print(instance)


def create_instance(conn):

    ha_instance = {
        "name": "Test",
        "region": "cn-north-4",
        "availability_zone": "cn-north-4b,cn-north-4b",
        "datastore": {
            "type": "MySQL",
            "version": "5.7"
        },
        "ha": {
            "mode": "Ha",
            "replication_mode": "semisync"
        },
        "port":"8645",
        "password": "YourDBS_234",
        "flavor_ref": "rds.mysql.s1.medium.ha",
        "volume": {
            "type": "ULTRAHIGH",
            "size": 40
        },
        "backup_strategy": {
            "start_time": "09:00-10:00",
            "keep_days": 1
        }
    }

    single_instance = {
        "name": "Test",
        "region": "cn-north-4",
        "availability_zone": "cn-north-4a",
        "datastore": {
            "type": "MySQL",
            "version": "5.7"
        },
        "password": "YourDBS_234",
        "flavor_ref": "rds.mysql.s1.large",
        "volume": {
            "type": "ULTRAHIGH",
            "size": 40
        },
        "backup_strategy": {
            "start_time": "09:00-10:00",
            "keep_days": 1
        }
    }

    ro_instance = {
        "name": "Test",
        "replica_of_id": "replica_of_id",
        "flavor_ref": "rds.mysql.s1.medium.rr",
        "volume": {
            "type": "ULTRAHIGH",
            "size": 40
        },
        "region": "cn-north-4",
        "availability_zone": "cn-north-4a",
    }
    result = conn.rdsv3.create_instance(**single_instance)
    if isinstance(result, ErrorResponse):
        output_error_response(result)
    else:
        print(result.job_id)


def resize_instance(conn):
    flavor_ref = 'rds.mysql.m1.large'
    instance = _instance.Instance()
    instance.id = "instanceId"
    result = conn.rdsv3.resize_instance(instance, flavor_ref)
    if isinstance(result, ErrorResponse):
        output_error_response(result)
    else:
        print(result.job_id)


def resize_instance_volume(conn):
    size = '50'
    instance = _instance.Instance()
    instance.id = "instanceId"
    print(conn.rdsv3.resize_instance_volume(instance, size))


def restart_instance(conn):
    instance = _instance.Instance()
    instance.id = "instanceId"
    print(conn.rdsv3.restart_instance(instance))


def single_to_ha(conn):
    instance = _instance.Instance()
    instance.id = "instanceId"
    single_to_ha_param = {
        "new_az_code": "cn-north-4a",
    }
    print(conn.rdsv3.single_to_ha(instance, **single_to_ha_param))


def output_error_response(response):
    print("Error Code: %s" % response.error_code)
    print("Error Message: %s" % response.error_msg)
