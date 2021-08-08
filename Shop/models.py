from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Categories(models.Model):
    category_icons = models.CharField(blank=True, max_length=150)
    categories = models.CharField(max_length=60)

    def __str__(self):
        return self.categories

    def natural_key(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    id_image = models.ImageField(blank=True, upload_to="uploaded_images/")
    product_info = RichTextField()
    category = models.ManyToManyField(Categories)

    def __str__(self):
        return self.name

class PostImages(models.Model):
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="uploaded_images/")
