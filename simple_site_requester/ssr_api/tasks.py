import requests

from django.utils import timezone
from celery import shared_task
from .models import SiteRequest


@shared_task
def request_site(url):
    request_obj = SiteRequest(url=url)
    request_obj.save()
    elapsed_time = requests.get(url).elapsed.total_seconds()
    request_obj.datetime_ended = timezone.now()
    request_obj.elapsed_time = elapsed_time
    request_obj.save()
    print("Requested: {} with elapsed time: {}s".format(url, elapsed_time))
