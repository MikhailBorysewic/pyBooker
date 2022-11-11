from django.db import models

from .book import Book


class Review(models.Model):
    text = models.TextField(max_length=356)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.text[:20:]}..."
