"""
WSGI config for django_framework project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import main.django_settings as django_settings
import utils
from utils import TimeDecorator
from utils.logger.file_logger import FileLogger

django_settings.ALLOWED_HOSTS = ['*']
django_settings.DEBUG = False
utils.logger = TimeDecorator(FileLogger('output/log.txt'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_framework.settings')

application = get_wsgi_application()
