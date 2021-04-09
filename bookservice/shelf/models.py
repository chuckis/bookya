from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse_lazy

import uuid

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, verbose_name='Автор книги', null=True)
    description = models.CharField(max_length=200, verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(upload_to='shelf_images')

    def get_absolute_url(self):
        return reverse_lazy('')


class BookInstance(models.Model):
    id =models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный ид.номер экземпляра книги")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
     
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('T', 'Читают'),
        ('A', 'В наличии'),
        ('R', 'Занята'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='A',
        help_text='Доступность книги')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.book.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)


