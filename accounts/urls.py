from django.urls import path
from accounts.views import *

urlpatterns = [
    path("", home_view, name='home'),
    path("dashboard/", dashboard_view, name='dashboard'),
    path("login/", login_view , name='login'),
    path("signup/", signup_view , name='signup')
]