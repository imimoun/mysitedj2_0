# coding: utf-8
"""Settings for developers."""

from mysitedj2_0.utils import read_json_file
from mysitedj2_0.settings.base import *  # noqa

SECRET_KEY = "tlt#^9^3gg-jqm+qr__sp58$&k*8u92hyz2r1&c2iziay@on9m"
DEBUG = True
TEMPLATE_DEBUG = True

db_config = read_json_file('mysitedj2_0/json/db_config_local.json')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_config['NAME'],
        'USER': db_config['USER'],
        'PASSWORD': db_config['PASSWORD'],
        'HOST': db_config['HOST'],
        'PORT': db_config['PORT'],
    }
}
