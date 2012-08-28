import os
import sys
sys.path.append('/home/sparkstar/sa_translate/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'sa_translate.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
