from django.db import models

from .author import Author
from .genre import Genre


class Book(models.Model):
    title = models.CharField(max_length=64)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    description = models.TextField(max_length=256, blank=True, null=True)
    isbn = models.CharField(max_length=64)
    year_of_creation = models.DateField(blank=True, null=True)
    year_of_publication = models.DateField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title}"
