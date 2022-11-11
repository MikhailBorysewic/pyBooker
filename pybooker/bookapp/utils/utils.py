from django.urls import reverse
from django.http.request import HttpRequest


def get_full_url(request: HttpRequest, *, view_name: str) -> str:
    return request.build_absolute_uri("/") + reverse(view_name)[1::]
