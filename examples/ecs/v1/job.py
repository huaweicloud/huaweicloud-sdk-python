import sys

from openstack import connection
from openstack import utils

utils.enable_logging(debug=True, stream=sys.stdout)

# create connection
username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # endpoint url

conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)


def get_job():
    data = {
        "reboot": {
            "type": "SOFT",
            "servers": [
                {
                    "id": "3ba7bd88-9c49-44ee-b4d4-a776d6dffad5"
                },
                {
                    "id": "3e0fe563-6dbe-43f9-8b38-dbca1fc1c9dd"
                }
            ]
        }
    }
    ff = conn.ecs.reboot_server(**data)
    job = conn.ecs.get_job(ff.job_id)
    print(job)


if __name__ == "__main__":
    get_job()



