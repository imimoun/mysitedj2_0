"""
WSGI config for mysitedj2_0 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if 'STATE_APP' in os.environ:
    if os.environ.get('STATE_APP', '') == 'dev':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysitedj2_0.settings.heroku_dev")
    elif os.environ['STATE_APP'].get('STATE_APP', '') == 'prod':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysitedj2_0.settings.heroku_prod")
    else:
        raise ValueError('ERROR: variable STATE_APP have to be init in heroku settings')

application = get_wsgi_application()
