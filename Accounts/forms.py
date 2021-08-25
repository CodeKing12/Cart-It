from django import forms
from django.contrib.auth.forms import User, UserCreationForm
import random
import string

class CreateAccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=30)
    username = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "phone_number"]

class LoginForm(forms.Form):
    loginmail = forms.EmailField(max_length=60)
    login_password = forms.CharField(widget=forms.PasswordInput())
