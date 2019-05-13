# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
#      Huawei has modified this source file.
#     
#         Copyright 2018 Huawei Technologies Co., Ltd.
#         
#         Licensed under the Apache License, Version 2.0 (the "License"); you may not
#         use this file except in compliance with the License. You may obtain a copy of
#         the License at
#         
#             http://www.apache.org/licenses/LICENSE-2.0
#         
#         Unless required by applicable law or agreed to in writing, software
#         distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#         WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#         License for the specific language governing permissions and limitations under
#         the License.

import six

from openstack import utils


class MetadataMixin(object):

    def _metadata(self, method, key=None, clear=False, delete=False,
                  **metadata):
        for k, v in metadata.items():
            if not isinstance(v, six.string_types):
                raise ValueError("The value for %s (%s) must be "
                                 "a text string" % (k, v))

        # If we're in a ServerDetail, we need to pop the "detail" portion
        # of the URL off and then everything else will work the same.
        pos = self.base_path.find("detail")
        if pos != -1:
            base = self.base_path[:pos]
        else:
            base = self.base_path

        if key is not None:
            url = utils.urljoin(base, self.id, "metadata", key)
        else:
            url = utils.urljoin(base, self.id, "metadata")

        kwargs = {"endpoint_filter": self.service}
        if metadata or clear:
            # 'meta' is the key for singular modifications.
            # 'metadata' is the key for mass modifications.
            key = "meta" if key is not None else "metadata"
            kwargs["json"] = {key: metadata}

        headers = {"Accept": ""} if delete else {}
        endpoint_override = self.service.get_endpoint_override()
        response = method(url, headers=headers, endpoint_override = endpoint_override, **kwargs)

        # DELETE doesn't return a JSON body while everything else does.
        return response.json() if not delete else None

    def get_metadata(self, session, key=None):
        """Retrieve metadata

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`
        :param key: The key of the metadata to get, if None, return all.
        :type key: str or None

        :returns: The requested metadata. All keys and values
                  are Unicode text.
        """
        result = self._metadata(session.get, key=key)
        return result

    def set_metadata(self, session, **metadata):
        """Update metadata

        This call will replace only the metadata with the same keys
        given here. Metadata with other keys will not be modified.

        :param session: The session to use for this request.
        :param kwargs metadata: key/value metadata pairs to be update on
                                this server instance. All keys and values
                                are stored as Unicode.

        :returns: A dictionary of the metadata after being updated.
                  All keys and values are Unicode text.
        :rtype: dict
        """
        if not metadata:
            return dict()

        result = self._metadata(session.post, **metadata)
        return result

    def update_metadata(self, session, key, value):
        """Creates or replaces a metadata item, by key

        :param session: The session to use for this request.
        :type session: :class:`~openstack.session.Session`
        :param str key: The key of the metadata to update.
        :param str value: The new value of the metadata.

        :returns: The metadata after being updated.
                  All keys and values are Unicode text.
        """
        if not key:
            raise Exception("The key is empty!")

        result = self._metadata(session.put, key=key, **{key: value})
        return result

    def delete_metadata(self, session, keys):
        """Delete metadata

        Note: This method will do a HTTP DELETE request for every key in keys.

        :param session: The session to use for this request.
        :param list keys: The keys to delete.

        :rtype: ``None``
        """
        for key in keys:
            self._metadata(session.delete, key=key, delete=True)
