# coding: utf-8
"""Settings for Heroku."""

from mysitedj2_0.settings.base import * # noqa

import django_heroku

SECRET_KEY = "2!fdh26q0ok21(3+5m&=-(45w&cxpsr8ay_ut0t%nz^y=z@m*!"
DEBUG = False

# Configure Django App for Heroku.
django_heroku.settings(locals())
