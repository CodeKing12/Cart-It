from .forms import CreateAccountForm
from django.shortcuts import render

# Create your views here.
def account_creation_view(request):
    return render(request, "accounts/create_an_account.html", {"create_form": CreateAccountForm})
