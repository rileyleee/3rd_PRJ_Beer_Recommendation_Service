from django import forms
from django.contrib.auth.forms import *
from account.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email",)


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "gender",
            "age",
        )
        pass

    field_order = ["username", "password1", "password2", "email", "gender", "age"]
    pass