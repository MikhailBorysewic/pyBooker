import requests
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from ..forms import PublisherForm
from ..utils import get_full_url


class PublishersPageView(TemplateView):
    template_name = "bookapp/publisher/publishers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = get_full_url(self.request, view_name="publishers-list")
        publishers_json = requests.get(url).json()

        context["publishers"] = publishers_json
        return context


class AddPublisherPageView(TemplateView):
    template_name = "bookapp/publisher/add_publisher.html"
    success_url_name = "publishers"
    form_class = PublisherForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["form"] = self.form_class()
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST, request.FILES)
        context["form"] = form
        if form.is_valid():
            form.save()
            return redirect(self.success_url_name)
        else:
            context["errors"] = form.errors.as_json()
            return render(request, self.template_name, context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_legend"] = "Add Publisher"

        return context
