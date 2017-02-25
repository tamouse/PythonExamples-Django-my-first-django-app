"""
WSGI config for my_first_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

app_path = os.path.dirname(__file__)
if app_path not in sys.path:
    sys.path.append(app_path)

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_first_django.settings")

application = StaticFilesHandler(get_wsgi_application())
