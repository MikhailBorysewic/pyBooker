from django import forms
from django.apps import apps


class PublisherForm(forms.ModelForm):
    class Meta:
        model = apps.get_model("bookapi", "Publisher")
        fields = ["name", "year_of_foundation", "description", "books", "logo"]
