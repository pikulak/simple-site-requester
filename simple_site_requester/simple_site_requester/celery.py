import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'simple_site_requester.settings')

celery_app = Celery('simple_site_requester')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
