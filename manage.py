#!/usr/bin/env python
import os
import sys

#TODO: remember to set dev enviroment variable
if __name__ == "__main__":
    if os.environ['DEV_ENVIROMENT'] == 'dev':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beeep.settings.development")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beeep.settings.production")
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
