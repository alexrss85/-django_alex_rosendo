from django import forms
from .models import Usuari

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correu electrònic", max_length=100)
    contrasenya = forms.CharField(label="Contrasenya", widget=forms.PasswordInput)
