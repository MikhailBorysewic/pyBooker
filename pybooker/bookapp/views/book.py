import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import redirect

from ..forms import BookForm
from ..utils import get_full_url


class BooksPageView(TemplateView):
    template_name = "bookapp/book/books.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = get_full_url(self.request, view_name="books-list")
        books_json = requests.get(url).json()

        context["books"] = books_json
        return context


class AddBookPage(TemplateView):
    template_name = "bookapp/book/add_book.html"
    success_url_name = "books"
    form_class = BookForm

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
        context["form_legend"] = "Add Book"

        return context
