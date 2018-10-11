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
from openstack.rds.v1 import backup as _backup
from openstack.rds.v1 import datastore as _datastore
from openstack.rds.v1 import flavor as _flavor
from openstack.rds.v1 import instance as _instance
from openstack.rds.v1 import rdsversion as _version





class Proxy(proxy2.BaseProxy):

    def datastore_versions(self, dbname):
        """List datastore versions

        :param dbname: MySQL, PostgreSQL or SQLServer
        :returns: A generator of version object
        :rtype: :class:`~openstack.rds.v1.datastore.Version
        """

        return self._list(_datastore.Version, paginated=False,
                          datastore_name=dbname)

    def instances(self):
        """List instances

        :returns: A generator of version object
        :rtype: :class:`~openstack.rds.v1.instance.Instance
        """
        return self._list(_instance.Instance, paginated=False)

    def get_instance(self, instance):
        """Get instance by id

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :returns: The results of instance
        :rtype: :class:`~openstack.rds.v1.instance.Instance`.
        """
        return self._get(_instance.Instance, instance)

    def delete_instance(self, instance, ignore_missing=False):
        """Delete an instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
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
        :rtype: :class:`~openstack.rds.v1.instance.Instance`.

        """
        return self._create(_instance.Instance, **kwargs)

    def resize_instance(self, instance, flavorRef):
        """Resize an instance by providing flavorRef

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
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
                         :class:`~openstack.rds.v1.instance.Instance`.
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
                         :class:`~openstack.rds.v1.instance.Instance`.
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
                         :class:`~openstack.rds.v1.instance.Instance`.

        :returns: a job id
        :rtype: dict
        """

        if isinstance(instance, _instance.Instance):
            obj = instance
        else:
            obj = self._find(_instance.Instance, instance,
                             ignore_missing=False)

        return obj.restore(self._session, backupRef)

    def set_instance_params(self, instance, **params):
        """Set params on an instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param dict \*\*params: Params dict to set.
        :returns: An object contains result of the set operation,
                  :class:`~openstack.rds.v1.instance.InstanceParameter`
        :rtype: :class:`~openstack.rds.v1.instance.InstanceParameter`.
        """
        if isinstance(instance, _instance.Instance):
            instanceId = instance.id
        else:
            instanceId = instance

        return _instance.InstanceParameter.set_params(self._session,
                                                      instanceId=instanceId,
                                                      **params)

    def reset_instance_params(self, instance):
        """Reset params on an instance to default.

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :returns: An object contains result of the set operation,
                  :class:`~openstack.rds.v1.instance.InstanceParameter`
        :rtype: :class:`~openstack.rds.v1.instance.InstanceParameter`.
        """

        if isinstance(instance, _instance.Instance):
            instanceId = instance.id
        else:
            instanceId = instance

        return _instance.InstanceParameter.reset_params(self._session,
                                                        instanceId=instanceId)

    def list_instance_errorlog(self, instance, **query):
        """List error log of instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param dict \*\*query: A dict to query error log, startDate and
                               endDate are required (e.g. 2016-08-29+06:35),
                               curPage and perPage are optional.
        :returns: A generator of error log object
        :rtype: :class:`~openstack.rds.v1.instance.InstanceErrorLog
        """

        if isinstance(instance, _instance.Instance):
            instanceId = instance.id
        else:
            instanceId = instance

        return self._list(_instance.InstanceErrorLog,
                          instanceId=instanceId,
                          **query)

    def list_instance_slowlog(self, instance, **query):
        """List slow log of instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param dict \*\*query: A dict to query error log, sftype is required,
                               (INSERT, UPDATE, SELECT, DELETE, CREATE), top
                               is opitonal.

        :returns: A generator of slow log object
        :rtype: :class:`~openstack.rds.v1.instance.InstanceSlowLog
        """

        if isinstance(instance, _instance.Instance):
            instanceId = instance.id
        else:
            instanceId = instance

        return self._list(_instance.InstanceSlowLog,
                          instanceId=instanceId,
                          **query)

    def flavors(self, dbId, region):
        """List flavors of given datastore id and region

        :param dbId: database store id
        :param region: region

        :returns: A generator of flavor
        :rtype: :class:`~openstack.rds.v1.flavor.Flavor
        """
        query = {
            'dbId': dbId,
            'region': region
        }
        return self._list(_flavor.Flavor, paginated=False, **query)

    def get_flavor(self, id):
        """Get the detail of a flavor

        :param id: Flavor id or an object of class
                   :class:`~openstack.rds.v1.flavor.Flavor
        :returns: Detail of flavor
        :rtype: :class:`~openstack.rds.v1.flavor.Flavor
        """
        return self._get(_flavor.Flavor, id)

    def backups(self):
        """List all backups

        :returns: A generator of backup object
        :rtype: :class:`~openstack.rds.v1.backup.Backup
        """

        return self._list(_backup.Backup, paginated=False)

    def create_backup(self, instance, name, description):
        """Create backup for an instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param name: Name of the backup
        :param description: Description of the backup
        :returns: An object of :class:`~openstack.rds.v1.backup.Backup.
        :rtype: :class:`~openstack.rds.v1.backup.Backup
        """

        if isinstance(instance, _instance.Instance):
            instanceId = instance.id
        else:
            instanceId = instance

        kwargs = {}
        kwargs.update({'instance': instanceId,
                       'name': name,
                       'description': description})
        return self._create(_backup.Backup, **kwargs)

    def delete_backup(self, id, ignore_missing=False):
        """Delete a backup

        :param id: The value can be the ID of a backup or a object of
                   :class:`~openstack.rds.v1.backup.Backup`.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the backup does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent backup.
        :returns: None
        """
        self._delete(_backup.Backup, id, ignore_missing=ignore_missing)

    def create_backup_policy(self, instance, keepday, starttime):
        """Setup a backup policy

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param keepday: Days of the backup want to be kept
        :param startting: Backup start time
        :returns: A BackupPolicy object
        :rtype: :class:`~openstack.rds.v1.backup.BackupPolicy`.

        """
        if isinstance(instance, _instance.Instance):
            instanceId = instance.id
        else:
            instanceId = instance

        return self._create(_backup.BackupPolicy,
                            instanceId=instanceId,
                            keepday=keepday,
                            starttime=starttime)

    def get_backup_policy(self, instance):
        """Get the backup policy detail

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :returns: A BackupPolicy object
        :rtype: :class:`~openstack.rds.v1.backup.BackupPolicy`.
        """
        if isinstance(instance, _instance.Instance):
            instanceId = instance.id
        else:
            instanceId = instance

        return self._get(_backup.BackupPolicy, instanceId=instanceId,
                         requires_id=False)

    def parameters(self, datastore):
        """List parameters of a datastore

        :param datastore: Id of the datastore version
        :returns: A generator of object Parameter.
        :rtype: :class:`~openstack.rds.v1.datastore.Parameter`.
        """
        if isinstance(datastore, _datastore.Version):
            datastore_version_id = datastore.id
        else:
            datastore_version_id = datastore

        return self._list(_datastore.Parameter,
                          datastore_version_id=datastore_version_id)

    def get_parameter(self, datastore, name):
        """Get parameter of a datastore by name

        :param datastore: Id of the datastore version
        :param name: name of the parameter
        :returns: A object of Parameter.
        :rtype: :class:`~openstack.rds.v1.datastore.Parameter`.
        """
        if isinstance(datastore, _datastore.Version):
            datastore_version_id = datastore.id
        else:
            datastore_version_id = datastore

        return self._get(_datastore.Parameter, name,
                         datastore_version_id=datastore_version_id)


    def get_rds_version(self,version):
        """Get version by id

        :param version: The value can be the ID of a version
        :returns: The results of versions
        :rtype: :class:`~openstack.rds.v1._version.rdsverion`.
        """
        if isinstance(version, _version.rdsverion):
            version_id = version.id

        else:
            version_id = version



        return self._get(_version.rdsverion,version_id)


    def list_rds_version(self):
        """Get instance by id

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :returns: The results of instance
        :rtype: :class:`~openstack.rds.v1.instance.Instance`.
        """
        return self._list(_version.rdsverion, paginated=False)