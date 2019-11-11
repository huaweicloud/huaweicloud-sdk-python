# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack import service_filter


class RDSService(service_filter.ServiceFilter):
    """The RDS service."""

    valid_versions = [service_filter.ValidVersion('v1')]

    def __init__(self, version=None):
        """Create a RDS service."""
        super(RDSService, self).__init__(
            service_type='rdsv1',
            version=version,
            requires_project_id=True,
        )


class RDSServiceV3(service_filter.ServiceFilter):
    """The RDS  v3 service."""

    valid_versions = [service_filter.ValidVersion('v3')]

    def __init__(self, version=None):
        """Create a RDS service."""
        super(RDSServiceV3, self).__init__(
            service_type='rdsv3',
            version=version,
            requires_project_id=True,
        )

    def get_service_module(self):
        # Note: This value will be used as the attribute name in connection
        # for the _proxy instance. We need to override the method to avoid
        # the conflict with rds version v3.
        return 'rdsv3'