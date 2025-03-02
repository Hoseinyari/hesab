from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from accounts.models import *
from accounts.forms import MyLoginForm , CreateAccountForm
from transitions.views import home_view


# Create your views here.
def main_page_view(request):

    return render(request,"accounts/main_page.html")
     

def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            data = form.cleaned_data
            username = data["username"]
            password = data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('home_view')
            else:
                return render(request, "accounts/login.html", {
                    'form': form,
                    'error': 'Invalid username or password.'
                })
        else:
            print(form.errors)
            return render(request, "accounts/login.html", {
                'form': form,
                'error': 'Form is not valid. Please correct the errors.'
            })
    else:
        form = MyLoginForm()  # Instantiate the form for GET requests
        return render(request, "accounts/login.html", {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))        



def signup_view(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Use the custom manager's create_user method to create the account
            account = Account.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"]  
            )
            login(request, account)
            return redirect('home')
        else:
            return render(request, "accounts/signup.html", {"form": form})
    else:
        form = CreateAccountForm()
        return render(request, "accounts/signup.html", {"form": form})

