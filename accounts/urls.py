from django.urls import path
from accounts.views import *

urlpatterns = [
    path("", main_page_view, name='main_page'),
    path("dashboard/", dashboard_view, name='dashboard'),
    path("login/", login_view , name='login'),
    path("signup/", signup_view , name='signup')
]