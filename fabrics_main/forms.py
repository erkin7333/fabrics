from django import forms
from .models import Order


class OrderModelForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone', 'address', 'payment_type', 'delivery_type')
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'inp form-control',
                'type': 'text',
                'placeholder': 'Ф.И.О.'
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'inp phone form-control',
                'type': 'text',
                'placeholder': 'Телефон'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'E-mail'
            }),
            'address': forms.TextInput(attrs={
                'class': 'inp form-control',
                'type': 'text',
                'placeholder': 'Адрес'
            }),
            'payment_type': forms.RadioSelect(attrs={
                'class': 'payment',
                'type': 'radio',

            }),
            'delivery_type': forms.RadioSelect(attrs={
                'class': 'payment',
                'type': 'radio',
            })
        }