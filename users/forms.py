from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        label='Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Máximo 20 caracteres'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Al menos 8 caracteres'})
    )
    password2 = forms.CharField(
        label='Repetir contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Ya existe un usuario con ese nombre.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("El correo electrónico ya está registrado.")
        return email    

def validate_letters(value):
    if not re.match(r'^[A-Za-z]+$', value):
        raise ValidationError('Este campo solo puede contener letras.')

class UserEditForm(UserChangeForm):
    email = forms.EmailField(label="Email", disabled=True)  
    password = None
    last_name = forms.CharField(label="Apellido", required=False, validators=[validate_letters])
    first_name = forms.CharField(label="Nombre", required=False, validators=[validate_letters])
    imagen = forms.ImageField(label="Avatar",required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'imagen']

