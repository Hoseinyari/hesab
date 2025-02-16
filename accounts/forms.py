from django import forms

class MyLoginForm(forms.Form):

    username = forms.CharField(max_length=50, label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput(), label="رمز عبور")

class CreateAccountForm(forms.Form):
    username = forms.CharField(max_length=50, label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput(), label="رمز عبور")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="تایید رمز عبور")

class DeletAgentForm(forms.Form):
    phone_number = forms.CharField(max_length=20)

