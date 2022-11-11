from django.db import models

from ..models.book import Book


class Quote(models.Model):
    text = models.TextField(max_length=256)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.text[:20:]}..."
