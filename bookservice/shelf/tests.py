from django.test import TestCase
from .models import Book, TimeStampedModel


class BookModelTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="War and Peace", description="Biiig Book", price=123.2)

    def test_is_book_created(self):
        war = Book.objects.get(title="War and Peace")
        self.assertTrue(isinstance(war, Book))
    
    def test_has_a_book_created_attr(self):
        time_stamped_book = Book.objects.get(title="War and Peace")
        self.assertTrue(hasattr(time_stamped_book, 'created'))