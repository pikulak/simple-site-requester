from rest_framework import serializers
from .models import SiteRequest


class SiteRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteRequest
        fields = ('url', 'datetime_started', 'datetime_ended',
                  'elapsed_time', 'response_code')