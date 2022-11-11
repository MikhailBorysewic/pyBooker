from rest_framework import serializers

from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "cover",
            "description",
            "isbn",
            "year_of_creation",
            "year_of_publication",
            "author",
            "genre",
            "publishers",
        ]
