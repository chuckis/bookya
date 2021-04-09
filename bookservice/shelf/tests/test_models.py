import pytest
from mixer.backend.django import mixer

@pytest.mark.django_db
class TestBook:
    def test_model(self):
      book = mixer.blend('shelf.Book')
      assert book.pk == 1, 'Should create a Book instance'

@pytest.mark.django_db
class TestAuthor:
    def test_model(self):
      author = mixer.blend('shelf.Author')
      assert author.pk == 1, 'Should create a Author instance'


@pytest.mark.django_db
class TestBookInstance:
    def test_model(self):
      book_instance = mixer.blend('shelf.BookInstance')
      assert book_instance.status == 'A', 'Should return a BookInstance default status'