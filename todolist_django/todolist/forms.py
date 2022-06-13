from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegUserForm(UserCreationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Логин', 'autocomplete':'off'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input', 'placeholder':'E-MAIL', 'autocomplete':'off'}))
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'Пароль', 'autocomplete':'off'}))
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'Подтвердите пароль', 'autocomplete':'off'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LogUserForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Логин', 'autocomplete':'off'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'Пароль', 'autocomplete':'off'}))