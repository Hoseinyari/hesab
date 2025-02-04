from django.urls import path
from accounts.views import *

urlpatterns = [
    path("", home_view, name='home'),
    path("login/", login_view , name='login'),
    path("signup/", signup_view , name='signup')
]