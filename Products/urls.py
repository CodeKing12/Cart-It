from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("<product_info>", views.product_details, name="product_details")
]

urlpatterns += staticfiles_urlpatterns()
