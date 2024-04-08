from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discounted_price = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)