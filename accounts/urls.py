from django.urls import path
from accounts.views import *

urlpatterns = [
    path("", login_view , name='login'),
    path("signup/", signup_view , name='signup')
]