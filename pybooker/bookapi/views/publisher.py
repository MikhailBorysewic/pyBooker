from rest_framework import status, viewsets

from ..serializers import PublisherSerializer
from ..models import Publisher


class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
