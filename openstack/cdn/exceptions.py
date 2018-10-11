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

"""
Exception definitions for CDN service.
"""

from openstack import exceptions


class CDNException(exceptions.HttpException):
    """The exception class for all exceptions the CDN service raises."""
    def __init__(self, message=None, code=None, details=None, response=None,
                 request_id=None, url=None, method=None,
                 http_status=None, cause=None):
        super(CDNException, self).__init__(message=message, details=details,
                                           response=response,
                                           request_id=request_id,
                                           url=url,
                                           method=method,
                                           http_status=http_status,
                                           cause=cause)
        self.code = code

    def __unicode__(self):
        msg = super(CDNException, self).__unicode__()
        if self.code:
            msg += '(%s)' % self.code
        return msg
