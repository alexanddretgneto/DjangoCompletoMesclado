"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from app.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_("Senha"), widget=forms.PasswordInput({
        'class': 'form-control',
        'placeholder': 'Senha'
    }))
    confirm_password = forms.CharField(label=_("Confirmar Senha"), widget=forms.PasswordInput({
        'class': 'form-control',
        'placeholder': 'Confirmar Senha'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        return confirm_password