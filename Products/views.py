from django.shortcuts import render
from Shop.models import Product

# Create your views here.
def product_details(request, product_info):
    product = Product.objects.get(pk=product_info)
    return render(request, "products/product_info.html", {"product": product})
