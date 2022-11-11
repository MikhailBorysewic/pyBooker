from rest_framework import status, viewsets

from ..serializers import QuoteSerializer
from ..models import Quote


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
