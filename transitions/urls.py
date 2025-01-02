from django.urls import path
from .views import home_view,income_view,expose_view,add_transitions

urlpatterns = [
path("", home_view ,name='home'),
path("income/",income_view,name="income"),    
path("expose/",expose_view,name="expose"),    
path("add_transitions/",add_transitions,name="add_transitions"),

]
