import yaml
from openstack import connection


username = "xxxxxx"
password = "xxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"           # tenant ID
userDomainId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"        # user account ID
auth_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"            # endpoint url

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


# create stack
def stack_create(conn):
    template_file = "server.yaml"

    with open(template_file) as fd:
        template_str = fd.read()
        template = yaml.load(template_str, Loader=yaml.BaseLoader)

        parameters = {
            'name': 'server-demo',
            'availability_zone': 'eu-de-01',
            'key_name': 'KeyPair-c39b',
            'image': '6d20bfd7-449d-401a-9758-5cebd5135b83',
            'flavor': 's2.medium.1',
            'network': '8511d35a-24b3-44f1-9723-b8e827a728ac'
        }

        data = {
            'stack_name': 'server-xl',
            'template': template,
            'parameters': parameters
        }
        stack = conn.orchestration.create_stack(**data)
        print stack
        conn.orchestration.wait_for_status(
            stack, status='CREATE_COMPLETE', failures=['CREATE_FAILED']
        )

        return stack.id


# get list of stack
def stack_list(conn):
    stacks = conn.orchestration.stacks()
    for stack in stacks:
        print stack


# find a stack by id or name
def stack_find(conn, stack_id_or_name):

    stack = conn.orchestration.find_stack(stack_id_or_name)
    print stack


# get a stack by id or name
def stack_get(conn, stack_id_or_name):

    stack = conn.orchestration.get_stack(stack_id_or_name)
    print stack


# update stack
def stack_update(conn, stack_id):

    template_file = "server.yaml"

    with open(template_file) as fd:
        template_str = fd.read()
        template = yaml.load(template_str, Loader=yaml.BaseLoader)
        parameters = {
            'name': 'server-update',
            'key_name': 'KeyPair-c39b',
            'image': '6d20bfd7-449d-401a-9758-5cebd5135b83',
            'flavor': 's2.medium.1',
            'network': '8511d35a-24b3-44f1-9723-b8e827a728ac'
        }
        data = {
            'template': template,
            'parameters': parameters
        }
        stack = conn.orchestration.update_stack(stack_id, **data)
        print stack
        conn.orchestration.wait_for_status(
            stack, status='UPDATE_COMPLETE', failures=['CREATE_FAILED']
        )


# check stack
def stack_check(conn, stack_id_or_name):

    conn.orchestration.check_stack(stack_id_or_name)


# delete stack
def stack_delete(conn, stack_id_or_name):

    conn.orchestration.delete_stack(stack_id_or_name)


# list resources of stack
def stack_resources(conn, stack_id_or_name):

    resources = conn.orchestration.resources(stack_id_or_name)
    for res in resources:
        print res


if __name__ == '__main__':
    stack_list(conn)
    stack_id = stack_create(conn)
    stack_update(conn, stack_id)
    stack_check(conn, stack_id)
    stack_resources(conn, stack_id)
    stack_find(conn, stack_id)
    stack_get(conn, stack_id)
    stack_delete(conn, stack_id)
