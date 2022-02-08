from authentication.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]

