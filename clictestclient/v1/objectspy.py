# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import copy

from oslo_utils import encodeutils
from oslo_utils import strutils
import six
import six.moves.urllib.parse as urlparse

from clictestclient.common import utils
from clictestclient.openstack.common.apiclient import base


OS_REQ_ID_HDR = 'x-openstack-request-id'


class ObjectspyManager(base.ManagerWithFind):
    

   def show(self, test, **kwargs):
        """Get the jnlpfile from object spy
        """
        resp, body = self.client.head('/v1/objectspy')
        return resp

    
