from django import forms
from django.contrib.auth.models import User
from .models import Profile  # Importa el modelo Profile si lo usas

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date', 'website'] # Ajusta los campos del Profile