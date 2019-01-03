import yaml
from openstack import connection

username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"     # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"      # endpoint url

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


# create software deployment
def software_deployment_create(conn):
    template_file = "deployment.yaml"

    with open(template_file) as fd:
        template_str = fd.read()
        template = yaml.load(template_str, Loader=yaml.BaseLoader)
        props = template['resources']['dep_test']['properties']
        data = {
            'action': props['actions'],
            'config_id': props['config_id'],
            'server_id': props['server_id']
        }
        deployment = conn.orchestration.create_software_deployment(**data)
        print deployment
        conn.orchestration.wait_for_status(
            deployment, status='CREATE_COMPLETE', failures=['CREATE_FAILED']
        )
        return deployment.id


# get software deployment
def software_deployment_get(conn, deployment_id):
    deployment = conn.orchestration.get_software_deployment(deployment_id)
    print deployment


# get list of software deployment
def software_deployment_list(conn):
    deployments = conn.orchestration.software_deployments()
    for deployment in deployments:
        print deployment


# delete software deployment
def software_deployment_delete(conn, deployment_id):
    conn.orchestration.delete_software_deployment(deployment_id)


# update software deployment
def software_deployment_update(conn, deployment_id):
    template_file = "deployment.yaml"

    with open(template_file) as fd:
        template_str = fd.read()
        template = yaml.load(template_str, Loader=yaml.BaseLoader)
        props = template['resources']['dep_test']['properties']
        data = {
            'action': props['actions'],
            'config_id': props['config_id'],
            'server_id': props['server_id']
        }
        deployment = conn.orchestration.update_software_deployment(
            deployment_id, **data)
        print deployment


if __name__ == '__main__':
    software_deployment_list(conn)
    deployment_id = software_deployment_create(conn)
    software_deployment_get(conn, deployment_id)
    software_deployment_update(conn, deployment_id)
    software_deployment_delete(conn, deployment_id)
