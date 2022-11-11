from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        error_messages={
            "unique": "This genre already exists.",
        },
    )

    def __str__(self):
        return f"{self.name}"
