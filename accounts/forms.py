from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Account  # Import your custom user model


class MyLoginForm(forms.Form):

    username = forms.CharField(max_length=50, label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")


# accounts/forms.py

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'your@email.com'
        }),
        help_text='Required. We\'ll never share your email.'
    )

    class Meta:
        model = Account  # Use your custom user model here
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():  # Use your custom user model
            raise ValidationError("This email is already registered.")
        return email
        
# class CreateAccountForm(forms.Form):
#     username = forms.CharField(max_length=50, label="username")
#     password = forms.CharField(widget=forms.PasswordInput(), label="password")
#     confirm_password = forms.CharField(widget=forms.PasswordInput(), label="confirm password")
# forms.py

# class CreateAccountForm(UserCreationForm):
#     class Meta:
#         model = Account
#         fields = ['username', 'email', 'password1', 'password2']