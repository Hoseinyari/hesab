from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from users.models import *
from users.forms import AddUserForm

# Create your views here.
def login_view(request):
    # checks for http method
    if request.method == "POST":
        data = request.POST
        username = data['username']
        users = User.objects.filter(username = username)
        if len(users) == 0:
            return HttpResponseRedirect(reverse("signup"))
        else:
            if data['password'] == users[0].password:
                return HttpResponseRedirect(reverse("dashboard"))
            else:
                return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "users/login.html")
    


def dashboard_view(request):
    return render(request,"users/dashboard.html")


def show_status(request):
    all_users = User.objects.all()
    return render(request,"users/index.html", {"users":all_users})


def signup_view(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        status = form.is_valid
        return render(request, "users/login.html", {"stat":status})
    else:
            form = AddUserForm()
            return render(request,"users/signup.html", {"form":form})
        

def logout_view(request):
    pass