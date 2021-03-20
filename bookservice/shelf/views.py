from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Book


# def index(request):
#     return HttpResponse("Hello, world. You're at the shelfapp index.")


class BookList(ListView):
    model = Book
    template_name = 'Book_list.html'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context