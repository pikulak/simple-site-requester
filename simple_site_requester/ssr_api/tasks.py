import requests

from django.utils import timezone
from celery import shared_task
from .models import SiteRequest


@shared_task
def request_site(url):
    request_obj = SiteRequest(url=url)
    request_obj.save()

    with requests.Session() as session:
        response = session.get(url)
        elapsed_time = response.elapsed.total_seconds()
        response_code = response.status_code

    request_obj.datetime_ended = timezone.now()
    request_obj.elapsed_time = elapsed_time
    request_obj.response_code = response_code
    request_obj.save()
    print("Requested: {} with elapsed time: {}s".format(url, elapsed_time))
