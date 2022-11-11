from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404

from ..models import Book


def get_recent_published_books(days: int | None = None) -> list[Book]:
    """
    Returns books that was published less than `N` days ago (by default 30 days), from today.
    """
    if not days:
        days = 30

    today = datetime.today()
    recent_published_books = Book.objects.prefetch_related("publishers").filter(
        year_of_publication__range=[today - timedelta(days), today + timedelta(1)]
    )

    return recent_published_books


def get_book_by_pk(pk: int) -> Book:
    book = get_object_or_404(Book, pk=pk)
    return book
