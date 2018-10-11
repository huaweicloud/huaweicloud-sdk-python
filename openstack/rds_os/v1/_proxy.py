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

from openstack import proxy2

from openstack.rds_os.v1 import configuration as _configuration
from openstack.rds_os.v1 import datastore as _datastore
from openstack.rds_os.v1 import flavor as _flavor
from openstack.rds_os.v1 import instance as _instance


class Proxy(proxy2.BaseProxy):
    def instances(self):
        """List instances

        :returns: A generator of version object
        :rtype: :class:`~openstack.rds_os.v1.instance.Instance
        """
        return self._list(_instance.Instance, paginated=False)

    def get_instance(self, instance):
        """Get instance by id

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds_os.v1.instance.Instance`.
        :returns: The results of instance
        :rtype: :class:`~openstack.rds_os.v1.instance.Instance`.
        """
        return self._get(_instance.Instance, instance)

    def delete_instance(self, instance, ignore_missing=True):
        """Delete an instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds_os.v1.instance.Instance`.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the instance does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent instance.

        :returns: None
        """
        self._delete(_instance.Instance, instance,
                     ignore_missing=ignore_missing)

    def create_instance(self, **kwargs):
        """Create a new instance from attributes

        :param dict attrs: Keyword arguments which will be used to create
        :returns: The results of instance
        :rtype: :class:`~openstack.rds_os.v1.instance.Instance`.

        """
        return self._create(_instance.Instance, **kwargs)

    def resize_instance(self, instance, flavorRef):
        """Resize an instance by providing flavorRef

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds_os.v1.instance.Instance`.
        :param flavorRef: flavor reference
        :returns: a job id
        :rtype: dict
        """
        if isinstance(instance, _instance.Instance):
            obj = instance
        else:
            obj = self._find(_instance.Instance, instance,
                             ignore_missing=False)

        return obj.resize(self._session, flavorRef)

    def resize_instance_volume(self, instance, size):
        """Resize volume an instance by providing volume size

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds_os.v1.instance.Instance`.
        :param size: new volume size
        :returns: a job id
        :rtype: dict
        """

        if isinstance(instance, _instance.Instance):
            obj = instance
        else:
            obj = self._find(_instance.Instance, instance,
                             ignore_missing=False)

        return obj.resize_volume(self._session, size)

    def restart_instance(self, instance):
        """Resize volume an instance by providing volume size

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds_os.v1.instance.Instance`.
        :param size: new volume size
        :returns: None
        """
        if isinstance(instance, _instance.Instance):
            obj = instance
        else:
            obj = self._find(_instance.Instance, instance,
                             ignore_missing=False)

        return obj.restart(self._session)

    def restore_instance(self, instance, backupRef):
        """Restore an instance by backupRef

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds_os.v1.instance.Instance`.

        :returns: a job id
        :rtype: dict
        """

        if isinstance(instance, _instance.Instance):
            obj = instance
        else:
            obj = self._find(_instance.Instance, instance,
                             ignore_missing=False)

        return obj.restore(self._session, backupRef)

    def flavors(self, dbId, region):
        """List flavors of given datastore id and region

        :param dbId: database store id
        :param region: region

        :returns: A generator of flavor
        :rtype: :class:`~openstack.rds_os.v1.flavor.Flavor
        """
        query = {
            'dbId': dbId,
            'region': region
        }
        return self._list(_flavor.Flavor, paginated=False, **query)

    def get_flavor(self, id):
        """Get the detail of a flavor

        :param id: Flavor id or an object of class
                   :class:`~openstack.rds_os.v1.flavor.Flavor
        :returns: Detail of flavor
        :rtype: :class:`~openstack.rds_os.v1.flavor.Flavor
        """
        return self._get(_flavor.Flavor, id)

    def parameters(self, datastore_version_id):
        """List parameters of a datastore

        :param datastore_id: Id of the datastore version
        :returns: A generator of object Parameter.
        :rtype: :class:`~openstack.rds_os.v1.datastore.Parameter`.
        """
        return self._list(_datastore.Parameter,
                          datastore_version_id=datastore_version_id)

    def get_parameter(self, datastore_version_id, name):
        """Get parameter of a datastore by name

        :param datastore: Id of the datastore version
        :param name: name of the parameter
        :returns: A object of Parameter.
        :rtype: :class:`~openstack.rds_os.v1.datastore.Parameter`.
        """
        return self._get(_datastore.Parameter, name,
                         datastore_version_id=datastore_version_id)

    def get_instance_default_configuration(self, instance):
        """Obtaining Default Parameters of a DB Instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds_os.v1.instance.Instance`.
        :returns: Default Parameters of a DB Instance
        :rtype: :class:`~openstack.rds_os.v1.configuration.Configuration`
        """

        if isinstance(instance, _instance.Instance):
            instanceId = instance.id
        else:
            instanceId = instance

        return self._get(_configuration.Configuration,
                         instanceId=instanceId,
                         requires_id=False)

    def list_configuration_group(self):
        """Obtaining a Parameter Group List

        :returns: A generator of Configurations object
        :rtype: :class:`~openstack.rds_os.v1.configuration.Configurations
        """

        return self._list(_configuration.Configurations,
                          paginated=False)

    def create_configuration_group(self, **kwargs):
        """Creating a Parameter Group

        :param dict \*\*params: Dict to overwrite Configurations object
        :returns: A Parameter Group Object
        :rtype: :class:`~openstack.rds_os.v1.configuration.Configurations`.
        """
        return self._create(_configuration.Configurations, **kwargs)

    def get_configuration_group(self, cg):
        """Obtaining a Parameter Group

        :param cg: The value can be the ID of a Parameter Group or a object of
                   :class:`~openstack.rds_os.v1.configuration.Configurations`.
        :returns: A Parameter Group Object
        :rtype: :class:`~openstack.rds_os.v1.configuration.Configurations`.

        """
        return self._get(_configuration.Configurations, cg)

    def delete_configuration_group(self, cg, ignore_missing=True):
        """Deleting a Parameter Group

        :param cg: The value can be the ID of a Parameter Group or a object of
                   :class:`~openstack.rds_os.v1.configuration.Configurations`.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the Parameter Group does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent Parameter Group.

        :returns: None
        """
        self._delete(_configuration.Configurations, cg,
                     ignore_missing=ignore_missing)

    def update_configuration_group(self, cg, **params):
        """Changing Parameter Information of a Parameter Group

        :param cg: The value can be the ID of a Parameter Group or a object of
                   :class:`~openstack.rds_os.v1.configuration.Configurations`.
        :param dict \*\*params: Dict to overwrite Configurations object
        :returns: A Parameter Group Object
        :rtype: :class:`~openstack.rds_os.v1.configuration.Configurations`.
        """
        return self._update(_configuration.Configurations, cg, **params)

    def patch_configuration_group(self, cg, **params):
        """Adding a Self-defined Parameter

        :param cg: The value can be the ID of a Parameter Group or a object of
                   :class:`~openstack.rds_os.v1.configuration.Configurations`.
        :param dict \*\*params: Dict to use create Self-defined Parameter
        :returns: A Parameter Group Object
        """
        if isinstance(cg, _configuration.Configurations):
            obj = cg
        else:
            obj = self._find(_configuration.Configurations, cg,
                             ignore_missing=False)

        return obj.patch(self._session, **params)

    def get_configuration_group_associated_instances(self, cg):
        """Obtaining the DB Instances Associated with the Parameter Group

        :param cg: The value can be the ID of a Parameter Group or a object of
                   :class:`~openstack.rds_os.v1.configuration.Configurations`.
        :returns: A dict contains a instance list
        :rtype: dict
        """

        if isinstance(cg, _configuration.Configurations):
            obj = cg
        else:
            obj = self._find(_configuration.Configurations, cg,
                             ignore_missing=False)
        return obj.get_associated_instances(self._session)
