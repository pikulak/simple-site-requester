from django.db import models


class SiteRequest(models.Model):

    url = models.URLField()
    datetime_started = models.DateTimeField(auto_now_add=True)
    datetime_ended = models.DateTimeField(null=True)
    delta_time = models.IntegerField(null=True)
