from django.db import models
from django.urls import reverse_lazy

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(upload_to='shelf_images')

    def get_absolute_url(self):
        return reverse_lazy('')
        