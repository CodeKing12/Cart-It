from .forms import CreateAccountForm
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def account_creation_view(request):
    if request.method == "POST":
        register_form = CreateAccountForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("confirm_email")
    else:
        register_form = CreateAccountForm()
    return render(request, "accounts/create_an_account.html", {"create_form": register_form})

def email_confirm(request):
    return render(request, "accounts/confirm_email.html")

def login_view(request):
    render(request, 'homepage.html')
