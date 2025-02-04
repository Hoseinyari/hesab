from django import forms

class MyLoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput(), label="رمز عبور")


class CreateAccountForm(forms.Form):
    phone_number = forms.CharField(max_length=20, label="شماره تلفن", widget=forms.TextInput(attrs={"class" :"form-control" }))
    name = forms.CharField(max_length=20, label="نام", widget=forms.TextInput(attrs={"class" :"form-control" }))
    last_name = forms.CharField(max_length=20, label="نام خانوادگی", widget=forms.TextInput(attrs={"class" :"form-control" }))

class DeletAgentForm(forms.Form):
    phone_number = forms.CharField(max_length=20)

