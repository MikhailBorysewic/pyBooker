from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from ..serializers import BookSerializer, AuthorSerializer
from ..services.book import get_recent_published_books, get_book_by_pk
from ..models import Book


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.prefetch_related("publishers").all()

    @action(detail=False, url_path=r"recent-published")
    def recent_published(self, request):

        days = request.query_params.get("days")
        recent_published_books = get_recent_published_books(days=days)

        serializer = self.get_serializer(recent_published_books, many=True)
        return Response(serializer.data)

    @action(detail=True, url_path=r"author")
    def book_author(self, request, pk: int):

        book = get_book_by_pk(pk)
        return Response(AuthorSerializer(book.author).data)
