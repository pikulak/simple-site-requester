from rest_framework import viewsets
from .serializers import SiteRequestSerializer
from .models import SiteRequest


class SiteRequestViewSet(viewsets.ModelViewSet):
    queryset = SiteRequest.objects.all()
    serializer_class = SiteRequestSerializer
