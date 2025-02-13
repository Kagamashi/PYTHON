# Django
# Django is a high-level web framework designed for rapid development.
# It comes with many built-in features like authentication, admin panel, and ORM.
from django.http import HttpResponse # type: ignore
from django.urls import path # type: ignore

def home(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path('', home),
]
