from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from accounts.models import *
from accounts.forms import MyLoginForm , SignUpForm
from transitions.views import home_view
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

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
            
            print(user)
            
            # First check if user exists (authentication succeeded)
            if user is not None:
                # Then you can check if user is staff
                if user.is_staff:
                    # Staff user - do something special if needed
                    print("User authenticated as staff")
                # Log the user in (for both staff and regular users)
                login(request, user)
                print("User authenticated successfully")
                return redirect('home_view')
            else:
                # Authentication failed
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
        form = MyLoginForm()
        return render(request, "accounts/login.html", {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))        

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #if validation be succesfull it will save account and log user in
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home_view')
    else:
        #else it will send you to signup page with signup form
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})