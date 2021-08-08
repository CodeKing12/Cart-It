from django.shortcuts import render, get_object_or_404
from .models import Categories, Product, PostImages
from django.db.models import Q

# Create your views here.
def shophome(request):
    all_categories = Categories.objects.all()
    all_products = Product.objects.all()
    context = {'categories': all_categories, 'all_products': all_products}
    return render(request, 'shop/home.html', context=context)

def category_items(request, categories):
    all_categories = Categories.objects.all()
    cat_id = Categories.objects.get(categories=categories)
    cid = cat_id.id
    category_list = Product.objects.filter(category=cid)
    return render(request, "shop/category_products.html", {"category_list": category_list, "categories": all_categories})

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_images = PostImages.objects.filter(post=product)
    return render(request, "shop/product_info.html", {"product": product, "product_images": product_images})
