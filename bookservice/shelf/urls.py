from django.urls import path
from . import views
from shelf.views import BookList, BookCreate, BookUpdate, BookDelete, showhelp
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('show-help/', showhelp),
    path('', BookList.as_view(), name='book-list'),
    path('add/', login_required(BookCreate.as_view()), name='book-add'),
    path('<int:pk>/', login_required(BookUpdate.as_view()), name='book-update'),
    path('<int:pk>/delete/', login_required(BookDelete.as_view()), name='book-delete'),
]
