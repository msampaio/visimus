import os
import sys

from django.core.handlers.wsgi import WSGIHandler

PROJECT = os.path.expanduser('~/webapps/visimus/visimus/')
sys.path.append(PROJECT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'visimus.settings'
application = WSGIHandler()
