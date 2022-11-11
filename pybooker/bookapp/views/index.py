from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "bookapp/index.html"
