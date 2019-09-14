# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.  You may obtain a copy
# of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.

from keystoneauth1 import session

from openstack.resource2 import Body
from openstack.resource2 import Resource

# Default root url for the openstack metadata apis.
OPENSTACK_METADATA_ROOT = "/openstack/latest"
# Default root url for the metadata apis compatible with EC2.
EC2_METADATA_ROOT = "/latest/meta-data"

# Default endpoint for the ECS Instance Metadata Service.
ECS_METADATA_SERIVCE_URL = "http://169.254.169.254"


class ECSMetadataUtils(object):
    """Utility class for retrieving ECS instance metadata.

    Examples:
        ECSMetadataUtils.get_instance_type()
        ECSMetadataUtils.get_security_key().security_token
    """

    @classmethod
    def get_security_key(cls):
        """Get the temporary security credentials of the instance.

        Returns the temporary security credentials (access, secret,
        securitytoken, and expires_at) associated with the IAM roles on
        the instance."""
        return cls.get_resource(SecurityKey,
                                OPENSTACK_METADATA_ROOT + "/securitykey")

    @classmethod
    def get_instance_type(cls):
        """Get the type of the instance."""
        return cls.get_resource(str.__class__,
                                EC2_METADATA_ROOT + "/instance-type")

    @classmethod
    def get_resource(cls, resource_class, url):
        """Get resource and return contents from metadata service.
         :param resource_class: The type of resource to get.
         :param url: URL of request.
        """
        session_obj = session.Session()
        resp = session_obj.get(url, endpoint_override=ECS_METADATA_SERIVCE_URL)
        if issubclass(resource_class, Resource):
            response_json = resp.json()
            resource_json = Resource.find_value_by_accessor(
                response_json, resource_class.resource_key)
            resource = resource_class.existing(**resource_json)
        else:
            resource = resp.text
        return resource


class SecurityKey(Resource):
    """The temporary security credentials associated with the IAM role."""

    resource_key = "credential"

    #: access of security key
    access = Body('access')
    #: secret of security key
    secret = Body('secret')
    #: security token of security key
    security_token = Body('securitytoken')
    #: expires_at of security key
    expires_at = Body('expires_at')
