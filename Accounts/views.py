from .forms import CreateAccountForm, LoginForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .models import Cart

# Create your views here.
def account_creation_view(request):
    register_form = CreateAccountForm()
    login_form = LoginForm()
    if request.method == "POST":
        if 'creation_form' in request.POST:
            # return HttpResponse("Creation Form received")
            register_form = CreateAccountForm(request.POST)
            #login_form = LoginForm()
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account'
                message = render_to_string('accounts/confirm_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                })
                to_email = register_form.cleaned_data["email"]
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                info = "An activation link has been sent to your email address. Click on it to fully activate your account and login."
                info_icon = 'shop/images/email-2935508_1280 1.png'
                return render(request, "message_template.html", {"message": info, "message_icon": info_icon })
            else:
                return HttpResponse("Invalid Input")
        elif 'login_form' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data["loginmail"]
                password = login_form.cleaned_data["login_password"]
                try:
                    username = User.objects.get(email=email)
                except User.DoesNotExist:
                    return HttpResponse("Invalid Email")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    info = "Login Successful"
                    info_icon = "shop/images/20210414_144233_0000.png"
                    return render(request, "message_template.html", {"message": info, "message_icon": info_icon})
                else:
                    return HttpResponse("Invalid Password")
    return render(request, "accounts/create_an_account.html", {"create_form": register_form, "login_form": login_form})

def email_confirm(request):
    return render(request, "accounts/confirm_email.html")

def login_view(request):
    render(request, 'homepage.html')

def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        create_cart = Cart(user=user)
        create_cart.save()
        return HttpResponse("Your account has been successfully activated. You can now login")
    else:
        return HttpResponse("Activation Link is Invalid")

def messages_view(request):
    info = "An activation link has been sent to your email address. Click on it to fully activate your account and login."
    info_icon = 'static/shop/images/email-2935508_1280 1.png'
    return render(request, "message_template.html", {"message": info, "message_icon": info_icon})

def account_home(request):
    cart = Cart.objects.get(user=request.user)
    all_products = cart.products.all()
    return render(request, "accounts/account_home.html", {"cart": cart, "all_products": all_products})
