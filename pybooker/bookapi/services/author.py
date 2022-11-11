from django.shortcuts import get_object_or_404

from ..models import Author


def get_author_by_pk(pk: int) -> Author:
    author = get_object_or_404(Author, pk=pk)
    return author
