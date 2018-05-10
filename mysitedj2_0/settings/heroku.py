# coding: utf-8
"""Settings for Heroku."""

from mysitedj2_0.settings.base import * # noqa

import django_heroku

SECRET_KEY = "2!fdh26q0ok21(3+5m&=-(45w&cxpsr8ay_ut0t%nz^y=z@m*!"
DEBUG = False

# Configure Django App for Heroku.
django_heroku.settings(locals())

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dc23utbh1vi2v2',
        'USER': 'kyorgvxewlksou',
        'PASSWORD': '150a4c01f2c90d4112c8f1a39c85e9e21ccfa5e2b71160a0245fb08ed8413da6',
        'HOST': 'ec2-174-129-41-64.compute-1.amazonaws.com',
        'PORT': '5432',
    }
