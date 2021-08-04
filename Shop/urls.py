from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.shophome, name="shop_home"),
    path("<categories>", views.category_items, name="category_items"),
    path("<product_info>", views.product_details, name="product_detals")
]

urlpatterns += staticfiles_urlpatterns()
