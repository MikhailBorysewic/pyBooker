from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=64)
    year_of_foundation = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=256, blank=True, null=True)
    books = models.ManyToManyField(
        "Book", related_name="publishers", blank=True
    )
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
