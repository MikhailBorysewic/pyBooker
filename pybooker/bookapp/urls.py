from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.IndexPageView.as_view(), name="index"),
    path("authors/", views.AuthorsPageView.as_view(), name="authors"),
    path("authors/add/", views.AddAuthorPageView.as_view(), name="authors-add"),
    path("books/", views.BooksPageView.as_view(), name="books"),
    path("books/add/", views.AddBookPage.as_view(), name="books-add"),
    path("publishers/", views.PublishersPageView.as_view(), name="publishers"),
    path(
        "publishers/add/", views.AddPublisherPageView.as_view(), name="publishers-add"
    ),
]
