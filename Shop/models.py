from django.db import models

# Create your models here.
class Categories(models.Model):
    categories = models.CharField(max_length=60)

class Product(models.Model):
    name = models.CharField(max_length=120)
    id_image = models.ImageField()
    product_info = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)