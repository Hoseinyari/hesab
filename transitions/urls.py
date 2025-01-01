from django.urls import path
from transitions.views import *

urlpatterns = [
path("", home_view ,name='home'),
path("income/",income_view,name="income"),    
path("expose/",expose_view,name="expose"),    
# path("add_transitions/",add_transitions,name="add_transitions"),


]