from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class MyLoginForm(forms.Form):

    username = forms.CharField(max_length=50, label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
# class CreateAccountForm(forms.Form):
#     username = forms.CharField(max_length=50, label="username")
#     password = forms.CharField(widget=forms.PasswordInput(), label="password")
#     confirm_password = forms.CharField(widget=forms.PasswordInput(), label="confirm password")
# forms.py

# class CreateAccountForm(UserCreationForm):
#     class Meta:
#         model = Account
#         fields = ['username', 'email', 'password1', 'password2']