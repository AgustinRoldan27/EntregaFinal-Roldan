from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Contraseña actual')
    new_password1 = forms.CharField(widget=forms.PasswordInput, label='Nueva contraseña')
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar nueva contraseña')

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']