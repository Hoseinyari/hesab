from django.urls import path
from .views import home_view,income_view,expose_view,add_transitions

urlpatterns = [
path("", home_view ,name='home_view'),

path("income/",income_view,name="income_view"),    

path("expose/",expose_view,name="expose_view"),    

path("add_transitions/",add_transitions,name="add_transitions"),

]
