from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from .models import User

#  Registratsiya uchun Forma

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=80, required=True)
    phone = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=60, required=True)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True)
    confirm = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True)
    men = forms.BooleanField(widget=forms.CheckboxInput)
    women = forms.BooleanField(widget=forms.CheckboxInput)

