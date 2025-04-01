from django.urls import path
from accounts.views import *
from transitions.views import *

urlpatterns = [
    path("", main_page_view, name='main_page'),

    path("home/", home_view ,name='home_view'),

    path("income/",income_view,name="income_view"),    

    path("expose/",expose_view,name="expose_view"),

    path("add_transitions/",add_transitions,name="add_transitions"),

    path("login/", login_view , name='login'),
    
    path("signup/", signup_view , name='signup')
]