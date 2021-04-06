from django.test import TestCase
from .models import Book

class BookModelTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="War and Peace", description="Biiig Book", price=123.2)

    def test_is_book_created(self):
        war = Book.objects.get(title="War and Peace")
        self.assertTrue(isinstance(war, Book))