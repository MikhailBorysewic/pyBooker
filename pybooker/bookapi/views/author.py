from rest_framework import status, viewsets

from ..serializers import AuthorSerializer
from ..models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
