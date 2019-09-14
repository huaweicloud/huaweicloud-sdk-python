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

import copy
from openstack.fgs.v2 import functions as _function
from openstack.fgs.v2 import triggers as _trigger
from openstack import proxy2


class Proxy(proxy2.BaseProxy):
    def functions(self, **attrs):
        """Querying a Function List"""
        return self._list(_function.Function, paginated=True, **attrs)

    def get_function_metadata(self, function_urn):
        """Querying the Metadata Information of a Function
        :param function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
                               :class:`~openstack.fgs.v2.functions.FunctionMetadata`
        :returns: A generator of Function (:class:`~openstack.fgs.v2.functions.FunctionMetadata`)
                  instances
        """
        return self._get(_function.FunctionMetadata, requires_id=False, function_urn=function_urn)

    def get_function_code(self, function_urn):
        """Querying the Code of a Function
        :param function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
                               :class:`~openstack.fgs.v2.functions.FunctionCode`
        :returns: A generator of Function (:class:`~openstack.fgs.v2.functions.FunctionCode`)
                  instances
        """
        return self._get(_function.FunctionCode, requires_id=False, function_urn=function_urn)

    def create_function(self, **attrs):
        """
        This API is used to create a function.
        :param attrs: data to create function see more info from support website
        :return: :class:`~openstack.fgs.v2.functions.Functions`
        """
        return self._create(_function.Function, prepend_key=False, **attrs)

    def delete_function(self, function_urn):
        """Deleting a Function or Function Version
        :param function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
                               :class:`~openstack.fgs.v2.functions.FunctionExpansion`
        :returns: ``None``
        """
        return self._delete(_function.FunctionExpansion, function_urn=function_urn)

    def update_function_code(self, function_urn, **attrs):
        """
        Modifying the Code of a Function
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :param  attrs: data to create function see more info from support website
        :return: :class:`~openstack.fgs.v2.functions.FunctionCode`
        """
        return self._update(_function.FunctionCode, function_urn=function_urn, **attrs)

    def update_function_metadata(self, function_urn, **attrs):
        """
        Modifying the Metadata Information of a Function
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :param  attrs: data to create function see more info from support website
        :return: :class:`~openstack.fgs.v2.functions.FunctionMetadata`
        """
        return self._update(_function.FunctionMetadata, function_urn=function_urn, **attrs)

    def publish_function_version(self, function_urn, **attrs):
        """
        Publishing a Function Version
        :param function_urn:
        :param  attrs: data to create function see more info from support website
        :return: :class:`~openstack.fgs.v2.functions.FunctionVersion`
        """
        return self._create(_function.FunctionVersion, function_urn=function_urn, **attrs)

    def get_function_version(self, function_urn, **attrs):
        """Querying the Versions of a Function
        :param function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
                               :class:`~openstack.fgs.v2.functions.FunctionVersion`
        :param  attrs: data to create function see more info from support website
        :returns: A generator of Function (:class:`~openstack.fgs.v2.functions.FunctionVersion`)
                  instances
        """
        return self._list(_function.FunctionVersion, paginated=True, function_urn=function_urn, **attrs)

    def create_function_aliase(self, function_urn, **attrs):
        """
        Creating an Alias for a Function Version
        :param function_urn:
        :param  attrs: data to create function see more info from support website
        :return: :class:`~openstack.fgs.v2.functions.FunctionAliase`
        """
        return self._create(_function.FunctionAliase, function_urn=function_urn, **attrs)

    def update_function_aliase(self, function_urn, alias_name, **attrs):
        """
        Modifying the Alias Information of a Function Version
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :param  alias_name: The alias of function
        :param  attrs: data to create function see more info from support website
        :return: :class:`~openstack.fgs.v2.functions.FunctionAliaseExpansion`
        """
        return self._update(_function.FunctionAliaseExpansion, function_urn=function_urn, alias_name=alias_name,
                            **attrs)

    def delete_function_aliase(self, function_urn, alias_name):
        """Deleting an Alias of a Function Version
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :param  alias_name: The alias of function
                               :class:`~openstack.fgs.v2.functions.FunctionAliaseExpansion`
        :returns: ``None``
        """
        return self._delete(_function.FunctionAliaseExpansion, function_urn=function_urn, alias_name=alias_name)

    def get_function_aliase(self, function_urn, alias_name):
        """
        Querying the Alias Information of a Function Version
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :param  alias_name: The alias of function
        :return: :class:`~openstack.fgs.v2.functions.FunctionAliaseExpansion`
        """
        return self._get(_function.FunctionAliaseExpansion, requires_id=False, function_urn=function_urn,
                         alias_name=alias_name)

    def function_aliases(self, function_urn, **function):
        """
        Querying the Aliases of All Versions of a Function
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :return: :class:`~openstack.fgs.v2.functions.FunctionAliase
        """
        return self._list(_function.FunctionAliase, function_urn=function_urn, paginated=False, **function)

    def execute_function_synchronously(self, function_urn, **attrs):
        """
        Executing a Function Synchronously
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :param  attrs: usedata
        :return: :class:`~openstack.fgs.v2.functions.FunctionInvocations
        """
        req_body = copy.deepcopy(attrs)
        attrs["function_urn"] = function_urn
        res = _function.FunctionInvocations.new(**attrs)
        return res.create(self._session, prepend_key=False, **req_body)

    def execute_function_asynchronously(self, function_urn, **attrs):
        """
       Executing a Function Asynchronously
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :return: :class:`~openstack.fgs.v2.functions.FunctionInvocationsAsync
        """
        req_body = copy.deepcopy(attrs)
        attrs["function_urn"] = function_urn
        res = _function.FunctionInvocationsAsync.new(**attrs)
        return res.create(self._session, prepend_key=False, **req_body)

    def create_trigger(self, function_urn, **attrs):
        """
        This API is used to create a trigger.
        :param function_urn:
        :param attrs: data to create trigger see more info from support website
        :return: :class:`~openstack.fgs.v2.triggers.Trigger`
        """
        return self._create(_trigger.Trigger, prepend_key=False, function_urn=function_urn, **attrs)

    def get_trigger(self, function_urn, trigger_type_code, trigger_id):
        """
        Querying the Information About a Trigger
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :param  trigger_type_code: Trigger type. Options: SMN, DMS, OBS, DIS, APIG, TIMER, LTS, and CTS.
        :param  trigger_id: Trigger ID.
        :return: :class:`~openstack.fgs.v2.triggers.TriggerExpansion`
        """
        attrs = {
            "function_urn": function_urn,
            "tg_type": trigger_type_code,
            "tg_id": trigger_id
        }
        return self._get(_trigger.TriggerExpansion, requires_id=False, **attrs)

    def triggers(self, function_urn, **attrs):
        """
       Querying All Triggers of a Function
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :return: :class:`~openstack.fgs.v2.triggers.Trigger`
        """
        return self._list(_trigger.Trigger, function_urn=function_urn, paginated=False, **attrs)

    def delete_trigger(self, function_urn, trigger_type_code, trigger_id):
        """Deleting a Trigger
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :param  trigger_type_code: Trigger type. Options: SMN, DMS, OBS, DIS, APIG, TIMER, LTS, and CTS.
        :param  trigger_id: Trigger ID.
        :returns: ``None``
        """
        attrs = {
            "function_urn": function_urn,
            "tg_type": trigger_type_code,
            "tg_id": trigger_id
        }
        return self._delete(_trigger.TriggerExpansion, **attrs)

    def delete_all_triggers(self, function_urn):
        """Deleting All Triggers of a Function
        :param  function_urn: Uniform Resource Name (URN) used to uniquely identify a function.
        :returns: ``None``
        """
        return self._delete(_trigger.Trigger, function_urn=function_urn)
