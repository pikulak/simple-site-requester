from django.db import models


class SiteRequest(models.Model):

    url = models.URLField()
    datetime_started = models.DateTimeField(auto_now_add=True)
    datetime_ended = models.DateTimeField(null=True)
    elapsed_time = models.FloatField(null=True)
