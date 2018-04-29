# coding: utf-8
"""Settings for Heroku."""

from mysitedj2_0.settings.base import * # noqa

import django_heroku

DEBUG = False

# Configure Django App for Heroku.
django_heroku.settings(locals())
