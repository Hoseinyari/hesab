from django.urls import path
from users.views import *

urlpatterns = [
    path("", show_status),
    path("signup/", signup_view , name='signup'),
    path("login/", login_view , name='login'),
    path("dashboard/", dashboard_view , name="dashboard")
]