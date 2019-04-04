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

from openstack.compute import compute_service
from openstack import resource2 as resource
from openstack import exceptions
import six
from keystoneauth1 import exceptions
from openstack import utils


class Tag(resource.Resource):
    base_path = 'servers/%(server)s/tags'

    service = compute_service.ComputeService()

    # capabilities
    allow_get = True
    allow_delete = True
    allow_create = True

    put_create = True
    server = resource.URI('server')
    tag = resource.URI('tag')
    tags = resource.Body('tags')

    def create(self, session, prepend_key=True):
        """Create a remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param prepend_key: A boolean indicating whether the resource_key
                            should be prepended in a resource creation
                            request. Default to True.

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_create` is not set to ``True``.
        """
        if not self.allow_create:
            raise exceptions.MethodNotSupported(self, "create")

        endpoint_override = self.service.get_endpoint_override()
        if self.put_create:
            # create tag do not need requires_id
            request = self._prepare_request(requires_id=False,
                                            prepend_key=prepend_key)
            response = session.put(request.uri, endpoint_filter=self.service,
                                   endpoint_override=endpoint_override,
                                   json=request.body, headers=request.headers)
        self._translate_response(response)
        return self

    def delete(self, session, params=None, has_body=False):
        """Delete the remote resource based on this instance.

        :param session: The session to use for making this request.
        :type session: :class:`~openstack.session.Session`
        :param params: http params to be sent
        :param bool has_body: should mapping response body to resource

        :return: This :class:`Resource` instance.
        :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
                 :data:`Resource.allow_update` is not set to ``True``.
        """
        if not self.allow_delete:
            raise exceptions.MethodNotSupported(self, "delete")
        # delete tag do not need requires_id
        request = self._prepare_request(requires_id=False)

        endpoint_override = self.service.get_endpoint_override()
        response = session.delete(request.uri, endpoint_filter=self.service,
                                  endpoint_override=endpoint_override,
                                  headers={"Accept": ""},
                                  params=params)
        self._translate_response(response, has_body=has_body)
        return self


class TagAction(Tag):
    base_path = 'servers/%(server)s/tags/%(tag)s'


class TagMixin(object):
    def _tag(self, method, key=None, delete=False, tags=None, session=None):
        if tags:
            for v in tags:
                if not isinstance(v, six.string_types):
                    raise ValueError("The value for %s must be "
                                     "a text string" %v)

        # If we're in a ServerDetail, we need to pop the "detail" portion
        # of the URL off and then everything else will work the same.
        pos = self.base_path.find("detail")
        if pos != -1:
            base = self.base_path[:pos]
        else:
            base = self.base_path

        if key is not None:
            url = utils.urljoin(base, self.id, "tags", key)
        else:
            url = utils.urljoin(base, self.id, "tags")

        endpoint_filter = self.get_endpoint_filter(self, session)
        endpoint_filter.interface = "public"
        endpoint_override = self.service.get_endpoint_override()
        kwargs = {"endpoint_filter": endpoint_filter,
                  "microversion": endpoint_filter.microversion,
                  "endpoint_override": endpoint_override}
        if tags:
            kwargs["json"] = {'tags': tags}
        headers = {"Accept": ""} if delete else {}

        response = method(url, headers=headers, **kwargs)

        # DELETE doesn't return a JSON body
        # PUT a special tag doesn't return a JSON body
        return response.json() if not delete and key is None else None

    def list_tags(self, session):
        """List all tags of the server

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`

        :returns: A list of the requested tags. All tags are Unicode text.
        :rtype: list
        """
        result = self._tag(session.get, session=session)
        return result['tags']

    def set_tags(self, session, *tags):
        """Replace all tags of the server with the new set of tags

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`
        :param args tags: A list of tags.

        :returns: A list of the tags after being updated.
        :rtype: list
        """
        if not tags:
            return list()

        result = self._tag(session.put, tags=list(tags), session=session)
        return result['tags']

    def delete_tags(self, session):
        """Delete all tags from the server

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`

        :rtype: ``None``
        """
        self._tag(session.delete, delete=True, session=session)

    def check_tag(self, session, tag):
        """Checks tag existence on the server

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`
        :param str tag: The tag to check.

        :returns: ``True`` if the tag existed, otherwise ``False``.
        :rtype: bool
        """
        if not tag:
            return False

        try:
            self._tag(session.get, key=tag, session=session)
            return True
        except exceptions.NotFound:
            return False

    def add_tag(self, session, tag):
        """Add a single tag to the server

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`
        :param str tag: The tag to add.

        :rtype: ``None``
        """
        self._tag(session.put, key=tag, session=session)

    def delete_tag(self, session, tag):
        """Deletes a single tag from the server

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`
        :param str tag: The tag to delete.

        :rtype: ``None``
        """
        self._tag(session.delete, key=tag, delete=True, session=session)

    def create_tag(self, session, tags):
        """Create single tag to the server

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`
        :param str tag: The tag to add.

        :rtype: ``None``
        """
        self._tag(session.put, tags=tags, session=session)
