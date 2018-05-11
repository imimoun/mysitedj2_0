# coding: utf-8
"""Settings for Heroku."""

from mysitedj2_0.utils import read_json_file
import mysitedj2_0.settings.base as s_base

import django_heroku

SECRET_KEY = "2!fdh26q0ok21(3+5m&=-(45w&cxpsr8ay_ut0t%nz^y=z@m*!"
DEBUG = False

# Configure Django App for Heroku.
django_heroku.settings(locals())

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

db_config = read_json_file(s_base.BASE_DIR + '/json/db_config_dev.json')

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
