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


# create software config
def software_config_create(conn):
    template_file = "config.yaml"

    with open(template_file) as fd:
        template_str = fd.read()
        template = yaml.load(template_str, Loader=yaml.BaseLoader)
        props = template['resources']['config_test']['properties']
        data = {
            'config': props['config'],
            'group': props['group'],
            'name': 'test_config'
        }

        config = conn.orchestration.create_software_config(**data)
        conn.orchestration.wait_for_status(
            config, status='CREATE_COMPLETE', failures=['CREATE_FAILED']
        )
        return config.id


# get software config
def software_config_get(conn, config_id):
    config = conn.orchestration.get_software_config(config_id)
    print config


# delete software config
def software_config_delete(conn, config_id):
    config = conn.orchestration.delete_software_config(config_id)
    print config


# get list of software config
def software_config_list(conn):
    configs = conn.orchestration.software_configs()
    for config in configs:
        print config


if __name__ == '__main__':
    software_config_list(conn)
    config_id = software_config_create(conn)
    software_config_get(conn, config_id)
    software_config_delete(conn, config_id)
