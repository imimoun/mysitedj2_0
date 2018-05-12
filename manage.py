#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    on_heroku = False
    if 'IN_HEROKU' in os.environ:
        on_heroku = True
        if 'STATE_APP' in os.environ:
            if os.environ.get('STATE_APP', '') == 'dev':
                os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysitedj2_0.settings.heroku_dev")
            elif os.environ['STATE_APP'].get('STATE_APP', '') == 'prod':
                os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysitedj2_0.settings.heroku_prod")
            else:
                raise ValueError('ERROR: variable STATE_APP have to be init in heroku settings')
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysitedj2_0.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
