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

from openstack.anti_ddos import anti_ddos_service
from openstack import resource2 as resource


class AntiDDosMin(resource.Resource):

    service = anti_ddos_service.AntiDDosService()

    @classmethod
    def list(cls, session, paginated=False, **params):
        query_params = cls._query_mapping._transpose(params)
        uri = cls.base_path % params

        endpoint_override = cls.service.get_endpoint_override()
        resp = session.get(uri, endpoint_filter=cls.service,
                           endpoint_override=endpoint_override,
                           headers={"Accept": "application/json"},
                           params=query_params)
        resp = resp.json()
        return cls.existing(**resp)


class QueryConfigList(resource.Resource):

    base_path = '/antiddos/query_config_list'
    service = anti_ddos_service.AntiDDosService()

    # capabilities
    allow_get = True

    # Properties
    #: A list of traffic limited.
    #: *Type: list*
    traffic_limited_list = resource.Body('traffic_limited_list', type=list)
    #: Http limit list
    #: *Type: list*
    http_limited_list = resource.Body('http_limited_list', type=list)
    #: Connection limit list
    #: *Type: list*
    connection_limited_list = resource.Body('connection_limited_list',
                                            type=list)
    #: A list of extended ddos config of user
    #: *Type: list*
    extend_ddos_config = resource.Body('extend_ddos_config', type=list)


class FloatingIP(resource.Resource):

    resources_key = 'ddosStatus'
    base_path = '/antiddos'
    service = anti_ddos_service.AntiDDosService()

    # capabilities
    allow_list = True
    allow_get = True
    allow_delete = True
    allow_update = True

    _query_mapping = resource.QueryParameters('status',
                                              'limit',
                                              'offset',
                                              'ip')

    # Properties
    floating_ip_id = resource.Body('floating_ip_id', alternate_id=True)
    #: Whether enable L7 protect
    #: *Type: bool*
    enable_L7 = resource.Body('enable_L7', type=bool)
    #: Traffic segment id
    #: Valid values are from `1` to `9`
    #: *Type: int*
    traffic_pos_id = resource.Body('traffic_pos_id', type=int)
    #: Http request segment id
    #: Valid values are from `1` to `15`
    #: *Type: int*
    http_request_pos_id = resource.Body('http_request_pos_id', type=int)
    #: Cleaning access limit id
    #: Valid values are from `1` to `8`
    #: *Type: int*
    cleaning_access_pos_id = resource.Body('cleaning_access_pos_id', type=int)
    #: Application type id
    #: Valid values are from `0`, `1`
    #: *Type: int*
    app_type_id = resource.Body('app_type_id', type=int)
    #: Floating ipaddress
    floating_ip_address = resource.Body('floating_ip_address')
    #: Network type: EIP or ELB
    network_type = resource.Body('network_type')
    #: Status of the EIP
    status = resource.Body('status')
    #: Task id
    task_id = resource.Body('task_id')

    def create(self, session, prepend_key=True):
        endpoint_override = self.service.get_endpoint_override()
        request = self._prepare_request(requires_id=True,
                                        prepend_key=prepend_key)
        request.body.pop('floating_ip_id')
        response = session.post(request.uri, endpoint_filter=self.service,
                                endpoint_override=endpoint_override,
                                json=request.body, headers=request.headers)

        self._translate_response(response)
        return self

    def update(self, session, prepend_key=True, has_body=True):
        # floating update requires body to have `enable_L7, traffic_pos_id
        # http_request_pos_id, cleaning_access_pos_id, app_type_id`
        # but resource2.py won't put them into body is they are not
        # dirty

        # The id cannot be dirty for an update
        self._body._dirty.discard("id")

        # Only try to update if we actually have anything to update.
        if not any([self._body.dirty, self._header.dirty]):
            return self

        request = self._prepare_request(prepend_key=prepend_key)

        endpoint_override = self.service.get_endpoint_override()

        for r in ('enable_L7', 'traffic_pos_id', 'http_request_pos_id',
                  'cleaning_access_pos_id', 'app_type_id'):
            if r not in request.body:
                request.body[r] = getattr(self, r)

        response = session.put(request.uri, endpoint_filter=self.service,
                               endpoint_override=endpoint_override,
                               json=request.body, headers=request.headers)

        self._translate_response(response, has_body=has_body)
        return self


class TaskStatus(AntiDDosMin):

    base_path = '/query_task_status'

    _query_mapping = resource.QueryParameters('task_id')

    # Properties
    #: Status of task
    #: validate status are `success`, `failed`, `waiting`, `running`
    task_status = resource.Body('task_status')
    #: Additional task status message
    task_msg = resource.Body('task_msg')


class EIPStatus(resource.Resource):

    base_path = '/antiddos/%(floating_ip_id)s/status'
    service = anti_ddos_service.AntiDDosService()

    # capabilities
    allow_get = True

    # Properties
    floating_ip_id = resource.URI('floating_ip_id')
    #: Status of Anti-DDos
    #: validate status are `normal`, `configging`, `notConfig`,
    #: `packetcleaning`, `packetdropping`
    status = resource.Body('status')


class EIPDaily(resource.Resource):

    resources_key = 'data'
    base_path = '/antiddos/%(floating_ip_id)s/daily'
    service = anti_ddos_service.AntiDDosService()

    # capabilities
    allow_list = True

    # Properties
    #: Data start time
    #: *Type: int*
    period_start = resource.Body('period_start', type=int)
    #: In (bit/s)
    #: *Type: int*
    bps_in = resource.Body('bps_in', type=int)
    #: Attack (bit/s)
    #: *Type: int*
    bps_attack = resource.Body('bps_attack', type=int)
    #: Total data (bit/s)
    #: *Type: int*
    total_bps = resource.Body('total_bps', type=int)
    #: Package in speed (/s)
    #: *Type: int*
    pps_in = resource.Body('pps_in', type=int)
    #: Package attack speed (/s)
    #: *Type: int*
    pps_attack = resource.Body('pps_attack', type=int)
    #: Total package speed (/s)
    #: *Type: int*
    total_pps = resource.Body('total_pps', type=int)


class EIPLog(resource.Resource):

    resources_key = 'logs'
    base_path = '/antiddos/%(floating_ip_id)s/logs'
    service = anti_ddos_service.AntiDDosService()

    _query_mapping = resource.QueryParameters('limit', 'offset', 'sort_dir')

    # capabilities
    allow_list = True

    # Properties
    #: start time
    #: *Type: int*
    start_time = resource.Body('start_time', type=int)
    #: end time
    #: *Type: int*
    end_time = resource.Body('end_time', type=int)
    #: Anti-ddos status
    #: *Type: int*
    status = resource.Body('status', type=int)
    #: Trigger bps (bit/s)
    #: *Type: int*
    trigger_bps = resource.Body('trigger_bps', type=int)
    #: Trigger package per second
    #: *Type: int*
    trigger_pps = resource.Body('trigger_pps', type=int)
    #: Trigger http requests
    #: *Type: int*
    trigger_http_pps = resource.Body('trigger_http_pps', type=int)


class EIPWeekly(AntiDDosMin):

    base_path = '/antiddos/weekly'

    _query_mapping = resource.QueryParameters('period_start_date')

    # Properties
    #: Intercept time in one week
    #: *Type: int*
    ddos_intercept_times = resource.Body('ddos_intercept_times', type=int)
    #: A list of data in one week
    #: *Type: list*
    weekdata = resource.Body('weekdata', type=list)
    #: Top 10 ip address in one week
    #: *Type: list*
    top10 = resource.Body('top10', type=list)
