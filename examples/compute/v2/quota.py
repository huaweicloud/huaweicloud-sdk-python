# -*-coding:utf-8 -*-

from openstack import connection

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


# get tenant quota limits
def get_limits():
    quota_limit = conn.compute.get_limits()
    print (quota_limit)
    print ("absolute:", quota_limit.absolute)


# get tenant quota
def query_quota(project_id):
    quota = conn.compute.query_quota(project_id)
    print ("project id is: ", quota.id)


# get default quota
def query_quota_default(project_id):
    quota_default = conn.compute.query_quota_default(project_id)
    print ("project id is: ", quota_default.id)


if __name__ == "__main__":
    project_id = "project_id"
    get_limits()
    query_quota(project_id)
    query_quota_default(project_id)