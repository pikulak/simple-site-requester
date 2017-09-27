from rest_framework import serializers
from .models import SiteRequest


class SiteRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteRequest
        fields = ('url', 'datetime_started', 'elapsed_time', 'response_code')
