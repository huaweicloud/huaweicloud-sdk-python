from openstack.bssintl import bss_intl_service
from openstack import resource2 as resource


class Version(resource.Resource):
    resource_key = 'version'
    resources_key = 'versions'
    base_path = '/'
    service = bss_intl_service.BssIntlService(
        version=bss_intl_service.BssIntlService.UNVERSIONED
    )

    # capabilities
    allow_list = True

    # Properties
    links = resource.Body('links')
    status = resource.Body('status')
