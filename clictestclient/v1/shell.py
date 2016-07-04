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

from __future__ import print_function

import copy
import functools
import os
import six
import sys

from oslo_utils import encodeutils
from oslo_utils import strutils

from clictestclient.common import progressbar
from clictestclient.common import utils
from clictestclient import exc
import clictestclient.v1.objectspy

CONTAINER_FORMATS = 'Acceptable formats: ami, ari, aki, bare, and ovf.'
DISK_FORMATS = ('Acceptable formats: ami, ari, aki, vhd, vmdk, raw, '
                'qcow2, vdi, and iso.')
DATA_FIELDS = ('location', 'copy_from', 'file')

_bool_strict = functools.partial(strutils.bool_from_string, strict=True)


def _objectspy_show(test, human_readable=False, max_column_width=80):
    # Flatten test properties dict for display
    info = copy.deepcopy(test._info)
    if human_readable:
        info['size'] = utils.make_size_human_readable(info['size'])
    for (k, v) in six.iteritems(info.pop('properties')):
        info['Property \'%s\'' % k] = v

    utils.print_dict(info, max_column_width=max_column_width)


