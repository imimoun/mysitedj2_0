#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if 'HEROKU_RUNNING' in locals() or 'HEROKU_RUNNING' in globals():
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysitedj2_0.settings.heroku")
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
