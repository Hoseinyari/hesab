from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class MyLoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    
    # phone_number = forms.IntegerField(required=True )
    # class meta:
    #     model = Account
    #     fields = ("username","password") 

class CreateAccounttForm(forms.Form):
    username = forms.CharField(max_length=50, label="نام کاربری")
    phone_number = forms.IntegerField(required=True )
    password = forms.PasswordInput()
    password_confirm= forms.PasswordInput()

# class RegistrationForm(UserCreationForm):
#     phone_number = forms.CharField(max_length=11,required=True )
#     class meta:
#         model = Account
#         fields = ('username','phone_number','password 1','password 2') 

