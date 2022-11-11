from django import forms
from django.apps import apps


class AuthorForm(forms.ModelForm):
    class Meta:
        model = apps.get_model("bookapi", "Author")
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "date_of_death",
            "biography",
            "photo",
        ]
