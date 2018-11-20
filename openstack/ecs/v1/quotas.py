# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
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

from openstack import resource2
from openstack.ecs import ecs_service


class Quota(resource2.Resource):
    resource_key = "absolute"
    base_path = "/cloudservers/limits"
    service = ecs_service.EcsService()

    allow_get = True

    # Maximum number of cloud server applications
    maxtotalinstances = resource2.Body("maxTotalInstances", type=int)
    # CPU core maximum number of applications
    maxtotalcores = resource2.Body("maxTotalCores", type=int)
    # Maximum memory application capacity Unit: MB
    maxtotalramsize = resource2.Body("maxTotalRAMSize", type=int)
    # The maximum number of SSH key pairs that can be applied
    maxtotalkeypairs = resource2.Body("maxTotalKeypairs", type=int)
    # The maximum length of metadata that can be entered
    maxservermeta = resource2.Body("maxServerMeta", type=int)
    # The maximum number of files that can be injected
    maxpersonality = resource2.Body("maxPersonality", type=int)
    # Maximum length of injected file content Unit: Byte
    maxpersonalitysize = resource2.Body("maxPersonalitySize", type=int)
    # The maximum number of server groups
    maxservergroups = resource2.Body("maxServerGroups", type=int)
    # Maximum number of elastic cloud servers in the server group
    maxservergroupmembers = resource2.Body("maxServerGroupMembers", type=int)
    # Number of server groups used
    totalservergroupsused = resource2.Body("totalServerGroupsUsed", type=int)
    # The maximum number of security groups used.
    # Description:
    # The specific quota limit is subject to the VPC quota limit.
    maxsecuritygroups = resource2.Body("maxSecurityGroups", type=int)
    # The maximum number of configurations of security group rules in a security group.
    # Description:
    # The specific quota limit is subject to the VPC quota limit.
    maxsecuritygrouprules = resource2.Body("maxSecurityGroupRules", type=int)
    # The maximum number of floating IPs used
    maxtotalfloatingips = resource2.Body("maxTotalFloatingIps", type=int)
    # Maximum length of mirrored metadata
    maximagemeta = resource2.Body("maxImageMeta", type=int)
    # Current cloud server usage
    totalinstancesused = resource2.Body("totalInstancesUsed", type=int)
    # The number of CPU cores currently used
    totalcoresused = resource2.Body("totalCoresUsed", type=int)
    # Current memory usage unit: MB
    totalramused = resource2.Body("totalRAMUsed", type=int)
    # Current security group usage
    totalsecuritygroupsused = resource2.Body("totalSecurityGroupsUsed", type=int)
    # Current floating IP usage
    totalfloatingipsused = resource2.Body("totalFloatingIpsUsed", type=int)