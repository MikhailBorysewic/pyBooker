from rest_framework import status, viewsets

from ..serializers import GenreSerializer
from ..models import Genre


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
