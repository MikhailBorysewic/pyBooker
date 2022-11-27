from django.contrib import admin
from django.apps import apps

# Register your models here.

admin.site.register(apps.get_model("bookapi", "Author"))
admin.site.register(apps.get_model("bookapi", "Book"))
admin.site.register(apps.get_model("bookapi", "Genre"))
admin.site.register(apps.get_model("bookapi", "Publisher"))
admin.site.register(apps.get_model("bookapi", "Quote"))
admin.site.register(apps.get_model("bookapi", "Review"))
