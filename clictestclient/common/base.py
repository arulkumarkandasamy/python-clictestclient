import warnings

from clictestclient.openstack.common.apiclient import base


warnings.warn("The 'clictestclient.common.base' module is deprecated post "
              "v.0.12.0. Use 'clictestclient.openstack.common.apiclient.base' "
              "instead of this one.", DeprecationWarning)


getid = base.getid
Manager = base.ManagerWithFind
Resource = base.Resource
