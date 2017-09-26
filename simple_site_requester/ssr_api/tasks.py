import requests
from django.utils import timezone
from celery import shared_task
from .models import SiteRequest


@shared_task
def request_site():
    url = 'http://www.wp.pl'
    site_request_obj = SiteRequest(url=url)
    site_request_obj.save()
    delta_time = requests.get(url).elapsed.total_seconds()
    site_request_obj.delta_time = delta_time
    site_request_obj.datetime_ended = timezone.now()
    site_request_obj.save()
    print("dupa")