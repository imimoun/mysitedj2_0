# coding: utf-8
"""Settings for Travis."""

from mysitedj2_0.utils import read_json_file
import mysitedj2_0.settings.base as s_base

SECRET_KEY = "tlt#^9^3gg-jqm+qr__sp58$&k*8u92hyz2r1&c2iziay@on9m"
DEBUG = False
TEMPLATE_DEBUG = True

db_config = read_json_file(s_base.BASE_DIR + '/json/db_config_travis.json')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_config['NAME'],
        'USER': db_config['USER'],
        'PASSWORD': db_config['PASSWORD'],
        'HOST': db_config['HOST'],
    }
}
