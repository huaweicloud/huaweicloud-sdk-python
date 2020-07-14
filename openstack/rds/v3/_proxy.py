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
from openstack.rds.v3 import backup as _backup
from openstack.rds.v3 import datastore as _datastore
from openstack.rds.v3 import flavor as _flavor
from openstack.rds.v3 import instance as _instance
from openstack.rds.v3 import rdsversion as _version
from openstack.rds.v3 import configuration as _configurations
from openstack.rds.v3 import database as _database


class Proxy(proxy2.BaseProxy):

    def datastore_versions(self, dbname):
        """List datastore versions

        :param dbname: MySQL, PostgreSQL or SQLServer
        :returns: A generator of version object
        :rtype: :class:`~openstack.rds.v1.datastore.Version
        """

        return self._list(_datastore.Version, paginated=False,
                          datastore_name=dbname)

    def flavors(self, **kwargs):
        """List flavors of given datastore id and region

        :param project_id: database store id
        :param database_name: region

        :returns: A generator of flavor
        :rtype: :class:`~openstack.rds.v1.flavor.Flavor
        """
        return self._list(_flavor.Flavor, paginated=False, **kwargs)


    def configurations(self,**kwargs):
        """List configurations of given datastore id and region

        :returns: A generator of configurations
        :rtype: :class:`~openstack.rds.v1.flavor.Flavor
        """
        # query = {
        #     'project_id': project_id,
        #     'database_name': database_name,
        #     'version_name': version_name
        # }
        return self._list(_configurations.Configurations, paginated=False, **kwargs)

    def instances(self, **kwargs):
        """List instances

        :returns: A generator of version object
        :rtype: :class:`~openstack.rds.v1.instance.Instance
        """
        return self._list(_instance.Instance, paginated=False, **kwargs)

    def backups(self, **kwargs):
        """List all backups

        :returns: A generator of backup object
        :rtype: :class:`~openstack.rds.v1.backup.Backup
        """

        return self._list(_backup.Backup, paginated=False, **kwargs)

    def create_backup_policy(self, **kwargs):
        """Setup a backup policy

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param keep_days: Days of the backup want to be kept
        :param start_time: Backup start time
        :returns: A BackupPolicy object
        :rtype: :class:`~openstack.rds.v1.backup.BackupPolicy`.

        """
        return self._create(_backup.BackupPolicy, **kwargs)

    def get_backup_policy(self, **kwargs):
        """Get the backup policy detail

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :returns: A BackupPolicy object
        :rtype: :class:`~openstack.rds.v1.backup.BackupPolicy`.
        """
        return self._get(_backup.BackupPolicy, requires_id=False, **kwargs)

    def create_instance(self, **kwargs):
        """Create a new instance from attributes

        :param dict attrs: Keyword arguments which will be used to create
        :returns: The results of instance
        :rtype: :class:`~openstack.rds.v1.instance.Instance`.

        """
        return self._create(_instance.Instance, **kwargs)

    def delete_instance(self, instance, ignore_missing=True):
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
        return self._delete(_instance.Instance, instance, has_body=True,
                            ignore_missing=ignore_missing)

    def create_backup(self, **kwargs):
        """Create backup for an instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param name: Name of the backup
        :param description: Description of the backup
        :returns: An object of :class:`~openstack.rds.v1.backup.Backup.
        :rtype: :class:`~openstack.rds.v1.backup.Backup
        """
        # kwargs.update({'instance': instanceId,
        #                'name': name,
        #                'description': description})
        return self._create(_backup.Backup, **kwargs)

    def delete_backup(self, backup_id, ignore_missing=True):
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
        return self._delete(_backup.Backup, backup_id, ignore_missing=ignore_missing)

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

    def single_to_ha(self, instance, **single_to_ha_param):
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

        return obj.single_to_ha(self._session, **single_to_ha_param)

    def recovery_instance(self, instance, **kwargs):
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

        return obj.recovery_instance(self._session, **kwargs)

    def restore_time(self, **query):
        # if isinstance(instance, _instance.Instance):
        #     obj = instance
        # else:
        #     obj = self._find(_instance.Instance, instance,
        #                      ignore_missing=False)
        #
        # return obj.restore_time(self._session, **restore_time)
        return self._list(_instance.InstanceRestoreTime, **query)

    def backup_files(self, **kwargs):
        """List all backup files
        """
        return self._list(_backup.Backup, paginated=False, **kwargs)

    def list_instance_errorlog(self, **query):
        """List error log of instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param dict \*\*query: A dict to query error log, startDate and
                               endDate are required (e.g. 2016-08-29+06:35),
                               curPage and perPage are optional.
        :returns: A generator of error log object
        :rtype: :class:`~openstack.rds.v1.instance.InstanceErrorLog
        """

        # if isinstance(instance, _instance.Instance):
        #     instanceId = instance.id
        # else:
        #     instanceId = instance

        return self._list(_instance.InstanceErrorLog, **query)

    def list_instance_slowlog(self, **query):
        """List slow log of instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param dict \*\*query: A dict to query error log, sftype is required,
                               (INSERT, UPDATE, SELECT, DELETE, CREATE), top
                               is opitonal.

        :returns: A generator of slow log object
        :rtype: :class:`~openstack.rds.v1.instance.InstanceSlowLog
        """

        return self._list(_instance.InstanceSlowLog,
                          **query)

    def set_instance_params(self, instance, **params):
        """Set params on an instance

        :param instance: The value can be the ID of a instance or a object of
                         :class:`~openstack.rds.v1.instance.Instance`.
        :param dict \*\*params: Params dict to set.
        :returns: An object contains result of the set operation,
                  :class:`~openstack.rds.v1.instance.InstanceParameter`
        :rtype: :class:`~openstack.rds.v1.instance.InstanceParameter`.
        """
        if isinstance(instance, _instance.InstanceParameter):
            obj = instance
        else:
            obj = self._find(_instance.InstanceParameter, instance,
                             ignore_missing=False)

        return obj.set_params(self._session, **params)

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

    def create_database(self, **kwargs):
        """Create a new database from attributes

        :param dict kwargs: Keyword arguments which will be used to create
                           a :class:`~openstack.rds.v3.database.Database`,
                           comprised of the properties on the Database class.

        :returns: The results of server creation
        :rtype: :class:`~openstack.database.v3.database.Database`
        """
        return self._create(_database.Database, **kwargs)

    def delete_database(self, database, instance=None, ignore_missing=True):
        """Delete a database

        :param database: The value can be either the name of a database or a
               :class:`~openstack.rds.v3.database.Database` instance.
        :param instance: This can be either the ID of an instance
                         or a :class:`~openstack.database.v3.instance.Instance`
                         instance that the interface belongs to.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the database does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent database.

        :returns: ``None``
        """
        instance = self._get_resource(_instance.Instance, instance)
        self._delete(_database.Database, database, instance_id=instance.id,
                     ignore_missing=ignore_missing)

    def databases(self, instance, details=True, **query):
        """Return a generator of databases

        :param details: When ``True``, returns
            :class:`~openstack.rds.v3.database.DatabaseDetail` objects,
            otherwise :class:`~openstack.rds.v3.database.Database`.
            *Default: ``True``*
        :param instance: This can be either the ID of an instance
                         or a :class:`~openstack.rds.v3.instance.Instance`
                         instance that the interface belongs to.
        :param kwargs \*\*query: Optional query parameters to be sent to limit
                                 the resources being returned.

        :returns: A generator of database objects
        :rtype: :class:`~openstack.database.v3.database.Database`
        """
        instance = self._get_resource(_instance.Instance, instance)
        res_type = _database.DatabaseDetail if details else _database.Database
        return self._list(res_type, paginated=False,
                          instance_id=instance.id, **query)
