from django.contrib import admin
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100,default='')
    def fulbabyl_name(self):
        return f'Name: {self.name} , L_name: {self.last_name}'
    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.DecimalField(decimal_places=2, max_digits=5, validators=[MinValueValidator(0), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books',null=True)
    is_bestseller = models.BooleanField( default=False)
    slug = models.SlugField(default='',null=False,db_index=True)
    def get_absolute_url(self):
        return reverse('book_detail',args=[self.slug])
    def __str__(self):
        return f'{self.title} , Rating: {self.rating}'

