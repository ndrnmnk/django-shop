from django.forms import TextInput
from django import forms
from django.contrib.auth.forms import UserCreationForm, User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    default_currency = forms.CharField(required=True)
    default_language = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'default_currency', 'default_language', 'email']

        labels = {
            'username': '',
            'password': '',
            'default_language': '',
            'default_currency': '',
            }

        widgets = {
            "username": TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}),
            "password1": TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            "password2": TextInput(attrs={'class': 'form-control', 'placeholder': 'Repeat it'}),
            "email": TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "default_currency": TextInput(attrs={'class': 'form-control', 'placeholder': 'UAH, PLN, EUR or USD'}),
            "default_language": TextInput(attrs={'class': 'form-control', 'placeholder': 'UA or EN'}),
        }