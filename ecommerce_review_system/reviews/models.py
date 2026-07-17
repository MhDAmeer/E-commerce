from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
   
    name = models.CharField(max_length=200)
   
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
    description = models.TextField(blank=True)
   
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews',)
   
    reviewer_name = models.CharField(max_length=150)
   
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Rating must be between 1 and 5.',
    )
   
    comment = models.TextField(blank=True)
   
    review_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-review_date']

    def __str__(self):
        return f'{self.reviewer_name} - {self.product.name} ({self.rating}/5)'
