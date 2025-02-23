from django import forms
from django.core.exceptions import ValidationError
from .models import Account

class MyLoginForm(forms.Form):

    username = forms.CharField(max_length=50, label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")

# class CreateAccountForm(forms.Form):
#     username = forms.CharField(max_length=50, label="username")
#     password = forms.CharField(widget=forms.PasswordInput(), label="password")
#     confirm_password = forms.CharField(widget=forms.PasswordInput(), label="confirm password")
# forms.py

class CreateAccountForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data


