from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.shophome, name="shop_home"),
    path("product_info/<product_id>", views.product_details, name="product_details"),
    path("<categories>", views.category_items, name="category_items"),
]

urlpatterns += staticfiles_urlpatterns()
