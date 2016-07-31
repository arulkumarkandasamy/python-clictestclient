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
import urllib

from clictestclient.common import utils
from clictestclient.openstack.common.apiclient import base


OS_REQ_ID_HDR = 'x-openstack-request-id'

class Objectspy(base.Resource):
    def __repr__(self):
        return "<Objectspy %s>" % self._info

    def update(self, **fields):
        self.manager.update(self, **fields)

    def delete(self, **kwargs):
        return self.manager.delete(self)

    def show(self,userid,prjid,browser,url,chvr, **kwargs):
        return self.manager.show(self,userid,prjid,browser,url,chvr, **kwargs)

class ObjectspyManager(base.ManagerWithFind):
    resource_class = Objectspy

    def _list(self, url, response_key, obj_class=None, body=None):
        resp, body = self.client.get(url)

        if obj_class is None:
            obj_class = self.resource_class

        data = body[response_key]
        return ([obj_class(self, res, loaded=True) for res in data if res],
                resp) 

    def show(self,userid,prjid,browser,url,chvr, **kwargs):
        """Get the jnlpfile from object spy
        """
        #url = urllib.quote(url)
        #print('Encoded url in Clictest client object spy show method = %s' % url)
        return self.client.get('/v1/objectspy/%s/%s/%s/%s/%s' % (userid,prjid,browser,url,chvr))
    
