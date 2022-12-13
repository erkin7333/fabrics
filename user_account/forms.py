from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from .models import User
from fabrics_config.validators import PhoneValidator

#  Registratsiya uchun Forma

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=80, required=True)
    phone = forms.CharField(max_length=20, required=True, validators=[PhoneValidator()])
    email = forms.CharField(max_length=60, required=True)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True,
                               validators=[MinLengthValidator(3), MaxLengthValidator(6)])
    confirm = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True,
                              validators=[MinLengthValidator(3), MaxLengthValidator(6)])
    men = forms.BooleanField(required=False)
    women = forms.BooleanField(required=False)


    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get('username')).exists():
            raise ValidationError("Ushbu username band")
        return self.cleaned_data["username"]


    def clean_phone(self):
        if User.objects.filter(phone=self.cleaned_data.get('phone')).exists():
            raise ValidationError('Ushbu telefon raqam band')
        return self.cleaned_data['phone']


    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data.get('email')).exists():
            raise ValidationError('Ushbu elektron pochta manzili band')
        return self.cleaned_data['email']


    def clean_confirm(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm']:
            raise ValidationError("Iltimos parollar bir xilligini tekshiring")
        return self.cleaned_data['confirm']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)