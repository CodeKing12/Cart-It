from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("create_account", views.account_creation_view, name="create_an_account"),
    path("confirm_email", views.email_confirm, name="confirm_email")
]

urlpatterns += staticfiles_urlpatterns()