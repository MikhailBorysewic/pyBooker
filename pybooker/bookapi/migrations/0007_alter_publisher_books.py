# Generated by Django 4.1.3 on 2022-11-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookapi", "0006_author_photo_publisher_logo_alter_genre_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publisher",
            name="books",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="publishers", to="bookapi.book"
            ),
        ),
    ]
