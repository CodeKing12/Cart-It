from django.contrib import admin
from .models import Product, Categories

class ProductAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Categories)