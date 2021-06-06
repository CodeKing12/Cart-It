from django.shortcuts import render, HttpResponse
from .models import Categories, Product
from django.db.models import Q

# Create your views here.
def shophome(request):
    all_categories = Categories.objects.all()
    all_products = Product.objects.all()
    return render(request, 'shop/home.html', {'categories': all_categories, 'all_products': all_products})

def category_items(request, categories):
    cat_id = Categories.objects.get(categories=categories)
    cid = cat_id.id
    category_list = Product.objects.filter(category=cid)
    return render(request, "shop/category_products.html", {"category_list": category_list})