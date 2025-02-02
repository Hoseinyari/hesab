from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from accounts.models import *
from accounts.forms import MyLoginForm , CreateAccounttForm

# Create your views here.
def login_view(request):
        
    if not request.user.is_authenticated:
             
        if request.method == "POST":
                form = MyLoginForm(request.POST)
                if form.is_valid():
                
                    username = form.cleaned_data["username"]
                    password = form.cleaned_data["password"]
                    try:
                        Account = Account.objects.get(username = username)
                    except Exception as error:
                        print(error)
                        return HttpResponse("not ok")
                        # return HttpResponseRedirect(reverse("login"))
                    if Account is not None:
                        if password == Account.password:
                            login(request,Account)
                            return render(request,"home", {"Account":Account})     
                        else:
                            
                            return HttpResponseRedirect(reverse("login"))
                    
                    else:
            
                        return HttpResponse(f"<h2>No such a User : {username}</h2>")
                else:
                     return HttpResponse("onvalid")
        else:
             form =  MyLoginForm()
             return HttpResponse("REQUEST METHOD ")
            #  return render(request,'accounts/login.html',{"form":form})

    else:    
        return HttpResponseRedirect(reverse("home"))
     
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))        


def signup_view(request):
    if request.method == "POST":
        form =  CreateAccounttForm(request.POST)
        if form.is_valid :
            new_account = Account(
                 username = form['username'],
                 password = form['password'],
                 password_confirm = form['password_confirm']
            )
            # if password == password_confirm :
            
            new_account.save()
              
            return HttpResponseRedirect(reverse("home"))
    else:
            return render(request,"accounts/signup.html")
        