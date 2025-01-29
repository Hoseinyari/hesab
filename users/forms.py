from django.contrib.auth.forms import UserCreationForm
from users.models import *

class AddUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ["username","password"]