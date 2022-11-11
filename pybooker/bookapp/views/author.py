import requests
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from ..forms import AuthorForm
from ..utils import get_full_url


class AuthorsPageView(TemplateView):
    template_name = "bookapp/author/authors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = get_full_url(self.request, view_name="authors-list")
        authors_json = requests.get(url).json()

        context["authors"] = authors_json
        return context


class AddAuthorPageView(TemplateView):
    template_name = "bookapp/author/add_author.html"
    success_url_name = "authors"
    form_class = AuthorForm

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
        context["form_legend"] = "Add Author"

        return context
