# coding: utf-8
"""Settings for Travis."""

from mysitedj2_0.settings.base import * # noqa


SECRET_KEY = "tlt#^9^3gg-jqm+qr__sp58$&k*8u92hyz2r1&c2iziay@on9m"
DEBUG = False
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travis_ci_db',
        'USER': 'travis',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}
