from django.contrib import admin
from .models import Product, Categories, PostImages

class PostImagesAdmin(admin.StackedInline):
    model = PostImages

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "id"]
    inlines = [PostImagesAdmin]

class PostImagesAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Categories)
admin.register(PostImages, PostImagesAdmin)
