import os
import sys
path = '/home/lab/chain-hotel-book-system/'
if path not in sys.path:
    sys.path.insert(0, '/home/lab/chain-hotel-book-system/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'chain-hotel-book-system.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
#application = get_wsgi_application()