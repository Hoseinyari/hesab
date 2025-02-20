from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from accounts.models import *
from accounts.forms import MyLoginForm , CreateAccountForm

# Create your views here.
def home_view(request):

    return render(request,"accounts/main_page.html")

@login_required
def dashboard_view(request):
    # if request.method == "POST":
        # print(request.method)
    # else:
    
    #   return HttpResponse("request is not post")
        # return render(request, template_name="accounts/login.html", context={"form": form})  
    return HttpResponseRedirect(reverse("home"))

     

def login_view(request):
        
        form = MyLoginForm (request.POST)
        if form.is_valid():
            print('valid')
            data = form.cleaned_data
            username = data["username"]
            password = data["password"]
            try:
                account = get_object_or_404(Account,username=username)
            except Exception as error:
                print(error)
                # return HttpResponseRedirect(reverse("login"))
                return HttpResponse("error")

            if account is not None:
                if password == account.password:
                    login(request, account)
                    return HttpResponse("finaly")
                    # return render(request, "home.html", {"account": account})
                else:
                    return HttpResponseRedirect(reverse("login"))
            else:
                    return HttpResponse(f"<h2>No such a User : {username}</h2>")
        else:
            print(form.errors)  # Print form errors to debug
            return HttpResponse("form is not valid")
     
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))        


def signup_view(request):

    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            print(form.cleaned_data)
            
                # print(data)
            account = Account(
                username=data["username"],
                password=data["password"],
                confirm_password=data["confirm_password"])
            
            account.save() 
            return HttpResponseRedirect(reverse("home"))
        else:
            return HttpResponse(f"{form.errors.as_data()}")
    else:
        form = CreateAccountForm()
        return render(request,"accounts/main_page.html", {"form":form})

