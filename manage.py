#!/usr/bin/env python
from os.path import abspath, dirname, join
from django.core.management import execute_manager
import imp
import sys


try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)


import settings

if __name__ == "__main__":
    sys.path.insert(0, join(settings.SITE_ROOT, 'apps'))
    execute_manager(settings)
