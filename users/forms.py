from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # Takes an arg: required. If false then optional to add email. True by default

    class Meta:
        model = User
        # The Model this form will interact with. Whenever this form validates, it's going to create a new user
        fields = ["username", "email", "password1", "password2"]
