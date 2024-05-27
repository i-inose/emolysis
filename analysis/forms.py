from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TextInput

class SignUpForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")

class TextInputForm(forms.ModelForm):
  class Meta:
    model = TextInput
    fields = ["text"]