from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r"books", views.BookViewSet, basename="books")
router.register(r"authors", views.AuthorViewSet, basename="authors")
router.register(r"publishers", views.PublisherViewSet, basename="publishers")
router.register(r"reviews", views.ReviewViewSet, basename="reviews")
router.register(r"genres", views.GenreViewSet, basename="genrs")
router.register(r"quotes", views.QuoteViewSet, basename="quotes")

urlpatterns = [
    path("", include(router.urls)),
]
