from openstack.bss import bss_service
from openstack import resource2 as resource


class Version(resource.Resource):
    resource_key = 'version'
    resources_key = 'versions'
    base_path = '/'
    service = bss_service.BssService(
        version=bss_service.BssService.UNVERSIONED
    )

    # capabilities
    allow_list = True

    # Properties
    links = resource.Body('links')
    status = resource.Body('status')
