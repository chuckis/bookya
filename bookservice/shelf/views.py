from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Book, BookInstance



class BookList(ListView):
    model = Book
    template_name = 'Book_list.html'

class BookCreate(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'description', 'photo', 'price']
    success_url = reverse_lazy('book-list')

class BookUpdate(UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = ['title', 'description', 'photo', 'price']
    success_url = reverse_lazy('book-list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')
    

def showhelp(request):
    raise Exception('Django middleware')


class IndexView(ListView):
    model = BookInstance
    template_name = 'index.html'