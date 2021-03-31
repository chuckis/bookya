from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Book
from .forms import CheckboxSelectionForm

@login_required()
class BookList(ListView, FormView):
    model = Book
    form_class = CheckboxSelectionForm
    template_name = 'Book_list.html'

    def form_invalid(self, form):
        form.make_feed
        return super().form_valid(form)

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
    