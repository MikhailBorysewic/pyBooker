from rest_framework import status, viewsets

from ..serializers import ReviewSerializer
from ..models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
