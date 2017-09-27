from django.db import models


class SiteRequest(models.Model):

    url = models.URLField()
    datetime_started = models.DateTimeField(auto_now_add=True)
    elapsed_time = models.FloatField(null=True)
    response_code = models.IntegerField(null=True)
