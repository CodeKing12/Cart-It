from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("create_account", views.account_creation_view, name="create_an_account"),
    path("confirm_email", views.email_confirm, name="confirm_email"),
    path("login", views.login_view, name="login_account"),
    path("activate/<uidb64>/<token>", views.activate_account, name="activate_account"),
    path("messages", views.messages_view, name="messenger"),
    path("home_view", views.account_home, name="account_home")
]

urlpatterns += staticfiles_urlpatterns()