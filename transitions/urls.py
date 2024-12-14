from django.urls import path
from transitions.views import *

urlpatterns = [
path("", home_view ,name='home'),
path("income/",add_transitions,name="income"),    
path("expose/",add_transitions,name="expose"),    
path("add_transitions/",add_transitions,name="add_transitions"),


]