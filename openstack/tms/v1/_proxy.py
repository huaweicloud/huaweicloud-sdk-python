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

from openstack import proxy2
from openstack.tms.v1 import predefine_tag as _tag

class Proxy(proxy2.BaseProxy):
    def create_predefine_tag(self, **attrs):
        """create a predefine_tag.
        """
        return self._create(_tag.PredefineTagAction, **attrs)

    def list_predefine_tags(self, **query):
        """list predefine_tags.
        """
        return self._get(_tag.PredefineTag, **query)

    def update_predefine_tag(self, **attrs):
        """Update a predefine_tag.
        """
        return self._update(_tag.PredefineTag, **attrs)