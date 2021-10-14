from collections import namedtuple
import socket
import pynetbox

from configuration import config, discovery_tag
from netbox_templates import NetBoxTemplate

nb = pynetbox.api(url=config['netbox']['url'], token=config['netbox']['api_token'])
Device = namedtuple('Device', ('manufacturer', 'model', 'role', 'platform'), defaults=(None, None, None, None))
NB_DEFAULT_SITE = config['netbox']['default_devices_site']
netbox_template = NetBoxTemplate(
    default_tags=[{
        'name': discovery_tag
    }],
    default_site=NB_DEFAULT_SITE
)
