from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Account  # Import your custom user model
from django.contrib.auth import get_user_model

class MyLoginForm(forms.Form):

    username = forms.CharField(max_length=50, label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")


#for getting default django user
User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # easy password validation
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
        # add simpler password validation setting
        for validator in self.fields['password1'].validators[:]:
            self.fields['password1'].validators.remove(validator)
        
        #make minimum password length
        self.fields['password1'].min_length = 6