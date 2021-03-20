from django.urls import path
from . import views
from shelf.views import BookList


urlpatterns = [
    path('', BookList.as_view()),
]