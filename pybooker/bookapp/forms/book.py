from django import forms
from django.apps import apps


class BookForm(forms.ModelForm):
    class Meta:
        model = apps.get_model("bookapi", "Book")
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
        ]
