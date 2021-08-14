from django import forms
from django.contrib.auth.forms import User, UserCreationForm

class CreateAccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2", "phone_number"]
