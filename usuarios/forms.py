from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'bio']