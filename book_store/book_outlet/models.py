from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.DecimalField(decimal_places=2, max_digits=5, validators=[MinValueValidator(0), MaxValueValidator(5)])
    author = models.CharField(null=True , max_length=100)
    is_bestseller = models.BooleanField( default=False)

    def __str__(self):
        return f'{self.title} , Rating: {self.rating}'

