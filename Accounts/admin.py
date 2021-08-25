from django.contrib import admin
from .models import Cart, Product

class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "id"]

admin.site.register(Cart, CartAdmin)
# Register your models here.
