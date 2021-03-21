from django.urls import path
from . import views
from shelf.views import BookList, BookCreate, BookUpdate, BookDelete


urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('add/', BookCreate.as_view(), name='book-add'),
    path('<int:pk>/', BookUpdate.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]
